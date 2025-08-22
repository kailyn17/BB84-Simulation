"""
Public-safe hybrid simulation stub.
PQC×QKD 的整合流程與錯誤處理為專利核心，移至私庫。
"""

def run_hybrid_demo(sample_len: int = 128):
    return {
        "sample_len": sample_len,
        "hybrid_key_preview": "****",
        "status": "demo",
        "note": "Full hybrid algorithm is private (patent pending).",
    }
