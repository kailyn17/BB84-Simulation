# 🗂️ 專案結構與模組導覽 | Project Structure Index

此開源專案為量子資安模擬與密碼學應用系列，涵蓋 BB84 協定、Eve 攻擊模型、後量子加密（PQC）、傳統 RSA 加密、混合式密鑰交換架構與紅隊攻擊模擬。

| 📁 資料夾                         | 主題內容                 | 代表功能或檔案                                                                  |
| ------------------------------ | -------------------- | ------------------------------------------------------------------------ |
| `bb84_qkd/`                    | BB84 協定模擬 + 攻擊模型     | `bb84_basic.py`, `eve_basic_attack.py`, `qber_vs_intercept_ratio.py`     |
| `pqc_qkd_hybrid/`              | 後量子密碼 × QKD 混合密鑰交換模擬 | `pqc_qkd_hybrid_simulation.py`, `images/hybrid_flowchart.png`            |
| `pqc_rsa_diagram/`             | RSA 加解密流程圖示與模擬程式     | `rsa_process_diagram.py`, `images/rsa_process.png`                       |
| `quantum_red_team_simulation/` | 量子資安紅隊攻擊模擬腳本         | `eve_impostor_bob.py`, `eve_memory_attack.py`, `qber_alert_simulator.py` |
| `certificates_proof/`          | 多元學習證明與參與紀錄          | 台積電、布萊恩課程、科教館參訪等證書資料與補充說明                                                |
| `whitepaper/`                  | 申請用白皮書文件（PDF）        | `李佳穎_白皮書_交大資工.pdf`                                                       |
| `images/`                      | 各模組對應的圖像與可視化資源       | QBER 圖、流程圖、表格圖片等                                                         |
| `LICENSE`                      | 授權條款（MIT License）    | 全專案套用 MIT 開源授權                                                           |
| `自述文件.md`                      | 中文主自述文件（README）      | 專案說明與背景導覽                                                                |

---

🚀 導覽建議（建議閱讀順序）
從 bb84_qkd/README_BB84_BASIC.md 開始了解 QKD 基礎流程

接著進入 eve_basic_attack.py 與 eve_impostor_attack.py，了解攻擊者模型設計

參考 qber_vs_intercept_ratio.py 與圖表，觀察錯誤率變化

閱讀 pqc_qkd_hybrid/ 模擬，體會 QKD 與 PQC 混合應用的安全策略

最後探索 quantum_red_team_simulation/ 紅隊腳本，思考真實攻擊情境下的防禦對策

補充：certificates_proof/ 可查閱相關證書與學習佐證、whitepaper/ 為本次申請之完整研究文件

📎 其他說明

所有模擬程式皆具備中文註解，並盡可能維持工程師風格（含主函式、模組結構）

本專案將持續擴充更多模組與紅隊攻擊腳本

若有使用建議、錯誤回報或改進想法，歡迎於 Issues 區回報 🙌
