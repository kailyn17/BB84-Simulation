import random
import matplotlib.pyplot as plt

def plot_qber_vs_intercept_ratio(n=500):
    """
    模擬 QBER 對攔截比例的變化，並繪製圖表
    n：模擬 qubit 數量
    """
    intercept_ratios = [i / 10 for i in range(11)]
    qber_values = []

    for intercept_ratio in intercept_ratios:
        alice_bits = [random.randint(0, 1) for _ in range(n)]
        alice_bases = [random.choice(['X', 'Z']) for _ in range(n)]
        bob_results = []
        bob_bases = []
        
        for i in range(n):
            if random.random() < intercept_ratio:
                # Eve 攔截並測量
                eve_basis = random.choice(['X', 'Z'])
                eve_bit = alice_bits[i] if eve_basis == alice_bases[i] else random.randint(0, 1)
                bob_basis = random.choice(['X', 'Z'])
                bob_bit = eve_bit if bob_basis == eve_basis else random.randint(0, 1)
            else:
                # 無攔截，Bob 直接測量
                bob_basis = random.choice(['X', 'Z'])
                bob_bit = alice_bits[i] if bob_basis == alice_bases[i] else random.randint(0, 1)

            bob_results.append(bob_bit)
            bob_bases.append(bob_basis)

        # 篩選基底一致位置作為 sifted key
        sifted_indices = [i for i in range(n) if alice_bases[i] == bob_bases[i]]
        errors = sum(1 for i in sifted_indices if alice_bits[i] != bob_results[i])
        qber = errors / len(sifted_indices) if sifted_indices else 0
        qber_values.append(qber)

    # 繪製圖表
    plt.plot(intercept_ratios, qber_values, marker='o')
    plt.xlabel('攔截比率')
    plt.ylabel('QBER（量子位元錯誤率）')
    plt.title('QBER vs 攔截比率')
    plt.ylim(0, 0.6)
    plt.grid(True)

    # 儲存與顯示圖片
    plt.savefig('images/qber_vs_intercept_ratio.png')
    plt.show()

def main():
    plot_qber_vs_intercept_ratio()
    print("✅ 圖片已儲存為 images/qber_vs_intercept_ratio.png")

if __name__ == "__main__":
    main()

