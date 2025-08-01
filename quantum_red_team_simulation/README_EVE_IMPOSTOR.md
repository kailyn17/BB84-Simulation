# Eve 假冒 Bob 攻擊模型 (Eve Impostor Attack)

## 概要
本程式模擬 **Eve 假冒 Bob** 的攻擊情境。  
Eve 嘗試以 30% 機率翻轉 Alice 傳送的比特，並冒充 Bob 接收訊號。  
透過多次模擬，可以觀察 **QBER (Quantum Bit Error Rate)** 的變化，並計算平均錯誤率。

---

## 程式檔案
- `eve_impostor_bob.py`  
  單次攻擊版本，模擬一次假冒攻擊並回傳 QBER。  

- `eve_impostor_average.py`  
  多次攻擊版本，支援多次模擬並計算平均 QBER。  

---

## 使用方式

### 單次攻擊模擬
```bash
python eve_impostor_bob.py

範例輸出

[Eve 假冒 Bob 攻擊] 單次 QBER = 0.32

多次攻擊模擬

python eve_impostor_average.py

範例輸出

[Eve 假冒 Bob 攻擊] 模擬次數: 50
各次 QBER: [0.25, 0.30, 0.40, ...]
平均 QBER = 0.32

結果分析
單次 QBER 可能隨機浮動。

多次模擬後，平均 QBER 約落在 0.30 左右，符合攻擊設定 (30% 翻轉率)。

QBER 超過 11% 已可被 Alice 與 Bob 偵測到，代表此攻擊在理論上難以隱匿。

後續擴充
繪製 QBER 與模擬次數的折線圖。

與 eve_memory_attack.py 比較不同攻擊模型的 QBER 分佈。

加入 紅隊模擬腳本，結合多種攻擊模式進行對照。


---
