import numpy as np
import plotly.graph_objects as go
from ipywidgets import interact, FloatSlider

# 定义函数和梯度
def f(x, Q, v):
    return x.T @ Q @ x + v.T @ x

def grad_f(x, Q, v):
    return (Q + Q.T) @ x + v

# 绘制函数与梯度场
def plot_quadratic(Q11=2.0, Q12=0.5, Q21=0.5, Q22=1.0, v1=0.0, v2=-1.0):
    Q = np.array([[Q11, Q12],
                  [Q21, Q22]])
    v = np.array([v1, v2])

    x1 = np.linspace(-3, 3, 40)
    x2 = np.linspace(-3, 3, 40)
    X1, X2 = np.meshgrid(x1, x2)

    F = np.zeros_like(X1)
    U = np.zeros_like(X1)
    V = np.zeros_like(X2)

    for i in range(X1.shape[0]):
        for j in range(X1.shape[1]):
            x = np.array([X1[i, j], X2[i, j]])
            F[i, j] = f(x, Q, v)
            g = grad_f(x, Q, v)
            U[i, j], V[i, j] = g[0], g[1]

    # 创建 3D 曲面
    surface = go.Surface(x=X1, y=X2, z=F, colorscale="Viridis", opacity=0.8)

    # 梯度箭头 (下采样)
    step = 4
    quiver_x = X1[::step, ::step]
    quiver_y = X2[::step, ::step]
    quiver_u = U[::step, ::step]
    quiver_v = V[::step, ::step]
    quiver_z = np.zeros_like(quiver_x)

    quiver3d = go.Cone(
        x=quiver_x.flatten(),
        y=quiver_y.flatten(),
        z=quiver_z.flatten(),
        u=quiver_u.flatten(),
        v=quiver_v.flatten(),
        w=np.zeros_like(quiver_u.flatten()),
        sizemode="absolute",
        sizeref=1.0,
        showscale=False,
        colorscale="Reds",
        opacity=0.7,
        anchor="tail"
    )

    fig = go.Figure(data=[surface, quiver3d])
    fig.update_layout(
        title=r"Interactive visualization of $f(x)=x^TQx+v^Tx$",
        scene=dict(
            xaxis_title="x₁",
            yaxis_title="x₂",
            zaxis_title="f(x)",
            camera=dict(eye=dict(x=1.5, y=1.5, z=1))
        ),
        height=700
    )
    # fig.show()
    fig.write_html("10-7.html", auto_open=True)

# 使用滑块交互控制 Q 和 v
interact(
    plot_quadratic,
    Q11=FloatSlider(value=2.0, min=-3, max=3, step=0.1, description="Q11"),
    Q12=FloatSlider(value=0.5, min=-3, max=3, step=0.1, description="Q12"),
    Q21=FloatSlider(value=0.5, min=-3, max=3, step=0.1, description="Q21"),
    Q22=FloatSlider(value=1.0, min=-3, max=3, step=0.1, description="Q22"),
    v1=FloatSlider(value=0.0, min=-3, max=3, step=0.1, description="v₁"),
    v2=FloatSlider(value=-1.0, min=-3, max=3, step=0.1, description="v₂")
);
