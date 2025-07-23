# 📁 `pqc_qkd_hybrid/`：混合式密鑰交換模擬模組

本模組為 PQC（Post-Quantum Cryptography）與 QKD（Quantum Key Distribution）結合應用的模擬設計，展示如何將 QKD 產生的量子金鑰轉換為 PQC 的位移量，用於模擬混合加密流程。

---

## 📌 模組用途與情境

- 教學應用：可做為 NIST PQC 與 QKD 混合應用的基礎教材
- 實作練習：具工程邏輯的模組設計，模擬混合式加密場景
- 研究延伸：可進一步結合國際標準與真實應用案例（軍事/產業）

---

## 🧩 模組內容與功能說明

| 檔案名稱                       | 說明 |
|------------------------------|------|
| `pqc_qkd_hybrid_simulation.py` | 主程式，整合 QKD 金鑰導出位移量，結合 PQC 加密文字 |
| `qkd_module.py`                | QKD 模組，模擬 BB84 協定產生密鑰（隨機位元與量子基底） |
| `pqc_module.py`                | PQC 模組，簡化 Kyber 架構為整數位移式公開金鑰加密 |
| `draw_hybrid_flowchart.py`     | 流程圖產生器，輸出 hybrid_flowchart.png |
| `images/hybrid_flowchart.png`  | 混合式密鑰交換流程圖（需先執行流程圖程式生成） |
| `README_HYBRID_SIM.md`         | 主程式分步說明（範例與結果輸出） |
| `README_PQC_MODULE.md`         | PQC 模組說明 |
| `README_QKD_MODULE.md`         | QKD 模組說明 |
| `requirements.txt`             | 所需安裝的 Python 套件清單 |

---

## 🛠️ 執行方式

先安裝套件：
```bash
pip install -r requirements.txt

執行主程式：

python pqc_qkd_hybrid_simulation.py

產生流程圖：

python draw_hybrid_flowchart.py

📈 混合式流程圖展示（Hybrid Flowchart）
以下為 PQC × QKD 混合式加密流程示意圖：

![Hybrid Flowchart](./pqc_qkd_hybrid/images/hybrid_flowchart.png)
(後續會優化圖片預覽問題，可先自行參閱pqc_qkd_hybrid/images/hybrid_flowchart.png)
此圖展示如何從 QKD 金鑰推導出位移量，並搭配 PQC 進行整體加密流程的模擬應用。

📚 延伸說明
可搭配以下說明檔案閱讀：

README_HYBRID_SIM.md：主程式操作與觀察項目

README_PQC_MODULE.md：PQC 模組介紹與加密邏輯

README_QKD_MODULE.md：QKD 密鑰生成模擬原理

📌 本模組可作為後續混合式加密實驗的起點，未來可延伸加入：

國際 PQC 標準（如 Kyber、NTRU）
BB84 真實實驗數據
安全閥值、自動 QBER 告警機制（例如 QBER 異常時觸發提示）


---
