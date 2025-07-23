# 🔐 RSA 加解密流程圖模擬

本模擬專案以圖像方式呈現 RSA 演算法的關鍵步驟，包含金鑰生成與加解密邏輯，適合用於教學展示與初學者理解非對稱加密機制。

---

## 📌 演算法步驟

流程圖依序展示下列步驟：

1. 選兩個質數 `p`, `q`  
2. 計算 `n = p × q`  
3. 計算歐拉函數 `φ(n) = (p - 1)(q - 1)`  
4. 選定公開金鑰 `e`  
5. 計算私鑰 `d`  
6. 加密：`c = m^e mod n`  
7. 解密：`m = c^d mod n`  

---

## 🧪 使用方式
```bash
pip install matplotlib
python rsa_process_diagram.py

執行後，流程圖將自動輸出至：
images/rsa_process.png

<img src="images/images/rsa_process.png" width="600">

📁 資料夾結構

pqc_rsa_diagram/
├── rsa_process_diagram.py     # 繪製 RSA 流程圖的主程式
├── images/
│   └── rsa_process.png        # RSA 加解密流程圖輸出檔案
├── README.md                  # 本自述文件
└── requirements.txt           # 所需套件清單（matplotlib）

🧩 延伸應用建議
結合 RSA 實作程式碼，輔助流程理解

與 PQC 模組結合，模擬過渡期混合加密架構

擴充為互動式 CLI 工具或圖形介面展示

📄 授權 License
本專案採用 MIT License 授權，歡迎自由使用與修改。



---
