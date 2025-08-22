# qkd_module.py
# QKD 模組範例，僅公開接口與基礎流程

"""
Public-safe QKD module stub.
金鑰處理/抽樣/容錯/閾值細節 → 私有倉庫。
"""

class PublicQKD:
    def simulate_bb84(self, n: int = 128):
        return {"n": n, "sifted_key_len": n // 2, "qber": 0.23}  # placeholder
