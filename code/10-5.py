import numpy as np

# 定义透视投影矩阵 (实现 (x, y, z) -> (x/z, y/z))
M = np.array([
    [1, 0, 0, 0],  # X' = x
    [0, 1, 0, 0],  # Y' = y
    [0, 0, 0, 0],  # Z' 无关，这里设为 0
    [0, 0, 1, 0]   # W' = z
], dtype=float)

# 定义三维点（齐次坐标形式）
points_3d = np.array([
    [6, 4, 2, 1],
    [15, 21, 3, 1]
])

# 应用线性变换
projected_homogeneous = points_3d @ M.T  # 每个点乘以 M^T

# 执行透视除法（除以最后一项 W）
projected_2d = projected_homogeneous[:, :2] / projected_homogeneous[:, [3]]

# 输出结果
for i, (p3d, p2d) in enumerate(zip(points_3d, projected_2d)):
    print(f"3D 点 {i+1}: {p3d[:3]} → 投影到 2D 点: {p2d}")

# output
'''
3D 点 1: [6 4 2] → 投影到 2D 点: [3. 2.]
3D 点 2: [15 21  3] → 投影到 2D 点: [5. 7.]
'''