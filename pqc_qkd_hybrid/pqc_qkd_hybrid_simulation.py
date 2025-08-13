# pqc_qkd_hybrid_simulation.py
from __future__ import annotations

import math
from typing import Dict, Any, Optional

import qkd_module  # 需要有 simulate_bb84(...)
import pqc_module  # 僅用於示範整合（不影響回傳介面）


def _bits_to_bytes(bit_str: str) -> bytes:
    """
    將 '0101...' 的 bit 串轉為 bytes。
    若長度不是 8 的倍數，會在呼叫端先截斷。
    """
    if len(bit_str) % 8 != 0:
        raise ValueError("bit string length must be a multiple of 8 before conversion")

    out = bytearray()
    for i in range(0, len(bit_str), 8):
        byte_bits = bit_str[i:i+8]
        out.append(int(byte_bits, 2))
    return bytes(out)


def _derive_demo_pqc_shift_from_bits(bit_str: str) -> int:
    """
    以 sifted bits 派生一個 1~10 的整數位移量（僅 demo / 教學用途）。
    這個值會放進 meta['demo_pqc_shift']，不會影響回傳的 session_key。
    """
    if not bit_str:
        return 3
    s = sum(1 for b in bit_str if b == "1")
    return (s % 10) + 1


def hybrid_key_exchange(
    n_bits: int = 256,
    eve_mode: str = "none",
    intercept_ratio: float = 0.0,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """
    PQC × QKD 的混合密鑰交換（教學/模擬版）
    - 透過 QKD 取得 sifted bits 與 QBER
    - 將 sifted bits 對齊 8 的倍數後，轉為十六進位字串作為 session_key
    - 回傳格式符合 api/app.py 的預期

    參數：
      n_bits:       QKD 原始位元長度（未篩選前）
      eve_mode:     "none" / "basic" / "impostor" / "memory"（由 qkd_module 實作細節）
      intercept_ratio: 0.0~1.0（交給 qkd_module 決定如何使用）
      seed:         隨機種子（可重現）

    回傳：
      {
        "session_key": "<hex string>",
        "qber": 0.0~1.0,
        "meta": {
          "source": "BB84",
          "used_bits": int,
          "dropped_bits": int,
          "eve_mode": str,
          "intercept_ratio": float,
          "seed": int|None,
          "status": "ok" | "warn_high_qber",
          "qber_threshold": 0.11,
          "demo_pqc_shift": int,
          "example_ciphertext": str  # 以 demo_pqc_shift 對 'HELLO' 加密的示意
        }
      }
    """
    # 1) 跑 QKD 模擬
    sim = qkd_module.simulate_bb84(
        length=n_bits,
        eve_mode=eve_mode,
        intercept_ratio=intercept_ratio,
        seed=seed,
    )

    alice_key = str(sim.get("alice_key", ""))  # sifted bits (Alice)
    bob_key   = str(sim.get("bob_key", ""))    # sifted bits (Bob)
    qber      = float(sim.get("qber", 0.0))

    # 2) 我們以「Alice 的 sifted bits」作為 session key 的素材
    #    （在真實環境會做抽樣比對/資訊調整/隱私放大；這裡為教學簡化版）
    sifted_bits = alice_key

    # 對齊至 8 的倍數長度（丟棄尾端不足 8 的位元，讓 bytes 轉換簡單可逆）
    usable_len = (len(sifted_bits) // 8) * 8
    used = sifted_bits[:usable_len]
    dropped = len(sifted_bits) - usable_len

    if usable_len == 0:
        raise ValueError(
            "Sifted key length is 0 after alignment. Increase n_bits or check QKD pipeline."
        )

    # 3) 轉 bytes → hex 當作 session_key，便於跨系統傳遞與記錄
    key_bytes = _bits_to_bytes(used)
    session_key_hex = key_bytes.hex()

    # 4) 設定一個教學閾值，若 QBER 太高，提醒要做隱私放大或棄用
    #    常見安全門檻會依場景不同；這裡先用 11% 當示意
    qber_threshold = 0.11
    status = "ok" if qber <= qber_threshold else "warn_high_qber"

    # 5) 示範與 pqc_module 的簡單整合（僅放 meta，不影響主回傳）
    demo_shift = _derive_demo_pqc_shift_from_bits(used)
    example_ciphertext = pqc_module.encrypt("HELLO", str(demo_shift))["ciphertext"]

    return {
        "session_key": session_key_hex,
        "qber": qber,
        "meta": {
            "source": "BB84",
            "used_bits": usable_len,
            "dropped_bits": dropped,
            "eve_mode": eve_mode,
            "intercept_ratio": float(intercept_ratio),
            "seed": seed,
            "status": status,
            "qber_threshold": qber_threshold,
            # 下面兩個欄位僅為示範 PQC 結合
            "demo_pqc_shift": demo_shift,
            "example_ciphertext": example_ciphertext,
        },
    }


def _selftest():
    print(">>> Running hybrid_key_exchange() self-test")
    res = hybrid_key_exchange(n_bits=256, eve_mode="none", intercept_ratio=0.0, seed=42)
    print("QBER:", res["qber"])
    print("Session key (hex, first 32):", res["session_key"][:32] + "...")
    print("Used bits:", res["meta"]["used_bits"], "Dropped:", res["meta"]["dropped_bits"])
    print("Status:", res["meta"]["status"])
    print("Demo PQC shift:", res["meta"]["demo_pqc_shift"])
    print("Example ciphertext (HELLO):", res["meta"]["example_ciphertext"])


def main():
    _selftest()


if __name__ == "__main__":
    main()
