"""
homogeneous_transform_plotly.py
演示齐次坐标变换 (4x4 矩阵)：旋转 + 平移
依赖: plotly, numpy
"""

import numpy as np
import plotly.graph_objects as go

# === 定义一个立方体 ===
def cube_points(size=1.0):
    s = size / 2
    pts = np.array([
        [-s,-s,-s],
        [ s,-s,-s],
        [ s, s,-s],
        [-s, s,-s],
        [-s,-s, s],
        [ s,-s, s],
        [ s, s, s],
        [-s, s, s],
    ])
    return pts

cube = cube_points()

# === 1) 定义旋转 (绕 Z 轴) + 平移矩阵 ===
theta = np.deg2rad(35)
Rz = np.array([
    [ np.cos(theta), -np.sin(theta), 0, 0],
    [ np.sin(theta),  np.cos(theta), 0, 0],
    [ 0,              0,             1, 0],
    [ 0,              0,             0, 1],
])

T = np.array([
    [1,0,0,1.5],
    [0,1,0,1.0],
    [0,0,1,0.5],
    [0,0,0,1],
])

# 合成矩阵 M = T * Rz
M = T @ Rz

# === 2) 把立方体点扩展为齐次坐标 (x,y,z,1) ===
cube_h = np.hstack([cube, np.ones((cube.shape[0],1))])

# 变换后的立方体
cube_trans = (M @ cube_h.T).T[:, :3]

# === 3) Plotly 可视化 ===
def make_edges(pts, color):
    edges_idx = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]
    edges = []
    for i,j in edges_idx:
        edges.append(go.Scatter3d(
            x=[pts[i,0], pts[j,0]],
            y=[pts[i,1], pts[j,1]],
            z=[pts[i,2], pts[j,2]],
            mode='lines',
            line=dict(width=4, color=color),
            showlegend=False
        ))
    return edges

fig = go.Figure()

# 原始立方体（蓝色）
for e in make_edges(cube, 'blue'):
    fig.add_trace(e)

# 变换后的立方体（红色）
for e in make_edges(cube_trans, 'red'):
    fig.add_trace(e)

# 调整视角
fig.update_layout(
    title="齐次坐标: 平移 + 旋转 (T·Rz)",
    scene=dict(
        xaxis_title='X', yaxis_title='Y', zaxis_title='Z',
        aspectmode='cube'
    ),
    legend=dict(x=0.02, y=0.98)
)

# 在 Jupyter 中使用:
# fig.show()
fig.write_html("4.html", auto_open=True)
