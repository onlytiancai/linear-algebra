"""
EDEN / TurboQuant MSE Decoder Visualization
===========================================
Demonstrates the DRIVE encoder + MSE decoder (EDEN / TurboQuant).

EDEN:  Normalizes by η_x = √d/||x||_2, quantizes with Lloyd-Max codebook,
       stores S = ||x||_2^2 / <R(x), Q(η_x R(x))>, decodes x̂ = R^T(Q(η_x R(x))·S)

TurboQuant:  Same but fixes per-vector scale to a constant c.

Reference: chapter_103.md §3.5 — EDEN (Vargaftik et al., ICML 2022),
          TurboQuant (Zandieh et al., 2025)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False


def haar_orthogonal(d: int) -> np.ndarray:
    """Generate a uniform random orthogonal matrix via QR decomposition (Haar measure)."""
    with np.errstate(invalid='ignore', divide='ignore', over='ignore'):
        A = np.random.randn(d, d)
        Q, _ = np.linalg.qr(A)
        if np.linalg.det(Q) < 0:
            Q[:, 0] *= -1
    return Q


# Lloyd-Max codebooks for standard normal (approximated for 1-bit and 2-bit)
# 1-bit:  {± √(2/π)} ≈ {±0.798}
# 2-bit:  {±0.453, ±1.510}
CODEBOOKS = {
    1: np.array([-np.sqrt(2 / np.pi), np.sqrt(2 / np.pi)]),       # ≈ {-0.798, 0.798}
    2: np.array([-1.510, -0.453, 0.453, 1.510]),
}


def quantize_lloyd_max(y: np.ndarray, codebook: np.ndarray) -> np.ndarray:
    """Quantize each coordinate of y to the nearest codebook level (vectorized)."""
    if len(codebook) == 2:
        # 1-bit: simple sign-based quantization (codebook = {±√(2/π)})
        return np.where(y >= 0, codebook[1], codebook[0])
    else:
        # General case: vectorized nearest-neighbor across all coordinates
        # For each y_i, find argmin_c |y_i - c|^2
        diffs = codebook[np.newaxis, :] - y[:, np.newaxis]  # shape (n, k)
        indices = np.argmin(diffs ** 2, axis=1)
        return codebook[indices]


def eden_encode(x: np.ndarray, R: np.ndarray, b: int = 1):
    """
    EDEN encoder for b-bit quantization.

    Steps:
      y = Rx
      η_x = √d / ||x||_2          (normalize so y' ≈ N(0,1))
      y' = η_x * y
      Q(y')  (Lloyd-Max quantization)
      S = ||x||_2^2 / <y, Q(y')>  (unbiased scale)
    Returns: sign/sign-set, S, η_x, quantized y'
    """
    d = len(x)
    y = R @ x
    eta_x = np.sqrt(d) / np.linalg.norm(x)     # η_x = √d / ||x||_2
    y_normalized = eta_x * y                    # ≈ N(0,1) per coordinate

    codebook = CODEBOOKS.get(b, CODEBOOKS[1])
    q_y = quantize_lloyd_max(y_normalized, codebook)

    # Unbiased scale: S = ||x||_2^2 / <y, Q(y')>
    S = np.dot(x, x) / np.dot(y, q_y)

    return y, q_y, S, eta_x


def eden_decode(sign_q: np.ndarray, S: float, R: np.ndarray) -> np.ndarray:
    """
    EDEN MSE decoder:
        x̂ = R^T (Q(y') · S)

    Note: Q(y') is stored as sign_q in our simplified version.
    For full EDEN (multi-bit), Q(y') values are stored.
    """
    # In our simplified encoder, we store the quantized values
    return R.T @ (sign_q * S)


def turboquant_encode(x: np.ndarray, R: np.ndarray, b: int = 1, c: float = None):
    """
    TurboQuant encoder: same as EDEN but fixes scale to constant c.

    If c is None, estimates c as median of EDEN scales over calibration set.
    For simplicity, we use the theoretical value: E[S] = √(π/2) * ||x||_2 / √d
    (approximately, for unbiased EDEN with 1-bit).
    """
    d = len(x)
    y = R @ x
    eta_x = np.sqrt(d) / np.linalg.norm(x)
    y_normalized = eta_x * y

    codebook = CODEBOOKS.get(b, CODEBOOKS[1])
    q_y = quantize_lloyd_max(y_normalized, codebook)

    # Theoretical scale constant (≈ √(π/2) for 1-bit)
    if c is None:
        # For 1-bit: E[|y_i|] = √(2/π)  →  S ≈ ||x||_2 / √d * √(π/2)
        c = np.sqrt(np.pi / 2) * np.linalg.norm(x) / np.sqrt(d)

    return y, q_y, c, eta_x


def turboquant_decode(q_y: np.ndarray, c: float, R: np.ndarray) -> np.ndarray:
    """TurboQuant MSE decoder: x̂ = R^T (Q(y') · c)"""
    return R.T @ (q_y * c)


def compute_rel_mse(x: np.ndarray, x_hat: np.ndarray) -> float:
    """Relative MSE: ||x̂ - x||_2^2 / ||x||_2^2"""
    return np.sum((x_hat - x) ** 2) / np.sum(x ** 2)


def main():
    np.random.seed(42)

    d = 1024       # Dimension
    n_trials = 200

    print("=" * 65)
    print("EDEN / TurboQuant MSE Decoder")
    print("=" * 65)
    print(f"Dimension d = {d}")
    print()

    # Compare 1-bit and 2-bit EDEN
    for b in [1, 2]:
        print(f"{'='*40}")
        print(f"  {b}-bit EDEN vs TurboQuant")
        print(f"{'='*40}")

        rel_errors_eden = []
        rel_errors_turbo = []
        biases_eden = []
        biases_turbo = []

        for trial in range(n_trials):
            R = haar_orthogonal(d)
            x = np.random.randn(d)

            # EDEN
            y, q_y, S_eden, eta_x = eden_encode(x, R, b=b)
            x_hat_eden = eden_decode(q_y, S_eden, R)
            rel_err_eden = compute_rel_mse(x, x_hat_eden)
            bias_eden = np.linalg.norm(x_hat_eden) / np.linalg.norm(x) - 1
            rel_errors_eden.append(rel_err_eden)
            biases_eden.append(bias_eden)

            # TurboQuant
            y2, q_y2, c, _ = turboquant_encode(x, R, b=b)
            x_hat_turbo = turboquant_decode(q_y2, c, R)
            rel_err_turbo = compute_rel_mse(x, x_hat_turbo)
            bias_turbo = np.linalg.norm(x_hat_turbo) / np.linalg.norm(x) - 1
            rel_errors_turbo.append(rel_err_turbo)
            biases_turbo.append(bias_turbo)

        print(f"\nEDEN ({b}-bit):")
        print(f"  Mean rel-MSE:  {np.mean(rel_errors_eden):.4f}")
        print(f"  Std  rel-MSE:  {np.std(rel_errors_eden):.4f}")
        print(f"  Mean norm bias: {np.mean(biases_eden):.4f}  (||x̂||/||x|| - 1)")
        # Quick check: vector unbiasedness over 50 random rotations
        n_check = 50
        x_fixed = np.random.randn(d)
        x_fixed = x_fixed / np.linalg.norm(x_fixed)
        biases_over_R = []
        for _ in range(n_check):
            R_rnd = haar_orthogonal(d)
            _, q_rnd, S_rnd, _ = eden_encode(x_fixed, R_rnd, b=b)
            x_hat_rnd = eden_decode(q_rnd, S_rnd, R_rnd)
            biases_over_R.append(np.mean(x_hat_rnd - x_fixed))
        print(f"  Vector bias (E_R[x̂-x]): {np.mean(biases_over_R):.4f}  (should be ≈0)")
        print(f"  Std across R: {np.std(biases_over_R):.4f}")

        print(f"\nTurboQuant ({b}-bit, fixed c):")
        print(f"  Mean rel-MSE:  {np.mean(rel_errors_turbo):.4f}")
        print(f"  Std  rel-MSE:  {np.std(rel_errors_turbo):.4f}")
        print(f"  Mean norm bias: {np.mean(biases_turbo):.4f}  (biased, but stable)")

        # Compare bias/variance tradeoff
        print(f"\n  EDEN MSE-optimal vs unbiased:")
        print(f"    MSE = bias^2 + var = ({np.mean(biases_eden):.4f})^2 + ({np.std(rel_errors_eden):.4f})^2")

    print()
    print("=" * 65)
    print("Summary:  EDEN uses per-vector S → unbiased but higher variance")
    print("         TurboQuant fixes S=c → slightly biased but lower variance")
    print("         Both store: rotation R (shared), codebook Q, η_x (EDEN only)")
    print("=" * 65)

    # Show a concrete example
    print("\n--- Concrete example (d=16, 1-bit) ---")
    d_demo = 16
    R_demo = haar_orthogonal(d_demo)
    x_demo = np.random.randn(d_demo)

    y_demo = R_demo @ x_demo
    eta_demo = np.sqrt(d_demo) / np.linalg.norm(x_demo)
    y_norm_demo = eta_demo * y_demo
    q_demo = quantize_lloyd_max(y_norm_demo, CODEBOOKS[1])
    S_demo = np.dot(x_demo, x_demo) / np.dot(y_demo, q_demo)

    x_hat_demo = eden_decode(q_demo, S_demo, R_demo)
    x_hat_turbo_demo = turboquant_decode(q_demo, np.sqrt(np.pi/2) * np.linalg.norm(x_demo) / np.sqrt(d_demo), R_demo)

    print(f"  ||x||_2      = {np.linalg.norm(x_demo):.4f}")
    print(f"  ||x̂_EDEN||_2 = {np.linalg.norm(x_hat_demo):.4f}")
    print(f"  ||x̂_TURBO||_2= {np.linalg.norm(x_hat_turbo_demo):.4f}")
    print(f"  rel-MSE EDEN  = {compute_rel_mse(x_demo, x_hat_demo):.4f}")
    print(f"  rel-MSE TURBO = {compute_rel_mse(x_demo, x_hat_turbo_demo):.4f}")
    print(f"\n  x (first 5):   {x_demo[:5].round(3)}")
    print(f"  x̂ EDEN (first 5): {x_hat_demo[:5].round(3)}")

    # ===================================================================
    # 2D 可视化
    # ===================================================================
    # 2D helpers
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

    rng = np.random.default_rng(seed=99)
    theta_x = rng.uniform(0, 2 * np.pi)
    r_x = rng.uniform(0.8, 1.2)
    x_2d = np.array([r_x * np.cos(theta_x), r_x * np.sin(theta_x)])
    theta_R = rng.uniform(0, 2 * np.pi)
    R_2d = haar_orthogonal_2d(theta_R)

    # Encode
    y_2d = R_2d @ x_2d
    eta_2d = np.sqrt(2) / np.linalg.norm(x_2d)
    y_norm_2d = eta_2d * y_2d
    codebook_1d = np.array([-np.sqrt(2 / np.pi), np.sqrt(2 / np.pi)])
    q_y_2d = np.where(y_norm_2d >= 0, codebook_1d[1], codebook_1d[0])
    S_eden_2d = np.dot(x_2d, x_2d) / np.dot(y_2d, q_y_2d)

    # EDEN 1-bit decode
    x_hat_eden_2d = eden_decode(q_y_2d, S_eden_2d, R_2d)
    # TurboQuant 1-bit decode: c ≈ √(π/2) * E[|y_i|] ≈ 1
    c_fixed = 1.0
    x_hat_turbo_2d = turboquant_decode(q_y_2d, c_fixed, R_2d)

    # Compute errors
    err_eden = np.linalg.norm(x_hat_eden_2d - x_2d) / np.linalg.norm(x_2d)
    err_turbo = np.linalg.norm(x_hat_turbo_2d - x_2d) / np.linalg.norm(x_2d)

    # Quantization level lines for Panel 2
    # In 1D (rotated space), the quantization thresholds are at 0 for sign
    q_levels = np.array([-np.sqrt(2 / np.pi), np.sqrt(2 / np.pi)])

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("EDEN / TurboQuant MSE Decoder: 2D 可视化", fontsize=14, fontweight='bold')

    all_vecs = [x_2d, y_2d, x_hat_eden_2d, x_hat_turbo_2d]
    max_range = max(np.linalg.norm(v) for v in all_vecs) * 1.5

    # Panel 1: x and y
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

    # Panel 2: Quantized y' (EDEN normalized) on 1D axis
    ax = axes[1]
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range * 0.3, max_range * 0.3)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    ax.axvline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    # Draw quantization thresholds as vertical lines
    for lvl in q_levels:
        ax.axvline(lvl * np.linalg.norm(x_2d) * 0.5, color='red', ls='--',
                   lw=1.0, alpha=0.5, label=f'level={lvl:.3f}' if lvl == q_levels[0] else '')
    ax.set_title("② y' = η_x · y (green→), Q(y') (red bars)", fontsize=11)
    ax.set_xlabel("rotated axis")
    ax.set_ylabel("")
    ax.grid(True, alpha=0.3)
    # Show y and quantized q_y as arrows on x-axis projection
    draw_vector(ax, y_2d, 'green', 'y', alpha=0.7, lw=2.0)
    draw_vector(ax, q_y_2d * np.linalg.norm(x_2d) * 0.3, 'red', 'Q(y\')',
                alpha=0.9, lw=2.5, ls='--')
    ax.legend(handles=[
        Line2D([0], [0], color='green', lw=2.0, label='y (continuous)'),
        Line2D([0], [0], color='red', lw=2.5, ls='--', label='Q(y\') (quantized)'),
    ], loc='upper right', fontsize=9)

    # Panel 3: Reconstructed x_hat
    ax = axes[2]
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    ax.axvline(0, color='gray', lw=0.5, ls='--', alpha=0.5)
    draw_circle(ax, 1.0, color='gray', ls=':', lw=1.0, alpha=0.4)
    ax.set_title(f"③ EDEN vs TurboQuant reconstruction", fontsize=11)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    draw_vector(ax, x_2d, 'blue', 'x (true)')
    draw_vector(ax, x_hat_eden_2d, 'orange', 'x_hat EDEN')
    draw_vector(ax, x_hat_turbo_2d, 'purple', 'x_hat TURBO')
    # Error annotation
    err_text = (f"EDEN rel-err: {err_eden:.3f}\n"
                f"TURBO rel-err: {err_turbo:.3f}\n"
                f"c_fixed = {c_fixed:.2f}")
    ax.text(max_range * 0.05, -max_range * 0.75, err_text,
            fontsize=9, va='top', ha='left',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Legend
    legend_elements = [
        Line2D([0], [0], color='blue', lw=2.5, label='x (true)'),
        Line2D([0], [0], color='green', lw=2.5, label='y = R·x (rotated)'),
        Line2D([0], [0], color='orange', lw=2.5, label='x_hat EDEN'),
        Line2D([0], [0], color='purple', lw=2.5, label='x_hat TurboQuant'),
    ]
    fig.legend(handles=legend_elements, loc='lower center', ncol=4,
               fontsize=10, framealpha=0.9)

    plt.tight_layout(rect=[0, 0.08, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    main()
