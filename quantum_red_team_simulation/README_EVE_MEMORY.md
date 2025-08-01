# Eve 記憶型攻擊模型 (Eve Memory Attack)

## 概要
本程式模擬 **Eve 的記憶型攻擊 (Memory-based Attack)**。  
不同於單純的攔截或假冒，Eve 會 **暫存部分比特**，等到觀察到基底資訊後再進行竊聽或竄改。  
此攻擊比單純假冒更隱匿，可能降低被 Alice 與 Bob 偵測的機率。

---

## 程式檔案
- `eve_memory_attack.py`  
  記憶型攻擊模擬，支援設定攔截比例與翻轉策略，輸出 QBER。  

---

## 使用方式
```bash
python eve_memory_attack.py

範例輸出

[Eve 記憶型攻擊] 攔截比例: 0.50
各次 QBER: [0.12, 0.20, 0.18, ...]
平均 QBER = 0.17

結果分析
攔截比例：Eve 攔截的比特數量越高，QBER 也會隨之增加。

記憶策略：由於 Eve 會等到基底公開後再進行竊聽，部分情況下 QBER 會低於假冒型攻擊。

安全意涵：此模型展示了 部分攔截 (Partial Intercept) 的真實威脅，提醒 QKD 系統需要額外的防禦機制，例如隨機取樣檢查或強化隱私放大。

後續擴充
加入 不同攔截比例 (10% ~ 100%) 的 QBER 曲線，觀察攻擊強度與偵測機率。

與 eve_impostor_average.py 對照，分析哪種攻擊較容易被偵測。

擴展至 紅隊模擬腳本 (Red Team Simulation)，整合多種攻擊策略。


---
