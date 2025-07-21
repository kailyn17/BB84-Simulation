# draw_hybrid_flowchart.py
"""
使用 matplotlib 與 networkx 畫出 PQC × QKD 混合流程圖
圖檔會輸出為 images/hybrid_flowchart.png
"""

import matplotlib.pyplot as plt
import networkx as nx
import os

def generate_flowchart():
    G = nx.DiGraph()

    # 節點設定（照順序命名）
    G.add_node("A1", label="🔐 Alice：輸入明文")
    G.add_node("A2", label="⚛️ QKD：產生共享密鑰\n（BB84）")
    G.add_node("A3", label="🔒 PQC 加密明文\n（用 QKD 密鑰）")
    G.add_node("T",  label="📡 傳送密文")
    G.add_node("B1", label="⚛️ QKD：取得密鑰")
    G.add_node("B2", label="🔓 PQC 解密密文")
    G.add_node("B3", label="📩 還原明文")

    # 邊設定
    G.add_edges_from([
        ("A1", "A2"),
        ("A2", "A3"),
        ("A3", "T"),
        ("T", "B1"),
        ("B1", "B2"),
        ("B2", "B3")
    ])

    # 圖片輸出資料夾
    output_dir = os.path.join(os.path.dirname(__file__), "images")
    os.makedirs(output_dir, exist_ok=True)

    # 圖形位置設定（從上往下）
    pos = {
        "A1": (0, 6),
        "A2": (0, 5),
        "A3": (0, 4),
        "T":  (0, 3),
        "B1": (0, 2),
        "B2": (0, 1),
        "B3": (0, 0),
    }

    # 取得節點標籤
    labels = nx.get_node_attributes(G, 'label')

    # 繪製流程圖
    plt.figure(figsize=(6, 9))
    nx.draw(
        G, pos, with_labels=True, labels=labels,
        node_size=3000, node_color="#CDEFFD",
        font_size=10, font_family='sans-serif',
        edge_color="gray", arrowsize=20
    )

    # 圖片輸出完整路徑
    output_path = os.path.join(output_dir, "hybrid_flowchart.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"✅ 成功輸出流程圖：{output_path}")

if __name__ == "__main__":
    generate_flowchart()
    
