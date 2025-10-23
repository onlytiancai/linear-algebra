"""
orthographic_projection_matplotlib.py
演示：把三维点正交投影到 XY 平面 (z=0)，并画出从原点到投影点的连线（箭头）。
依赖: matplotlib, numpy
在终端或 Jupyter 中运行： python orthographic_projection_matplotlib.py
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# === 字体设置（macOS 推荐 Heiti TC）===
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
# =====================================

# 随机/自定义三维点集
np.random.seed(1)
n = 12
points = np.random.uniform(-2, 2, size=(n, 3))

# 投影矩阵 P (2x3)
P = np.array([[1, 0, 0],
              [0, 1, 0]])

# 计算投影 (x,y) 与在 z=0 的三维表示 (x,y,0)
proj_2d = (P @ points.T).T             # shape (n,2)
proj_3d = np.hstack([proj_2d, np.zeros((n,1))])  # shape (n,3)

# 创建 3D 图
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,0.6])  # 视觉上压缩 z 轴（可选）

# 绘制原始点
ax.scatter(points[:,0], points[:,1], points[:,2], s=60, label='原始点 (x,y,z)', depthshade=True)

# 绘制投影点（在 z=0 平面）
ax.scatter(proj_3d[:,0], proj_3d[:,1], proj_3d[:,2], s=70, c='red', marker='o', label='投影点 (x,y,0)')

# 绘制从每个点到其投影的连线（箭头效果用短线 + 小箭头）
for p, q in zip(points, proj_3d):
    # 线
    xs, ys, zs = [p[0], q[0]], [p[1], q[1]], [p[2], q[2]]
    ax.plot(xs, ys, zs, linestyle='--', linewidth=1, color='gray', alpha=0.7)
    # 在中点处画个小箭头（简单效果）
    mid = (p + q) / 2
    # 画一个小短线表示箭头方向
    ax.plot([mid[0], mid[0]], [mid[1], mid[1]], [mid[2], mid[2]+0.02*np.sign(q[2]-p[2])],
            color='k', linewidth=1)

# 绘制 XY 平面（z=0）作为半透明网格
xx = np.linspace(-2.5, 2.5, 10)
yy = np.linspace(-2.5, 2.5, 10)
XX, YY = np.meshgrid(xx, yy)
ZZ = np.zeros_like(XX)
ax.plot_surface(XX, YY, ZZ, alpha=0.12, rstride=1, cstride=1, shade=False)

# 轴标签和图例
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('正交投影 (x,y,z) → (x,y) ，投影矩阵 P = [[1,0,0],[0,1,0]]')
ax.legend(loc='upper right')

# 另外在图边上写出投影矩阵（用文本框）
mat_text = "P = [[1, 0, 0],\n     [0, 1, 0]]"
plt.gcf().text(0.01, 0.02, mat_text, fontsize=10, family='monospace')

plt.tight_layout()
plt.show()
