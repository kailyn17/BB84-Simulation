# 🧪 BB84 量子金鑰分發模擬專案

---

## 📘 專案簡介

本專案模擬了 BB84 量子金鑰分發（Quantum Key Distribution, QKD）協定，並逐步加入不同的 Eve 攻擊模型，用於展示 QKD 在實際應用中對抗中間人攻擊（Man-in-the-Middle）與竊聽者（Eavesdropper）的強健性。透過 Python 實作，我們探討 BB84 協定在面對不同攻擊策略時的 QBER（Quantum Bit Error Rate）變化，並透過圖表可視化驗證其安全性。

---

## 📁 專案結構說明

| 檔案名稱 | 說明 |
|----------|------|
| `bb84_basic.py` | 基本 BB84 協定模擬（無 Eve） |
| `eve_basic_attack.py` | Eve 攔截 qubit 攻擊 + QBER 分析 |
| `eve_impostor_attack.py` | Eve 假冒 Alice 或 Bob 的進階攻擊模型 |
| `qber_vs_intercept_ratio.py` | 繪製攔截比例 vs QBER 圖表 |
| `images/qber_vs_intercept_ratio.png` | 攔截比例與 QBER 的可視化圖表 |
| `images/qber_mean_std_table.png` | QBER 資料的平均與標準差圖表 |
| `README.md` | 本說明文件 |

---

## 🧠 實作內容摘要

- 🔹 模擬 Alice 與 Bob 的量子位元生成與傳送流程  
- 🔹 加入 Eve 攻擊行為（攔截、假冒），觀察 QBER 變化  
- 🔹 以圖表可視化 QBER 與攔截比例之關係  
- 🔹 探討 QKD 在身份偽造與中間人攻擊下的安全性

---

## 📊 QBER 與攔截比例模擬

程式 `qber_vs_intercept_ratio.py` 中設計了 0.0～1.0 攔截比例（每次間距 0.1），觀察 QBER（錯誤率）變化趨勢。攔截比例越高，Eve 的干擾越強，QBER 越高。

📈 結果圖示：

![QBER 圖](images/qber_vs_intercept_ratio.png)

📋 QBER 資料來源（平均與標準差）：

![QBER 數據表](images/qber_mean_std_table.png)

---

## 📚 BB84 與 E91 協定比較（延伸補充）

| 比較項目         | BB84 協定                                      | E91 協定                                           |
|------------------|-----------------------------------------------|----------------------------------------------------|
| 發表年份         | 1984（Bennett & Brassard）                   | 1991（Artur Ekert）                                |
| 核心原理         | 利用隨機基底進行單光子編碼與測量              | 利用糾纏粒子對與貝爾不等式（Bell's inequality）     |
| 使用基底         | Z（+）與 X（×）                                | 根據量子糾纏與隨機量測方向                         |
| 抵禦攻擊         | 可偵測竊聽造成的錯誤（透過 QBER）             | 透過違反貝爾不等式來驗證糾纏是否受干擾              |
| 需不需要可信設備 | 是（需信任測量裝置）                          | 否（可實作裝置無關的安全性，DI-QKD）               |
| 實作難度         | 較低，已商業化部署                             | 較高，需建立穩定量子糾纏來源                        |
| 目前應用現況     | 已應用於部分衛星通訊、光纖 QKD 系統           | 多用於學術研究與安全性驗證用途                     |

> 📌 本專案聚焦於 BB84，但後續可延伸 E91 對應模擬或攻擊模型比較。

---

## 🚀 可延伸研究方向

- 🧪 部分攔截（Partial Intercept）、記憶型 Eve 攻擊邏輯
- 🔐 整合 PQC（Post-Quantum Cryptography）模擬與 QKD 結構
- 🔄 探討 BB84 與 E91 協定於實務應用的優劣比較
- 📈 建立 QBER 誤差條圖、風險模型與可視化資料分析工具
- 🛡️ 設計預警模組作為國防通訊下的安全實驗架構

---

## 💻 如何執行

請確認已安裝 Python 3 及套件 `matplotlib`：

```bash
pip install matplotlib
python bb84_basic.py
python eve_basic_attack.py
python eve_impostor_attack.py
python qber_vs_intercept_ratio.py

📅 更新紀錄
2025/07/23：整合 BB84 與 E91 比較段落，修正圖檔引用與說明

2025/07/15：新增 QBER vs 攔截比例模擬程式與圖表

2025/07/14：完成 Eve 假冒模型的初版程式架構

2025/07/13：整合基本 BB84 與攻擊模擬模組


---
