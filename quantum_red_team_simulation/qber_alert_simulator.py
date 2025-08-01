# qber_alert_simulator.py
# 根據 QBER 值判斷通道安全狀態

import random

def qber_alert(qber):
    """
    根據 QBER 值判斷通道狀態
    - QBER < 0.11 → ✅ 安全
    - 0.11 ≤ QBER < 0.25 → ⚠️ 可疑
    - QBER ≥ 0.25 → 🚨 攻擊中
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
    print(f"監測到 QBER = {qber:.2f} → 狀態：{status}")

if __name__ == "__main__":
    main()
