# 🧪 BB84 量子金鑰分發模擬專案

---

## 📘 專案簡介

本專案模擬了 BB84 量子金鑰分發 (Quantum Key Distribution, QKD) 協定的執行流程，並透過 Python 實作加入多種 Eve 攻擊模型，用來分析 BB84 面對關鍵監聽行為時的安全性變化。

本專案特色為：
- 可視化分析錯誤率 (QBER) ，用來驗證協定對攻擊的效應
- 實作包括：基礎 BB84 模擬、Eve 隨機攻擊、假写進階攻擊
- 支援採用自定義攻擊模型進行擴充與研究

---

## 📁 專案結構

```
.
├── bb84_basic.py               # 基本 BB84 協定模擬
├── eve_basic_attack.py         # Eve 攻擊 + QBER 分析
├── eve_impostor_attack.py      # Eve 假写 Alice/Bob 進階模擬
├── qber_vs_intercept_ratio.py  # QBER vs. 收盜比例解析
├── images/
│   ├── qber_vs_intercept_ratio.png       # QBER vs. 收盜圖
│   └── qber_mean_std_table.png           # QBER 數據表
├── requirements.txt           # 確保環境套件
├── LICENSE                    # MIT 授權條款
├── 自述文件.md               # 早期筆記備份
└── README.md                  # 本檔案，綜合介紹
```

---

## 🧠 實作綱要

- 模擬 Alice 與 Bob 用量子來回傳並篩選金鑰
- 實作 Eve 重送攻擊，觀察 QBER 上升變化
- 用 Matplotlib 繪製「QBER vs. 收盜比例」圖表
- 展示 Eve 假写第三方身份時的安全威脅

---

## 📊 QBER 与收盜比例關係（新增）

本模擬設計不同收盜比例 (0.0~1.0)，解析 Eve 攻擊對 BB84 安全性的影響：

> 當 Eve 採用錯誤基底進行解碼，將帶入錯誤，將影響 Bob 採檢結果

- 收盜比例越高，QBER 總變化越大
- 100%收盜時，QBER 可達約24%，證明 BB84 能採用 QBER 來偵測攻擊

### 🌎 國際標準與應用趨勢

- 🇺 **NIST PQC Finalist** ：Kyber、Dilithium 列為第一階步對懸象量子攻擊的加密機制
- 🇪 **ETSI QKD** ：推廣 QKD 與 PQC 合作通信標準
- 🌐 **ISO/IEC 23837** ：定義 QKD + PQC 組合的基約模型

---

## 🚀 延伸應用和課題

- 實作 Partial Intercept 攻擊模型
- 試驗 Memory-based Eve 與非常規攻擊子模型
- 組合 PQC + QKD 進行加密保護模擬
- 擴充為軍事/科技/金融報告應用

---

## 💻 執行指令

請確保你的 Python 環境已安裝下列套件：

```bash
pip install -r requirements.txt
```

執行程式:

```bash
python bb84_basic.py
python eve_basic_attack.py
python eve_impostor_attack.py
python qber_vs_intercept_ratio.py
```

---

## 📅 更新紀錄

- 2025/07/15 ：新增 QBER vs. 收盜比例模擬與圖表
- 2025/07/14 ：完成 Eve 假写模型第一版
- 2025/07/13 ：整合 BB84 與 Eve 攻擊程式碼

---

## 📄 授權 License

本專案採用 MIT License 授權，可自由使用、修改、分享並用於任何目的，但須保留原作者聲明。

詳要授權內容請看 [LICENSE](./LICENSE)
