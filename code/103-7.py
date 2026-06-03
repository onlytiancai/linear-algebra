"""
d=100 (高维) 情形演示：球面坐标近似高斯

复刻 web 交互 demo "Step three: high dimensions" 的 d=100, samples=10000 截图。

关键事实：
  - 球面 S^{d-1} 上均匀采样的任一坐标 x_0 服从
        f(x) = (1 - x^2)^{(d-3)/2} / B(1/2, (d-1)/2),   x ∈ [-1, 1]
    即 x_0^2 ~ Beta(1/2, (d-1)/2)
  - 当 d → ∞，这个分布在 0 附近近似 N(0, 1/d)，标准差 1/√d
  - d=30 已经肉眼像高斯，d=256 时几乎所有质量集中在 [-1/√d, 1/√d] 内
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.special import gammaln
from scipy.stats import norm, beta

# === 字体设置（macOS 推荐 Heiti TC）===
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

# -------- 理论分布 --------

def x0_pdf_exact(x: np.ndarray, d: int) -> np.ndarray:
    """
    球面 S^{d-1} 上 x_0 的精确边缘 PDF。

    推导：x_0^2 ~ Beta(1/2, (d-1)/2)
          令 Y = X^2，由对称性 f_X(x) = |x| f_Y(x^2)
          化简得 f_X(x) = (1 - x^2)^{(d-3)/2} / B(1/2, (d-1)/2)
    """
    # 用对数避免 (1 - x^2) 很小时下溢
    log_B = gammaln(0.5) + gammaln((d - 1) / 2.0) - gammaln(d / 2.0)
    log_pdf = -log_B + ((d - 3) / 2.0) * np.log(np.maximum(1 - x**2, 1e-300))
    return np.exp(log_pdf)


# -------- 主程序 --------

def main():
    # 初始参数（与截图一致）
    d_init, n_init = 100, 10000

    fig = plt.figure(figsize=(13, 6.5))
    ax = fig.add_axes([0.08, 0.18, 0.88, 0.72])
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 4.6)
    ax.set_xticks([-0.5, 0.0, 0.5])
    ax.set_xticklabels(['-0.50', '', '0.50'])
    ax.set_ylabel('density')
    ax.set_title(r'coord $x_0$ of uniform random unit vector',
                 loc='left', fontsize=11, family='monospace')

    # 预先画一组空 histogram / 曲线占位
    x_grid = np.linspace(-0.5, 0.5, 400)
    line_exact, = ax.plot(x_grid, np.zeros_like(x_grid), color='#d4a017',
                          lw=2.5, label=r'Beta PDF (exact)')
    line_gauss, = ax.plot(x_grid, np.zeros_like(x_grid), color='#2ec4a7',
                          lw=2.5, label=r'$\mathcal{N}(0, 1/d)$ approximation')
    hist_container = [None]  # 用 list 持有当前直方图容器，便于替换

    ax.legend(loc='upper right', frameon=True, fontsize=9,
              facecolor='white', edgecolor='lightgray')

    # 下方控件栏（用 add_axes 直接定位）
    ax_d = fig.add_axes([0.10, 0.10, 0.30, 0.025])
    slider_d = Slider(ax_d, 'DIMENSION  D', 2, 300,
                      valinit=d_init, valstep=1, color='#2a9d8f')

    ax_n = fig.add_axes([0.55, 0.10, 0.30, 0.025])
    slider_n = Slider(ax_n, 'SAMPLES', 100, 50000,
                      valinit=n_init, valstep=100, color='#2a9d8f')

    ax_btn = fig.add_axes([0.88, 0.085, 0.10, 0.04])
    btn = Button(ax_btn, 'RESAMPLE', color='white', hovercolor='#f0f0f0')

    # -------- 更新函数 --------
    state = {'seed': 0}

    def redraw(_=None):
        d = int(slider_d.val)
        n = int(slider_n.val)

        # 1) 在 S^{d-1} 上均匀采样
        rng = np.random.default_rng(seed=state['seed'])
        g = rng.standard_normal(size=(n, d))
        g /= np.linalg.norm(g, axis=1, keepdims=True)
        x0 = g[:, 0]  # 取第一个坐标

        # 2) 经验直方图
        counts, bins = np.histogram(x0, bins=80, range=(-0.5, 0.5),
                                    density=True)
        # 清掉旧柱子
        if hist_container[0] is not None:
            hist_container[0].remove()
        hist_container[0] = ax.bar(bins[:-1], counts, width=np.diff(bins),
                                   color='#c8a8ff', edgecolor='#9b7fd6',
                                   alpha=0.85, align='edge',
                                   label='empirical histogram')
        # 重新构建 legend，让直方图也能进入
        ax.legend(handles=[hist_container[0], line_exact, line_gauss],
                  loc='upper right', frameon=True, fontsize=9,
                  facecolor='white', edgecolor='lightgray')

        # 3) 精确 Beta PDF（只画 [-0.5, 0.5] 范围内，外部会被 y 限截掉）
        line_exact.set_ydata(x0_pdf_exact(x_grid, d))

        # 4) 高斯近似 N(0, 1/d)
        sigma = 1.0 / np.sqrt(d)
        line_gauss.set_ydata(norm.pdf(x_grid, loc=0, scale=sigma))

        # 5) 自适应 y 轴上限（保证两条曲线都可见）
        y_max = max(counts.max() if counts.size else 0,
                    x0_pdf_exact(x_grid, d).max(),
                    norm.pdf(0, scale=sigma))
        ax.set_ylim(0, y_max * 1.15)

        fig.canvas.draw_idle()

    def resample(_=None):
        state['seed'] += 1
        redraw()

    slider_d.on_changed(redraw)
    slider_n.on_changed(redraw)
    btn.on_clicked(resample)

    redraw()
    plt.suptitle('Step three: high dimensions',
                 fontsize=14, fontweight='bold',
                 family='monospace', x=0.05, ha='left', y=0.97)
    plt.show()


if __name__ == '__main__':
    main()
