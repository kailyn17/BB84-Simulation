# eve_impostor_bob.py
# 模擬 Eve 假冒 Bob 的攻擊模型，計算單次 QBER

"""
Public-safe stub: Eve impostor (pretend-to-be Bob) attack.

實際攻擊路徑與條件判斷已移至私有倉庫；本檔僅作為對接/教學用之介面保留。
"""

from typing import Dict, Any, Sequence

def run_impostor_bob(qubits: Sequence[int], *, noise: float = 0.0) -> Dict[str, Any]:
    """
    :param qubits: 示意輸入
    :param noise: 佔位參數（公開版不使用）
    :return: 固定示例，不含真實攻擊與通訊互動細節
    """
    return {
        "qber": 0.30,         # placeholder
        "detected": True,     # placeholder
        "note": "public demo; full logic is private (patent pending).",
    }
