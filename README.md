# BB84 量子金鑰分發模擬專案

##  專案簡介
本專案模擬了 BB84 量子金鑰分發（Quantum Key Distribution, QKD）協定，並逐步加入不同的 Eve 攻擊模型，用於展示 QKD 在實際應用中對抗中間人攻擊（Man-in-the-Middle）與竊聽者（Eavesdropper）的強健性。

##  專案結構說明

├── bb84_basic.py # 基本 BB84 協定模擬（無 Eve）
├── eve_basic_attack.py # Eve 隨機攔截攻擊模型
├── eve_impostor_attack.py # Eve 假冒 Alice/Bob 攻擊模型（進階）
├── 自述文件.md # 初期撰寫的簡要說明
└── README.md # 本檔案，完整介紹與說明

##  實作內容（摘要）
- 模擬 Alice 與 Bob 的量子位元生成與傳送流程
- 加入 Eve 攻擊行為，觀察 QBER（Quantum Bit Error Rate）變化
- 可視化密鑰錯誤率圖表，顯示攻擊前後安全性影響
- 進階版攻擊實作：Eve 假冒 Alice 或 Bob，探討身份偽造的風險

##  可延伸研究
- 加入部分攔截攻擊、記憶型攻擊等模型
- 整合 Post-Quantum Cryptography（PQC）概念
- 探討 BB84 與 E91 協定差異與應用場景
##  如何執行

請確保已安裝 Python 3 環境，可透過終端機依序執行：

```bash
python bb84_basic.py
python eve_basic_attack.py
python eve_impostor_attack.py
