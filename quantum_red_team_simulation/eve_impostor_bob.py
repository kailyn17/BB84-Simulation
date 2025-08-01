# eve_impostor_bob.py
# 模擬 Eve 假冒 Bob 的攻擊模型，計算單次 QBER

import random

def eve_impostor_attack(length=20):
    """
    Eve 假冒 Bob 的攻擊模型
    - Alice 產生隨機比特
    - Eve 以 30% 機率翻轉比特
    - 回傳單次攻擊的 QBER
    """
    alice_bits = [random.choice([0, 1]) for _ in range(length)]
    eve_bits = [bit if random.random() > 0.3 else 1 - bit for bit in alice_bits]
    qber = sum(1 for a, e in zip(alice_bits, eve_bits) if a != e) / length
    return qber

def main():
    qber = eve_impostor_attack()
    print(f"[Eve 假冒 Bob 攻擊] QBER = {qber:.2f}")

if __name__ == "__main__":
    main()
