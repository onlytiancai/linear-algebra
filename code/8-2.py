"""
Python script (do not execute here) to illustrate:
- A column-stochastic Markov transition matrix P
- Its eigenvalues/eigenvectors
- The invariant eigenvector for eigenvalue 1 (steady state)
- Trajectories x_k = P^k x0 converging toward steady state
All chart text/labels are in English.

Dependencies:
    numpy, matplotlib

Save as e.g. markov_eigs_plot.py and run in a local Python environment.
"""

import numpy as np
import matplotlib.pyplot as plt

# Example: 2-state column-stochastic matrix (columns sum to 1)
# P_{ij} = probability of moving from state j to state i
P = np.array([[0.9, 0.4],
              [0.1, 0.6]])

# Verify columns sum to 1 (numerical)
col_sums = P.sum(axis=0)
assert np.allclose(col_sums, np.ones(P.shape[1])), "Columns must sum to 1"

# Compute eigenvalues and right eigenvectors of P
eigvals, eigvecs = np.linalg.eig(P)

# Normalize eigenvectors for interpretation
# For each eigenvector, scale so its max absolute component = 1 (for plotting)
eigvecs_norm = eigvecs / np.max(np.abs(eigvecs), axis=0)

# Identify index of eigenvalue 1 (or closest to 1 numerically)
idx1 = np.argmin(np.abs(eigvals - 1.0))
steady_vec = eigvecs[:, idx1].real

# Convert steady vector to a probability vector if possible (nonnegative scaling)
# If eigenvector entries are all nonnegative (as for irreducible stochastic matrices),
# normalize to sum to 1 to interpret as steady distribution.
if np.all(steady_vec >= -1e-12):
    steady_prob = steady_vec / np.sum(steady_vec)
else:
    # If sign pattern not all nonnegative, produce a real-valued invariant direction for plotting
    steady_prob = steady_vec / np.sum(np.abs(steady_vec))

# Prepare several initial distributions (2D probability vectors)
# We'll choose points on the 1-simplex: x = [p, 1-p], p in [0,1]
p_values = np.linspace(0.02, 0.98, 9)
initial_points = np.vstack([p_values, 1 - p_values]).T

# Iterate each initial point under P several steps
num_steps = 15
trajectories = []
for x0 in initial_points:
    traj = [x0]
    x = x0.copy()
    for k in range(num_steps):
        x = P @ x
        # enforce numerical rounding to keep on the simplex
        x = np.maximum(x, 0.0)
        x = x / np.sum(x)
        traj.append(x.copy())
    trajectories.append(np.array(traj))

# Set up plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the 1-simplex (the line segment of probability vectors)
# In 2D it's the segment from (1,0) to (0,1)
simplex_x = [1.0, 0.0]
simplex_y = [0.0, 1.0]
ax.plot(simplex_x, simplex_y, linestyle='--', linewidth=1, label='Probability simplex')

# Plot trajectories
for traj in trajectories:
    ax.plot(traj[:, 0], traj[:, 1], marker='o', markersize=4, linewidth=1)
    # mark start and end
    ax.scatter(traj[0, 0], traj[0, 1], marker='s', s=40, label='start' if np.allclose(traj[0], trajectories[0][0]) else "")
    ax.scatter(traj[-1, 0], traj[-1, 1], marker='*', s=80, label='end' if np.allclose(traj[-1], trajectories[0][-1]) else "")

# Plot the steady-state (eigenvector for eigenvalue 1) as a large diamond
ax.scatter(steady_prob[0], steady_prob[1], marker='D', s=140, color='red', label='steady state (eig=1)')

# Plot eigenvector directions as arrows from origin for visualization (scaled)
origin = np.array([0.0, 0.0])
for i in range(eigvecs.shape[1]):
    v = eigvecs[:, i].real
    # Scale v for visibility on the simplex plot
    # We want to visualize direction, so normalize to unit length then scale
    v_norm = v / np.linalg.norm(v)
    scale = 0.6  # arbitrary scale for visibility
    ax.arrow(0.5, 0.1 + 0.15 * i, v_norm[0] * scale, v_norm[1] * scale,
             head_width=0.03, length_includes_head=True,
             linestyle='-', linewidth=1, label=f'eig {i}: {eigvals[i]:.3f}' if i == 0 else None)

# Annotate eigenvalues (text outside plotting area)
eig_texts = [f"lambda_{i} = {eigvals[i]:.6f}" for i in range(len(eigvals))]
ax.text(1.02, 0.8, "\n".join(eig_texts), transform=ax.transAxes, fontsize=9, va='top')

# Labels and formatting (all in English)
ax.set_xlabel('Probability of state 0')
ax.set_ylabel('Probability of state 1')
ax.set_title('Markov chain: trajectories and eigen-structure (2-state example)')
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':', linewidth=0.6)

# Legend (avoid duplicate labels)
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper right')

plt.tight_layout()

# Optionally save the figure instead of showing (uncomment to save)
# plt.savefig('markov_eigens_visualization.png', dpi=300)

# To display interactively, call plt.show()
plt.show()
