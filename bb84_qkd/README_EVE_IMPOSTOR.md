# 🎭 Eve 假冒身份攻擊模擬（Impersonation Attack Model）

本模組 `eve_impostor_attack.py` 模擬一種進階的量子攻擊手法 —— Eve 假冒 Alice 傳送 qubit 給 Bob，同時也假冒 Bob 接收來自 Alice 的 qubit。此模型可用於理解 QKD 系統中可能遭遇的假身分攻擊情境，並觀察密鑰錯誤率（QBER）變化。

---

## 🧪 攻擊模型概念說明

| 模型階段     | 說明 |
|--------------|------|
| Alice 傳送 qubit         | 傳送原始 bit 與基底編碼 |
| Eve 偽裝 Alice           | 擅自測量並重建 qubit 傳給 Bob |
| Eve 偽裝 Bob             | 對 Alice 的 qubit 進行偽裝測量 |
| Bob 測量                 | 使用自己的基底測量 Eve 傳來的 qubit |

📌 本攻擊模型模擬「雙面偽裝」，在真實世界中對通訊雙方造成極大威脅。

---

## 📘 模擬流程說明

1. **Alice 隨機產生 bit 與基底**
2. **Eve 隨機選擇兩組基底（模仿 Alice 與 Bob）**
3. **Eve 依序測量、重建、再次測量後傳給 Bob**
4. **Bob 使用自身基底測量並產生密鑰**
5. **計算 QBER：Alice 原始密鑰 vs Bob 接收密鑰**

---

## 💻 執行方式

```bash
python eve_impostor_attack.py

📋 示意輸出格式：
🔓 Eve 假冒攻擊模擬完成
原始 Alice 密鑰（前 20 位）: [1, 0, 1, 1, 0, ...]
最終 Bob 收到密鑰（前 20 位）: [1, 1, 1, 0, 0, ...]
模擬 QBER：24.00%

📌 QBER 以百分比格式顯示，便於理解錯誤比例。

⚙️ 模組參數
目前版本固定模擬 qubit 數量為 50，若需自訂長度可修改 main() 中的 n = 50 參數。

🔗 延伸模組建議
bb84_basic.py：對照組（無攻擊），QBER 接近 0%

eve_basic_attack.py：攔截重送攻擊（Intercept-Resend）

qber_vs_intercept_ratio.py：繪製 QBER vs 攔截比例的變化圖
| 模組名稱                     | 角色類型    | 說明                            |
| ------------------------ | ------- | ----------------------------- |
| `bb84_basic.py`          | ✅ 對照組   | 無干擾下的基礎金鑰產生流程                 |
| `eve_basic_attack.py`    | ⚠️ 攔截攻擊 | Eve 攔截 qubit 後隨機測量並重送         |
| `eve_impostor_attack.py` | 🎭 假冒攻擊 | Eve 同時假冒 Alice 與 Bob 傳送 qubit |

🛡️ 開發備註
使用 Python 內建模組 random，無需額外安裝

適合用於展示 QKD 在假冒攻擊情境下的錯誤率變化

可作為紅隊模擬或 QBER 異常分析基礎

yaml


---
