# 🔐 pqc_qkd_hybrid_simulation.py 模擬主程式

本程式為 PQC（後量子密碼）與 QKD（量子金鑰分發）混合架構的簡易模擬示範，整合 QKD 產生之共享密鑰與 PQC 加解密邏輯，展現未來可能的混合安全應用。

## 📌 模擬流程

1. 使用 BB84 協定模擬產生共享 bit 密鑰
2. 將密鑰加總並轉為整數，模擬 PQC 密鑰位移量
3. 利用簡化版 PQC 模組進行文字加密與解密

## 🧪 使用方法

```bash
python pqc_qkd_hybrid_simulation.py

🧠 說明
QKD 密鑰為 [0,1] 的位元串，代表 BB84 結果

PQC 為簡化版本，每個字元做位移操作

此模擬僅作為教學與展示用途，非實際密碼演算法

📂 檔案位置建議
├── pqc_qkd_hybrid/
│   ├── pqc_qkd_hybrid_simulation.py         # 主程式：模擬 PQC（如 Kyber）與 QKD（如 BB84）混合架構
│   ├── pqc_module.py                        # 獨立 PQC 演算法模組（如簡化版 Kyber 加解密流程）
│   ├── qkd_module.py                        # QKD 封裝模組，可重用現有 BB84 模擬邏輯
│   ├── hybrid_flowchart.png                 # 混合架構流程圖（PQC+QKD 加解密與密鑰管理流程）
│   ├── images/
│   │   └── hybrid_flowchart.png             # 流程圖備份存放
│   ├── README.md                            # 自述文件，說明模擬目標、結構與應用場景
│   └── requirements.txt                     # 專案獨立套件清單（可與主專案合併）

├── LICENSE                                  # 開源授權（MIT）
└── 自述文件.md                              # 主自述總覽，整合各子模組與內容介紹

🧩 未來延伸方向
將 PQC 換成 Kyber 類似參數與密鑰交換模擬

加入 Eve 攻擊者攔截或錯誤誘導情境

模擬密鑰長度對安全性的影響

📄 授權
MIT License

---
