# pqc_module.py
import random

def generate_pqc_keys():
    """
    產生模擬用的 PQC 公鑰與私鑰 (簡化版本)
    回傳:
        public_key: 公鑰 (模擬為整數位移)
        private_key: 私鑰 (與公鑰相對)
    """
    shift = random.randint(1, 10)  # 避免為 0 無加密效果
    public_key = shift
    private_key = -shift
    return public_key, private_key

def pqc_encrypt(message, public_key):
    """
    將明文加密 (每個字元做簡單位移)
    """
    ciphertext = ''.join([chr(ord(char) + public_key) for char in message])
    return ciphertext

def pqc_decrypt(ciphertext, private_key):
    """
    將密文解密 (根據私鑰還原)
    """
    message = ''.join([chr(ord(char) + private_key) for char in ciphertext])
    return message

# 測試用主函式
def main():
    public_key, private_key = generate_pqc_keys()
    print("產生的公鑰與私鑰:", public_key, private_key)

    message = "Quantum"
    encrypted = pqc_encrypt(message, public_key)
    print("加密後:", encrypted)

    decrypted = pqc_decrypt(encrypted, private_key)
    print("解密後:", decrypted)

if __name__ == "__main__":
    main()
