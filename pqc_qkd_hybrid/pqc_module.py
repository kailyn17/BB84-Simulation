# pqc_module.py
import random

def generate_pqc_keys():
    """
    產生模擬用的 PQC 公鑰與私鑰（整數位移版本）
    回傳:
        public_key: 公鑰（正整數，用於加密）
        private_key: 私鑰（負整數，為公鑰相反，用於解密）
    """
    shift = random.randint(1, 10)  # 避免為 0，確保加密有效
    return shift, -shift

def pqc_encrypt(message, public_key):
    """
    使用公鑰將明文加密（每個字元做簡單位移）
    參數:
        message: 原始明文字串
        public_key: 用於加密的整數位移量
    回傳:
        ciphertext: 加密後的密文字串
    """
    return ''.join([chr(ord(char) + public_key) for char in message])

def pqc_decrypt(ciphertext, private_key):
    """
    使用私鑰將密文解密（還原為明文）
    參數:
        ciphertext: 加密後的密文字串
        private_key: 用於解密的整數位移量
    回傳:
        message: 還原後的明文字串
    """
    return ''.join([chr(ord(char) + private_key) for char in ciphertext])

def main():
    # 使用範例：產生金鑰並加密/解密一段訊息
    public_key, private_key = generate_pqc_keys()
    message = "Quantum"
    ciphertext = pqc_encrypt(message, public_key)
    decrypted = pqc_decrypt(ciphertext, private_key)

    print("🔐 原始訊息:", message)
    print("📦 加密後:", ciphertext)
    print("🔓 解密後:", decrypted)

if __name__ == "__main__":
    main()
