import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# 1. 定义函数和梯度
# -----------------------
def f(x, Q, v):
    """计算 f(x) = x^T Q x + v^T x"""
    return x.T @ Q @ x + v.T @ x

def grad_f(x, Q, v):
    """计算梯度 ∇f(x) = (Q + Q^T)x + v"""
    return (Q + Q.T) @ x + v

# -----------------------
# 2. 生成参数
# -----------------------
Q = np.array([[2.0, 1.0],
              [0.0, 3.0]])
v = np.array([1.0, -2.0])

# -----------------------
# 3. 创建网格点
# -----------------------
x1 = np.linspace(-3, 3, 25)
x2 = np.linspace(-3, 3, 25)
X1, X2 = np.meshgrid(x1, x2)

F = np.zeros_like(X1)
U = np.zeros_like(X1)
V = np.zeros_like(X2)

# -----------------------
# 4. 计算函数值和梯度
# -----------------------
for i in range(X1.shape[0]):
    for j in range(X1.shape[1]):
        x = np.array([X1[i, j], X2[i, j]])
        F[i, j] = f(x, Q, v)
        g = grad_f(x, Q, v)
        U[i, j], V[i, j] = g[0], g[1]

# -----------------------
# 5. 可视化
# -----------------------
plt.figure(figsize=(8,6))
# 等高线
plt.contour(X1, X2, F, levels=20, cmap='viridis')
# 梯度场（箭头）
plt.quiver(X1, X2, U, V, color='red', alpha=0.6)

plt.title(r"Visualization of $f(x)=x^TQx+v^Tx$ and its gradient")
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.axis('equal')
plt.grid(True)
plt.show()
