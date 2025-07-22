import random

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(['Z', 'X']) for _ in range(n)]

def measure(bit, basis, measurement_basis):
    if basis == measurement_basis:
        return bit
    else:
        return random.randint(0, 1)

def eve_impostor_attack(alice_bits, alice_bases, bob_bases):
    n = len(alice_bits)
    eve_bases_to_alice = generate_bases(n)
    eve_bases_to_bob = generate_bases(n)

    eve_results = []
    bob_results = []

    for i in range(n):
        eve_bit = measure(alice_bits[i], alice_bases[i], eve_bases_to_alice[i])
        eve_results.append(eve_bit)

        bob_bit = measure(eve_bit, eve_bases_to_bob[i], bob_bases[i])
        bob_results.append(bob_bit)

    return eve_results, eve_bases_to_alice, eve_bases_to_bob, bob_results

def sift_key(bits1, bits2, bases1, bases2):
    return [b1 for b1, b2 in zip(bits1, bits2) if b1 == b2]

def calculate_qber(alice_key, bob_key):
    mismatches = sum(a != b for a, b in zip(alice_key, bob_key))
    return mismatches / len(alice_key) if alice_key else 0

def main():
    n = 50
    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)
    bob_bases = generate_bases(n)

    eve_results, eve_bases_to_alice, eve_bases_to_bob, bob_results = eve_impostor_attack(
        alice_bits, alice_bases, bob_bases
    )

    qber = calculate_qber(alice_bits, bob_results)

    print("🔓 Eve 假冒攻擊模擬完成")
    print("原始 Alice 密鑰（前 20 位）:", alice_bits[:20])
    print("最終 Bob 收到密鑰（前 20 位）:", bob_results[:20])
    print(f"模擬 QBER：{qber:.2f}")  # 或改為 {qber*100:.2f}% 表示百分比

if __name__ == "__main__":
    main()

