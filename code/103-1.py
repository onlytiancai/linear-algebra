"""
DRIVE Mean encoder/decoder demo (chapter_103 §0.9.1 / §3)

对单个向量 x 演示 DRIVE 一比特编码/解码过程：
  - 编码器:  y = sign(R x)     配合标量 S
  - 解码器:  x_hat = S * (R^T y)

两套缩放公式：
  1) MSE-optimal (biased):  S = ||R x||_1 / d
  2) Unbiased:              S = ||x||_2^2 / ||R x||_1   ⇒  E[x_hat] = x

旋转 R 取随机正交矩阵（Haar 测度），等价于对坐标做 i.i.d. 高斯后做 QR。
"""

import numpy as np


# ---------------------------------------------------------------------------
# 工具: 随机正交矩阵 (Haar 测度)
# ---------------------------------------------------------------------------
def haar_orthogonal(d: int, rng: np.random.Generator) -> np.ndarray:
    """从正交群 O(d) 上均匀采样一个正交矩阵 (det = +1)。"""
    A = rng.standard_normal((d, d))
    Q, R = np.linalg.qr(A)
    # 修正符号使 det = +1 (即 Haar SO(d))
    Q = Q * np.sign(np.diag(R))[None, :]
    return Q


# ---------------------------------------------------------------------------
# DRIVE 编码器
# ---------------------------------------------------------------------------
def drive_encode(x: np.ndarray, R: np.ndarray):
    """
    编码:
      y        = R x                          旋转向量
      sign_y   = sign(y) ∈ {+1, -1}^d         1 bit / 坐标
      S_mse    = ||y||_1 / d                  MSE-optimal 缩放
      S_unb    = ||x||_2^2 / ||y||_1          无偏缩放
    """
    y = R @ x
    sign_y = np.sign(y).astype(np.int8)            # +1 / -1
    S_mse = np.linalg.norm(y, 1) / len(x)
    S_unb = (np.dot(x, x)) / np.linalg.norm(y, 1)
    return {
        "y": y,
        "sign_y": sign_y,
        "S_mse": S_mse,
        "S_unb": S_unb,
        "bits_per_coord": 1.0,
    }


# ---------------------------------------------------------------------------
# DRIVE 解码器
# ---------------------------------------------------------------------------
def drive_decode(code: dict, R: np.ndarray, mode: str = "unbiased") -> np.ndarray:
    """
    解码:
      x_hat = S * R^T sign(R x)
    """
    sign_y = code["sign_y"].astype(float)
    if mode == "unbiased":
        S = code["S_unb"]
    elif mode == "mse_optimal":
        S = code["S_mse"]
    else:
        raise ValueError(f"unknown mode: {mode}")
    return S * (R.T @ sign_y)


# ---------------------------------------------------------------------------
# 演示
# ---------------------------------------------------------------------------
def main():
    rng = np.random.default_rng(seed=0)

    d = 1024                                # 维度
    x = rng.standard_normal(d)              # 真实向量
    x /= np.linalg.norm(x)                  # 归一化到 ||x||_2 = 1

    R = haar_orthogonal(d, rng)
    code = drive_encode(x, R)

    # --- 解码 ---
    x_hat_unb = drive_decode(code, R, mode="unbiased")
    x_hat_mse = drive_decode(code, R, mode="mse_optimal")

    # --- 误差度量 ---
    err_unb = np.linalg.norm(x_hat_unb - x) / np.linalg.norm(x)
    err_mse = np.linalg.norm(x_hat_mse - x) / np.linalg.norm(x)

    cos_unb = float(x @ x_hat_unb / (np.linalg.norm(x) * np.linalg.norm(x_hat_unb)))
    cos_mse = float(x @ x_hat_mse / (np.linalg.norm(x) * np.linalg.norm(x_hat_mse)))

    # --- 无偏性检验: 多次试验取平均 ---
    n_trials = 200
    mean_unb = np.zeros(d)
    mean_mse = np.zeros(d)
    for _ in range(n_trials):
        R_k = haar_orthogonal(d, rng)
        c_k = drive_encode(x, R_k)
        mean_unb += drive_decode(c_k, R_k, mode="unbiased")
        mean_mse += drive_decode(c_k, R_k, mode="mse_optimal")
    mean_unb /= n_trials
    mean_mse /= n_trials

    bias_unb = np.linalg.norm(mean_unb - x)
    bias_mse = np.linalg.norm(mean_mse - x)

    # --- 打印 ---
    print("=" * 64)
    print(f"DRIVE 1-bit Mean Encoder/Decoder  (d = {d})")
    print("=" * 64)
    print(f"bits stored per coordinate : {code['bits_per_coord']:.1f}")
    print(f"||x||_2                    : {np.linalg.norm(x):.6f}")
    print(f"S (MSE-optimal, biased)    : {code['S_mse']:.6f}")
    print(f"S (unbiased)               : {code['S_unb']:.6f}")
    print("-" * 64)
    print("Single-trial reconstruction")
    print(f"  unbiased   : rel-err = {err_unb:.4f}   "
          f"cos(x, x_hat) = {cos_unb:+.4f}")
    print(f"  mse_optimal: rel-err = {err_mse:.4f}   "
          f"cos(x, x_hat) = {cos_mse:+.4f}")
    print("-" * 64)
    print(f"Bias after {n_trials} trials (||mean(x_hat) - x||)")
    print(f"  unbiased   : {bias_unb:.6f}   ← 应随 trials→∞ 而趋于 0")
    print(f"  mse_optimal: {bias_mse:.6f}   ← 应当稳定在一个非零常数 (有偏)")
    print("=" * 64)


if __name__ == "__main__":
    main()
