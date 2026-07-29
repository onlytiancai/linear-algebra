import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)


class LloydMaxQuantizer:

    def __init__(self, n_levels, max_iter=50, tol=1e-6):
        self.n_levels = n_levels
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, x):

        x = np.asarray(x)

        # 初始化重建值（均匀初始化）
        self.levels = np.linspace(x.min(), x.max(), self.n_levels)

        mse_history = []

        for _ in range(self.max_iter):

            old_levels = self.levels.copy()

            # --------------------------
            # Step1 更新决策边界
            # --------------------------
            boundaries = np.zeros(self.n_levels + 1)
            boundaries[0] = -np.inf
            boundaries[-1] = np.inf
            boundaries[1:-1] = (self.levels[:-1] + self.levels[1:]) / 2

            # --------------------------
            # Step2 数据分配
            # --------------------------
            labels = np.digitize(x, boundaries[1:-1])

            # --------------------------
            # Step3 更新重建值（质心）
            # --------------------------
            for k in range(self.n_levels):

                if np.any(labels == k):
                    self.levels[k] = np.mean(x[labels == k])

            # --------------------------
            # Step4 计算MSE
            # --------------------------
            x_hat = self.levels[labels]
            mse = np.mean((x - x_hat) ** 2)
            mse_history.append(mse)

            if np.max(np.abs(self.levels - old_levels)) < self.tol:
                break

        self.boundaries = boundaries
        self.labels = labels
        self.mse_history = mse_history

    def quantize(self, x):
        labels = np.digitize(x, self.boundaries[1:-1])
        return self.levels[labels]

def visualize(data, title, n_levels=8):

    lm = LloydMaxQuantizer(n_levels=n_levels)
    lm.fit(data)

    quantized = lm.quantize(data)

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))

    # -----------------------------
    # 原始数据
    # -----------------------------
    ax[0].hist(data, bins=80, density=True,
               alpha=0.6, color='skyblue')

    for c in lm.levels:
        ax[0].axvline(c,
                      color='red',
                      linewidth=2)

    ax[0].set_title(title + "\nReconstruction Levels")

    # -----------------------------
    # 量化结果
    # -----------------------------
    ax[1].scatter(data,
                  quantized,
                  s=5,
                  alpha=0.3)

    ax[1].set_xlabel("Original")
    ax[1].set_ylabel("Quantized")
    ax[1].set_title("Quantization Mapping")

    # -----------------------------
    # 收敛曲线
    # -----------------------------
    ax[2].plot(lm.mse_history, '-o')
    ax[2].set_xlabel("Iteration")
    ax[2].set_ylabel("MSE")
    ax[2].set_title("Convergence")

    plt.tight_layout()
    plt.show()

    print("\nFinal Levels:")
    print(np.round(lm.levels, 4))

    print("\nDecision Boundaries:")
    print(np.round(lm.boundaries[1:-1], 4))

    print("\nFinal MSE:", lm.mse_history[-1])


uniform_data = np.random.uniform(-1, 1, 50000)

visualize(
    uniform_data,
    "Uniform Distribution",
    n_levels=8
)        

gaussian_data = np.random.randn(50000)

visualize(
    gaussian_data,
    "Gaussian Distribution",
    n_levels=8
)