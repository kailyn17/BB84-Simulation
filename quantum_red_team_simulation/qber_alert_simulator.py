# qber_alert_simulator.py
# QBER 狀態警示範例（自適應閾值邏輯移至私有）

"""
Public-safe demo for QBER status.
動態/自適應閾值、多參數融合與防禦觸發邏輯皆移至私有倉庫（專利準備中）。
"""

def qber_status_fixed(q: float) -> str:
    assert 0.0 <= q <= 1.0
    if q < 0.11: return "🟢 安全"
    if q < 0.25: return "🟡 可疑"
    return "🔴 攻擊中"
