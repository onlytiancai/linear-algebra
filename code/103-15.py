'''
相比前三个视图，这里新增了一个 Quantization Map（量化映射）：

- 横轴：输入 x
- 纵轴：输出 x^
- 每轮都会画出当前的阶梯函数（piecewise constant mapping）

随着迭代，你可以看到这条阶梯函数逐渐调整：高概率区域的台阶变得更密、低概率区域更稀。这实际上就是 Lloyd–Max 算法最终学习到的量化器，也是很多信号处理教材和论文最经典的展示方式。
'''
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
                "labels": labels.copy(),
                "x_hat": x_hat.copy(),
                "mse": mse,
            })
            # 保存完整状态，这样以后想画 reconstruction error, quantization error, mapping, Voronoi partition 都不用重新计算。

            if np.max(np.abs(new_levels - levels)) < 1e-6:
                break

            levels = new_levels

        # 最后收敛结果也可以直接使用，而不用从 history[-1] 中取。
        self.data = x
        self.mse_history = mse_history
        self.levels = new_levels.copy()
        self.boundaries = boundaries.copy()
        self.labels = labels.copy()
        self.x_hat = x_hat.copy()



def animate_quantizer(
    demo,
    interval=800,
    dist_type=None,
):
    """
    Four-panel Lloyd-Max animation

    demo.data
    demo.history
    demo.mse_history
    demo.n_levels
    dist_type : "uniform" | "gaussian" | None
        用于在左上子图中叠加真实 PDF 参考曲线。
    """

    x = demo.data
    history = demo.history

    xmin = np.min(x)
    xmax = np.max(x)

    # 用于 Sample Assignment 子图的轻微 y 抖动，避免点全部落在 y=0
    rng = np.random.default_rng(0)
    y_jitter = rng.uniform(-0.05, 0.05, size=len(x))

    colors = plt.cm.tab10(
        np.linspace(0, 1, demo.n_levels)
    )

    # ==========================================================
    # 真实 PDF（仅在知道分布类型时叠加）
    # ==========================================================
    xx_pdf = np.linspace(xmin, xmax, 400)
    if dist_type == "uniform":
        true_pdf = np.ones_like(xx_pdf) / (xmax - xmin)
    elif dist_type == "gaussian":
        true_pdf = (
            1.0 / np.sqrt(2.0 * np.pi)
            * np.exp(-0.5 * xx_pdf ** 2)
        )
    else:
        true_pdf = None

    # 16:9 横向，适合手机横屏观看；尺寸足够大以避免 suptitle 与子图标题重叠
    fig = plt.figure(figsize=(16, 9))

    gs = fig.add_gridspec(
        2,
        2,
        left=0.05,
        right=0.98,
        bottom=0.07,
        top=0.88,
        wspace=0.18,
        hspace=0.40,
    )

    ax_hist = fig.add_subplot(gs[0, 0])
    ax_assign = fig.add_subplot(gs[0, 1])
    ax_map = fig.add_subplot(gs[1, 0])
    ax_mse = fig.add_subplot(gs[1, 1])

    # ==========================================
    def update(frame):

        ax_hist.clear()
        ax_assign.clear()
        ax_map.clear()
        ax_mse.clear()

        info = history[frame]

        levels = info["levels"]

        boundaries = info["boundaries"]

        labels = info["labels"]

        mse = info["mse"]

        # ==========================================================
        # 1 Histogram
        # ==========================================================

        ax_hist.hist(
            x,
            bins=80,
            density=True,
            color="lightgray",
            edgecolor="white",
            label="Histogram"
        )

        # 真实 PDF 参考曲线
        if true_pdf is not None:
            ax_hist.plot(
                xx_pdf,
                true_pdf,
                color="blue",
                linewidth=2,
                label="True PDF",
            )

        for b in boundaries[1:-1]:

            ax_hist.axvline(
                b,
                color="green",
                linestyle="--",
                linewidth=2,
            )

        ax_hist.scatter(
            levels,
            np.zeros_like(levels),
            s=140,
            color="red",
            edgecolors="black",
            zorder=20,
            label="Levels",
        )

        ax_hist.set_xlim(xmin, xmax)

        ax_hist.set_title(
            f"Histogram + Decision Boundaries\nIteration {frame+1}/{len(history)}"
        )

        ax_hist.legend(loc="upper right", fontsize=8)
        ax_hist.grid(alpha=.3)

        # ==========================================================
        # 2 Sample Assignment
        # ==========================================================

        for k in range(demo.n_levels):

            idx = labels == k

            ax_assign.scatter(
                x[idx],
                y_jitter[idx],
                s=8,
                color=colors[k],
                alpha=.7,
            )

        for c in levels:

            ax_assign.axvline(
                c,
                color="black",
                linewidth=2,
            )

        ax_assign.set_xlim(xmin, xmax)

        ax_assign.set_ylim(-0.1, 0.1)

        ax_assign.set_yticks([])

        ax_assign.set_title("Sample Assignment")

        # ==========================================================
        # 3 Quantization Mapping
        # ==========================================================

        xx = np.linspace(xmin, xmax, 1000)

        yy = np.zeros_like(xx)

        for k in range(demo.n_levels):

            left = boundaries[k]

            right = boundaries[k + 1]

            mask = (xx >= left) & (xx < right)

            yy[mask] = levels[k]

        # y = x 参考线（无量化时的理想映射）
        ax_map.plot(
            [xmin, xmax],
            [xmin, xmax],
            "--",
            color="gray",
            linewidth=1.5,
            label="y = x",
        )

        # 当前阶梯函数
        ax_map.step(
            xx,
            yy,
            where="post",
            linewidth=3,
            color="royalblue",
            label="Quantizer",
        )

        ax_map.scatter(
            levels,
            levels,
            color="red",
            s=50,
            zorder=20,
            label="Levels",
        )

        ax_map.set_xlim(xmin, xmax)

        ax_map.set_ylim(xmin, xmax)

        ax_map.set_xlabel("Input")

        ax_map.set_ylabel("Output")

        ax_map.set_title("Quantization Mapping")

        ax_map.grid(alpha=.3)
        ax_map.legend(loc="upper left", fontsize=8)

        # ==========================================================
        # 4 MSE
        # ==========================================================

        ax_mse.plot(
            demo.mse_history,
            color="silver",
            linewidth=2,
        )

        ax_mse.plot(
            np.arange(frame + 1),
            demo.mse_history[:frame + 1],
            "-o",
            color="red",
            linewidth=2,
        )

        ax_mse.scatter(
            frame,
            mse,
            s=80,
            color="blue",
            zorder=20,
        )

        ax_mse.set_xlim(
            0,
            len(demo.mse_history) - 1,
        )

        ax_mse.set_xlabel("Iteration")

        ax_mse.set_ylabel("MSE")

        ax_mse.set_title(
            f"MSE = {mse:.6f}"
        )

        ax_mse.grid(alpha=.3)

        # 子图内文本框：当前迭代与 MSE
        ax_mse.text(
            0.03,
            0.92,
            f"Iteration : {frame+1}\n"
            f"MSE : {mse:.6f}",
            transform=ax_mse.transAxes,
            fontsize=11,
            verticalalignment="top",
            bbox=dict(
                facecolor="white",
                alpha=0.85,
                edgecolor="lightgray",
            ),
        )

        fig.suptitle(
            "Lloyd-Max Quantization",
            fontsize=22,
            fontweight="bold",
            y=0.965,
        )

        return []

    ani = FuncAnimation(
        fig,
        update,
        frames=len(history),
        interval=interval,
        repeat=False,
        blit=False,
    )

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


lm = LloydMaxAnimation(8, 20)
lm.fit(data)
ani = animate_quantizer(lm, dist_type=args.type)

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