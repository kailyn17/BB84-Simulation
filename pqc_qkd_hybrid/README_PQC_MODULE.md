# 📦 pqc_module.py 模組說明 — 簡化後量子加密模擬（整數位移版本）

本模組為簡化後量子密碼（Post-Quantum Cryptography, PQC）加密模擬，採用整數位移的方式實現類似 Kyber 的公開金鑰加密流程。設計目的為：

📌 初學者能快速理解公私鑰對、加解密邏輯，以及 PQC 在密鑰交換中的角色。

---

## 📘 模組功能總覽

| 函式名稱                                   | 功能說明                         |
| -------------------------------------- | ---------------------------- |
| `generate_pqc_keys()`                  | 隨機產生一組模擬用的 PQC 公鑰與私鑰（透過整數位移） |
| `pqc_encrypt(message, public_key)`     | 使用公鑰將明文逐字元加密（位移）             |
| `pqc_decrypt(ciphertext, private_key)` | 使用私鑰將密文還原為明文                 |

---

## 🔐 加密邏輯與說明

### 金鑰產生：

隨機位移值 shift ∈ [1, 10]（避免為 0，否則加密無意義）

```python
public_key = shift
private_key = -shift

加密與解密方式：
# 加密：位移每個字元
chr(ord(char) + public_key)

# 解密：逆向位移還原
chr(ord(char) + private_key)

適用範圍：英文與一般 ASCII 字元
⚠️ 本模組僅為概念模擬，實際安全性極低，請勿用於真實資料傳輸。

🧪 範例程式碼

from pqc_module import generate_pqc_keys, pqc_encrypt, pqc_decrypt

# 產生金鑰
public_key, private_key = generate_pqc_keys()

# 明文訊息
message = "Quantum"

# 加密過程
ciphertext = pqc_encrypt(message, public_key)
print("加密後:", ciphertext)

# 解密還原
recovered = pqc_decrypt(ciphertext, private_key)
print("解密後:", recovered)

📁 專案位置與關聯性

此模組位於專案子資料夾 pqc_qkd_hybrid/ 中，與以下模組整合使用：
pqc_qkd_hybrid/
├── pqc_qkd_hybrid_simulation.py   # 混合式主程式（QKD+PQC）
├── pqc_module.py                  # 本模組：後量子加密模擬
├── qkd_module.py                  # 量子金鑰分發模擬模組

🎯 適用場景
學習公私鑰概念與加解密邏輯

初步建立 PQC + QKD 混合模型的密鑰交換結構

為進階 PQC 演算法（如 Kyber、NTRU）做概念鋪墊

🚧 限制與建議
僅適用於教學與模擬用途

僅支援 ASCII 範圍，無處理超出字元錯誤

如需真實 PQC 實作，建議參考以下資源：

👉 NIST PQC Finalist: https://csrc.nist.gov/projects/post-quantum-cryptography
👉 Kyber 官方參考實作（C語言）

---
