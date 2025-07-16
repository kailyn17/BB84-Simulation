# 👁️ Eve 攔截攻擊模擬（Intercept-Resend）

本模組 `eve_basic_attack.py` 模擬經典 BB84 協定中常見的「中間人攔截」攻擊情境，攻擊者 Eve 嘗試在不被察覺的情況下攔截 qubit，造成金鑰錯誤率（QBER）上升。

---

## 🔍 模擬目標

- 模擬 Eve 對每個 qubit 以隨機基底測量並重新發送的過程
- 計算 Alice 與 Bob 金鑰比對後的 QBER
- 可作為後續圖表模組（qber_vs_intercept_ratio.py）輸入來源

---

## 🧠 模擬流程摘要

1. Alice 傳送 qubit（位元 + 基底）
2. Eve 攔截，隨機選基底測量，將 qubit 重送給 Bob
3. Bob 測量後公開基底，與 Alice 比對留下正確基底的位元
4. 統計 Alice 與 Bob 金鑰錯誤率（QBER）

---

## ⚙️ 適用場景

- 示範 QKD 攻擊模型對 QBER 的影響
- 作為基礎攻擊模型與後續進階攻擊的對照範本

---

## 📁 關聯模組

- `qber_vs_intercept_ratio.py`：統計不同攔截比例下的 QBER
- `eve_impostor_attack.py`：進階假冒攻擊模型（非此模組範疇）

---
