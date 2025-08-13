import pytest
from bb84_qkd.utils import compute_qber, qber_status

def test_compute_qber_basic():
    assert compute_qber([0,1,1,0], [0,1,1,0]) == 0.0
    assert compute_qber([0,1,1,0], [1,1,0,0]) == 0.5

def test_compute_qber_input_validation():
    with pytest.raises(AssertionError):
        compute_qber([], [])
    with pytest.raises(AssertionError):
        compute_qber([0,1], [0])
    with pytest.raises(AssertionError):
        compute_qber([0,2], [0,1])

def test_qber_status_thresholds():
    assert qber_status(0.00).startswith("🟢")
    assert qber_status(0.10).startswith("🟢")
    assert qber_status(0.11).startswith("🟡")
    assert qber_status(0.24).startswith("🟡")
    assert qber_status(0.25).startswith("🔴")

def test_qber_status_input_validation():
    with pytest.raises(AssertionError):
        qber_status(-0.01)
    with pytest.raises(AssertionError):
        qber_status(1.01)
