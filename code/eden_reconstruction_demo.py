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


def run_demo(n_vectors=1000, d=100, seed=42):
    rng = np.random.default_rng(seed)
    R = random_rotation(d, seed=seed + 1)
    X = rng.standard_normal((n_vectors, d))

    X_hat_simple = np.zeros_like(X)
    X_hat_unbiased = np.zeros_like(X)

    for i, x in enumerate(X):
        y = R @ x
        eta_x = np.sqrt(d) / np.linalg.norm(x)
        y_norm = eta_x * y
        q = quantize_1bit_standard_normal(y_norm)
        X_hat_simple[i] = reconstruct_simple(q, eta_x, R)
        X_hat_unbiased[i] = reconstruct_unbiased(x, y, q, R)

    metrics_simple = vector_metrics(X, X_hat_simple)
    metrics_unbiased = vector_metrics(X, X_hat_unbiased)

    print('=== 1000 个向量重构统计 ===')
    print('简单重构:')
    for k, v in metrics_simple.items():
        print(f'  {k}: {v:.6f}')
    print('EDEN 无偏重构:')
    for k, v in metrics_unbiased.items():
        print(f'  {k}: {v:.6f}')

    # 原始数据与重构数据的统计特征对比
    mean_orig = np.mean(X, axis=0)
    mean_hat = np.mean(X_hat_unbiased, axis=0)
    std_orig = np.std(X, axis=0)
    std_hat = np.std(X_hat_unbiased, axis=0)
    print('\n=== 数据集统计特征 ===')
    print(f'原始均值向量 L2: {np.linalg.norm(mean_orig):.6f}')
    print(f'重构均值向量 L2: {np.linalg.norm(mean_hat):.6f}')
    print(f'均值向量差异 L2: {np.linalg.norm(mean_hat - mean_orig):.6f}')
    print(f'原始 std 均值: {np.mean(std_orig):.6f}')
    print(f'重构 std 均值: {np.mean(std_hat):.6f}')

    # 内积误差测试
    v = rng.standard_normal(d)
    v = v / np.linalg.norm(v)
    ip_simple = inner_product_metrics(v, X, X_hat_simple)
    ip_unbiased = inner_product_metrics(v, X, X_hat_unbiased)

    print('\n=== 内积保持测试 (v·x vs v·x_hat) ===')
    print('简单重构:')
    for k, val in ip_simple.items():
        print(f'  {k}: {val:.6f}')
    print('EDEN 无偏重构:')
    for k, val in ip_unbiased.items():
        print(f'  {k}: {val:.6f}')

    # 可视化统计特征变化
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes[0, 0].hist(np.linalg.norm(X, axis=1), bins=30, alpha=0.6, label='原始', color='blue')
    axes[0, 0].hist(np.linalg.norm(X_hat_unbiased, axis=1), bins=30, alpha=0.6, label='重构', color='orange')
    axes[0, 0].set_title('向量范数分布')
    axes[0, 0].legend()

    axes[0, 1].hist(np.sum(X * X_hat_unbiased, axis=1) / (np.linalg.norm(X, axis=1) * np.linalg.norm(X_hat_unbiased, axis=1) + 1e-12), bins=30, color='green')
    axes[0, 1].set_title('原始与重构余弦相似度')

    axes[1, 0].scatter(np.sum(X * v, axis=1), np.sum(X_hat_unbiased * v, axis=1), alpha=0.4)
    axes[1, 0].plot([-4, 4], [-4, 4], 'r--')
    axes[1, 0].set_title('v·x vs v·x_hat (EDEN)')
    axes[1, 0].set_xlabel('原始内积')
    axes[1, 0].set_ylabel('重构内积')

    axes[1, 1].hist(np.sum(X_hat_unbiased * v, axis=1) - np.sum(X * v, axis=1), bins=30, color='purple')
    axes[1, 1].set_title('内积误差分布 (EDEN)')
    axes[1, 1].set_xlabel('v·x_hat - v·x')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run_demo()