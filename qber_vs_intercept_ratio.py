import random
import matplotlib.pyplot as plt

n = 500
intercept_ratios = [i / 10 for i in range(11)]
qber_values = []

for intercept_ratio in intercept_ratios:
    alice_bits = [random.randint(0, 1) for _ in range(n)]
    alice_bases = [random.choice(['X', 'Z']) for _ in range(n)]
    bob_results = []
    errors = 0

    for i in range(n):
        if random.random() < intercept_ratio:
            eve_basis = random.choice(['X', 'Z'])
            eve_bit = alice_bits[i] if eve_basis == alice_bases[i] else random.randint(0, 1)
            bob_basis = random.choice(['X', 'Z'])
            bob_bit = eve_bit if bob_basis == eve_basis else random.randint(0, 1)
        else:
            bob_basis = random.choice(['X', 'Z'])
            bob_bit = alice_bits[i] if bob_basis == alice_bases[i] else random.randint(0, 1)
        bob_results.append(bob_bit)

    sifted_key = [i for i in range(n) if alice_bases[i] == bob_basis]
    errors = sum(1 for i in sifted_key if alice_bits[i] != bob_results[i])
    qber = errors / len(sifted_key) if sifted_key else 0
    qber_values.append(qber)

plt.plot(intercept_ratios, qber_values, marker='o')
plt.xlabel('攔截比率')
plt.ylabel('QBER')
plt.title('QBER VS 攔截比率')
plt.ylim(0, 0.6)
plt.grid(True)
plt.savefig('images/qber_vs_intercept_ratio.png')
plt.show()
