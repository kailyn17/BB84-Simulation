# 📊 QBER 攻擊分析與可視化模組

本模組 `qber_vs_intercept_ratio.py` 用於分析 Eve 攔截 qubit 對金鑰錯誤率（QBER）的影響，並以圖表與統計方式展示其趨勢。

---

## 🎯 模擬目標

- 逐步調整 Eve 攔截比例（0.0 ～ 1.0）
- 每種攔截比例進行多輪模擬，計算平均 QBER 與標準差
- 繪製「攔截比例 vs QBER」折線圖與統計表

---

## 🧠 可視化邏輯

- X 軸：Eve 攔截 qubit 的比例（%）
- Y 軸：對應的 QBER（錯誤率 %）
- 趨勢顯示：**攔截比例越高，QBER 越高**

---

## 📁 圖表輸出

- `images/qber_vs_intercept_ratio.png`：主圖表
- `images/qber_mean_std_table.png`：平均值與標準差統計表

---

## 📌 應用場景

- 用於白皮書或報告中的錯誤率解釋
- 搭配其他模組（如 Eve 攻擊）作為學術補充資料
- 作為 QKD 系統健全性驗證方式之一

---
