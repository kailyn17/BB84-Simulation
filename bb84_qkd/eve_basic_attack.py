import random

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(['Z', 'X']) for _ in range(n)]

def measure(qubit, basis):
    return qubit if basis == 'Z' else 1 - qubit if random.random() < 0.5 else qubit

def eve_intercept(alice_bits, alice_bases):
    eve_bases = generate_bases(len(alice_bits))
    eve_results = []
    for i in range(len(alice_bits)):
        if eve_bases[i] == alice_bases[i]:
            eve_results.append(alice_bits[i])
        else:
            eve_results.append(random.randint(0, 1))
    return eve_results, eve_bases

def bob_measure(eve_results, eve_bases, bob_bases):
    bob_results = []
    for i in range(len(eve_results)):
        if eve_bases[i] == bob_bases[i]:
            bob_results.append(eve_results[i])
        else:
            bob_results.append(random.randint(0, 1))
    return bob_results

def sift_key(bits1, bits2, bases1, bases2):
    return [bit1 for bit1, base1, base2 in zip(bits1, bases1, bases2) if base1 == base2]

def calculate_qber(alice_key, bob_key):
    if not alice_key or not bob_key:
        return None
    mismatches = sum(a != b for a, b in zip(alice_key, bob_key))
    return mismatches / len(alice_key)

# Main simulation
n = 50
alice_bits = generate_bits(n)
alice_bases = generate_bases(n)
bob_bases = generate_bases(n)

eve_results, eve_bases = eve_intercept(alice_bits, alice_bases)
bob_results = bob_measure(eve_results, eve_bases, bob_bases)

alice_key = sift_key(alice_bits, bob_results, alice_bases, bob_bases)
bob_key = sift_key(bob_results, alice_bits, bob_bases, alice_bases)

qber = calculate_qber(alice_key, bob_key)

print(f"Alice Key: {alice_key}")
print(f"Bob Key:   {bob_key}")
print(f"QBER: {qber:.2%}")

if __name__ == "__main__":
    # 使用範例：執行一次攔截攻擊並顯示 QBER
    qber = eve_basic_attack_simulation(length=128, intercept_ratio=0.5)
    print("模擬結果 QBER:", qber)


