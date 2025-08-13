from typing import Iterable

def compute_qber(alice_bits: Iterable[int], bob_bits: Iterable[int]) -> float:
    """簡化版 QBER 計算（公開展示用）。"""
    alice = list(alice_bits); bob = list(bob_bits)
    assert len(alice) == len(bob) and len(alice) > 0, "bits must match and be non-empty"
    for b in alice + bob:
        assert b in (0, 1), "bits must be 0 or 1"
    errors = sum(a != b for a, b in zip(alice, bob))
    return errors / len(alice)

def qber_status(qber: float) -> str:
    """簡化版狀態分類（公開展示用；動態/融合邏輯留私庫）。"""
    assert 0.0 <= qber <= 1.0, "qber must be within [0, 1]"
    if qber < 0.11: return "🟢 安全"
    if qber < 0.25: return "🟡 可疑"
    return "🔴 攻擊中"
