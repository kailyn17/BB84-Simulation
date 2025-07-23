# 🎭 Eve 攔截重送攻擊模擬（Intercept-Resend Model）

本模組 `eve_basic_attack.py` 模擬 BB84 協定中最基礎的量子攻擊模型 —— Eve 攔截 qubit 後使用隨機基底測量，再重新發送給 Bob（Intercept-Resend）。  
透過比較 Alice 與 Bob 的密鑰一致性，可觀察錯誤率（QBER）隨攔截比例變化的情況。

---

## 🧪 攻擊模型概念說明

| 模型階段     | 說明 |
|--------------|------|
| Alice 傳送 qubit | 使用隨機基底（Z/X）與 bit 編碼 |
| Eve 攔截測量     | 以隨機基底測量 qubit，可能造成干擾 |
| Eve 重送 qubit   | 將自身測量結果轉為 qubit 發送給 Bob |
| Bob 測量         | 以自身基底測量 Eve 傳來的 qubit |

📌 攔截比例（`intercept_ratio`）可調整 Eve 攻擊強度（1.0 = 攔截全部 qubit）

---

## 📘 模擬流程說明

1. **產生 Alice 的位元與基底**
2. **Eve 根據設定比例進行攔截與測量**
3. **Bob 接收並測量 Eve 傳來的 qubit**
4. **比對 Alice 與 Bob 密鑰，計算 QBER（錯誤率）**

---

## 💻 執行方式

```bash
python eve_basic_attack.py

📋 示意輸出格式：

Alice Key: [0, 1, 0, 1, 1, ...]
Bob Key:   [0, 1, 1, 1, 0, ...]
QBER: 20.00%

| 參數名稱              | 類型    | 預設值 | 說明                    |
| ----------------- | ----- | --- | --------------------- |
| `length`          | int   | 50  | 模擬 qubit 數量           |
| `intercept_ratio` | float | 1.0 | Eve 攔截 qubit 的比例（0～1） |

🔗 延伸模組建議
bb84_basic.py：無攻擊對照組，理想 QBER ≈ 0%

eve_impostor_attack.py：Eve 假冒 Alice/Bob 的進階版本

qber_vs_intercept_ratio.py：攔截比例 vs 錯誤率圖形化分析

| 模組名稱                     | 角色類型    | 說明                        |
| ------------------------ | ------- | ------------------------- |
| `bb84_basic.py`          | ✅ 對照組   | 無干擾狀況下建立共享密鑰              |
| `eve_basic_attack.py`    | ⚠️ 攻擊組  | 模擬最基本攔截測量後重送的攻擊方式         |
| `eve_impostor_attack.py` | 🎭 假冒攻擊 | 模擬 Eve 冒充 Alice 或 Bob 的場景 |

🛡️ 開發備註
無需額外安裝套件，僅使用 Python 內建 random 模組

攻擊模型可擴充為部分攔截、錯誤誘導或假冒身分等進階版本

適用於教學、學習歷程、密鑰錯誤率研究


---
