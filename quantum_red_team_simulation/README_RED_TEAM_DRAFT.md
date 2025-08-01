# Quantum Red Team Simulation (Draft)

## 1. 模組簡介
本模組用於模擬紅隊對量子金鑰分配 (QKD, BB84) 的攻擊情境，並透過 QBER (Quantum Bit Error Rate) 的觀察，進一步判斷通道是否遭受竊聽或惡意干擾。  
此部分屬於 **紅隊視角 (Red Team Perspective)** 的初步成果，提供 QKD 系統在攻擊下的可視化與安全判斷依據。

---

## 2. QBER 趨勢圖 (Visualization)

在 Eve 攻擊 Alice 與 Bob 的傳輸通道時，QBER 會隨時間/實驗次數浮動，若 QBER 過高，則代表可能存在竊聽或干擾。

### 折線圖展示
![QBER 趨勢圖](images/eve_qber_simulation.png)

- 藍線：每次實驗的 QBER  
- 紅線：平均 QBER (0.31)  

---

## 3. QBER 數據統計 (Statistical Results)

以下為 10 次模擬實驗的 QBER 結果：

| 實驗次數 | QBER |
|----------|------|
| 1  | 0.20 |
| 2  | 0.35 |
| 3  | 0.30 |
| 4  | 0.35 |
| 5  | 0.25 |
| 6  | 0.45 |
| 7  | 0.25 |
| 8  | 0.35 |
| 9  | 0.25 |
| 10 | 0.35 |

**平均值 (Mean QBER)：** 0.31  
**標準差 (Std)：** 0.07  

> 📌 解讀：QBER 大於 **0.25** 的情境已顯示攻擊痕跡，超過安全閾值。

---

## 4. QBER 安全狀態模擬 (Alert Simulation)

為了讓系統能即時判斷 QKD 通道是否安全，以下程式根據 QBER 數值給出三種狀態：

```python
# qber_alert_simulator.py
# 根據 QBER 值判斷通道安全狀態

import random

def qber_alert(qber):
    """
    根據 QBER 值判斷通道狀態
    - QBER < 0.11  → ✅ 安全
    - 0.11 ≦ QBER < 0.25 → ⚠️ 可疑
    - QBER ≧ 0.25 → 🚨 攻擊中
    """
    if qber < 0.11:
        return "✅ 安全"
    elif qber < 0.25:
        return "⚠️ 可疑"
    else:
        return "🚨 攻擊中"

def main():
    qber = random.uniform(0, 0.4)
    status = qber_alert(qber)
    print(f"監測到 QBER = {qber:.2f} → 狀態: {status}")

if __name__ == "__main__":
    main()

5. 未來延伸方向
加入更多攻擊模型（例如：部分攔截、記憶型攻擊、假冒攻擊）

結合 PQC × QKD 混合架構，測試紅隊攻擊下的防禦效能

建立即時監測系統，輸出報表與安全警示

📌 本文件為 草稿版本 (Draft)，隨著後續紅隊模組的完整實作將持續更新。

---

