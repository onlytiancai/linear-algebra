"""
103-8.py
========

Lloyd–Max：已知分布的最优标量量化（Universal Codebook 的核心）

复刻 web 交互 demo "Lloyd–Max: the optimal partition of a known distribution"
的 b=2, d=64, σ=1/√d 情形。核心要点：

  1. 旋转后每个坐标近似 N(0, 1/d) —— 分布完全已知
  2. Lloyd–Max 迭代两个步骤：
       (a) 最近邻划分：把 x 分到最近的码字 c_k
       (b) 质心更新：c_k ← 该 bin 在 f 下的条件期望 E[x | x ∈ bin k]
  3. 逐坐标 MSE 与 Shannon 下界 1 / (4^b · d) 比较
  4. 显式质心 b=1: {±√(2/π)},  b=2: {±0.453, ±1.510}, ...

运行：
    /Users/huhao/.pyenv/versions/qlib/bin/python code/103-8.py
"""

import numpy as np
from scipy.stats import norm


# ============================================================
# 1. 目标分布：旋转后坐标的边缘分布 N(0, 1/d)
# ============================================================

def sample_marginal(n: int, d: int, rng: np.random.Generator) -> np.ndarray:
    """
    模拟"旋转后坐标"的边缘采样。

    做法（等价于真实流程的简版）：
        1. 采样一个随机正交矩阵 R ∈ R^{d×d}
        2. 采一个标准球面方向 v ∈ S^{d-1}
        3. 取 R v 的第 0 维

    对大 d，第 0 维的分布是 Beta(1/2, (d-1)/2)，经 √d 缩放后近似 N(0,1)。

    这里为了算法演示直接采样 N(0, 1/d) —— 两种分布在 d=64 时
    视觉上几乎不可区分。
    """
    sigma = 1.0 / np.sqrt(d)
    return rng.normal(loc=0.0, scale=sigma, size=n)


def pdf_marginal(x: np.ndarray, d: int) -> np.ndarray:
    """边缘分布的精确 PDF：N(0, 1/d)。"""
    sigma = 1.0 / np.sqrt(d)
    return norm.pdf(x, loc=0.0, scale=sigma)


# ============================================================
# 2. Lloyd–Max 迭代
# ============================================================

def lloyd_max(
    d: int,
    b: int,
    n_samples: int = 200_000,
    max_iter: int = 60,
    tol: float = 1e-9,
    rng_seed: int = 0,
    verbose: bool = True,
) -> dict:
    """
    对 N(0, 1/d) 跑 Lloyd–Max 迭代，返回 (码本, 边界, MSE 序列, 质心历史)。

    Parameters
    ----------
    d : int
        维度（只决定 σ = 1/√d，对单坐标 Lloyd–Max 而言 d 影响缩放但不影响归一化形状）
    b : int
        每个坐标的比特数；码本大小 K = 2^b
    n_samples : int
        用于估计 bin 质心的 Monte-Carlo 样本量
    max_iter : int
        最大迭代次数
    tol : float
        收敛阈值：相邻两次码本最大位移
    rng_seed : int
        随机种子
    """
    rng = np.random.default_rng(rng_seed)
    K = 2 ** b
    sigma = 1.0 / np.sqrt(d)

    # 1) 初始化：均匀地把样本分到 K 个分位点（mean-of-K 个高斯分位）
    #    等价于"高分辨率初始码本" —— 收敛最快
    quantiles = (np.arange(K) + 0.5) / K
    init_levels = sigma * norm.ppf(quantiles)   # N(0, σ²) 的 K 个分位中心
    codebook = init_levels.copy()

    # 历史
    mse_history = []
    codebook_history = [codebook.copy()]

    # 采样一个大池子反复用
    x = rng.normal(loc=0.0, scale=sigma, size=n_samples)

    for it in range(max_iter):
        # (a) 最近邻划分：把每个 x 映到最近码字
        #     对称分布可以排序码本后用 searchsorted
        sorted_cb = np.sort(codebook)
        # 每个 x 落入 [sorted_cb[i], sorted_cb[i+1]) 中 → 归到 sorted_cb[i]
        # 简化做法：直接用广播 + argmin（对 K=256 仍很快）
        dists = np.abs(x[:, None] - sorted_cb[None, :])
        assignments = np.argmin(dists, axis=1)

        # (b) 质心更新：每个 bin 的条件期望
        new_codebook = np.array([
            x[assignments == k].mean() if np.any(assignments == k) else sorted_cb[k]
            for k in range(K)
        ])
        # 重新按从小到大排序（保持单调）
        new_codebook = np.sort(new_codebook)

        # 计算当前 MSE
        mse = np.mean((x - new_codebook[assignments]) ** 2)
        mse_history.append(mse)

        # 收敛？
        shift = np.max(np.abs(new_codebook - codebook))
        codebook_history.append(new_codebook.copy())
        codebook = new_codebook

        if verbose:
            print(f"  iter {it+1:3d}  shift={shift:.3e}  MSE/coord = {mse:.4e}  "
                  f"Shannon-bound = {shannon_bound_1d(b, d):.4e}")

        if shift < tol:
            break

    # 边界 = 相邻码字的中点
    boundaries = 0.5 * (codebook[:-1] + codebook[1:])

    return {
        "codebook": codebook,
        "boundaries": boundaries,
        "mse_history": np.array(mse_history),
        "codebook_history": codebook_history,
        "K": K,
        "b": b,
        "d": d,
        "sigma": sigma,
        "n_iter": len(mse_history),
    }


# ============================================================
# 3. Shannon 下界（一维）
# ============================================================

def shannon_bound_1d(b: int, d: int) -> float:
    """
    Shannon–Lloyd 高分辨率下界（per-coord 形式）。

    对 d 维旋转后坐标：每坐标 MSE ≥ 1 / (4^b · d)。
    """
    return 1.0 / ((4 ** b) * d)


def shannon_bound_1d_full(b: int, d: int) -> float:
    """
    完整形式（含一阶常数）：  1 / (12 K^2) · ∫ (f'(x)^2 / f(x)) dx  / d

    对 N(0, σ²)，Panter–Dite 公式：
        MSE*_asym = (π/6) · (3σ^2 / K^2)^(2/3) · σ^(2/3) · σ^(-2) · (...)
    简化为：   ≈ σ^2 / (3 K^2) · √3 · π  (高分辨率极限)
    """
    sigma = 1.0 / np.sqrt(d)
    K = 2 ** b
    # 高分辨率下 MSE ≈ σ^2 / (12 K^2) · √(12/π) ... 给个常用近似：
    #   Panter–Dite:  MSE_asym = (π/3√3) · σ^(2/3) · 1/K^2 · (...)  用
    #   对 K 大、K 大到分箱小到 1/K<<σ 渐近成立。
    # 这里给一个等价表示：用 (√3π/2) * σ^2 / (3 K^2) ≈ 0.9069 * σ^2 / K^2
    return (np.sqrt(3) * np.pi / 2.0) * (sigma ** 2) / (3.0 * K ** 2)


# ============================================================
# 4. 主程序
# ============================================================

def main():
    # 与图上一致的参数
    d = 64
    b = 2
    K = 2 ** b
    sigma = 1.0 / np.sqrt(d)

    print("=" * 72)
    print(f"Lloyd–Max for N(0, 1/d),   b = {b} bits,  K = {K} levels,  "
          f"d = {d},  σ = 1/√d = {sigma:.4f}")
    print("=" * 72)

    result = lloyd_max(d=d, b=b, n_samples=400_000, max_iter=80)

    print()
    print("-" * 72)
    print(f"收敛码本（按 √d 归一化后）: {result['codebook'] / sigma}")
    print(f"论文显式值 b=2:             [{-0.453:.3f}, {-1.510:.3f}, "
          f"{0.453:.3f}, {1.510:.3f}]")
    print("-" * 72)
    print(f"最终 MSE per coord = {result['mse_history'][-1]:.4e}")
    print(f"Shannon 下界  1/(4^b·d) = {shannon_bound_1d(b, d):.4e}")
    print(f"图上初始值 iter=0       = 2.966e-3   (与 K-means 初始码字有关)")
    print(f"迭代次数                 = {result['n_iter']}")
    print("=" * 72)

    # 把关键量写到返回值供后续使用
    return result


if __name__ == "__main__":
    out = main()
