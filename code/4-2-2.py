import matplotlib.pyplot as plt
import numpy as np

# 创建一个3D图形
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 定义x-y平面的网格
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = 0 * X + 0 * Y  # z坐标始终为0

# 绘制x-y平面
ax.plot_surface(X, Y, Z, alpha=0.5, color='lightblue', label='x-y plane')

# 绘制坐标轴
ax.quiver(0, 0, 0, 5, 0, 0, color='red', arrow_length_ratio=0.1, label='x-axis')
ax.quiver(0, 0, 0, 0, 5, 0, color='green', arrow_length_ratio=0.1, label='y-axis')
ax.quiver(0, 0, 0, 0, 0, 5, color='blue', arrow_length_ratio=0.1, label='z-axis')

# 添加标签和标题
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('The x-y plane as a subspace in R^3')

# 添加一个位于平面上的向量，以表示集合中的元素
ax.quiver(0, 0, 0, 3, 4, 0, color='purple', arrow_length_ratio=0.1, label='A vector in W')
ax.text(3, 4, 0.5, '(3, 4, 0)', color='purple')

# 设置图例
ax.legend()

# 显示图形
plt.show()