# 🔐 PQC × QKD 混合式密鑰交換模擬

本模擬專案展示如何結合 QKD（量子金鑰分發）與 PQC（後量子密碼學），將 BB84 協定產生的金鑰導入後量子加密模組中，實現混合式加密流程。可用於教學展示、模擬實驗與研究應用。

---

## 📈 模擬流程圖展示

以下為 PQC × QKD 混合式加密流程示意圖：  
（點擊圖片可放大預覽）

[![Hybrid Flowchart](https://github.com/kailyn17/BB84-Simulation/raw/main/pqc_qkd_hybrid/images/hybrid_flowchart.png)](https://github.com/kailyn17/BB84-Simulation/blob/main/pqc_qkd_hybrid/images/hybrid_flowchart.png)

## 📌 模擬步驟流程

1. 執行 QKD 模組產生金鑰  
2. 將 QKD 金鑰總和導出整數位移量  
3. 使用 PQC 公鑰加密文字（模擬位移加密）  
4. 解密流程中還原明文  
5. 可搭配流程圖理解整體交換過程

---

## 🧪 使用方式

先安裝所需套件：

```bash
pip install -r requirements.txt

執行主模擬程式：
python pqc_qkd_hybrid_simulation.py

產生流程圖：
python draw_hybrid_flowchart.py

📂 專案結構與說明
| 檔案名稱                           | 說明                      |
| ------------------------------ | ----------------------- |
| `pqc_qkd_hybrid_simulation.py` | 主程式：整合 QKD 金鑰與 PQC 加密模擬 |
| `qkd_module.py`                | 模擬 QKD（BB84）協定產生金鑰      |
| `pqc_module.py`                | 模擬 PQC 加密流程（整數位移邏輯）     |
| `draw_hybrid_flowchart.py`     | 自動產生流程圖                 |
| `images/hybrid_flowchart.png`  | 混合流程圖示意圖                |
| `README_HYBRID_SIM.md`         | 主程式模擬分解說明               |
| `README_PQC_MODULE.md`         | PQC 模組細節說明              |
| `README_QKD_MODULE.md`         | QKD 模組細節說明              |
| `requirements.txt`             | 所需 Python 套件列表          |

🧠 延伸應用與未來方向
🔒 國際 PQC 標準補充（Kyber、NTRU）

⚛️ QKD 實驗資料模擬與 QBER 錯誤率展示

🚨 QBER 超出安全閾值時的警示模擬（安全機制觸發）

本模組為 QKD × PQC 混合應用的模擬起點，適合教學實驗、研究延伸與國防科技應用場景分析。

---


