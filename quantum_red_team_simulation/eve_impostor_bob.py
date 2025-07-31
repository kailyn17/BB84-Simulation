import random

def eve_impostor_attack(length=20):
    # Alice 傳送比特
    alice_bits = [random.choice([0,1]) for _ in range(length)]
    # Eve 假冒 Bob，30% 機率翻轉比特
    eve_bits = [bit if random.random() > 0.3 else 1-bit for bit in alice_bits]
    # QBER 計算
    qber = sum([1 for a, e in zip(alice_bits, eve_bits) if a != e]) / length
    return qber

def main():
    qber = eve_impostor_attack()
    print(f"[Eve 假冒 Bob 攻擊] QBER = {qber:.2f}")

if __name__ == "__main__":
    main()

