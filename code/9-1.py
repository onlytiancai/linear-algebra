import numpy as np
import matplotlib.pyplot as plt

# --- 1. 定义协方差矩阵 ---
Sigma = np.array([[2, 1.9],
                  [1.9, 2]])

# --- 2. 生成服从该协方差的二维高斯样本 ---
mean = np.array([0, 0])
data = np.random.multivariate_normal(mean, Sigma, size=500)

# --- 3. 计算特征值和特征向量 ---
eigvals, eigvecs = np.linalg.eigh(Sigma)

# --- 4. 按特征值从大到小排序 ---
order = np.argsort(eigvals)[::-1]
eigvals = eigvals[order]
eigvecs = eigvecs[:, order]

# --- 5. 绘制散点图 ---
plt.figure(figsize=(6,6))
plt.scatter(data[:,0], data[:,1], alpha=0.3, label="data")

# --- 6. 绘制主成分方向 ---
origin = mean  # 向量起点
for i in range(2):
    vec = eigvecs[:, i] * np.sqrt(eigvals[i]) * 2  # 缩放便于可视化
    plt.plot([origin[0], origin[0] + vec[0]],
             [origin[1], origin[1] + vec[1]],
             linewidth=3,
             label=f'PC{i+1} (λ={eigvals[i]:.1f})')

# --- 7. 绘制 y=x 参考线 ---
x = np.linspace(-5,5,100)
plt.plot(x, x, 'k--', label='y = x')

# --- 8. 美化图形 ---
plt.axis('equal')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('2D Data and Principal Components')
plt.legend()
plt.grid(True)
plt.show()
