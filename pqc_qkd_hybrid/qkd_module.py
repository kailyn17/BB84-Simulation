# qkd_mode.py
import random

def generate_qkd(length=128):
    """
    產生 QKD 密鑰 (使用 BB84 協定模擬)
    參數:
        lengh: 欲產生的總位元數 (含未篩選前)
    回傳:  
        sifted_key:Alice 與 Bob 根據相同基底所得的共同密鑰
    """
    alice_bits = [random.randint(0, 1) for _ in range(length)]
    alice_bases = [random.choice(['X', 'Z']) for _ in range(length)]
    
    bob_bases = [random.choice(['X', 'Z']) for _ in range(length)]

    sifted_key = []
    for i in range(length):
        if alice_bases[i] == bob_bases[i]:
            sifted_key.append(alice_bits[i])

    return sifted_key

def main():
    key = generate_qkd(length=128)
    print(f"🔐 產生的共用密鑰長度: {len(key)}")
    print("前 20 位密鑰內容:", key[:20])  # 用切片比指定第20位安全

if __name__ == "__main__":
    main()
