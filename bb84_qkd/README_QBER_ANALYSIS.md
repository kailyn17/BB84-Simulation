# 📈 QBER 與攔截比例圖像模擬

本模組 `qber_vs_intercept_ratio.py` 用於繪製 BB84 協定中，**攔截比例與 QBER（Quantum Bit Error Rate）之間的變化圖**。可視化攔截攻擊對密鑰錯誤率的影響，有助於進一步理解量子金鑰分發的安全性。

---

## 🧪 模擬概念

模擬過程中，設定 Eve 以不同攔截比例（0～1）對 qubit 進行測量，再將 qubit 傳給 Bob。

- 攔截比例越高，Eve 對通訊干擾越強
- QBER 為 Alice 與 Bob 產生密鑰的錯誤比例
- 圖表展示 QBER 隨攔截比例變化的趨勢

---

## 💻 執行方式

```bash
python qber_vs_intercept_ratio.py

執行後會：

自動產生 QBER 與攔截比率的圖像

將圖片儲存於 images/qber_vs_intercept_ratio.png

✅ 圖片預設大小為 500 qubit，Y 軸限制在 0～0.6 之間
✅ 結果圖檔可用於報告、教學或與其他模組比對

| 攔截比例 | 對應 QBER |
| ---- | ------- |
| 0.0  | 約 0.0   |
| 0.5  | 約 0.25  |
| 1.0  | 約 0.5   |

圖像預期呈現遞增趨勢，代表攻擊強度越高，錯誤率越高。

📎 注意事項
請確認 images/ 資料夾存在，否則圖片將無法儲存

若原檔名為 .png.png 請改為 .png 以利後續使用與顯示

可自行修改 n 值調整模擬長度（預設 500）

| 模組名稱                         | 功能定位       | 說明               |
| ---------------------------- | ---------- | ---------------- |
| `qber_vs_intercept_ratio.py` | 📈 錯誤率分析模組 | QBER 對攔截比例之關係圖繪製 |
| `eve_basic_attack.py`        | ⚠️ 攻擊模擬    | 攔截單次攻擊的錯誤率觀察     |
| `bb84_basic.py`              | ✅ 對照模組     | 無攻擊時的理想密鑰產生流程    |

🛡️ 開發備註
使用套件：matplotlib、random（請先安裝 matplotlib）

所有邏輯封裝於 plot_qber_vs_intercept_ratio() 函式中

適用於教學演示、錯誤率分析、模組對照


---

