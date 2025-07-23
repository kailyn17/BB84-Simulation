# 🔐 RSA 加解密流程圖模擬

本模擬專案以圖像方式呈現 RSA 演算法的關鍵步驟，包含金鑰生成與加解密邏輯，適合用於教學展示與初學者理解非對稱加密機制。

---

## 🖼️ 模擬流程圖預覽

<p align="center">
  <img src="https://github.com/kailyn17/BB84-Simulation/blob/main/pqc_rsa_diagram/images/rsa_process.png?raw=true" width="600">
</p>

流程圖展示了 RSA 金鑰產生與加解密的基本步驟（如 p、q 的選擇與 φ(n)、加密與解密公式等）。

---

## 🧪 執行方式

請先安裝必要套件（若未安裝 `matplotlib`）：

```bash
pip install matplotlib

接著執行：

python rsa_process_diagram.py

成功執行後會於 images/ 資料夾自動輸出：

pqc_rsa_diagram/images/rsa_process.png

📘 演算法步驟（對照流程圖）
選兩個質數 p, q

計算 n = p × q

計算歐拉函數 φ(n) = (p - 1)(q - 1)

選定公開金鑰 e

計算私鑰 d

加密：c = m^e mod n

解密：m = c^d mod n

🌱 延伸應用與說明
本模擬可作為理解非對稱加密的入門範例，未來可結合下列主題：

模擬實際 RSA 加解密過程

改寫為更貼近實際安全需求的參數位元長度

對接 QKD/PQC 架構，探討 RSA 與量子加密技術的落差

---

