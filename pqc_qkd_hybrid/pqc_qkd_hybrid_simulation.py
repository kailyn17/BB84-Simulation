# pqc_qkd_hybrid_simulation.py
from pqc_module import generate_pqc_keys, pqc_encrypt, pqc_decrypt
from qkd_module import generate_qkd_key

def main():
    print("🔐 PQC + QKD 混合式密鑰交換模擬\n")
    print("=== Step 1: 透過 QKD 協定產生共享密鑰 ===")
    
    # 模擬 QKD 協定取得對稱密鑰（假設長度 16）
    qkd_key = generate_qkd_key(length=16)
    print("QKD 產生的共享密鑰（bit 串）:")
    print(qkd_key)

    print("\n=== Step 2: 將 QKD 密鑰轉換成 PQC 用的位移量 ===")
    # 將 QKD 密鑰轉成整數作為 PQC 加密用途（模擬混合）
    key_sum = sum(qkd_key)
    qkd_shift = key_sum % 10 + 1  # 保證不為 0
    print("QKD 推導出的位移量（模擬用）:", qkd_shift)

    print("\n=== Step 3: 使用 PQC 模組進行加解密 ===")
    message = "QuantumHybrid"
    ciphertext = pqc_encrypt(message, qkd_shift)
    decrypted = pqc_decrypt(ciphertext, -qkd_shift)

    print("原始訊息:", message)
    print("加密後密文:", ciphertext)
    print("解密後還原:", decrypted)

if __name__ == "__main__":
    main()
