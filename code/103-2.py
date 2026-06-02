"""
DRIVE 2D Visualization Demo (chapter_103)

Shows the full encode/decode process:
  1. Original vector x (blue)
  2. Rotated y = R x (green)
  3. sign(y) = +-1 vector (red dashed, direction only)
  4. Reconstructed x_hat = S * R^T sign(y) (orange)

Each run generates a random R and x to show how sign(y) direction
approximates y, and how R^T sign(y) recovers a direction close to x.
"""

# === 字体设置（macOS 推荐 Heiti TC）===
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
# ====================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# ---------------------------------------------------------------------------
# 工具: 随机正交矩阵 (2D)
# ---------------------------------------------------------------------------
def haar_orthogonal_2d(theta: float) -> np.ndarray:
    """2D 旋转矩阵，角度 theta 均匀来自 [0, 2π)。"""
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])


# ---------------------------------------------------------------------------
# DRIVE 编码/解码
# ---------------------------------------------------------------------------
def drive_encode_2d(x: np.ndarray, R: np.ndarray):
    y = R @ x
    sign_y = np.sign(y)
    S_mse = np.linalg.norm(y, 1) / len(x)
    S_unb = np.dot(x, x) / np.linalg.norm(y, 1)
    return y, sign_y, S_mse, S_unb


def drive_decode_2d(sign_y: np.ndarray, R: np.ndarray, S: float) -> np.ndarray:
    return S * (R.T @ sign_y)


# ---------------------------------------------------------------------------
# 可视化
# ---------------------------------------------------------------------------
def draw_vector(ax, vec, color, label, alpha=1.0, lw=2.0, ls='-'):
    """在原点到 vec 处画一个箭头."""
    ax.annotate(
        "",
        xy=vec,
        xytext=(0, 0),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                        mutation_scale=15, alpha=alpha, linestyle=ls),
        zorder=5,
    )
    # 标签
    norm = np.linalg.norm(vec)
    if norm > 0.01:
        ax.text(vec[0] * 0.55, vec[1] * 0.55, label,
                color=color, fontsize=11, fontweight='bold',
                ha='center', va='center', alpha=alpha)


def draw_circle(ax, radius, color='gray', ls='--', lw=1.0, alpha=0.5):
    circle = plt.Circle((0, 0), radius, fill=False,
                        color=color, linestyle=ls, linewidth=lw, alpha=alpha)
    ax.add_patch(circle)


# ---------------------------------------------------------------------------
# 主程序
# ---------------------------------------------------------------------------
def main():
    rng = np.random.default_rng(seed=42)

    # --- 随机生成 ---
    theta_x = rng.uniform(0, 2 * np.pi)
    # x 长度 0.5~1.5，在单位圆附近
    r_x = rng.uniform(0.8, 1.2)
    x = np.array([r_x * np.cos(theta_x), r_x * np.sin(theta_x)])

    theta_R = rng.uniform(0, 2 * np.pi)
    R = haar_orthogonal_2d(theta_R)

    y, sign_y, S_mse, S_unb = drive_encode_2d(x, R)
    x_hat_mse = drive_decode_2d(sign_y, R, S_mse)
    x_hat_unb = drive_decode_2d(sign_y, R, S_unb)

    # --- 打印过程 ---
    print("=" * 60)
    print("DRIVE 2D 可视化 — 编码/解码过程")
    print("=" * 60)
    print(f"\n[1] 原始向量 x")
    print(f"    x          = [{x[0]:+.4f}, {x[1]:+.4f}]")
    print(f"    ||x||_2    = {np.linalg.norm(x):.4f}")
    print(f"    角度 θ_x   = {np.degrees(np.arctan2(x[1], x[0])):.1f}°")

    print(f"\n[2] 随机旋转矩阵 R (角度 θ_R = {np.degrees(theta_R):.1f}°)")
    print(f"    R = [[{R[0,0]:+.4f}, {R[0,1]:+.4f}],")
    print(f"        [{R[1,0]:+.4f}, {R[1,1]:+.4f}]]")

    print(f"\n[3] 旋转向量 y = R @ x")
    print(f"    y          = [{y[0]:+.4f}, {y[1]:+.4f}]")
    print(f"    ||y||_2    = {np.linalg.norm(y):.4f}  (≈ ||x||_2，旋转保长度)")
    print(f"    角度 θ_y   = {np.degrees(np.arctan2(y[1], y[0])):.1f}°")
    print(f"    θ_y - θ_x  = {np.degrees(np.arctan2(y[1], y[0]) - np.arctan2(x[1], x[0])):.1f}°  (≈ θ_R)")

    print(f"\n[4] Quantized sign(y)")
    print(f"    sign(y)    = [{int(sign_y[0])}, {int(sign_y[1])}]  (only +/-1)")
    sx, sy = int(sign_y[0] > 0), int(sign_y[1] > 0)
    qname = {(1,1): "I", (-1,1): "II", (-1,-1): "III", (1,-1): "IV"}
    print(f"    Quadrant   : {qname[(sx*2-1, sy*2-1)]}")

    print(f"\n[5] 缩放因子")
    print(f"    S_mse      = ||y||_1 / d = {np.linalg.norm(y, 1):.4f} / 2 = {S_mse:.4f}  (MSE最优，有偏)")
    print(f"    S_unb      = ||x||_2² / ||y||_1 = {np.dot(x,x):.4f} / {np.linalg.norm(y, 1):.4f} = {S_unb:.4f}  (无偏)")

    print(f"\n[6] 解码: x_hat = S * R^T @ sign(y)")
    z = R.T @ sign_y
    print(f"    R^T @ sign(y) = [{z[0]:+.4f}, {z[1]:+.4f}]  ← 逆旋转后的方向向量")
    print(f"    x_hat_mse    = {S_mse:.4f} * z = [{x_hat_mse[0]:+.4f}, {x_hat_mse[1]:+.4f}]  (MSE 有偏)")
    print(f"    x_hat_unb    = {S_unb:.4f} * z = [{x_hat_unb[0]:+.4f}, {x_hat_unb[1]:+.4f}]  (无偏)")

    print(f"\n[7] 误差对比")
    err_mse = np.linalg.norm(x_hat_mse - x) / np.linalg.norm(x)
    err_unb = np.linalg.norm(x_hat_unb - x) / np.linalg.norm(x)
    cos_mse = float(x @ x_hat_mse) / (np.linalg.norm(x) * np.linalg.norm(x_hat_mse))
    cos_unb = float(x @ x_hat_unb) / (np.linalg.norm(x) * np.linalg.norm(x_hat_unb))
    print(f"    MSE 版本: 相对误差 = {err_mse:.4f}, cos(x, x_hat) = {cos_mse:+.4f}")
    print(f"    Unb 版本: 相对误差 = {err_unb:.4f}, cos(x, x_hat) = {cos_unb:+.4f}")
    print("=" * 60)

    # --- 绘图 ---
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("DRIVE 2D 可视化: 编码 → 量化 → 解码", fontsize=14, fontweight='bold')

    all_vecs = [x, y, sign_y * max(np.linalg.norm(x), 1.0),
                x_hat_mse, x_hat_unb]
    max_range = max(np.linalg.norm(v) for v in all_vecs) * 1.4

    titles = [
        "① 原始向量 x (蓝色) 和旋转后 y (绿色)",
        "② sign(y) 量化 (红色虚线 = ±1 方向)",
        "③ 重建 x_hat (橙色=MSE, 紫色=无偏)",
    ]
    colors = ['blue', 'green', 'red', 'orange', 'purple']
    labels_list = [
        [("x", 'blue'), ("y = R·x", 'green')],
        [("sign(y)", 'red')],
        [("x (真值)", 'blue'), ("x_hat MSE", 'orange'), ("x_hat Unb", 'purple')],
    ]

    for ax, title, labels in zip(axes, titles, labels_list):
        ax.set_xlim(-max_range, max_range)
        ax.set_ylim(-max_range, max_range)
        ax.set_aspect('equal')
        ax.axhline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
        ax.axvline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
        draw_circle(ax, 1.0, color='gray', ls=':', lw=1.0, alpha=0.4)
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("x 轴")
        ax.set_ylabel("y 轴")
        ax.grid(True, alpha=0.3)

        for lbl, col in labels:
            vec_map = {
                "x": x,
                "y = R·x": y,
                "sign(y)": sign_y * max(np.linalg.norm(x), 1.0),
                "x (真值)": x,
                "x_hat MSE": x_hat_mse,
                "x_hat Unb": x_hat_unb,
            }
            vec = vec_map[lbl]
            ls = '--' if 'sign' in lbl else '-'
            lw = 1.5 if 'sign' in lbl else 2.5
            alpha = 0.6 if 'sign' in lbl else 1.0
            draw_vector(ax, vec, col, lbl, alpha=alpha, lw=lw, ls=ls)

    # 图例
    legend_elements = [
        Line2D([0], [0], color='blue', lw=2.5, label='x (原始)'),
        Line2D([0], [0], color='green', lw=2.5, label='y = R·x (旋转后)'),
        Line2D([0], [0], color='red', lw=1.5, ls='--', label='sign(y) (量化方向)'),
        Line2D([0], [0], color='orange', lw=2.5, label='x_hat MSE (有偏)'),
        Line2D([0], [0], color='purple', lw=2.5, label='x_hat Unb (无偏)'),
    ]
    fig.legend(handles=legend_elements, loc='lower center', ncol=5,
               fontsize=10, framealpha=0.9)

    plt.tight_layout(rect=[0, 0.08, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    main()
