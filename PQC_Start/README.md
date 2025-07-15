# 🔐 RSA 金鑰產生模擬（使用 Python cryptography 套件）

---

## 📌 專案簡介

本專案使用 Python 中的 `cryptography` 套件模擬產生 RSA 金鑰對（公鑰與私鑰），以展示現代加密中非對稱金鑰生成的基本流程。此程式可作為日後實作加密／解密／簽章驗證等應用的基礎模組。

---

## 📁 專案內容

| 檔案名稱 | 說明 |
|----------|------|
| `rsa_simulation.py` | RSA 金鑰產生模擬主程式 |
| `README.md` | 本說明文件（繁體中文） |

---

## ⚙️ 使用說明

### ✅ 執行環境

- Python 3.8+
- 已安裝 [`cryptography`](https://pypi.org/project/cryptography/) 套件

安裝方式：

```bash
pip install cryptography

▶️ 執行方式
bash
python rsa_simulation.py
執行後會印出生成的 RSA 公鑰與私鑰（PEM 格式）。

🔎 結果範例
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkq...
-----END PRIVATE KEY-----

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqh...
-----END PUBLIC KEY-----

🔧 延伸建議

加入加密與解密測試模組

模擬 RSA 簽章與驗證流程

製作圖示：金鑰生成 → 加密 → 解密的完整流程圖

實作攻擊場景，如金鑰長度不足導致的破解風險分析

📅 更新紀錄
2025/07/15：建立初版 RSA 金鑰模擬程式與自述
