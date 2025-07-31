import random

def eve_impostor_attack(length=20):
    """
    Eve 假冒 Bob 的攻擊模型
    - Alice 產生隨機比特
    - Eve 以 30% 機率翻轉比特
    - 回傳單次攻擊的 QBER
    """
    # Alice 傳送比特（隨機產生 0 或 1）
    alice_bits = [random.choice([0,1]) for _ in range(length)]  
    
    # Eve 假冒 Bob，30% 機率翻轉比特
    eve_bits = [bit if random.random() > 0.3 else 1-bit for bit in alice_bits]
    
    # QBER 計算：比對 Alice 與 Eve 的比特差異比例
    qber = sum([1 for a, e in zip(alice_bits, eve_bits) if a != e]) / length 
    return qber

def simulate_attacks(runs=50, length=20):
    """
    執行多次攻擊模擬，統計平均 QBER
    """
    qber_values = [eve_impostor_attack(length) for _ in range(runs)]
    avg_qber = sum(qber_values) / runs
    return avg_qber, qber_values

def main():
    runs = 50
    avg_qber, qber_values = simulate_attacks(runs=runs, length=20)
    
    print(f"[Eve 假冒 Bob 攻擊] 模擬次數: {runs}")
    print(f"各次 QBER: {qber_values}")
    print(f"平均 QBER = {avg_qber:.2f}")

if __name__ == "__main__":
    main()
