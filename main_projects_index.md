# 🗂️ 專案結構與模組導覽 | Project Structure Index (Updated)

本專案為量子資安模擬與密碼學應用系列，涵蓋 **BB84 協定**、**Eve 攻擊模型**、**後量子加密（PQC）**、**RSA**、**混合密鑰交換**及**紅隊攻擊腳本**，並整合證書佐證與白皮書文件。

| 📁 資料夾 / 檔案                   | 主題內容                           | 代表功能或檔案                                                                                                                |
| -------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `bb84_qkd/`                      | **BB84 協定與攻擊模型**               | `bb84_basic.py`, `eve_basic_attack.py`, `eve_impostor_attack.py`, `qber_vs_intercept_ratio.py`<br>`README_BB84_BASIC.md`, `README_EVE_BASIC.md`, `README_EVE_IMPOSTOR.md`, `README_QBER_ANALYSIS.md`, `images/`（QBER 圖表等） |
| `pqc_qkd_hybrid/`                | **PQC × QKD 混合模擬**               | `pqc_qkd_hybrid_simulation.py`, `pqc_module.py`, `qkd_module.py`, `draw_hybrid_flowchart.py`<br>`README_HYBRID_SIM.md`, `README_PQC_MODULE.md`, `README_QKD_MODULE.md`, `images/hybrid_flowchart.png` |
| `pqc_rsa_diagram/`               | **RSA 流程圖與教學**                  | `rsa_process_diagram.py`, `README.md`, `images/rsa_process.png`                                                            |
| `quantum_red_team_simulation/`   | **紅隊攻擊與進階腳本**                 | `eve_impostor_bob.py`, `eve_impostor_average.py`, `eve_memory_attack.py`, `eve_qber_simulation.py`, `qber_alert_simulator.py`<br>`README_EVE_IMPOSTOR.md`, `README_EVE_MEMORY.md`, `README_RED_TEAM_DRAFT.md`, `images/eve_qber_simulation.png` |
| `tests/`                         | **測試與驗證**                        | `test_utils.py`                                                                                                            |
| `certificates_proof/`            | **多元學習證明**                       | `certificates/`（TSMC、Fulbright 辯論課程、WCS 巡迴等證書）                                                                |
| `whitepaper/`                    | **研究與申請文件**                      | `Whitepaper_BB84-PQC_Public_v3.0.pdf`, `李佳穎_白皮書_交大資工.pdf`, `李佳穎_資工系特殊選材_白皮書.pdf`                           |
| **全域文件與授權**                   |                                  | `LICENSE`, `README.md`, `main_projects_index.md`                                                                          |

---

### 🚀 導覽建議
1. **從基礎開始**：閱讀 `bb84_qkd/README_BB84_BASIC.md` 了解 QKD 基礎流程  
2. **進入攻擊模型**：依序看 `eve_basic_attack.py`、`eve_impostor_attack.py`  
3. **觀察結果**：參考 `qber_vs_intercept_ratio.py` 與 `images/` 中圖表  
4. **進階混合應用**：研究 `pqc_qkd_hybrid/` 下的 PQC × QKD 模擬  
5. **紅隊思維**：探索 `quantum_red_team_simulation/` 紅隊腳本與防禦策略  
6. **補充學習**：`certificates_proof/` 為學習佐證，`whitepaper/` 為完整研究文件  

---

### 📎 附註
- **證書資料夾**內部路徑仍在整理中，之後將更新顯示  
- 所有主要 Python 腳本已補充中文註解與工程師習慣（`main()`、`__main__`、錯誤處理）  
- 未來將持續擴增模組與改善 README  

若有使用建議、錯誤回報或改進想法，歡迎於 Issues 區回報 🙌
