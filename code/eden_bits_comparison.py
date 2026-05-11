import numpy as np
import matplotlib.pyplot as plt

# 中文支持
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Hiragino Sans GB', 'Heiti TC', 'SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def random_rotation(d, seed=None):
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((d, d))
    Q, _ = np.linalg.qr(A)
    return Q


def quantize_uniform(z, bits):
    # 均匀量化：将 z 映射到 [-3, 3] 范围，分为 2^bits 个 bin
    levels = 2 ** bits
    z_clipped = np.clip(z, -3, 3)
    quantized = np.round((z_clipped + 3) / (6 / levels)) * (6 / levels) - 3
    return quantized


def quantize_1bit_standard_normal(z):
    # 1-bit Lloyd-Max 码本近似标准正态的最优值
    return np.sign(z) * np.sqrt(2 / np.pi)


def reconstruct_simple(q, eta_x, R):
    # 简单重构：先把量化值从归一化域恢复到旋转域，再逆旋转
    y_hat = q / eta_x
    return R.T @ y_hat


def reconstruct_unbiased(x, y, q, R):
    # EDEN 1-bit 无偏缩放：S = ||x||^2 / <y, q>
    denom = np.dot(y, q)
    if np.isclose(denom, 0.0):
        return reconstruct_simple(q, np.sqrt(y.shape[0]) / np.linalg.norm(x), R)
    S = np.linalg.norm(x) ** 2 / denom
    return R.T @ (q * S)


def vector_metrics(X, X_hat):
    diffs = X_hat - X
    mse = np.mean(np.sum(diffs ** 2, axis=1))
    bias = np.mean(np.sum(diffs, axis=1))
    mean_norm_orig = np.mean(np.linalg.norm(X, axis=1))
    mean_norm_hat = np.mean(np.linalg.norm(X_hat, axis=1))
    cosines = np.sum(X * X_hat, axis=1) / (np.linalg.norm(X, axis=1) * np.linalg.norm(X_hat, axis=1) + 1e-12)
    return {
        'mse': mse,
        'mean_bias': bias,
        'mean_norm_orig': mean_norm_orig,
        'mean_norm_hat': mean_norm_hat,
        'mean_cosine': np.mean(cosines),
        'std_cosine': np.std(cosines),
    }


def inner_product_metrics(V, X, X_hat):
    ip_orig = X @ V
    ip_hat = X_hat @ V
    return {
        'mean_abs_error': np.mean(np.abs(ip_hat - ip_orig)),
        'mean_rel_error': np.mean(np.abs(ip_hat - ip_orig) / (np.abs(ip_orig) + 1e-12)),
        'mse': np.mean((ip_hat - ip_orig) ** 2),
        'corr': np.corrcoef(ip_orig, ip_hat)[0, 1],
    }


def run_comparison(n_vectors=100, d=100, seed=42):
    rng = np.random.default_rng(seed)
    R = random_rotation(d, seed=seed + 1)
    X = rng.standard_normal((n_vectors, d))

    bits_list = [1, 2, 4, 8]
    results = {}

    for bits in bits_list:
        print(f'=== {bits}-bit 量化 ===')
        X_hat = np.zeros_like(X)

        for i, x in enumerate(X):
            y = R @ x
            eta_x = np.sqrt(d) / np.linalg.norm(x)
            y_norm = eta_x * y
            if bits == 1:
                q = quantize_1bit_standard_normal(y_norm)
                X_hat[i] = reconstruct_unbiased(x, y, q, R)
            else:
                q = quantize_uniform(y_norm, bits)
                X_hat[i] = reconstruct_simple(q, eta_x, R)

        metrics = vector_metrics(X, X_hat)
        v = rng.standard_normal(d)
        v = v / np.linalg.norm(v)
        ip_metrics = inner_product_metrics(v, X, X_hat)

        results[bits] = {'vector': metrics, 'inner_product': ip_metrics}

        print('向量指标:')
        for k, v in metrics.items():
            print(f'  {k}: {v:.6f}')
        print('内积指标:')
        for k, v in ip_metrics.items():
            print(f'  {k}: {v:.6f}')
        print()

    # 可视化
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # MSE vs bits
    axes[0, 0].plot(bits_list, [results[b]['vector']['mse'] for b in bits_list], marker='o', label='MSE')
    axes[0, 0].set_title('MSE vs Bits')
    axes[0, 0].set_xlabel('Bits')
    axes[0, 0].set_ylabel('MSE')
    axes[0, 0].set_xticks(bits_list)
    axes[0, 0].grid(True)

    # Bias vs bits
    axes[0, 1].plot(bits_list, [results[b]['vector']['mean_bias'] for b in bits_list], marker='o', label='Mean Bias', color='orange')
    axes[0, 1].set_title('Mean Bias vs Bits')
    axes[0, 1].set_xlabel('Bits')
    axes[0, 1].set_ylabel('Mean Bias')
    axes[0, 1].set_xticks(bits_list)
    axes[0, 1].grid(True)

    # Cosine Similarity vs bits
    axes[1, 0].plot(bits_list, [results[b]['vector']['mean_cosine'] for b in bits_list], marker='o', label='Mean Cosine', color='green')
    axes[1, 0].set_title('Mean Cosine Similarity vs Bits')
    axes[1, 0].set_xlabel('Bits')
    axes[1, 0].set_ylabel('Mean Cosine')
    axes[1, 0].set_xticks(bits_list)
    axes[1, 0].grid(True)

    # Inner Product Correlation vs bits
    axes[1, 1].plot(bits_list, [results[b]['inner_product']['corr'] for b in bits_list], marker='o', label='Correlation', color='red')
    axes[1, 1].set_title('Inner Product Correlation vs Bits')
    axes[1, 1].set_xlabel('Bits')
    axes[1, 1].set_ylabel('Correlation')
    axes[1, 1].set_xticks(bits_list)
    axes[1, 1].grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run_comparison()