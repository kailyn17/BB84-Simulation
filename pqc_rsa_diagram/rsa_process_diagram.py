import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 7))
ax.axis('off')

# 步驟文字與座標
steps = [
    ("1. 選兩個質數 p, q", (0.35, 0.85)),
    ("2. 計算 n = p × q", (0.35, 0.7)),
    ("3. 計算 φ(n) = (p-1)(q-1)", (0.35, 0.55)),
    ("4. 選定公開金鑰 e", (0.35, 0.4)),
    ("5. 求得私鑰 d", (0.35, 0.25)),
    ("6. 加密：c = m^e mod n", (0.35, 0.1)),
    ("7. 解密：m = c^d mod n", (0.35, -0.05)),
]

# 繪製方框與文字
for text, (x, y) in steps:
    rect = patches.FancyBboxPatch((x, y), 0.35, 0.08, boxstyle="round,pad=0.02",
                                   edgecolor='black', facecolor='#87CEEB')
    ax.add_patch(rect)
    ax.text(x + 0.175, y + 0.04, text, ha='center', va='center', fontsize=10)

    # 箭頭（不加在最後一個）
    if y > -0.05:
        ax.annotate('', xy=(x + 0.175, y - 0.01), xytext=(x + 0.175, y - 0.07),
                    arrowprops=dict(arrowstyle='->', lw=1.5))

# 標題
plt.title("RSA 演算法流程圖", fontsize=14, y=1.05)
plt.savefig("images/rsa_process.png", bbox_inches='tight')
plt.show()
if __name__ == "__main__":
    
# 使用範例：繪製 RSA 加解密流程圖
draw_rsa_process()
print("✅ 圖檔已輸出為 images/rsa_process.png")

