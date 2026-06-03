"""
d=3 情形演示：单位球面上的均匀分布

演示为什么 S^2 (d=3 维球面) 上均匀采样的 x1 坐标 marginal 是 [-1,1] 上的均匀分布，
不是高斯（钟形）曲线 —— 这与 d=2 的 arcsine (U 形) 不同。

几何直觉：
  - 在 3-D 球面 S^2 上，"x1 = t 处切出一片圆环"的面积
  - 与 t 无关（球面是旋转对称的）
  - 因此 x1 的边缘密度为常数 → 均匀分布
  - 关键结论：标准差 = 1/√3 ≈ 0.577，与 d=1 一样是均匀，
    但量级上预示了 d→∞ 时会变成"窄高斯"
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# === 字体设置（macOS 推荐 Heiti TC）===
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

# Theoretical uniform density on [-1, 1]
UNIFORM_DENSITY = 0.5  # 1 / (1 - (-1)) = 1/2

def sample_unit_sphere(n: int, d: int = 3, rng=None) -> np.ndarray:
    """
    在 d 维单位球面 S^{d-1} 上均匀采样 n 个点。

    方法：高斯向量归一化。对任意 d 都成立（Marsaglia 1972）。
    """
    if rng is None:
        rng = np.random.default_rng(seed=42)
    g = rng.standard_normal(size=(n, d))
    g /= np.linalg.norm(g, axis=1, keepdims=True)
    return g

def main():
    rng = np.random.default_rng(seed=42)

    # Sample on unit sphere S^2
    n_samples = 5000
    points = sample_unit_sphere(n_samples, d=3, rng=rng)  # shape (n, 3)
    x1 = points[:, 0]
    x2 = points[:, 1]
    x3 = points[:, 2]

    # Create figure with two subplots
    fig = plt.figure(figsize=(12, 5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1.2], wspace=0.3)

    # ========== Left: 2-D projection of the sphere ==========
    ax1 = fig.add_subplot(gs[0])
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    ax1.add_patch(plt.Circle((0, 0), 1, fill=False, color='gray', linewidth=2))

    # 2-D 投影（沿 x3 轴）: 用 |x3| 模拟深度
    depth = np.abs(x3)  # 离观察者远近（用作颜色）
    ax1.scatter(x1, x2, c=depth, cmap='BuGn', s=8, alpha=0.7,
                edgecolors='none')

    # Highlight the x1 axis
    ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax1.axvline(x=0, color='gray', linestyle='--', alpha=0.5)

    # 红色虚线箭头表示 x1 坐标
    ax1.annotate('', xy=(1.0, 0), xytext=(0.5, 0),
                 arrowprops=dict(arrowstyle='->', color='red',
                                 lw=1.5, linestyle='--'))
    ax1.text(1.02, 0.0, r'$x_1$', color='red', fontsize=14,
             ha='left', va='center')

    ax1.set_xlabel(r'$x_1$', fontsize=12)
    ax1.set_ylabel(r'$x_2$', fontsize=12)
    ax1.set_title('单位球面 S² 上的均匀采样 (沿 $x_3$ 投影)',
                  fontsize=12, fontweight='bold')

    # 文字说明
    ax1.text(-1.45, 1.25,
             r'球面旋转对称' + '\n' +
             r'$x_1 = t$ 处的圆环面积与 $t$ 无关' + '\n' +
             r'$\Rightarrow$ $x_1$ 边缘是均匀分布',
             fontsize=9, bbox=dict(boxstyle='round',
                                   facecolor='wheat', alpha=0.8),
             verticalalignment='top', horizontalalignment='left')

    # ========== Right: Distribution ==========
    ax2 = fig.add_subplot(gs[1])

    bins = np.linspace(-1, 1, 41)
    ax2.hist(x1, bins=bins, density=True, alpha=0.7,
             color=plt.get_cmap('BuGn')(0.6),
             edgecolor='darkcyan', label='采样直方图')

    # 理论均匀分布水平参考线
    ax2.axhline(y=UNIFORM_DENSITY, color='orange', lw=2.5,
                label=r'均匀: $f(x_1)=\frac{1}{2}$')

    ax2.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
    ax2.set_xlim(-1.05, 1.05)
    ax2.set_ylim(0, 0.9)
    ax2.set_xlabel(r'$x_1$', fontsize=12)
    ax2.set_ylabel('密度', fontsize=12)
    ax2.set_title(r'$x_1$ 的边缘分布 (d=3，应为均匀)',
                  fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=10)

    # ========== Bottom: statistics card ==========
    std_x1 = np.std(x1)
    theoretical_std = 1 / np.sqrt(3)  # 0.577 for d=3
    stats_text = (f'分布形状: 均匀 (uniform on $[-1, 1]$)\n'
                  r'$\mathrm{std}(x_1)$: ' + f'{std_x1:.3f}\n'
                  r'$1/\sqrt{d}$: ' + f'{theoretical_std:.3f}')

    # 用一个独立的小 axes 装统计卡，避免 fig.text 字体问题
    ax_stat = fig.add_axes([0.55, 0.02, 0.40, 0.10])
    ax_stat.axis('off')
    ax_stat.text(0.0, 0.5, stats_text,
                 fontsize=11,
                 bbox=dict(boxstyle='round',
                           facecolor='lightyellow', alpha=0.9),
                 verticalalignment='center', horizontalalignment='left')

    plt.suptitle(r'Step two: the sphere $(d=3)$',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.subplots_adjust(left=0.06, right=0.98, top=0.90, bottom=0.18,
                        wspace=0.30)
    plt.show()

if __name__ == '__main__':
    main()
