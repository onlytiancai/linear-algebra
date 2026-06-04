"""
103-9.py
========

Lloyd–Max 与 EDEN / TurboQuant 论文表对照

论文给出的标准正态边缘分布最优码本（Vargaftik et al. ICML 2022 §5 / TurboQuant §4），
按 √d 归一化（即对 N(0, 1) 的码字）：

  b=1: {±√(2/π)}                      ≈ {±0.7979}
  b=2: {±0.453, ±1.510}               (4 levels)
  b=3: {±0.245, ±0.756, ±1.344, ±2.151}
  b=4: {±0.128, ±0.380, ±0.656, ±0.942, ±1.281, ±1.681, ±2.165, ±2.764}
  ...

本程序：
  1) 在 b=1..6 上跑 Lloyd–Max
  2) 报告收敛码本 vs 论文表
  3) 报告 MSE vs Shannon 下界 1/(4^b·d)
  4) 报告 1/4 缩放律：每加 1 bit，MSE 减少到原来的 ≈ 1/4

运行：
    /Users/huhao/.pyenv/versions/qlib/bin/python code/103-9.py
"""

import numpy as np
import sys
sys.path.insert(0, ".")
from importlib import import_module

# 直接复用 103-8 的算法，避免重复代码
mod = import_module("code.103-8") if False else None  # 占位
# 因为包名带数字不能直接 import，用 exec 拿到模块
import importlib.util
spec = importlib.util.spec_from_file_location("lm_mod", "code/103-8.py")
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)


# ============================================================
# 论文显式码本（按 √d 归一化 → 即 N(0,1) 的最优码字）
# 来自 EDEN (Vargaftik et al., ICML 2022) 附录 A
# ============================================================

PAPER_CODEBOOKS = {
    1: np.array([-np.sqrt(2.0 / np.pi),  np.sqrt(2.0 / np.pi)]),
    2: np.array([-1.510, -0.453,  0.453,  1.510]),
    3: np.array([-2.151, -1.344, -0.756, -0.245,  0.245,  0.756,  1.344,  2.151]),
    4: np.array([-2.764, -2.165, -1.681, -1.281, -0.942, -0.656, -0.380, -0.128,
                  0.128,  0.380,  0.656,  0.942,  1.281,  1.681,  2.165,  2.764]),
}


def run_all(bits_range=range(1, 7), d: int = 64, n_samples: int = 500_000):
    print("=" * 90)
    print(f"{'b':>3} {'K':>4} {'Lloyd–Max MSE':>16} {'Shannon':>14} "
          f"{'ratio':>9} {'MSE·4^b·d':>12}  {'max|Δcb|':>10}")
    print("=" * 90)

    rows = []
    for b in bits_range:
        out = lm.lloyd_max(d=d, b=b, n_samples=n_samples, max_iter=80,
                            tol=1e-10, verbose=False, rng_seed=b)
        cb = out["codebook"]
        mse = out["mse_history"][-1]
        shannon = lm.shannon_bound_1d(b, d)
        ratio = mse / shannon
        # 把码本按 √d 归一化
        cb_norm = cb / (1.0 / np.sqrt(d))

        # 与论文表对照（仅在论文有 b 时）
        max_dev = "—"
        if b in PAPER_CODEBOOKS:
            paper = np.sort(PAPER_CODEBOOKS[b])
            mine = np.sort(cb_norm)
            max_dev = float(np.max(np.abs(paper - mine)))
            max_dev = f"{max_dev:.3f}"

        rows.append((b, 2**b, mse, shannon, ratio, b, max_dev))
        print(f"{b:>3} {2**b:>4d} {mse:>16.4e} {shannon:>14.4e} "
              f"{ratio:>8.3f}x {mse * 4**b * d:>12.4f}  {max_dev:>10}")

    print("=" * 90)
    print("解释列：")
    print("  • Shannon = 1 / (4^b · d)，信息论下界")
    print("  • ratio   = Lloyd–Max / Shannon  （TurboQuant 论文 ≈ 1.45 at b=1）")
    print("  • MSE·4^b·d  应近似为常数 = ratio（验证 1/4 缩放律）")
    print("  • max|Δcb|   = 与 EDEN 附录 A 论文码本的最大偏差（按 √d 归一化）")
    print("=" * 90)

    # 验证 1/4 缩放律
    print("\n缩放律验证：MSE(b) / MSE(b+1) 应当 ≈ 4")
    for i in range(len(rows) - 1):
        b1, b2 = rows[i][0], rows[i + 1][0]
        if b2 == b1 + 1:
            r = rows[i][2] / rows[i + 1][2]
            print(f"  b={b1} → b={b2}:  MSE 缩放 = {r:.3f}x   (理论 4.000x)")
    print()


if __name__ == "__main__":
    run_all()
