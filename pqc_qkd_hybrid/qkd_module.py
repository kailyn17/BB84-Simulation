import random

def simulate_bb84(length=128, eve_mode="none", intercept_ratio=0.0, seed=None):
    """
    模擬 BB84 協定並回傳統一格式結果
    （目前僅實作基本版 QKD，QBER 固定為 0.0，可後續加入攻擊模型）

    參數:
        length: 欲產生的總位元數 (含未篩選前)
        eve_mode: 攻擊模式（none/basic/impostor/memory）
        intercept_ratio: 攔截比例 (0.0~1.0)
        seed: 隨機種子（可重現）

    回傳:
        dict{
            "sifted_len": int,
            "qber": float,
            "alice_key": str,
            "bob_key": str,
            "notes": str
        }
    """
    if seed is not None:
        random.seed(seed)

    # Alice 產生位元與基底
    alice_bits = [random.randint(0, 1) for _ in range(length)]
    alice_bases = [random.choice(['X', 'Z']) for _ in range(length)]

    # Bob 隨機選擇基底（目前無 Eve）
    bob_bases = [random.choice(['X', 'Z']) for _ in range(length)]
    bob_bits = []

    for i in range(length):
        if alice_bases[i] == bob_bases[i]:
            bob_bits.append(alice_bits[i])
        else:
            bob_bits.append(random.randint(0, 1))

    # 篩選出基底相同的位元
    sifted_key_a = []
    sifted_key_b = []
    for i in range(length):
        if alice_bases[i] == bob_bases[i]:
            sifted_key_a.append(alice_bits[i])
            sifted_key_b.append(bob_bits[i])

    sifted_len = len(sifted_key_a)

    # 計算 QBER（目前假設無攻擊 → QBER=0.0）
    if sifted_len > 0:
        errors = sum(1 for a, b in zip(sifted_key_a, sifted_key_b) if a != b)
        qber = errors / sifted_len
    else:
        qber = 0.0

    return {
        "sifted_len": sifted_len,
        "qber": qber,
        "alice_key": "".join(map(str, sifted_key_a)),
        "bob_key": "".join(map(str, sifted_key_b)),
        "notes": f"Basic BB84 simulation with eve_mode={eve_mode}, intercept_ratio={intercept_ratio}"
    }

def main():
    result = simulate_bb84(length=128)
    print(f"🔐 共用密鑰長度: {result['sifted_len']}")
    print(f"QBER: {result['qber']:.4f}")
    print("Alice key (前 20 位):", result['alice_key'][:20])
    print("Bob key   (前 20 位):", result['bob_key'][:20])

if __name__ == "__main__":
    main()
