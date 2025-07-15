# 🔐 RSA 加密演算法模擬教學（入門版）

---

## 📘 專案簡介

本模擬專案使用 Python 實作 RSA 公鑰加密演算法，從金鑰生成、訊息加密、到解密流程皆涵蓋其中。RSA 為現今最廣泛使用的非對稱加密系統之一，其核心概念基於大數分解的困難性。

本專案設計簡單清晰，適合初學者理解加密技術的原理與實作邏輯，亦可作為後續進入 Post-Quantum Cryptography（PQC）學習前的基礎鋪陳。

---

## 📌 演算法流程圖

![RSA 流程圖](images/rsa_process.png)

> 可補上金鑰生成 → 加密 → 傳送 → 解密流程的圖示

---

## 🧠 模擬重點功能

- ✅ 自動生成公鑰與私鑰（使用 `cryptography` 套件）
- ✅ 將明文進行加密（使用接收者的公鑰）
- ✅ 將密文解密回原始訊息（使用接收者的私鑰）
- ✅ 全程中文註解，適合學習與教學

---

## 📂 專案結構

rsa_simulation/
├── rsa_simulation.py # 主程式：含金鑰產生、加解密流程與註解
├── images/
│ └── rsa_process.png # RSA 流程圖（示意圖，自行補圖）
└── README.md # 本說明文件


---

## 🧪 教學程式碼簡介

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 金鑰生成（使用 2048 位元）
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# 待加密的訊息（僅限英文或轉為 byte）
message = b"Quantum Security"

# 加密（使用接收者公鑰）
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# 解密（使用接收者私鑰）
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

print("原始訊息:", message)
print("解密結果:", plaintext)

🔍 注意：Python 字串若含非 ASCII（如中文）須轉為 .encode() 才能加密（例如 b"文字" 或 "文字".encode()）

📖 RSA 概念簡述（高中生也能懂！）
RSA 是一種 非對稱加密（Asymmetric Encryption）

它使用一組金鑰：公鑰（公開）、私鑰（保密）

發送者用你的公鑰加密訊息，只有你能用私鑰解開

這就是為什麼能「公開傳送」而不怕被偷聽

💡 延伸應用建議
模擬多人之間的公鑰交換與加密通訊

加入數位簽章（Digital Signature）模組

與 QKD 模擬整合 → 探討 PQC 結合模型

💻 執行方式

bash
pip install cryptography
python rsa_simulation.py

📅 更新紀錄
2025/07/15：完成 RSA 加密模擬初版與教學 README 編寫

🪪 授權方式
本專案採用 MIT License，允許自由使用、修改、散布，唯需保留原作者註明。
