"""
103-10.py
=========

可交互复刻 web demo: "Lloyd–Max: the optimal partition of a known distribution"

控件：
  • BITS  B (1..6)              — 码本大小 K = 2^b
  • DIMENSION  D (16..256)      — 决定 σ = 1/√d
  • 1 LLOYD STEP                — 单步迭代
  • CONVERGE                    — 跑到底
  • RESET                       — 用高斯分位数重新初始化

界面：
  上半图：高斯密度 N(0, 1/d) + 质心（蓝点）+ bin 边界（红色虚线）
  下半栏：ITERATION / MSE PER COORD / SHANNON BOUND 1/4^b / D

运行：
    /Users/huhao/.pyenv/versions/qlib/bin/python code/103-10.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.stats import norm
import importlib.util

# 复用 103-8 的算法
spec = importlib.util.spec_from_file_location("lm_mod", "code/103-8.py")
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)

# 中文字体
plt.rcParams['font.sans-serif'] = ['Heiti TC', 'PingFang SC', 'Hiragino Sans GB']
plt.rcParams['axes.unicode_minus'] = False


# ============================================================
# 主程序
# ============================================================

def main():
    # ---------- 初始参数 ----------
    b_init = 2
    d_init = 64
    sigma_init = 1.0 / np.sqrt(d_init)
    n_samples = 400_000

    # 静态高斯曲线缓存
    x_grid = np.linspace(-0.5, 0.5, 600)

    # ---------- 画布 ----------
    fig = plt.figure(figsize=(13, 6.8))
    ax = fig.add_axes([0.08, 0.18, 0.88, 0.70])
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 4.6)
    ax.set_xticks([-0.5, 0.0, 0.5])
    ax.set_xticklabels(['-0.50', '', '0.50'])
    ax.set_ylabel('density')
    ax.set_title(
        r'coord $x_0$ of uniform random unit vector  '
        r'(Lloyd–Max codebook for $\mathcal{N}(0, 1/d)$)',
        loc='left', fontsize=11, family='monospace',
    )

    # ---------- 画占位元素 ----------
    # 高斯曲线
    line_pdf, = ax.plot(x_grid, norm.pdf(x_grid, 0, sigma_init),
                        color='#d4a017', lw=2.5,
                        label=r'$\mathcal{N}(0,\,1/d)$')
    # 质心（蓝点）
    cb_dots = ax.scatter([], [], c='#1f77b4', s=55, zorder=5,
                          edgecolors='white', linewidths=1.0,
                          label='centroids $c_b$')
    # bin 边界（红色虚线）
    bin_vlines = []

    ax.legend(loc='upper right', frameon=True, fontsize=9,
              facecolor='white', edgecolor='lightgray')

    # ---------- 控件 ----------
    ax_b = fig.add_axes([0.10, 0.10, 0.18, 0.025])
    sB = Slider(ax_b, 'BITS  B', 1, 6, valinit=b_init,
                valstep=1, color='#2a9d8f')

    ax_d = fig.add_axes([0.36, 0.10, 0.22, 0.025])
    sD = Slider(ax_d, 'DIMENSION  D', 16, 256, valinit=d_init,
                valstep=1, color='#2a9d8f')

    ax_step = fig.add_axes([0.62, 0.095, 0.11, 0.04])
    btn_step = Button(ax_step, '1 LLOYD STEP',
                       color='white', hovercolor='#f0f0f0')

    ax_conv = fig.add_axes([0.74, 0.095, 0.10, 0.04])
    btn_conv = Button(ax_conv, 'CONVERGE',
                       color='white', hovercolor='#f0f0f0')

    ax_rst = fig.add_axes([0.85, 0.095, 0.10, 0.04])
    btn_rst = Button(ax_rst, 'RESET',
                      color='white', hovercolor='#f0f0f0')

    # ---------- 状态 ----------
    state = {
        'b': b_init,
        'd': d_init,
        'sigma': sigma_init,
        'n_iter': 0,
        'codebook': None,
        'assignments': None,
        'x': None,
        'mse': None,
    }

    # ---------- 文本面板（ITER / MSE / Shannon）----------
    txt_iter = fig.text(0.10, 0.045, "ITERATION\n0",
                        fontsize=10, family='monospace', va='center')
    txt_mse = fig.text(0.40, 0.045, "MSE PER COORD\n—",
                        fontsize=10, family='monospace', va='center',
                        color='#c0392b')
    txt_shannon = fig.text(0.65, 0.045, "SHANNON BOUND  1/4^b / D\n—",
                           fontsize=10, family='monospace', va='center',
                           color='#b9770e')

    def clear_bin_vlines():
        for v in bin_vlines:
            v.remove()
        bin_vlines.clear()

    def reset_codebook():
        """按 (b, d) 重新生成样本 + 高斯分位初始化码本。"""
        b, d = state['b'], state['d']
        sigma = 1.0 / np.sqrt(d)
        state['sigma'] = sigma
        rng = np.random.default_rng(42)
        state['x'] = rng.normal(0, sigma, size=n_samples)
        # 高斯分位初始化
        quantiles = (np.arange(2 ** b) + 0.5) / (2 ** b)
        state['codebook'] = sigma * norm.ppf(quantiles)
        state['n_iter'] = 0
        state['assignments'] = None
        state['mse'] = None

    def one_lloyd_step():
        """一次完整 Lloyd–Max 迭代。"""
        x, cb = state['x'], state['codebook']
        sorted_cb = np.sort(cb)
        dists = np.abs(x[:, None] - sorted_cb[None, :])
        assigns = np.argmin(dists, axis=1)
        new_cb = np.array([
            x[assigns == k].mean() if np.any(assigns == k) else sorted_cb[k]
            for k in range(len(sorted_cb))
        ])
        new_cb = np.sort(new_cb)
        state['codebook'] = new_cb
        state['assignments'] = assigns
        state['n_iter'] += 1
        state['mse'] = float(np.mean((x - new_cb[assigns]) ** 2))

    def update_plot():
        b, d, sigma = state['b'], state['d'], state['sigma']
        K = 2 ** b
        cb = state['codebook']

        # 1) 高斯曲线
        line_pdf.set_ydata(norm.pdf(x_grid, 0, sigma))
        line_pdf.set_label(rf'$\mathcal{{N}}(0,\,1/d),\ \sigma=1/\sqrt{{d}}={sigma:.4f}$')

        # 2) 标题
        ax.set_title(
            rf'b={b}, d={d}, $\sigma = 1/\sqrt{{d}}$ = {sigma:.3f},   '
            rf'K = 2$^{b}$ = {K} levels',
            loc='left', fontsize=11, family='monospace',
        )

        # 3) 质心（用 x=0 的小竖线代替散点更清晰）
        clear_bin_vlines()
        # 边界 = 相邻码字中点
        boundaries = 0.5 * (cb[:-1] + cb[1:])
        for bd in boundaries:
            v = ax.axvline(bd, color='#e63946', ls='--', lw=1.0, alpha=0.55)
            bin_vlines.append(v)
        # 质心画在密度曲线上（x = 码字, y = 0 略下）
        cb_dots.set_offsets(np.c_[cb, np.zeros_like(cb) - 0.15])
        cb_dots.set_sizes(np.full(K, 50.0))
        cb_dots.set_label('centroids $c_b$')

        ax.legend(loc='upper right', frameon=True, fontsize=9,
                  facecolor='white', edgecolor='lightgray')

        # 4) 数值
        txt_iter.set_text(f"ITERATION\n{state['n_iter']}")
        if state['mse'] is not None:
            txt_mse.set_text(f"MSE PER COORD\n{state['mse']:.3e}")
        else:
            txt_mse.set_text("MSE PER COORD\n—")
        shannon = lm.shannon_bound_1d(b, d)
        txt_shannon.set_text(f"SHANNON BOUND  1/4^b / D\n{shannon:.3e}")

        fig.canvas.draw_idle()

    # ---------- 事件回调 ----------
    def on_b_change(val):
        state['b'] = int(sB.val)
        reset_codebook()
        update_plot()

    def on_d_change(val):
        state['d'] = int(sD.val)
        reset_codebook()
        update_plot()

    def on_step(event):
        one_lloyd_step()
        update_plot()

    def on_converge(event):
        for _ in range(200):
            prev = state['codebook'].copy()
            one_lloyd_step()
            if np.max(np.abs(state['codebook'] - prev)) < 1e-10:
                break
        update_plot()

    def on_reset(event):
        reset_codebook()
        update_plot()

    sB.on_changed(on_b_change)
    sD.on_changed(on_d_change)
    btn_step.on_clicked(on_step)
    btn_conv.on_clicked(on_converge)
    btn_rst.on_clicked(on_reset)

    # ---------- 初始化 ----------
    reset_codebook()
    update_plot()

    plt.show()


if __name__ == "__main__":
    main()
