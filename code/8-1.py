# -*- coding: utf-8 -*-
"""
Phase portrait and eigenvectors for the linear system x' = A x.
Requires: numpy, matplotlib, scipy
保存为 plot_phase.py 并运行： python plot_phase.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ---------- 配置矩阵 A（可替换为你感兴趣的矩阵） ----------
A = np.array([[2.0, 0.0],
              [0.0, 1.0]])   # 示例：对角矩阵，两个实特征值 2 和 1

A = np.array([[4.0, 1.0],
              [0.0, 2.0]]) 

A = np.array([[-2, 0],
              [0.0, -1.0]]) 

A = np.array([[2, 0],
              [0.0, -1.0]]) 
# ---------- 绘图网格，用 quiver 显示向量场 ----------
x_min, x_max, y_min, y_max = -5, 5, -5, 5
nx, ny = 20, 20
x = np.linspace(x_min, x_max, nx)
y = np.linspace(y_min, y_max, ny)
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

plt.figure(figsize=(8,8))
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=20, alpha=0.6)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)

# ---------- 计算并绘制若干轨线（不同初始条件） ----------
def lin_sys(t, z):
    return A.dot(z)

t_span = (0.0, 3.0)     # 向前看 0 到 3 秒
t_eval = np.linspace(t_span[0], t_span[1], 200)

# 选择几组初始条件（环绕原点）
init_conds = [
    np.array([4.0, 0.5]),
    np.array([0.5, 4.0]),
    np.array([3.0, 3.0]),
    np.array([-3.0, 1.0]),
    np.array([1.0, -3.0]),
    np.array([-2.5, -2.5]),
]

for z0 in init_conds:
    sol = solve_ivp(lin_sys, t_span, z0, t_eval=t_eval, rtol=1e-8)
    plt.plot(sol.y[0], sol.y[1], linewidth=1.5)

# 也画向后（t < 0）的轨线，帮助看稳定/不稳定流形
t_span_back = (0.0, -3.0)
t_eval_back = np.linspace(t_span_back[0], t_span_back[1], 200)
for z0 in init_conds:
    solb = solve_ivp(lin_sys, t_span_back, z0, t_eval=t_eval_back, rtol=1e-8)
    plt.plot(solb.y[0], solb.y[1], linewidth=1.0, linestyle='--', alpha=0.7)

# ---------- 计算并绘制特征值/特征向量 ----------
eigvals, eigvecs = np.linalg.eig(A)
origin = np.zeros(2)
max_eigvec_len = 4.5   # 绘图时特征向量伸缩因子

for i in range(len(eigvals)):
    v = eigvecs[:, i].real
    # 统一伸缩以便显示
    v_plot = (v / np.linalg.norm(v)) * max_eigvec_len
    plt.plot([0, v_plot[0]], [0, v_plot[1]], linewidth=3, label=f"eig {i+1}: {eigvals[i]:.2g}")
    plt.plot([0, -v_plot[0]], [0, -v_plot[1]], linewidth=3)  # 画正反两个方向

# ---------- 美化与标注 ----------
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(r'Phase portrait for $\dot{x}=Ax$' + f'\nA = {A.tolist()}')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

# ---------- 显示或保存 ----------
plt.tight_layout()
plt.show()
# plt.savefig("phase_portrait.png", dpi=300)
