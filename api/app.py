# api/app.py
from __future__ import annotations

import importlib
import logging
import os
from typing import Optional, Literal, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# -------------------------
# 基礎設定
# -------------------------
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

logger = logging.getLogger("uvicorn.error")

app = FastAPI(
    title="Q-Hybrid Defense API",
    version=APP_VERSION,
    description="""
API for BB84/QKD simulation, PQC demo, and PQC×QKD hybrid key exchange.
This app auto-detects your local modules and routes accordingly.
""",
)

# CORS（如需前端調用可調整）
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ALLOW_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# 動態載入你現有的模組（有就用；沒有就回錯）
# -------------------------
def _optional_import(path: str):
    try:
        return importlib.import_module(path)
    except Exception as e:
        logger.info(f"Module '{path}' not available: {e}")
        return None

mod_bb84_basic = _optional_import("bb84_qkd.bb84_basic")
mod_qkd_module = _optional_import("qkd_module")
mod_pqc_module = _optional_import("pqc_module")
mod_hybrid = _optional_import("pqc_qkd_hybrid_simulation")
mod_eve_basic = _optional_import("bb84_qkd.eve_basic_attack")
mod_eve_impostor = _optional_import("bb84_qkd.eve_impostor_attack")

# -------------------------
# 請求/回應模型
# -------------------------
class HealthResponse(BaseModel):
    status: str
    version: str

class BB84Request(BaseModel):
    length: int = Field(256, ge=8, le=100000, description="原始位元長度")
    eve_mode: Literal["none", "basic", "impostor", "memory"] = "none"
    intercept_ratio: float = Field(0.0, ge=0.0, le=1.0)
    seed: Optional[int] = Field(None, description="隨機種子（可重現）")

class BB84Response(BaseModel):
    sifted_len: int
    qber: float
    alice_sample: str
    bob_sample: str
    notes: Optional[str] = None

class PQCEncryptRequest(BaseModel):
    plaintext: str
    key: Optional[str] = Field(None, description="若留空，模組自行產生或用預設")

class PQCEncryptResponse(BaseModel):
    ciphertext: str
    key: Optional[str] = None
    meta: Optional[dict] = None

class PQCDecryptRequest(BaseModel):
    ciphertext: str
    key: str

class PQCDecryptResponse(BaseModel):
    plaintext: str

class HybridRequest(BaseModel):
    n_bits: int = Field(256, ge=32, le=8192)
    eve_mode: Literal["none", "basic", "impostor", "memory"] = "none"
    intercept_ratio: float = Field(0.0, ge=0.0, le=1.0)
    seed: Optional[int] = None

class HybridResponse(BaseModel):
    session_key: str
    qber: float
    method: str = "PQC×QKD"
    meta: Optional[dict] = None

# -------------------------
# 工具：統一呼叫你現有的函式
# （你可以在對應模組內實作以下「預期介面」）
# -------------------------
def run_bb84(length: int, eve_mode: str, intercept_ratio: float, seed: Optional[int]) -> BB84Response:
    """
    預期優先使用：
      - qkd_module.simulate_bb84(length, eve_mode, intercept_ratio, seed) -> dict
      - 否則 bb84_qkd.bb84_basic.run_bb84(length=..., eve=..., intercept_ratio=..., seed=...)
    回傳 dict 結構需包含：sifted_len, qber, alice_key, bob_key
    """
    if mod_qkd_module and hasattr(mod_qkd_module, "simulate_bb84"):
        try:
            result = mod_qkd_module.simulate_bb84(
                length=length,
                eve_mode=eve_mode,
                intercept_ratio=intercept_ratio,
                seed=seed,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"qkd_module.simulate_bb84 error: {e}")
    elif mod_bb84_basic and hasattr(mod_bb84_basic, "run_bb84"):
        try:
            result = mod_bb84_basic.run_bb84(
                length=length,
                eve=eve_mode,
                intercept_ratio=intercept_ratio,
                seed=seed,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"bb84_basic.run_bb84 error: {e}")
    else:
        raise HTTPException(
            status_code=501,
            detail="No BB84 simulator found. Provide qkd_module.simulate_bb84(...) or bb84_qkd.bb84_basic.run_bb84(...).",
        )

    try:
        sifted = int(result["sifted_len"])
        qber = float(result["qber"])
        alice_key = str(result["alice_key"])
        bob_key = str(result["bob_key"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected BB84 result format: {e}")

    return BB84Response(
        sifted_len=sifted,
        qber=qber,
        alice_sample=alice_key[:64],
        bob_sample=bob_key[:64],
        notes=result.get("notes"),
    )

def pqc_encrypt(plaintext: str, key: Optional[str]) -> PQCEncryptResponse:
    """
    預期介面：
      - pqc_module.encrypt(plaintext: str, key: Optional[str]) -> dict{ciphertext, key?, meta?}
    """
    if not (mod_pqc_module and hasattr(mod_pqc_module, "encrypt")):
        raise HTTPException(status_code=501, detail="pqc_module.encrypt(...) not found.")
    try:
        res = mod_pqc_module.encrypt(plaintext, key)
        return PQCEncryptResponse(
            ciphertext=str(res["ciphertext"]),
            key=res.get("key"),
            meta=res.get("meta"),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"pqc_module.encrypt error: {e}")

def pqc_decrypt(ciphertext: str, key: str) -> PQCDecryptResponse:
    """
    預期介面：
      - pqc_module.decrypt(ciphertext: str, key: str) -> str/plaintext 或 dict{plaintext}
    """
    if not (mod_pqc_module and hasattr(mod_pqc_module, "decrypt")):
        raise HTTPException(status_code=501, detail="pqc_module.decrypt(...) not found.")
    try:
        res = mod_pqc_module.decrypt(ciphertext, key)
        plaintext = res["plaintext"] if isinstance(res, dict) else str(res)
        return PQCDecryptResponse(plaintext=plaintext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"pqc_module.decrypt error: {e}")

def hybrid_exchange(n_bits: int, eve_mode: str, intercept_ratio: float, seed: Optional[int]) -> HybridResponse:
    """
    預期介面：
      - pqc_qkd_hybrid_simulation.hybrid_key_exchange(n_bits, eve_mode, intercept_ratio, seed)
        -> dict{session_key, qber, meta?}
    """
    if not (mod_hybrid and hasattr(mod_hybrid, "hybrid_key_exchange")):
        raise HTTPException(status_code=501, detail="pqc_qkd_hybrid_simulation.hybrid_key_exchange(...) not found.")
    try:
        res = mod_hybrid.hybrid_key_exchange(n_bits, eve_mode, intercept_ratio, seed)
        return HybridResponse(
            session_key=str(res["session_key"]),
            qber=float(res["qber"]),
            meta=res.get("meta"),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"hybrid_key_exchange error: {e}")

# -------------------------
# 路由
# -------------------------
@app.get("/health", response_model=HealthResponse, tags=["system"])
def health():
    return HealthResponse(status="ok", version=APP_VERSION)

@app.post("/bb84/simulate", response_model=BB84Response, tags=["qkd"])
def api_bb84_simulate(req: BB84Request):
    return run_bb84(
        length=req.length,
        eve_mode=req.eve_mode,
        intercept_ratio=req.intercept_ratio,
        seed=req.seed,
    )

@app.post("/pqc/encrypt", response_model=PQCEncryptResponse, tags=["pqc"])
def api_pqc_encrypt(req: PQCEncryptRequest):
    return pqc_encrypt(plaintext=req.plaintext, key=req.key)

@app.post("/pqc/decrypt", response_model=PQCDecryptResponse, tags=["pqc"])
def api_pqc_decrypt(req: PQCDecryptRequest):
    return pqc_decrypt(ciphertext=req.ciphertext, key=req.key)

@app.post("/hybrid/exchange", response_model=HybridResponse, tags=["hybrid"])
def api_hybrid_exchange(req: HybridRequest):
    return hybrid_exchange(
        n_bits=req.n_bits,
        eve_mode=req.eve_mode,
        intercept_ratio=req.intercept_ratio,
        seed=req.seed,
    )

# -------------------------
# 本機啟動
# -------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api.app:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=bool(int(os.getenv("RELOAD", "1"))),
        log_level=os.getenv("LOG_LEVEL", "info"),
    )
