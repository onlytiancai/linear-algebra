import numpy as np
import matplotlib.pyplot as plt

# =========================
# Data and model y = a x + b
# =========================
x = np.array([1, 2, 3], dtype=float)
y = np.array([1, 2, 2], dtype=float)

A = np.column_stack([x, np.ones_like(x)])
b = y

# Least squares solution
a, b0 = np.linalg.lstsq(A, b, rcond=None)[0]

# Projection and residual
b_hat = A @ np.array([a, b0])
r = b - b_hat

# =========================
# 3D visualization
# =========================
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Column space plane (gray)
s = np.linspace(-1, 1, 20)
t = np.linspace(-1, 1, 20)
S, T = np.meshgrid(s, t)

v1 = A[:, 0]
v2 = A[:, 1]

plane = np.outer(S.flatten(), v1) + np.outer(T.flatten(), v2)
plane = plane.reshape(20, 20, 3)

ax.plot_surface(
    plane[:, :, 0],
    plane[:, :, 1],
    plane[:, :, 2],
    alpha=0.25
)

# Vectors with different colors
ax.quiver(
    0, 0, 0, b[0], b[1], b[2],
    color="red", linewidth=3, arrow_length_ratio=0.1,
    label="b"
)

ax.quiver(
    0, 0, 0, b_hat[0], b_hat[1], b_hat[2],
    color="green", linewidth=3, arrow_length_ratio=0.1,
    label="Projection $\hat b$"
)

ax.quiver(
    b_hat[0], b_hat[1], b_hat[2],
    r[0], r[1], r[2],
    color="purple", linewidth=3, arrow_length_ratio=0.1,
    label="Residual $r=b-\hat b$"
)

# Labels
ax.set_xlabel("dim 1")
ax.set_ylabel("dim 2")
ax.set_zlabel("dim 3")
ax.set_title("Least Squares as Projection onto a Plane (y = ax + b)")
ax.legend()

plt.show()
