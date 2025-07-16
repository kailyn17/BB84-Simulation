# rsa_simulation.py
# 模擬產生 RSA 公私鑰對，並印出 PEM 格式金鑰

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# 產生 RSA 私鑰（2048 bits）
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# 匯出私鑰（PEM 格式，無密碼保護）
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# 產生對應公鑰
public_key = private_key.public_key()

# 匯出公鑰（PEM 格式）
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 顯示結果
print("🔐 產生的 RSA 私鑰（PEM 格式）：\n")
print(pem_private.decode())

print("\n📡 對應的 RSA 公鑰（PEM 格式）：\n")
print(pem_public.decode())

