# draw_hybrid_flowchart.py
"""
產生 PQC × QKD 混合式加密流程圖
會自動輸出 hybrid_flowchart.png 到 images 資料夾
"""

import os
from graphviz import Digraph

def generate_flowchart():
    os.makedirs('pqc_qkd_hybrid/images', exist_ok=True)
    dot = Digraph(comment="PQC × QKD 混合流程圖")

    # Alice 端
    dot.node('A1', '🔐 Alice：輸入明文')
    dot.node('A2', '⚛️ QKD：產生共享密鑰（BB84）')
    dot.node('A3', '🔒 PQC 加密明文（用 QKD 密鑰）')
    dot.node('T', '📡 傳送密文')

    # Bob 端
    dot.node('B1', '⚛️ QKD：取得密鑰')
    dot.node('B2', '🔓 PQC 解密密文')
    dot.node('B3', '📩 還原明文')

    # 流程連線
    dot.edge('A1', 'A2')
    dot.edge('A2', 'A3')
    dot.edge('A3', 'T')
    dot.edge('T', 'B1')
    dot.edge('B1', 'B2')
    dot.edge('B2', 'B3')

    # 輸出圖檔（.png）
    dot.render('pqc_qkd_hybrid/images/hybrid_flowchart', format='png', cleanup=True)
    print("✅ 流程圖已產生 → images/hybrid_flowchart.png")

if __name__ == "__main__":
    generate_flowchart()
