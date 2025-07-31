import random

def qber_alert(qber):
    if qber < 0.11:
        return "✅ 安全"
    elif qber < 0.25:
        return "⚠️ 可疑"
    else:
        return "🚨 攻擊中"

def main():
    # 模擬 QBER 值
    qber = random.uniform(0, 0.4)
    status = qber_alert(qber)
    print(f"監測到 QBER = {qber:.2f} → 狀態：{status}")

if __name__ == "__main__":
    main()

