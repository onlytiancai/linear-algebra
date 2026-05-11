import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Hiragino Sans GB', 'Heiti TC', 'SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 检查字体
import matplotlib.font_manager as fm
print("可用字体:", [f.name for f in fm.fontManager.ttflist if 'PingFang' in f.name or 'Hiragino' in f.name or 'Hei' in f.name][:5])

# 设置维度
d = 100  # 高维空间
np.random.seed(42)  # 固定随机种子

# 1. 生成随机向量 x (单位向量，模拟高维数据)
x = np.random.randn(d)
x = x / np.linalg.norm(x)  # 归一化为单位向量

print(f"原始向量 x 的长度: {np.linalg.norm(x):.4f}")
print(f"x 的前5个坐标: {x[:5]}")

# 2. 生成随机正交矩阵 R (旋转矩阵)
A = np.random.randn(d, d)
Q, R = np.linalg.qr(A)  # QR 分解得到正交矩阵 Q
R_matrix = Q  # R_matrix 是正交矩阵

# 3. 旋转向量: y = R * x
y = R_matrix @ x

print(f"旋转后向量 y 的长度: {np.linalg.norm(y):.4f}")
print(f"y 的前5个坐标: {y[:5]}")

# 4. 计算归一化因子 eta_x = sqrt(d) / ||x||_2
eta_x = np.sqrt(d) / np.linalg.norm(x)
print(f"归一化因子 eta_x: {eta_x:.4f}")

# 5. 归一化: y_norm = eta_x * y
y_norm = eta_x * y

print(f"归一化后向量 y_norm 的长度: {np.linalg.norm(y_norm):.4f}")
print(f"y_norm 的前5个坐标: {y_norm[:5]}")

# 6. 简单量化演示 (1-bit: sign 函数)
quantized = np.sign(y_norm)
print(f"量化后 (sign) 的前5个坐标: {quantized[:5]}")

# 7. 可视化: 坐标分布
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 原始旋转向量 y 的坐标分布
axes[0].hist(y, bins=20, alpha=0.7, color='blue', edgecolor='black')
axes[0].set_title('旋转后向量 y 的坐标分布')
axes[0].set_xlabel('坐标值')
axes[0].set_ylabel('频次')
axes[0].axvline(np.mean(y), color='red', linestyle='--', label=f'均值: {np.mean(y):.4f}')
axes[0].axvline(np.std(y), color='green', linestyle='--', label=f'标准差: {np.std(y):.4f}')
axes[0].legend()

# 归一化后 y_norm 的坐标分布
axes[1].hist(y_norm, bins=20, alpha=0.7, color='orange', edgecolor='black')
axes[1].set_title('归一化后向量 y_norm 的坐标分布')
axes[1].set_xlabel('坐标值')
axes[1].set_ylabel('频次')
axes[1].axvline(np.mean(y_norm), color='red', linestyle='--', label=f'均值: {np.mean(y_norm):.4f}')
axes[1].axvline(np.std(y_norm), color='green', linestyle='--', label=f'标准差: {np.std(y_norm):.4f}')
axes[1].legend()

# 量化后 (sign) 的分布
axes[2].hist(quantized, bins=3, alpha=0.7, color='green', edgecolor='black')
axes[2].set_title('量化后 (1-bit sign) 的坐标分布')
axes[2].set_xlabel('坐标值')
axes[2].set_ylabel('频次')
axes[2].set_xticks([-1, 0, 1])

plt.tight_layout()
plt.show()