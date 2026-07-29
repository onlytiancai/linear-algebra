'''
三个图分别展示

- Histogram + 决策边界 + Reconstruction Level
- 每个样本属于哪个量化区域（颜色表示）
- MSE下降过程

这样可以非常直观看到

> 更新边界 → 数据重新分组 → 更新质心

整个过程。

'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(0)


class LloydMaxDemo:

    def __init__(self, K=8, max_iter=20):

        self.K = K
        self.max_iter = max_iter

    def fit(self, x):

        x = np.sort(x)

        levels = np.linspace(x.min(), x.max(), self.K)

        history = []

        mse_list = []

        for _ in range(self.max_iter):

            boundaries = np.zeros(self.K + 1)

            boundaries[0] = -np.inf
            boundaries[-1] = np.inf

            boundaries[1:-1] = (levels[:-1] + levels[1:]) / 2

            labels = np.digitize(x, boundaries[1:-1])

            new_levels = levels.copy()

            for k in range(self.K):

                if np.any(labels == k):
                    new_levels[k] = np.mean(x[labels == k])

            x_hat = new_levels[labels]

            mse = np.mean((x - x_hat) ** 2)

            mse_list.append(mse)

            history.append(
                (
                    new_levels.copy(),
                    boundaries.copy(),
                    labels.copy(),
                    mse
                )
            )

            if np.max(np.abs(new_levels-levels)) < 1e-6:
                break

            levels = new_levels

        self.history = history
        self.data = x
        self.mse = mse_list

def animate(lloyd):

    x = lloyd.data

    fig = plt.figure(figsize=(13,8))

    ax1 = plt.subplot2grid((2,2),(0,0),colspan=2)
    ax2 = plt.subplot2grid((2,2),(1,0))
    ax3 = plt.subplot2grid((2,2),(1,1))

    cmap = plt.cm.tab10

    def update(i):

        ax1.clear()
        ax2.clear()
        ax3.clear()

        levels,boundaries,labels,mse = lloyd.history[i]

        #########################################
        # Histogram
        #########################################

        ax1.hist(
            x,
            bins=80,
            density=True,
            color="lightgray"
        )

        for b in boundaries[1:-1]:
            ax1.axvline(
                b,
                color="green",
                linestyle="--",
                lw=2
            )

        ax1.scatter(
            levels,
            np.zeros_like(levels),
            s=150,
            color="red",
            zorder=10
        )

        ax1.set_title(
            f"Iteration {i+1}"
        )

        #########################################
        # Sample Assignment
        #########################################

        y = np.zeros_like(x)

        for k in range(lloyd.K):

            idx = labels==k

            ax2.scatter(
                x[idx],
                y[idx],
                s=8,
                color=cmap(k),
                alpha=.7
            )

        for c in levels:

            ax2.axvline(
                c,
                color="black",
                lw=2
            )

        ax2.set_yticks([])

        ax2.set_title("Sample Assignment")

        #########################################
        # MSE
        #########################################

        ax3.plot(
            lloyd.mse,
            color="lightgray"
        )

        ax3.plot(
            np.arange(i+1),
            lloyd.mse[:i+1],
            "-o",
            color="red"
        )

        ax3.set_title("MSE")

        ax3.set_xlabel("Iteration")

        ax3.grid(True)

        plt.tight_layout()

    ani = FuncAnimation(
        fig,
        update,
        frames=len(lloyd.history),
        interval=1200,
        repeat=False
    )

    plt.show()

    return ani

#x = np.random.uniform(-1,1,4000)
x = np.random.randn(4000)

demo = LloydMaxDemo(K=8)

demo.fit(x)

ani = animate(demo)        