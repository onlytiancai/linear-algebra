"""
perspective_projection_plotly.py
演示透视投影: (x, y, z) -> (x/z, y/z)
依赖: plotly, numpy
运行方式: 在 Jupyter Notebook 中直接 fig.show()，或保存为 HTML。
"""

import numpy as np
import plotly.graph_objects as go

# 生成一些 3D 点
np.random.seed(42)
n = 20
# 让 z 都 > 1 以避免除零
points = np.random.uniform(-2, 2, size=(n, 3))
points[:, 2] += 3.0  # 平移 z 方向，保证都在相机前方

# 透视投影 (x/z, y/z)
proj2 = np.column_stack((points[:, 0] / points[:, 2],
                         points[:, 1] / points[:, 2]))

# 投影平面（z = 1）
proj3 = np.column_stack((proj2, np.ones(n)))

# 相机位置（原点）
camera = np.array([0, 0, 0])

# 原始点
scatter_points = go.Scatter3d(
    x=points[:, 0], y=points[:, 1], z=points[:, 2],
    mode='markers',
    marker=dict(size=5, color='blue'),
    name='原始点 (x,y,z)'
)

# 投影点
scatter_proj = go.Scatter3d(
    x=proj3[:, 0], y=proj3[:, 1], z=proj3[:, 2],
    mode='markers',
    marker=dict(size=6, color='red', symbol='circle'),
    name='投影点 (x/z, y/z, 1)'
)

# 从相机到每个点的投影线
lines = []
for p, q in zip(points, proj3):
    lines.append(go.Scatter3d(
        x=[camera[0], p[0], q[0]],
        y=[camera[1], p[1], q[1]],
        z=[camera[2], p[2], q[2]],
        mode='lines',
        line=dict(width=2, color='gray', dash='dot'),
        showlegend=False
    ))

# 投影平面 z=1
xx = np.linspace(-2, 2, 20)
yy = np.linspace(-2, 2, 20)
XX, YY = np.meshgrid(xx, yy)
ZZ = np.ones_like(XX)
surface = go.Surface(
    x=XX, y=YY, z=ZZ,
    opacity=0.25, showscale=False,
    name='投影平面 z=1'
)

# 相机点
camera_point = go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode='markers+text',
    marker=dict(size=6, color='black'),
    text=["Camera (0,0,0)"],
    textposition="bottom center",
    name='相机'
)

# 组合绘图
fig = go.Figure(data=[surface, scatter_points, scatter_proj, camera_point] + lines)

# 设置布局
fig.update_layout(
    title="透视投影: (x, y, z) → (x/z, y/z)",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='auto',
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
    ),
    legend=dict(x=0.02, y=0.98)
)

# 在 Jupyter 中使用：
# fig.show()
# 或保存为 HTML：
fig.write_html("perspective_projection.html", auto_open=True)
