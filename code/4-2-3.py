import numpy as np
import matplotlib.pyplot as plt

# 定义矩阵 A
A = np.array([[1, 1],
              [2, 2]])

# 定义零空间中的一个向量 (满足 x2 = -x1)
# 这是一个在 y = -x 这条直线上的向量
x_in_null_space = np.array([2, -2])

# 定义一个不在零空间中的向量
x_not_in_null_space = np.array([1, 2])

# 计算这两个向量经过矩阵 A 变换后的结果
Ax_in_null_space = A @ x_in_null_space
Ax_not_in_null_space = A @ x_not_in_null_space

# --- 可视化 ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 子图1：原始向量
ax1.set_title('Original Vectors in R^2')
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.grid(True)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_aspect('equal', adjustable='box')

# 绘制零空间
x_vals = np.linspace(-3, 3, 10)
ax1.plot(x_vals, -x_vals, linestyle='--', color='gray', label='Null Space (y = -x)')

# 绘制零空间向量
ax1.quiver(0, 0, x_in_null_space[0], x_in_null_space[1], angles='xy', scale_units='xy', scale=1, color='red', label='A vector in Null Space')
ax1.text(x_in_null_space[0], x_in_null_space[1], '  (2, -2)', color='red')

# 绘制非零空间向量
ax1.quiver(0, 0, x_not_in_null_space[0], x_not_in_null_space[1], angles='xy', scale_units='xy', scale=1, color='blue', label='A vector NOT in Null Space')
ax1.text(x_not_in_null_space[0], x_not_in_null_space[1], '  (1, 2)', color='blue')

ax1.legend()

# 子图2：变换后的向量
ax2.set_title('Vectors After Transformation by Matrix A')
ax2.set_xlim(-1, 6)
ax2.set_ylim(-1, 6)
ax2.grid(True)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_aspect('equal', adjustable='box')

# 绘制变换后的零空间向量（它被映射到原点）
ax2.quiver(0, 0, Ax_in_null_space[0], Ax_in_null_space[1], angles='xy', scale_units='xy', scale=1, color='red', label='Transformed Null Space Vector')
ax2.text(Ax_in_null_space[0], Ax_in_null_space[1], '  (0, 0)', color='red')

# 绘制变换后的非零空间向量
ax2.quiver(0, 0, Ax_not_in_null_space[0], Ax_not_in_null_space[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Transformed Non-Null Space Vector')
ax2.text(Ax_not_in_null_space[0], Ax_not_in_null_space[1], '  (3, 6)', color='blue')

ax2.legend()
plt.tight_layout()
plt.show()