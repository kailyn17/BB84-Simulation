import random

def eve_memory_attack(length=20, intercept_ratio=0.5):
    # Alice 傳送比特
    alice_bits = [random.choice([0,1]) for _ in range(length)]
    # Eve 部分攔截（根據比例決定）
    eve_bits = []
    for bit in alice_bits:
        if random.random() < intercept_ratio:
            # Eve 攔截，50% 機率翻轉
            eve_bits.append(bit if random.random() > 0.5 else 1-bit)
        else:
            # Eve 沒攔截，直接傳送
            eve_bits.append(bit)
    # QBER 計算
    qber = sum([1 for a, e in zip(alice_bits, eve_bits) if a != e]) / length
    return qber

def main():
    qber = eve_memory_attack()
    print(f"[Eve 記憶型攻擊] 攔截比例 50% → QBER = {qber:.2f}")

if __name__ == "__main__":
    main()

