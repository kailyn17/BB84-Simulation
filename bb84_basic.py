import random

n = 20  # qubit 數量

# 產生 Alice 的隨機 bits 和 bases
alice_bits = [random.randint(0, 1) for _ in range(n)]
alice_bases = [random.choice(['+', 'x']) for _ in range(n)]

# 產生 Bob 的 bases
bob_bases = [random.choice(['+', 'x']) for _ in range(n)]

# Bob 接收 qubit 並測量
bob_results = []
for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        bob_results.append(alice_bits[i])
    else:
        bob_results.append(random.randint(0, 1))

# 比對 basis 並產生 key
raw_key = []
for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        raw_key.append(bob_results[i])

print("Raw key:", raw_key)
