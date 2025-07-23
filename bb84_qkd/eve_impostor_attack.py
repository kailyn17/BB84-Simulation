import random

def generate_bits(n):
    """產生隨機 bit 序列"""
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    """產生隨機基底序列（Z 或 X）"""
    return [random.choice(['Z', 'X']) for _ in range(n)]

def measure(bit, basis, measurement_basis):
    """根據測量基底測量 bit，若不同基底則有一定機率錯誤"""
    if basis == measurement_basis:
        return bit
    else:
        return random.randint(0, 1)

def eve_impostor_attack(alice_bits, alice_bases, bob_bases):
    """
    Eve 假冒攻擊：同時扮演 Alice 傳送 qubit，與 Bob 接收 qubit
    """
    n = len(alice_bits)
    eve_bases_to_alice = generate_bases(n)  # Eve 偽裝 Alice 用的基底
    eve_bases_to_bob = generate_bases(n)    # Eve 偽裝 Bob 測量的基底

    eve_results = []
    bob_results = []

    for i in range(n):
        # Eve 偽裝 Alice 發送 qubit
        eve_bit = measure(alice_bits[i], alice_bases[i], eve_bases_to_alice[i])
        eve_results.append(eve_bit)

        # Eve 偽裝 Bob 測量 qubit 並轉送給 Bob
        bob_bit = measure(eve_bit, eve_bases_to_bob[i], bob_bases[i])
        bob_results.append(bob_bit)

    return eve_results, eve_bases_to_alice, eve_bases_to_bob, bob_results

def sift_key(bits1, bits2, bases1, bases2):
    """雙方基底一致時提取密鑰（本版本未使用）"""
    return [b1 for b1, b2 in zip(bits1, bits2) if b1 == b2]

def calculate_qber(alice_key, bob_key):
    """計算錯誤率 QBER"""
    mismatches = sum(a != b for a, b in zip(alice_key, bob_key))
    return mismatches / len(alice_key) if alice_key else 0

def main():
    n = 50  # 模擬 qubit 數量

    # Step 1: Alice 資料產生
    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)

    # Step 2: Bob 的基底
    bob_bases = generate_bases(n)

    # Step 3: Eve 假冒攻擊模擬
    eve_results, eve_bases_to_alice, eve_bases_to_bob, bob_results = eve_impostor_attack(
        alice_bits, alice_bases, bob_bases
    )

    # Step 4: 計算錯誤率
    qber = calculate_qber(alice_bits, bob_results)

    # Step 5: 輸出結果
    print("🔓 Eve 假冒攻擊模擬完成")
    print("原始 Alice 密鑰（前 20 位）:", alice_bits[:20])
    print("最終 Bob 收到密鑰（前 20 位）:", bob_results[:20])
    print(f"模擬 QBER：{qber:.2%}")  # 百分比格式輸出

if __name__ == "__main__":
    main()


