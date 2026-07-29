import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(0)


class LloydMaxAnimation:

    def __init__(self, n_levels=8, max_iter=20):

        self.n_levels = n_levels
        self.max_iter = max_iter

    def fit(self, x):

        x = np.asarray(x)

        levels = np.linspace(x.min(), x.max(), self.n_levels)

        self.history = []

        mse_history = []

        for _ in range(self.max_iter):

            boundaries = np.zeros(self.n_levels + 1)
            boundaries[0] = -np.inf
            boundaries[-1] = np.inf
            boundaries[1:-1] = (levels[:-1] + levels[1:]) / 2

            labels = np.digitize(x, boundaries[1:-1])

            new_levels = levels.copy()

            for k in range(self.n_levels):

                if np.any(labels == k):
                    new_levels[k] = np.mean(x[labels == k])

            x_hat = new_levels[labels]
            mse = np.mean((x - x_hat) ** 2)
            mse_history.append(mse)

            self.history.append({
                "levels": new_levels.copy(),
                "boundaries": boundaries.copy(),
                "mse": mse
            })

            if np.max(np.abs(new_levels - levels)) < 1e-6:
                break

            levels = new_levels

        self.data = x
        self.mse_history = mse_history


# ----------------------------------------------------
# 动画函数
# ----------------------------------------------------

def animate_quantizer(data,
                      n_levels=8,
                      max_iter=15):

    lm = LloydMaxAnimation(n_levels, max_iter)
    lm.fit(data)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

    xmin = data.min()
    xmax = data.max()

    def update(frame):

        ax1.clear()
        ax2.clear()

        info = lm.history[frame]

        levels = info["levels"]
        boundaries = info["boundaries"]

        # -----------------------------
        # Histogram
        # -----------------------------
        ax1.hist(data,
                 bins=80,
                 density=True,
                 color="lightgray")

        # reconstruction levels
        ax1.scatter(levels,
                    np.zeros_like(levels),
                    color="red",
                    s=120,
                    zorder=5,
                    label="levels")

        # decision boundaries
        for b in boundaries[1:-1]:
            ax1.axvline(
                b,
                color="green",
                linestyle="--",
                linewidth=2)

        ax1.set_xlim(xmin, xmax)
        ax1.set_ylim(bottom=0)

        ax1.set_title(f"Iteration {frame+1}")

        # -----------------------------
        # MSE Curve
        # -----------------------------
        ax2.plot(lm.mse_history,
                 color="gray",
                 alpha=0.4)

        ax2.plot(
            np.arange(frame+1),
            lm.mse_history[:frame+1],
            '-o',
            color="red")

        ax2.set_xlim(0, len(lm.mse_history))

        ax2.set_ylim(
            min(lm.mse_history)*0.95,
            max(lm.mse_history)*1.05)

        ax2.set_xlabel("Iteration")
        ax2.set_ylabel("MSE")

        ax2.set_title(
            f"MSE = {lm.mse_history[frame]:.6f}")

        return []

    ani = FuncAnimation(
        fig,
        update,
        frames=len(lm.history),
        interval=1000,
        repeat=False)

    plt.tight_layout()
    plt.show()

    return ani

import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--save-gif', action='store_true')
parser.add_argument('--save-mp4', action='store_true')
parser.add_argument('--type', default=None)
args = parser.parse_args()

if args.type == 'uniform':
    data = np.random.uniform(-1,1,30000)

elif args.type == 'gaussian':
    data = np.random.randn(30000)
else:
    parser.print_help()
    sys.exit(0)

ani = animate_quantizer(
    data,
    n_levels=8,
    max_iter=20
)

if args.save_gif:
    print('save gif ...')
    ani.save(
        f"lloyd_max_{args.type}.gif",
        writer="pillow",
        fps=1
    )
if args.save_mp4:
    print('save mp4 ...')
    ani.save(
        f"lloyd_max_{args.type}.mp4",
        writer="ffmpeg",
        fps=1
    )    