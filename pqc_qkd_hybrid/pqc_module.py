# pqc_module.py
# PQC 模組範例，核心加解密/映射參數移至私有倉庫

"""
Public-safe PQC module stub.
實際加解密/映射/派生/抗攻擊參數 → 私有倉庫。
"""

class PublicPQC:
    def encrypt(self, data: bytes, key: bytes) -> bytes:
        return b"demo-" + data  # placeholder

    def decrypt(self, blob: bytes, key: bytes) -> bytes:
        assert blob.startswith(b"demo-")
        return blob[len(b"demo-"):]
