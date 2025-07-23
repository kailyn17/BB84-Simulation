import random

def main():
    n = 20  # qubit 數量

    # 👉 Step 1：Alice 隨機產生 bit 序列與量測基底
    alice_bits = [random.randint(0, 1) for _ in range(n)]              # Alice 的 bit（0 或 1）
    alice_bases = [random.choice(['+', 'x']) for _ in range(n)]       # Alice 的基底（+ 為 Z，x 為 X）

    # 👉 Step 2：Bob 隨機選擇量測基底
    bob_bases = [random.choice(['+', 'x']) for _ in range(n)]         # Bob 的基底

    # 👉 Step 3：Bob 測量 qubit，若基底相同則接收 bit，否則隨機猜
    bob_results = []
    for i in range(n):
        if alice_bases[i] == bob_bases[i]:
            bob_results.append(alice_bits[i])
        else:
            bob_results.append(random.randint(0, 1))

    # 👉 Step 4：比較基底，雙方一致時提取密鑰
    raw_key = []
    for i in range(n):
        if alice_bases[i] == bob_bases[i]:
            raw_key.append(bob_results[i])

    # 👉 最終輸出密鑰
    print("Raw key:", raw_key)

if __name__ == "__main__":
    main()
