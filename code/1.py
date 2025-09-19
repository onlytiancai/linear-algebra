import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. 定义零空间 (N(A))
# 零空间是一个穿过原点的平面。我们用两个向量来张成这个平面。
# 这里我们选择 x-y 平面，即 z=0。
x_plane = np.linspace(-3, 3, 10)
y_plane = np.linspace(-3, 3, 10)
X, Y = np.meshgrid(x_plane, y_plane)
Z_null = np.zeros_like(X)

# 2. 定义特解
# 特解向量为 (2, 2, 4)，代表平移的方向和距离。
xp_final = np.array([2, 2, 4])

# 3. 创建动画
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Translating a Plane in 3D Space')
ax.grid(True)

# 绘制零空间 (灰色透明平面)
ax.plot_surface(X, Y, Z_null, color='gray', alpha=0.5, rstride=1, cstride=1, label='Null Space ($Ax=0$)')

# 绘制动态的解集 (蓝色透明平面)
# 使用 rcount 和 ccount 控制网格密度，以便动画更新时能流畅
solution_surface = ax.plot_surface(X, Y, Z_null, color='dodgerblue', alpha=0.7, rstride=1, cstride=1)

def animate(t):
    """
    动画函数，t 从 0 到 1
    """
    # 计算当前帧的特解向量，随着 t 线性增长
    current_xp = xp_final * t
    
    # 将零空间平移
    X_solution = X + current_xp[0]
    Y_solution = Y + current_xp[1]
    Z_solution = Z_null + current_xp[2]
    
    # 移除旧的平面，绘制新的平面
    # 为了避免闪烁，通常需要清空旧的图形并重绘
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(True)
    
    # 重新绘制静态的零空间平面
    ax.plot_surface(X, Y, Z_null, color='gray', alpha=0.5, rstride=1, cstride=1)
    
    # 绘制当前帧的动态平面
    ax.plot_surface(X_solution, Y_solution, Z_solution, color='dodgerblue', alpha=0.7, rstride=1, cstride=1)
    
    ax.set_title(f'Translating Null Space (t={t:.2f})')
    
    return ax,

# 创建并保存动画
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 1, 100), interval=20)

# 保存为 GIF 文件
# ani.save('3d_plane_translation.gif', writer='pillow', fps=30)

plt.show()