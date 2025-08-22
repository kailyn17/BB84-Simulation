# eve_impostor_attack.py
# Eve 假冒 Bob 攻擊模擬，測試協議防禦能力（細節保護中）

"""
Public-safe stub for impostor attack.
完整策略與權重/閾值設計為私有實作（專利準備中）。
"""

from typing import Sequence, Dict

def run_impostor_demo(qubits: Sequence[int]) -> Dict[str, float]:
    return {"qber": 0.27, "success_rate": 0.5, "note": "public demo; full logic private"}
