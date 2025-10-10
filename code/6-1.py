# -*- coding: utf-8 -*-
"""
二维行列式性质演示：行替换（Row Replacement）
R_j <- R_j + k * R_i 不改变行列式（平行四边形面积不变）
✅ 中文字体 Heiti TC
✅ 多行文本矩阵显示（非 LaTeX）
✅ 统一坐标范围
✅ 网格线每 0.5 间隔
✅ 半透明填充视觉更直观
"""

import numpy as np
import matplotlib.pyplot as plt

# === 字体设置（macOS 推荐 Heiti TC）===
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
# =====================================

# 原矩阵 A (2x2)
A = np.array([[2.0, 1.0],
              [0.5, 1.5]])


# 行替换参数
i_row = 0
j_row = 1
k = 2.0

# 替换后矩阵 B
B = A.copy()
B[j_row, :] = B[j_row, :] + k * B[i_row, :]

# 行列式
detA = np.linalg.det(A)
detB = np.linalg.det(B)

# --- 定义绘制函数 ---
def plot_parallelogram(ax, v1, v2, title, label, M, det_val, color):
    origin = np.array([0.0, 0.0])
    corners = np.array([origin, v1, v1 + v2, v2, origin])
    # 填充半透明区域
    ax.fill(corners[:,0], corners[:,1], color=color, alpha=0.3)
    ax.plot(corners[:,0], corners[:,1], '-o', linewidth=2, color=color)
    ax.arrow(0, 0, v1[0], v1[1], head_width=0.08, length_includes_head=True, color=color)
    ax.arrow(0, 0, v2[0], v2[1], head_width=0.08, length_includes_head=True, color=color)
    ax.set_aspect('equal', 'box')

    # 网格设置：每 0.5 一格
    ax.set_xticks(np.arange(x_min, x_max + 0.1, 0.5))
    ax.set_yticks(np.arange(y_min, y_max + 0.1, 0.5))
    ax.grid(True, linestyle='--', alpha=0.6)

    ax.set_title(f"{title}\n|det|={abs(det_val):.2f}", fontsize=12)
    
    # 显示矩阵文本
    text = f"{label} = [\n  {M[0,0]:.2f}   {M[0,1]:.2f}\n  {M[1,0]:.2f}   {M[1,1]:.2f}\n]"
    ax.text(0.02, 0.98, text, transform=ax.transAxes,
            verticalalignment='top', fontsize=12, fontfamily='Heiti TC',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

# 列向量
v1_A, v2_A = A[:,0], A[:,1]
v1_B, v2_B = B[:,0], B[:,1]

# 统一坐标范围
all_points = np.array([
    [0,0],
    v1_A, v2_A, v1_A+v2_A,
    v1_B, v2_B, v1_B+v2_B
])
x_min, x_max = all_points[:,0].min() - 0.5, all_points[:,0].max() + 0.5
y_min, y_max = all_points[:,1].min() - 0.5, all_points[:,1].max() + 0.5

# 绘图
fig, axes = plt.subplots(1, 2, figsize=(11,5))
plot_parallelogram(axes[0], v1_A, v2_A, "原矩阵 A", "A", A, detA, color="tab:blue")
plot_parallelogram(axes[1], v1_B, v2_B, "行替换后矩阵 B", "B", B, detB, color="tab:orange")

# 设置统一坐标范围
for ax in axes:
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

plt.suptitle("二维行列式性质：行替换不改变平行四边形面积（Row Replacement）", fontsize=14)
plt.tight_layout()
plt.show()
