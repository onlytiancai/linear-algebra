import numpy as np
import matplotlib.pyplot as plt

# === 字体设置（macOS 推荐 Heiti TC）===
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
# =====================================

# Define M
M = np.array([[-0.6, -0.8],
              [ 3.2,  2.6]])

# Define v (eigenvector) and w (generalized eigenvector)
v = np.array([-1.0, 2.0])
w = np.array([5/8, 0.0])

# Compute Mv and Mw
Mv = M @ v
Mw = M @ w

# Build parallelograms before and after
# corners: origin, v, v+w, w, origin
before = np.array([[0,0], v, v+w, w, [0,0]])
after  = np.array([[0,0], Mv, Mw, Mv+Mw-Mv, [0,0]])  # same shape pattern

# Plot
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal', 'box')
ax.grid(True)

# plot before and after parallelograms
ax.plot(before[:,0], before[:,1], 'b-', lw=2, label='Before')
ax.plot(after[:,0], after[:,1], 'r--', lw=2, label='After (M applied)')

# arrows for edges
ax.arrow(0,0,v[0],v[1], head_width=0.1, length_includes_head=True, color='blue')
ax.arrow(0,0,w[0],w[1], head_width=0.1, length_includes_head=True, color='blue')
ax.arrow(0,0,Mv[0],Mv[1], head_width=0.1, length_includes_head=True, color='red')
ax.arrow(0,0,Mw[0],Mw[1], head_width=0.1, length_includes_head=True, color='red')

# annotate
ax.text(v[0], v[1], ' v', color='blue', va='bottom', fontsize=10)
ax.text(w[0], w[1], ' w', color='blue', va='bottom', fontsize=10)
ax.text(Mv[0], Mv[1], ' Mv', color='red', va='bottom', fontsize=10)
ax.text(Mw[0], Mw[1], ' Mw', color='red', va='bottom', fontsize=10)

ax.legend()
ax.set_title('平行四边形在基(v,w)下的剪切：一条边(v)完全重合')

# set limits
all_points = np.vstack([before, after])
ax.set_xlim(all_points[:,0].min()-0.5, all_points[:,0].max()+0.5)
ax.set_ylim(all_points[:,1].min()-0.5, all_points[:,1].max()+0.5)

plt.show()
