import numpy as np
import matplotlib.pyplot as plt

# Define vectors
A = np.array([1, 2, 3], dtype=float)
b = np.array([1, 2, 2], dtype=float)

# Least squares projection
k = (A @ b) / (A @ A)
b_hat = k * A
r = b - b_hat

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Column space: blue line
t = np.linspace(0, 1.2, 50)
ax.plot(
    t*A[0], t*A[1], t*A[2],
    color='blue', linewidth=3, label="Column space span(A)"
)

# Vector b: red arrow
ax.quiver(
    0, 0, 0, b[0], b[1], b[2],
    color='red', linewidth=3, arrow_length_ratio=0.1,
    label="b"
)

# Projection b_hat: green arrow
ax.quiver(
    0, 0, 0, b_hat[0], b_hat[1], b_hat[2],
    color='green', linewidth=3, arrow_length_ratio=0.1,
    label="Projection $\hat b$"
)

# Residual r: purple arrow (from b_hat to b)
ax.quiver(
    b_hat[0], b_hat[1], b_hat[2],
    r[0], r[1], r[2],
    color='purple', linewidth=3, arrow_length_ratio=0.1,
    label="Residual $r=b-\hat b$"
)

# Labels and legend
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Least Squares as Orthogonal Projection")
ax.legend()

plt.show()
