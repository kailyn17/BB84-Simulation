import random
import matplotlib.pyplot as plt

def eve_impostor_attack(length=20):
    """
    Eve 假冒 Bob 的攻擊模型
    - Alice 產生隨機比特
    - Eve 以 30% 機率翻轉比特
    - 回傳單次攻擊的 QBER
    """
    alice_bits = [random.choice([0, 1]) for _ in range(length)]  
    
    eve_bits = [bit if random.random() > 0.3 else 1-bit for bit in alice_bits]
    
    qber = sum([1 for a, e in zip(alice_bits, eve_bits) if a != e]) / length 
    return qber

def simulate_attacks(runs=50, length=20):
    """
    執行多次攻擊模擬，統計平均 QBER
    """
    qber_values = [eve_impostor_attack(length) for _ in range(runs)]
    avg_qber = sum(qber_values) / runs
    return avg_qber, qber_values

def plot_qber(qber_values):
    """
    繪製 QBER 變化圖
    """
    plt.plot(range(1, len(qber_values)+1), qber_values, marker='o')
    plt.axhline(y=sum(qber_values)/len(qber_values), color='r', linestyle='--', label='平均 QBER')
    plt.xlabel("模擬次數")
    plt.ylabel("QBER")
    plt.title("Eve 假冒 Bob 攻擊 - QBER 模擬結果")
    plt.legend()
    plt.grid(True)
    plt.savefig("images/eve_qber_simulation.png")  # 存圖到 images 資料夾
    plt.show()

def main():
    random.seed(42)  # 確保結果可重現
    runs = 50
    avg_qber, qber_values = simulate_attacks(runs=runs, length=20)
    
    print(f"[Eve 假冒 Bob 攻擊] 模擬次數: {runs}")
    print(f"各次 QBER: {qber_values}")
    print(f"平均 QBER = {avg_qber:.2f}")
    
    # 繪圖
    plot_qber(qber_values)

if __name__ == "__main__":
    main()
