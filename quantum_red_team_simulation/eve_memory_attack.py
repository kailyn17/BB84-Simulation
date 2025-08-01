# eve_memory_attack.py
# 模擬 Eve 記憶型攻擊，部分攔截並翻轉比特，計算 QBER

import random

def eve_memory_attack(length=20, intercept_ratio=0.5):
    """
    Eve 記憶型攻擊模型
    - Alice 傳送隨機比特
    - Eve 依照攔截比例決定是否攔截
    - 若攔截，50% 機率翻轉比特
    - 回傳單次攻擊的 QBER
    """
    alice_bits = [random.choice([0, 1]) for _ in range(length)]
    eve_bits = []
    for bit in alice_bits:
        if random.random() < intercept_ratio:
            eve_bits.append(bit if random.random() > 0.5 else 1 - bit)
        else:
            eve_bits.append(bit)
    qber = sum(1 for a, e in zip(alice_bits, eve_bits) if a != e) / length
    return qber

def main():
    qber = eve_memory_attack()
    print(f"[Eve 記憶型攻擊] 攔截比例 50% → QBER = {qber:.2f}")

if __name__ == "__main__":
    main()
