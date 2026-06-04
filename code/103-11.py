"""
103-11.py
=========

Lloyd–Max 迭代的静态可视化（一次性画 6 张子图）

复刻 web demo 的"Lloyd–Max iteration"面板，但改成静态图方便放进笔记。

用法：
    /Users/huhao/.pyenv/versions/qlib/bin/python code/103-11.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import importlib.util

# 复用 103-8
spec = importlib.util.spec_from_file_location("lm_mod", "code/103-8.py")
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)

plt.rcParams['font.sans-serif'] = ['Heiti TC', 'PingFang SC']
plt.rcParams['axes.unicode_minus'] = False


def lloyd_max_stepwise(b: int, d: int, n_samples: int = 200_000,
                       n_iters: int = 5, rng_seed: int = 0):
    """
    返回每次迭代后的码本（list of arrays），方便逐帧画图。
    """
    rng = np.random.default_rng(rng_seed)
    sigma = 1.0 / np.sqrt(d)
    K = 2 ** b

    # 初始化：高斯分位
    quantiles = (np.arange(K) + 0.5) / K
    cb = sigma * norm.ppf(quantiles)
    x = rng.normal(0, sigma, size=n_samples)

    history = [cb.copy()]
    for _ in range(n_iters):
        sorted_cb = np.sort(cb)
        dists = np.abs(x[:, None] - sorted_cb[None, :])
        assigns = np.argmin(dists, axis=1)
        new_cb = np.array([
            x[assigns == k].mean() if np.any(assigns == k) else sorted_cb[k]
            for k in range(K)
        ])
        cb = np.sort(new_cb)
        history.append(cb.copy())
    return history, x, sigma


def main():
    b, d = 2, 64
    sigma = 1.0 / np.sqrt(d)
    K = 2 ** b
    history, x, sigma = lloyd_max_stepwise(b, d, n_iters=5)

    # 收敛的 MSE 序列（用 103-8 跑出来的）
    out = lm.lloyd_max(d=d, b=b, n_samples=200_000, max_iter=80, verbose=False)
    mse_seq = out["mse_history"]
    shannon = lm.shannon_bound_1d(b, d)

    # 画 6 张子图：iter 0..5
    fig, axes = plt.subplots(2, 3, figsize=(13.5, 6.0))
    fig.suptitle(f'Lloyd–Max on $\\mathcal{{N}}(0, 1/d)$,  '
                 rf'b={b}, d={d}, $\sigma=1/\sqrt{{d}}={sigma:.3f}$',
                 fontsize=13, family='monospace')

    x_grid = np.linspace(-0.5, 0.5, 400)
    pdf_vals = norm.pdf(x_grid, 0, sigma)

    # 跑完所有 iter 后取最终的 MSE（如果 5 步不够就用跑到底的）
    # 简单地用前 5 个 + 一个 "converged" 视图
    panels = list(range(6))  # iter 0, 1, 2, 3, 4, 5
    panels[-1] = -1  # 最后一张 = 收敛视图

    for ax, it in zip(axes.flat, panels):
        ax.plot(x_grid, pdf_vals, color='#d4a017', lw=2.0,
                label=r'$\mathcal{N}(0, 1/d)$')

        if it == -1:
            cb = out["codebook"]
            mse = mse_seq[-1]
            title = f"CONVERGED (iter {len(mse_seq)})\nMSE = {mse:.3e}"
        else:
            cb = history[it] if it < len(history) else history[-1]
            mse = (mse_seq[it] if it < len(mse_seq) else mse_seq[-1])
            title = f"Iteration {it}\nMSE = {mse:.3e}"

        # 边界（虚线红）
        for bd in 0.5 * (cb[:-1] + cb[1:]):
            ax.axvline(bd, color='#e63946', ls='--', lw=0.9, alpha=0.5)

        # 质心（蓝点，画在密度曲线附近）
        ax.scatter(cb, np.zeros_like(cb) - 0.15,
                   c='#1f77b4', s=45, zorder=5,
                   edgecolors='white', linewidths=0.8,
                   label='centroids $c_b$')

        # Shannon 下界线
        ax.axhline(0, color='gray', lw=0.5)

        ax.set_xlim(-0.5, 0.5)
        ax.set_ylim(-0.35, 4.6)
        ax.set_xticks([-0.5, 0, 0.5])
        ax.set_xticklabels(['-0.50', '', '0.50'])
        ax.set_title(title, fontsize=9, family='monospace', loc='left')
        if it in (0, 3):
            ax.set_ylabel('density')
        if it in (3, 4, 5):
            ax.set_xlabel('coord $x_0$')
        ax.legend(loc='upper right', fontsize=7, frameon=True)

    # 全局 footer
    fig.text(0.5, 0.005,
             f"Shannon lower bound  1/(4^b·d) = {shannon:.3e}    "
             f"|    Lloyd–Max final MSE = {mse_seq[-1]:.3e}    "
             f"|    ratio = {mse_seq[-1] / shannon:.3f}x",
             ha='center', fontsize=10, family='monospace',
             color='#444')

    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    out_path = "code/103-11_lloyd_max_iteration.png"
    plt.savefig(out_path, dpi=130, bbox_inches='tight')
    print(f"Saved figure: {out_path}")
    plt.show()


if __name__ == "__main__":
    main()
