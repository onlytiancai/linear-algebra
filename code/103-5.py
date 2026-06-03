"""
d=2 情形演示：单位圆上的 arcsine 分布

演示为什么球面 S^1 上均匀采样的坐标 marginal distribution 是 U 形（arcsine）而非高斯。

几何直觉：
  - 在 x1 = ±1 处，圆是竖直的 → 小的 dx1 覆盖长弧
  - 在 x1 = 0 处，圆是水平的 → 同样的 dx1 覆盖短弧
  → 点在 ±1 附近聚集，形成 U 形
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import matplotlib.gridspec as gridspec

# === 字体设置（macOS 推荐 Heiti TC）===
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

# Theoretical arcsine density on [-1, 1]
def arcsine_density(x):
    """f(x) = 1 / (pi * sqrt(1 - x^2)) for x in [-1, 1]"""
    return 1.0 / (np.pi * np.sqrt(np.maximum(1 - x**2, 1e-10)))

def main():
    rng = np.random.default_rng(seed=42)

    # Generate uniform points on unit circle
    n_samples = 5000
    theta = rng.uniform(0, 2 * np.pi, n_samples)  # uniform angle
    x1 = np.cos(theta)  # x1 coordinate
    x2 = np.sin(theta)  # x2 coordinate

    # Create figure with two subplots
    fig = plt.figure(figsize=(12, 5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1.2], wspace=0.3)

    # ========== Left: Geometry ==========
    ax1 = fig.add_subplot(gs[0])
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    ax1.add_patch(plt.Circle((0, 0), 1, fill=False, color='gray', linewidth=2))

    # Sample and plot points
    ax1.scatter(x1, x2, c=theta, cmap='hsv', s=3, alpha=0.6)

    # Highlight the x1 axis
    ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax1.axvline(x=0, color='gray', linestyle='--', alpha=0.5)

    # Add annotation for x1 coordinate
    ax1.annotate('', xy=(1.0, 0), xytext=(0.5, 0),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax1.text(0.75, 0.15, r'$x_1$', color='red', fontsize=14, ha='center')

    # Highlight points near x1 = 1 (vertical tangent)
    near_plus1 = np.where(np.abs(x1 - 0.95) < 0.05)[0][:20]
    ax1.scatter(x1[near_plus1], x2[near_plus1], c='lime', s=50, 
                edgecolors='black', linewidths=1, zorder=5, label=r'靠近 $x_1=1$')

    # Highlight points near x1 = 0 (horizontal tangent)
    near_zero = np.where(np.abs(x1) < 0.05)[0][:20]
    ax1.scatter(x1[near_zero], x2[near_zero], c='cyan', s=50,
                edgecolors='black', linewidths=1, zorder=5, label=r'靠近 $x_1=0$')

    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlabel(r'$x_1$', fontsize=12)
    ax1.set_ylabel(r'$x_2$', fontsize=12)
    ax1.set_title('单位圆上的均匀采样点', fontsize=13, fontweight='bold')

    # Add text explaining geometric intuition
    ax1.text(-1.4, 1.2, 
             r'在 $x_1 = \pm 1$ 处：切线垂直' + '\n' +
             r'$\Rightarrow$ 小的 $\Delta x_1$ 覆盖长弧' + '\n' +
             r'$\Rightarrow$ 点更密集',
             fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             verticalalignment='top')

    # ========== Right: Distribution ==========
    ax2 = fig.add_subplot(gs[1])

    # Histogram of x1 coordinates
    bins = np.linspace(-1, 1, 51)
    ax2.hist(x1, bins=bins, density=True, alpha=0.7, color='cyan', 
             edgecolor='darkcyan', label='采样直方图')

    # Theoretical arcsine curve
    x_range = np.linspace(-0.999, 0.999, 500)
    ax2.plot(x_range, arcsine_density(x_range), 'r-', lw=2.5, 
             label=r'理论: $f(x_1)=\frac{1}{\pi\sqrt{1-x_1^2}}$')

    # Reference lines
    ax2.axvline(x=0, color='gray', linestyle=':', alpha=0.7)
    ax2.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

    # Statistics box
    std_x1 = np.std(x1)
    theoretical_std = 1 / np.sqrt(2)  # 0.707 for d=2
    stats_text = (f'分布形状: 反正弦 (arcsine)\n'
                   f'$x_1$ 标准差: {std_x1:.3f}\n'
                   f'$1/\\sqrt{{d}}$: {theoretical_std:.3f}')
    ax2.text(0.02, 0.98, stats_text, transform=ax2.transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(0, 2.5)
    ax2.set_xlabel(r'$x_1$', fontsize=12)
    ax2.set_ylabel('密度', fontsize=12)
    ax2.set_title('$x_1$ 的边缘分布 (d=2)', fontsize=13, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
