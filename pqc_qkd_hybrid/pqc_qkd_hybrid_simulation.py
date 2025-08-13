# pqc_module.py
from __future__ import annotations

import base64
import random
from typing import Optional, Dict, Any, Tuple

# -----------------------------
# 低階：位元組位移（安全可傳輸）
# -----------------------------
def _shift_bytes(data: bytes, shift: int) -> bytes:
    # 逐 byte 位移並取模 256，確保可逆
    return bytes((b + shift) % 256 for b in data)

def _normalize_key(key: Optional[str]) -> Tuple[int, bool]:
    """
    將 key 正規化成整數位移量。
    若 key 為 None → 隨機產生 1~10 的正整數並回傳 (key, generated=True)
    若 key 為字串 → 嘗試轉換為整數
    """
    if key is None:
        return random.randint(1, 10), True
    if isinstance(key, str):
        key = key.strip()
        if key == "":
            return random.randint(1, 10), True
        try:
            return int(key), False
        except Exception:
            # 若傳入非數字字串，退回隨機 key（避免壞輸入）
            return random.randint(1, 10), True
    # 其他型別（不預期），也退回隨機
    return random.randint(1, 10), True

# -----------------------------
# API 預期介面（供 FastAPI 呼叫）
# -----------------------------
def encrypt(plaintext: str, key: Optional[str] = None) -> Dict[str, Any]:
    """
    以「位元組位移 + Base64」加密：
    - 先將 plaintext 以 UTF-8 轉 bytes
    - 以 key（整數位移）位移每個 byte
    - 將結果做 Base64 編碼，回傳 ASCII 安全字串

    回傳：
      {
        "ciphertext": str,  # Base64 字串
        "key": str,         # 加密用正整數位移（若輸入 key 為 None 才會回傳）
        "meta": { "algo": "byte-shift+b64", "note": "...", "private_key": "-<key>" }
      }
    """
    k, generated = _normalize_key(key)  # k 可能是任意整數；我們以「加密用正整數」輸出
    # 將 key 規範為正整數做加密（可讀性較好）
    pub_k = abs(int(k)) if k != 0 else 3  # 避免 0 位移
    data = plaintext.encode("utf-8")
    shifted = _shift_bytes(data, pub_k)
    b64 = base64.b64encode(shifted).decode("ascii")

    result: Dict[str, Any] = {
        "ciphertext": b64,
        "meta": {
            "algo": "byte-shift+b64",
            "note": "Demo PQC-like placeholder (byte-shift + Base64). For teaching/demo only.",
            "private_key": str(-pub_k),  # 對應的解密位移
        },
    }
    # 若呼叫方沒有提供 key，就把產生的正整數 key 回傳給他保存
    if generated:
        result["key"] = str(pub_k)
    return result

def decrypt(ciphertext: str, key: str) -> Dict[str, Any]:
    """
    解密邏輯：
    - Base64 轉回位元組
    - 對每個 byte 做相反位移
      * 若使用者提供的是「加密用正整數 key」，我們自動取負值做解密
      * 若使用者直接提供負整數（私鑰）也 OK
    回傳：
      { "plaintext": str }
    """
    # 正規化 key：若 key > 0，解密要用 -key；若 key 已是負值，就直接用
    k, _ = _normalize_key(key)
    dec_k = -abs(int(k)) if k >= 0 else int(k)

    try:
        raw = base64.b64decode(ciphertext.encode("ascii"))
    except Exception as e:
        # 若不是合法 Base64，直接丟出錯（讓 FastAPI 捕捉成 400/500）
        raise ValueError(f"Invalid Base64 ciphertext: {e}")

    shifted_back = _shift_bytes(raw, dec_k)
    try:
        plaintext = shifted_back.decode("utf-8")
    except Exception:
        # 若無法以 UTF-8 解碼，代表 key 不對或密文壞掉
        raise ValueError("Decryption failed: wrong key or corrupted ciphertext (UTF-8 decode error).")

    return {"plaintext": plaintext}

# -----------------------------
# 與你原本的 API 相容的函式（保留）
# （不再建議在新 API 內部使用，但留著不破壞舊習慣）
# -----------------------------
def generate_pqc_keys():
    """
    產生模擬用的「公鑰 / 私鑰」概念：
    - public_key: 正整數位移
    - private_key: 負整數位移（解密用）
    """
    shift = random.randint(1, 10)
    return shift, -shift

def pqc_encrypt(message, public_key):
    """
    舊版字元位移（可能出現不可見字元）；保留以相容舊程式。
    建議改用 encrypt()（byte-shift + Base64）。
    """
    return ''.join([chr(ord(char) + int(public_key)) for char in message])

def pqc_decrypt(ciphertext, private_key):
    """
    舊版字元位移解密；保留以相容舊程式。
    建議改用 decrypt()。
    """
    return ''.join([chr(ord(char) + int(private_key)) for char in ciphertext])

# -----------------------------
# 可獨立執行的測試
# -----------------------------
def _selftest():
    pub, priv = generate_pqc_keys()
    msg = "量子資安 PQC×QKD Hybrid 🚀"
    # 新 API
    enc = encrypt(msg, str(pub))
    dec = decrypt(enc["ciphertext"], str(priv))  # 也可用正的 pub，decrypt 會自動取負
    # 舊 API（只適合 ASCII 範圍，中文會亂碼，故僅測英文）
    legacy_msg = "Quantum"
    legacy_ct = pqc_encrypt(legacy_msg, pub)
    legacy_pt = pqc_decrypt(legacy_ct, priv)

    print("=== New API ===")
    print("Plaintext:", msg)
    print("Ciphertext (b64):", enc["ciphertext"][:60] + "...")
    print("Decrypted:", dec["plaintext"])
    print("Meta:", enc.get("meta"))

    print("\n=== Legacy API (ASCII only) ===")
    print("Legacy Plaintext:", legacy_msg)
    print("Legacy Ciphertext:", legacy_ct)
    print("Legacy Decrypted:", legacy_pt)

def main():
    _selftest()

if __name__ == "__main__":
    main()
