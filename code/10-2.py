"""
orthographic_projection_plotly.py
交互式演示：三维点与其投影（鼠标旋转/缩放）。
依赖: plotly, numpy
在 Jupyter Notebook 中直接展示，或用 plotly.offline.plot 保存为 HTML。
"""

import numpy as np
import plotly.graph_objects as go

# 数据
np.random.seed(2)
n = 20
points = np.random.uniform(-2.5, 2.5, size=(n, 3))

P = np.array([[1, 0, 0],
              [0, 1, 0]])
proj2 = (P @ points.T).T
proj3 = np.hstack([proj2, np.zeros((n,1))])

# 原始点（蓝色）
scatter_orig = go.Scatter3d(
    x=points[:,0], y=points[:,1], z=points[:,2],
    mode='markers',
    marker=dict(size=5),
    name='原始点 (x,y,z)'
)

# 投影点（红色）
scatter_proj = go.Scatter3d(
    x=proj3[:,0], y=proj3[:,1], z=proj3[:,2],
    mode='markers',
    marker=dict(size=6, symbol='circle'),
    name='投影点 (x,y,0)'
)

# 连接线（每个点到其投影）
lines = []
for p, q in zip(points, proj3):
    lines.append(go.Scatter3d(
        x=[p[0], q[0]],
        y=[p[1], q[1]],
        z=[p[2], q[2]],
        mode='lines',
        line=dict(width=2, dash='dash'),
        showlegend=False
    ))

# XY 平面网格（z=0）
xx = np.linspace(-3, 3, 20)
yy = np.linspace(-3, 3, 20)
XX, YY = np.meshgrid(xx, yy)
ZZ = np.zeros_like(XX)
surface = go.Surface(x=XX, y=YY, z=ZZ, opacity=0.2, showscale=False, name='z=0 平面')

fig = go.Figure(data=[scatter_orig, scatter_proj, surface] + lines)

fig.update_layout(
    title="正交投影: (x,y,z) → (x,y); P = [[1,0,0],[0,1,0]]",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='auto'
    ),
    legend=dict(x=0.02, y=0.98)
)

# 在 Jupyter 中： fig.show()
fig.write_html("orthographic_projection.html", auto_open=True)
