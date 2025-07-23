import random

def generate_bits(n):
    """產生隨機 bit 序列"""
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    """產生隨機基底序列（Z 或 X）"""
    return [random.choice(['Z', 'X']) for _ in range(n)]

def eve_intercept(alice_bits, alice_bases, intercept_ratio=1.0):
    """
    Eve 攔截 Alice qubit 的過程
    intercept_ratio：攔截比例（1.0 表示全數攔截）
    """
    eve_bases = generate_bases(len(alice_bits))
    eve_results = []

    for i in range(len(alice_bits)):
        if random.random() < intercept_ratio:
            # 攔截：Eve 用隨機基底測量
            if eve_bases[i] == alice_bases[i]:
                eve_results.append(alice_bits[i])
            else:
                eve_results.append(random.randint(0, 1))
        else:
            # 不攔截：qubit 原封不動
            eve_results.append(alice_bits[i])
            eve_bases[i] = alice_bases[i]  # 基底保持一致
    return eve_results, eve_bases

def bob_measure(eve_results, eve_bases, bob_bases):
    """Bob 根據自身基底測量 Eve 傳來的 qubit"""
    bob_results = []
    for i in range(len(eve_results)):
        if eve_bases[i] == bob_bases[i]:
            bob_results.append(eve_results[i])
        else:
            bob_results.append(random.randint(0, 1))
    return bob_results

def sift_key(bits1, bits2, bases1, bases2):
    """比較雙方基底，過濾出一致位置的 bit 作為密鑰"""
    return [bit1 for bit1, base1, base2 in zip(bits1, bases1, bases2) if base1 == base2]

def calculate_qber(alice_key, bob_key):
    """計算量子位元錯誤率（Quantum Bit Error Rate, QBER）"""
    if not alice_key or not bob_key:
        return None
    mismatches = sum(a != b for a, b in zip(alice_key, bob_key))
    return mismatches / len(alice_key)

def eve_basic_attack_simulation(length=50, intercept_ratio=1.0):
    """主模擬函式：執行一次 Eve 攻擊並回傳 QBER"""
    alice_bits = generate_bits(length)
    alice_bases = generate_bases(length)
    bob_bases = generate_bases(length)

    eve_results, eve_bases = eve_intercept(alice_bits, alice_bases, intercept_ratio)
    bob_results = bob_measure(eve_results, eve_bases, bob_bases)

    alice_key = sift_key(alice_bits, bob_results, alice_bases, bob_bases)
    bob_key = sift_key(bob_results, alice_bits, bob_bases, alice_bases)

    qber = calculate_qber(alice_key, bob_key)

    # 印出結果
    print("Alice Key:", alice_key)
    print("Bob Key:  ", bob_key)
    print(f"QBER: {qber:.2%}")
    return qber

if __name__ == "__main__":
    # 使用範例：攔截比例為 0.5（50% qubit 被 Eve 攔截）
    eve_basic_attack_simulation(length=128, intercept_ratio=0.5)


