# 🗂️ 專案結構與模組導覽 | Project Structure Index

此開源專案為量子資安模擬與密碼學應用系列，涵蓋 BB84 協定、Eve 攻擊模型、後量子加密（PQC）、傳統 RSA 加密、混合式密鑰交換架構與紅隊攻擊模擬。

| 📁 資料夾                         | 主題內容                 | 代表功能或檔案                                                                                                                                                                                                                                       |
| ------------------------------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bb84_qkd/`                    | BB84 協定模擬 + 攻擊模型     | `bb84_basic.py`, `eve_basic_attack.py`, `eve_impostor_attack.py`, `qber_vs_intercept_ratio.py`, `README_BB84_BASIC.md`, `README_EVE_BASIC.md`, `README_EVE_IMPOSTOR.md`, `README_QBER_ANALYSIS.md`, `images/`                                 |
| `pqc_qkd_hybrid/`              | 後量子密碼 × QKD 混合密鑰交換模擬 | `pqc_qkd_hybrid_simulation.py`, `pqc_module.py`, `qkd_module.py`, `draw_hybrid_flowchart.py`, `README_HYBRID_SIM.md`, `README_PQC_MODULE.md`, `README_QKD_MODULE.md`, `images/hybrid_flowchart.png`                                           |
| `pqc_rsa_diagram/`             | RSA 加解密流程圖示與模擬程式     | `rsa_process_diagram.py`, `README.md`, `images/rsa_process.png`                                                                                                                                                                               |
| `quantum_red_team_simulation/` | 量子資安紅隊攻擊模擬腳本         | `eve_impostor_bob.py`, `eve_impostor_average.py`, `eve_memory_attack.py`, `eve_qber_simulation.py`, `qber_alert_simulator.py`, `README_EVE_IMPOSTOR.md`, `README_EVE_MEMORY.md`, `README_RED_TEAM_DRAFT.md`, `images/eve_qber_simulation.png` |
| `certificates_proof/`          | 多元學習證明與參與紀錄          | `certificates/`（台積電半導體雲端學院、傅爾布萊特英文辯論課程、WCS 高中女生科學教育巡迴計畫等證書）                                                                                                                                                                                       |
| `whitepaper/`                  | 申請用白皮書文件（PDF）        | `李佳穎_白皮書_交大資工.pdf`(第一版本), `李佳穎_資工系特殊選材_白皮書.pdf`(最新版本)                                                                                                                                                                                                     |
| `images/`                      | 全域圖像與可視化資源           | `qber_mean_std_table.png`, `qber_vs_intercept_ratio.png` 等                                                                                                                                                                                    |
| `LICENSE`                      | 授權條款（MIT License）    | 全專案套用 MIT 開源授權                                                                                                                                                                                                                                |
| `README.md` / `自述文件.md`        | 主自述文件（README）        | 專案總覽與導讀                                                                                                                                                                                                                                       |
| `main_projects_index.md`       | 專案目錄索引               | 總覽所有模組與成果                                                                                                                                                                                                                                     |
                                                                                                                                                                                                                             |

---

🚀 導覽建議（建議閱讀順序）
從 bb84_qkd/README_BB84_BASIC.md 開始了解 QKD 基礎流程

接著進入 eve_basic_attack.py 與 eve_impostor_attack.py，了解攻擊者模型設計

參考 qber_vs_intercept_ratio.py 與圖表，觀察錯誤率變化

閱讀 pqc_qkd_hybrid/ 模擬，體會 QKD 與 PQC 混合應用的安全策略

最後探索 quantum_red_team_simulation/ 紅隊腳本，思考真實攻擊情境下的防禦對策

補充：certificates_proof/ 可查閱相關證書與學習佐證、whitepaper/ 為本次申請之完整研究文件

📎 其他說明

註:部分證書還在修復圖片顯示問題，證書證明文件資料夾certificates_proof/目前仍有路徑問題，後續會更新完整

所有模擬程式皆具備中文註解，並盡可能維持工程師風格（含主函式、模組結構）

本專案將持續擴充更多模組與紅隊攻擊腳本

若有使用建議、錯誤回報或改進想法，歡迎於 Issues 區回報 🙌
