"""
DRIVE/Inner-product Decoder Visualization
==========================================
Demonstrates the DRIVE encoder + Inner-product decoder (RaBitQ/QJL).

Encoder:  y = Rx,  store sign(y) + per-vector scalar S
Decoder:  estimate <q, x> ≈ S * <R^T q, sign(y)>

Reference: chapter_103.md §3.5 — "The rotation step is shared. The decoder is what changes."
          RaBitQ (Gao & Long, SIGMOD 2024), QJL (2024)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive, no blocking
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# === 字体设置（macOS 推荐 Heiti TC）===
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
# ====================================


def haar_orthogonal(d: int) -> np.ndarray:
    """Generate a uniform random orthogonal matrix via QR decomposition (Haar measure)."""
    with np.errstate(invalid='ignore', divide='ignore', over='ignore'):
        A = np.random.randn(d, d)
        Q, _ = np.linalg.qr(A)
        if np.linalg.det(Q) < 0:
            Q[:, 0] *= -1
    return Q


def drive_encode(x: np.ndarray, R: np.ndarray):
    """DRIVE encoder: rotate, sign-quantize, compute scaling factor."""
    y = R @ x
    sign_y = np.sign(y)
    # Avoid zero signs (rare for continuous distribution)
    sign_y[sign_y == 0] = 1
    S = np.dot(x, x) / np.sum(np.abs(y))  # unbiased scale: S_unb = ||x||_2^2 / ||y||_1
    return y, sign_y, S


def inner_product_decode(sign_y: np.ndarray, S: float, R: np.ndarray, q: np.ndarray) -> float:
    """
    Inner-product decoder (RaBitQ/QJL):
        <q, x> ≈ <q, x̂>  where  x̂ = S * R^T sign(y)

    The encoder stores sign(y) and S; the decoder uses a query vector q
    to estimate the inner product by computing <q, x̂>.

    Geometrically: q_rot = R @ q (rotate q into y's basis), then
    <q, x̂> = S * <q_rot, sign(y)> = S * sum_i (Rq)_i * sign(y_i)
    """
    q_rot = R @ q           # Rotate query into the same basis as y
    return S * np.dot(q_rot, sign_y)


def main():
    np.random.seed(42)

    d = 1024        # Dimension
    n_trials = 200  # Number of random query trials

    # Generate random orthogonal matrix (shared encoder)
    R = haar_orthogonal(d)

    # Generate a random vector x (the data to encode)
    x = np.random.randn(d)
    x_norm = np.linalg.norm(x)
    true_norm_sq = np.dot(x, x)

    # Encode
    y, sign_y, S = drive_encode(x, R)

    print("=" * 60)
    print("DRIVE Encoder + Inner-product Decoder (RaBitQ/QJL)")
    print("=" * 60)
    print(f"Dimension d = {d}")
    print(f"||x||_2 = {x_norm:.4f}")
    print(f"||x||_2^2 = {true_norm_sq:.4f}")
    print(f"||y||_1 = {np.sum(np.abs(y)):.4f}")
    print(f"S = ||x||_2^2 / ||y||_1 = {S:.4f}")
    print()

    # Test with many random queries
    errors = []
    rel_errors = []
    inner_products = []

    for _ in range(n_trials):
        q = np.random.randn(d)
        q = q / np.linalg.norm(q)  # Unit query vector

        true_ip = np.dot(q, x)  # True <q, x>
        est_ip = inner_product_decode(sign_y, S, R, q)

        error = est_ip - true_ip
        rel_error = abs(error) / abs(true_ip) if abs(true_ip) > 1e-10 else 0.0

        errors.append(error)
        rel_errors.append(rel_error)
        inner_products.append(true_ip)

    errors = np.array(errors)
    rel_errors = np.array(rel_errors)
    inner_products = np.array(inner_products)

    mean_error = np.mean(errors)
    std_error = np.std(errors)
    mean_rel_error = np.mean(rel_errors)

    print(f"Inner-product Estimation over {n_trials} random queries:")
    print(f"  Mean error:       {mean_error:.6f}")
    print(f"  Std error:        {std_error:.4f}")
    print(f"  Mean |rel error|: {mean_rel_error:.4f}")
    print()

    # Correlation between estimated and true inner products
    q_test = np.random.randn(n_trials, d)
    q_test = q_test / np.linalg.norm(q_test, axis=1, keepdims=True)
    true_ips_test = np.array([np.dot(q_test[i], x) for i in range(n_trials)])
    est_ips_test = np.array([inner_product_decode(sign_y, S, R, q_test[i]) for i in range(n_trials)])

    corr = np.corrcoef(true_ips_test, est_ips_test)[0, 1]

    print(f"Correlation (true vs estimated inner products): {corr:.4f}")
    print()

    # Show a few specific examples
    print("Sample queries (first 5):")
    print(f"{'True <q,x>':>15}  {'Est <q,x>':>15}  {'Rel Error':>12}")
    print("-" * 45)
    for i in range(5):
        true_ip_s = true_ips_test[i]
        est_ip_s = est_ips_test[i]
        rel_err_s = abs(est_ip_s - true_ip_s) / abs(true_ip_s) if abs(true_ip_s) > 1e-10 else 0.0
        print(f"{true_ip_s:15.4f}  {est_ip_s:15.4f}  {rel_err_s:12.4f}")

    # ===================================================================
    # 2D 可视化
    # ===================================================================
    rng = np.random.default_rng(seed=123)

    # --- 2D 辅助函数（直接从 103-2 复制） ---
    def haar_orthogonal_2d(theta: float) -> np.ndarray:
        return np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta),  np.cos(theta)]
        ])

    def draw_vector(ax, vec, color, label, alpha=1.0, lw=2.0, ls='-'):
        ax.annotate(
            "",
            xy=vec,
            xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                           mutation_scale=15, alpha=alpha, linestyle=ls),
            zorder=5,
        )
        norm = np.linalg.norm(vec)
        if norm > 0.01:
            ax.text(vec[0] * 0.55, vec[1] * 0.55, label,
                    color=color, fontsize=11, fontweight='bold',
                    ha='center', va='center', alpha=alpha)

    def draw_circle(ax, radius, color='gray', ls='--', lw=1.0, alpha=0.5):
        circle = plt.Circle((0, 0), radius, fill=False,
                            color=color, linestyle=ls, linewidth=lw, alpha=alpha)
        ax.add_patch(circle)

    # --- 2D 数据生成 ---
    theta_x = rng.uniform(0, 2 * np.pi)
    r_x = rng.uniform(0.8, 1.2)
    x_2d = np.array([r_x * np.cos(theta_x), r_x * np.sin(theta_x)])

    theta_R = rng.uniform(0, 2 * np.pi)
    R_2d = haar_orthogonal_2d(theta_R)

    y_2d = R_2d @ x_2d
    sign_y_2d = np.sign(y_2d)
    sign_y_2d[sign_y_2d == 0] = 1
    S_2d = np.dot(x_2d, x_2d) / np.sum(np.abs(y_2d))

    # query q (random direction)
    theta_q = rng.uniform(0, 2 * np.pi)
    q_2d = np.array([np.cos(theta_q), np.sin(theta_q)])
    q_rot_2d = R_2d @ q_2d  # rotate q into y's basis

    true_ip_2d = np.dot(q_2d, x_2d)
    est_ip_2d = S_2d * np.dot(q_rot_2d, sign_y_2d)
    x_hat_2d = S_2d * (R_2d.T @ sign_y_2d)

    # --- 绘图 ---
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Inner-product Decoder (RaBitQ/QJL): 2D 可视化", fontsize=14, fontweight='bold')

    all_vecs = [x_2d, y_2d, sign_y_2d * max(np.linalg.norm(x_2d), 1.0), x_hat_2d, q_2d]
    max_range = max(np.linalg.norm(v) for v in all_vecs) * 1.5

    # Panel 1: x and y=Rx
    ax = axes[0]
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    ax.axvline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    draw_circle(ax, 1.0, color='gray', ls=':', lw=1.0, alpha=0.4)
    ax.set_title("① x (blue) and y=Rx (green)", fontsize=11)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    draw_vector(ax, x_2d, 'blue', 'x')
    draw_vector(ax, y_2d, 'green', 'y=Rx')

    # Panel 2: sign(y) + query q in rotated space
    ax = axes[1]
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    ax.axvline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    draw_circle(ax, 1.0, color='gray', ls=':', lw=1.0, alpha=0.4)
    ax.set_title("② sign(y) (red) + query q (magenta)", fontsize=11)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    draw_vector(ax, sign_y_2d * max(np.linalg.norm(x_2d), 1.0), 'red', 'sign(y)', lw=1.5, ls='--', alpha=0.7)
    draw_vector(ax, q_2d * max(np.linalg.norm(x_2d), 1.0), 'magenta', 'q')

    # Panel 3: x vs x_hat with inner product info
    ax = axes[2]
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    ax.axvline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    draw_circle(ax, 1.0, color='gray', ls=':', lw=1.0, alpha=0.4)
    ax.set_title(f"③ Reconstructed x_hat (orange)", fontsize=11)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    draw_vector(ax, x_2d, 'blue', 'x (true)')
    draw_vector(ax, x_hat_2d, 'orange', 'x_hat')
    # Add inner product annotation
    ip_text = (f"True <q,x> = {true_ip_2d:.3f}\n"
               f"Est  <q,x> = {est_ip_2d:.3f}\n"
               f"Error: {abs(est_ip_2d - true_ip_2d):.3f}")
    ax.text(max_range * 0.05, -max_range * 0.75, ip_text,
            fontsize=9, va='top', ha='left',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Legend
    legend_elements = [
        Line2D([0], [0], color='blue', lw=2.5, label='x (original)'),
        Line2D([0], [0], color='green', lw=2.5, label='y = R·x (rotated)'),
        Line2D([0], [0], color='red', lw=1.5, ls='--', label='sign(y) (quantized)'),
        Line2D([0], [0], color='magenta', lw=2.5, label='q (query)'),
        Line2D([0], [0], color='orange', lw=2.5, label='x_hat (reconstructed)'),
    ]
    fig.legend(handles=legend_elements, loc='lower center', ncol=5,
               fontsize=10, framealpha=0.9)

    plt.tight_layout(rect=[0, 0.08, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    main()
