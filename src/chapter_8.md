# Chapter 8. Eigenvalues and eigenvectors
第 8 章 特征值和特征向量

## 8.1 Definitions and Intuition
8.1 定义和直觉

The concepts of eigenvalues and eigenvectors reveal the most fundamental behavior of linear transformations. They identify the special directions in which a transformation acts by simple stretching or compressing, without rotation or distortion.
特征值和特征向量的概念揭示了线性变换最基本的行为。它们通过简单的拉伸或压缩（不进行旋转或变形）来识别变换所作用的特定方向。

### Definition
定义

Let $T: V \to V$ be a linear transformation on a vector space $V$. A nonzero vector $\mathbf{v} \in V$ is called an eigenvector of $T$ if
令 $T: V \to V$ 为向量空间 $V$ 上的线性变换。非零向量 $\mathbf{v} \in V$ 称为 $T$ 的特征向量，若

$$
T(\mathbf{v}) = \lambda \mathbf{v}
$$

for some scalar $\lambda \in \mathbb{R}$ (or $\mathbb{C}$). The scalar $\lambda$ is the eigenvalue corresponding to $\mathbf{v}$.
某个标量 $\lambda \in \mathbb{R}$ （或 $\mathbb{C}$ ）。标量 $\lambda$ 是对应于 $\mathbf{v}$ 的特征值。

Equivalently, if $A$ is the matrix of $T$, then eigenvalues and eigenvectors satisfy
等价地，如果 $A$ 是 $T$ 的矩阵，则特征值和特征向量满足

$$
A\mathbf{v} = \lambda \mathbf{v}.
$$

### Basic Examples
基本示例

Example 8.1.1. Let
例 8.1.1. 设

$$
A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}.
$$

Then
然后

$$
A(1,0)^T = 2(1,0)^T, \quad A(0,1)^T = 3(0,1)^T.
$$

So $(1,0)$ is an eigenvector with eigenvalue $2$, and $(0,1) is an eigenvector with eigenvalue \\3$.
因此 $(1,0)$ 是特征值为 $2 的特征向量， $, and $ (0,1) 是特征值为 \\ 3$ 的特征向量 。

Example 8.1.2. Rotation matrix in $\mathbb{R}^2$:
例 8.1.2。 $\mathbb{R}^2$ 中的旋转矩阵：

$$
R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}.
$$

If $\theta \neq 0, \pi$, $R_\theta$ has no real eigenvalues: every vector is rotated, not scaled. Over $\mathbb{C}$, however, it has eigenvalues $e^{i\theta}, e^{-i\theta}$.
如果 $\theta \neq 0, \pi$ ，𝑅 𝜃 R θ ​ 没有实数特征值：每个向量都经过旋转，而不是缩放。然而，在 $\mathbb{C}$ 上，它的特征值为 $e^{i\theta}, e^{-i\theta}$ 。

### Algebraic Formulation
代数公式

Eigenvalues arise from solving the characteristic equation:
特征值由求解特征方程得出：

$$
\det(A - \lambda I) = 0.
$$

This polynomial in $\lambda$ is the characteristic polynomial. Its roots are the eigenvalues.
$\lambda$ 中的这个多项式是特征多项式。它的根就是特征值。

### Geometric Intuition
几何直觉

*   Eigenvectors are directions that remain unchanged in orientation under a transformation; only their length is scaled.
    特征向量是在变换下方向保持不变的方向；只有它们的长度被缩放。
*   Eigenvalues tell us the scaling factor along those directions.
    特征值告诉我们沿这些方向的缩放因子。
*   If a matrix has many independent eigenvectors, it can often be simplified (diagonalized) by changing basis.
    如果矩阵具有许多独立的特征向量，则通常可以通过改变基来简化（对角化）。

### Applications in Geometry and Science
几何和科学中的应用

*   Stretching along principal axes of an ellipse (quadratic forms).
    沿椭圆的主轴拉伸（二次型）。
*   Stable directions of dynamical systems.
    动力系统的稳定方向。
*   Principal components in statistics and machine learning.
    统计学和机器学习中的主要成分。
*   Quantum mechanics, where observables correspond to operators with eigenvalues.
    量子力学，其中可观测量对应于具有特征值的算子。

### Why this matters
为什么这很重要

Eigenvalues and eigenvectors are a bridge between algebra and geometry. They provide a lens for understanding linear transformations in their simplest form. Nearly every application of linear algebra-differential equations, statistics, physics, computer science-relies on eigen-analysis.
特征值和特征向量是代数和几何之间的桥梁。它们为理解最简形式的线性变换提供了一个视角。几乎所有线性代数的应用——微分方程、统计学、物理学、计算机科学——都依赖于特征分析。

### Exercises 8.1
练习 8.1

1.  Find the eigenvalues and eigenvectors of $\begin{bmatrix} 4 & 0 \\ 0 & -1 \end{bmatrix}$.
    找到特征值和特征向量 $\begin{bmatrix} 4 & 0 \\ 0 & -1 \end{bmatrix}$ .
2.  Show that every scalar multiple of an eigenvector is again an eigenvector for the same eigenvalue.
    证明特征向量的每个标量倍数又是同一特征值的特征向量。
3.  Verify that the rotation matrix $R_\theta$ has no real eigenvalues unless $\theta = 0$ or $\pi$.
    验证旋转矩阵𝑅 𝜃 R θ ​ 除非 $\theta = 0$ 或 $\pi$ ，否则没有实数特征值。
4.  Compute the characteristic polynomial of $\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$.
    计算特征多项式 $\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$ .
5.  Explain geometrically what eigenvectors and eigenvalues represent for the shear matrix $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$.
    从几何角度解释特征向量和特征值对于剪切矩阵的意义 $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ .

## 8.2 Diagonalization
8.2 对角化

A central goal in linear algebra is to simplify the action of a matrix by choosing a good basis. Diagonalization is the process of rewriting a matrix so that it acts by simple scaling along independent directions. This makes computations such as powers, exponentials, and solving differential equations far easier.
线性代数的核心目标是通过选择合适的基来简化矩阵的运算。对角化是将矩阵重写，使其能够沿独立方向进行简单的缩放。这使得幂、指数和微分方程等计算变得更加容易。

### Definition
定义

A square matrix $A \in \mathbb{R}^{n \times n}$ is diagonalizable if there exists an invertible matrix $P$ such that
如果存在可逆矩阵 $P$ 并且满足以下条件，则方阵 $A \in \mathbb{R}^{n \times n}$ 可对角化

$$
P^{-1} A P = D,
$$

where $D$ is a diagonal matrix.
其中 $D$ 是一个对角矩阵。

The diagonal entries of $D$ are eigenvalues of $A$, and the columns of $P$ are the corresponding eigenvectors.
$D$ 的对角线项是 $A$ 的特征值， $P$ 的列是相应的特征向量。

### When is a Matrix Diagonalizable?
矩阵何时可对角化？

*   A matrix is diagonalizable if it has $n$ linearly independent eigenvectors.
    如果矩阵具有 $n$ 个线性无关的特征向量，则该矩阵可对角化。
*   Equivalently, the sum of the dimensions of its eigenspaces equals $n$.
    等效地，其特征空间的维数之和等于 $n$ 。
*   Symmetric matrices (over $\mathbb{R}$) are always diagonalizable, with an orthonormal basis of eigenvectors.
    对称矩阵（在 $\mathbb{R}$ 上）始终可对角化，且具有特征向量的正交基。

### Example 8.2.1
例 8.2.1

Let
让

$$
A = \begin{bmatrix} 4 & 1 \\ 0 & 2 \end{bmatrix}.
$$

1.  Characteristic polynomial:
    特征多项式：

$$
\det(A - \lambda I) = (4-\lambda)(2-\lambda).
$$

So eigenvalues are $\lambda_1 = 4$, $\lambda_2 = 2$.
所以特征值是 $\lambda_1 = 4$ ， $\lambda_2 = 2$ 。

2.  Eigenvectors:
    特征向量：

*   For $\lambda = 4$, solve $(A-4I)\mathbf{v}=0$: $\begin{bmatrix} 0 & 1 \\ 0 & -2 \end{bmatrix}\mathbf{v} = 0$, giving $\mathbf{v}_1 = (1,0)$.
    对于 $\lambda = 4$ ，求解 $(A-4I)\mathbf{v}=0$ ： $\begin{bmatrix} 0 & 1 \\ 0 & -2 \end{bmatrix}\mathbf{v} = 0$ ，得到 $\mathbf{v}_1 = (1,0)$ 。
*   For $\lambda = 2$: $(A-2I)\mathbf{v}=0$, giving $\mathbf{v}_2 = (1,-2)$.
    对于 $\lambda = 2$ ： $(A-2I)\mathbf{v}=0$ ，给出 $\mathbf{v}_2 = (1,-2)$ 。

3.  Construct $P = \begin{bmatrix} 1 & 1 \\ 0 & -2 \end{bmatrix}$. Then
    构造 $P = \begin{bmatrix} 1 & 1 \\ 0 & -2 \end{bmatrix}$ 。然后

$$
P^{-1} A P = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}.
$$

Thus, $A$ is diagonalizable.
因此， $A$ 是可对角化的。

### Why Diagonalize?
为什么要对角化？

*   Computing powers: If $A = P D P^{-1}$, then
    计算能力： 如果 $A = P D P^{-1}$ ，则
    
    $$
    A^k = P D^k P^{-1}.
    $$
    
    Since $D$ is diagonal, $D^k$ is easy to compute.
    由于 $D$ 是对角线，因此 $D^k$ 很容易计算。
    
*   Matrix exponentials: $e^A = P e^D P^{-1}$, useful in solving differential equations.
    矩阵指数： $e^A = P e^D P^{-1}$ ，有助于解决微分方程。
    
*   Understanding geometry: Diagonalization reveals the directions along which a transformation stretches or compresses space independently.
    理解几何：对角化揭示了变换独立拉伸或压缩空间的方向。
    

### Non-Diagonalizable Example
不可对角化的例子

Not all matrices can be diagonalized.
并非所有矩阵都可以对角化。

$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}
$$

has only one eigenvalue $\lambda = 1$, with eigenspace dimension 1. Since $n=2$ but we only have 1 independent eigenvector, $A$ is not diagonalizable.
只有一个特征值 $\lambda = 1$ ，特征空间维数为 1。由于 $n=2$ 但我们只有 1 个独立特征向量，因此 $A$ 不可对角化。

### Geometric Interpretation
几何解释

Diagonalization means we have found a basis of eigenvectors. In this basis, the matrix acts by simple scaling along each coordinate axis. It transforms complicated motion into independent 1D motions.
对角化意味着我们找到了特征向量的基。在此基上，矩阵通过沿每个坐标轴进行简单的缩放来发挥作用。它将复杂的运动转化为独立的一维运动。

### Why this matters
为什么这很重要

Diagonalization is a cornerstone of linear algebra. It simplifies computation, reveals structure, and is the starting point for the spectral theorem, Jordan form, and many applications in physics, engineering, and data science.
对角化是线性代数的基石。它简化了计算，揭示了结构，并且是谱定理、若尔当形式以及物理、工程和数据科学中许多应用的起点。

### Exercises 8.2
练习 8.2

1.  Diagonalize
    对角化
    
    $$
    A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}.
    $$
    
2.  Determine whether
    确定是否
    
    $$
    A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}
    $$
    
    is diagonalizable. Why or why not?
    是可对角化的。为什么或为什么不？
    
3.  Find $A^5$ for
    查找 $A^5$
    
    $$
    A = \begin{bmatrix} 4 & 1 \\ 0 & 2 \end{bmatrix}
    $$
    
    using diagonalization.
    使用对角化。
    
4.  Show that any $n \times n$ matrix with $n$ distinct eigenvalues is diagonalizable.
    证明任何具有 $n$ 个不同特征值的 $n \times n$ 矩阵都是可对角化的。
    
5.  Explain why real symmetric matrices are always diagonalizable.
    解释为什么实对称矩阵总是可对角化的。
    

## 8.3 Characteristic Polynomials
8.3 特征多项式

The key to finding eigenvalues is the characteristic polynomial of a matrix. This polynomial encodes the values of $\lambda$ for which the matrix $A - \lambda I$ fails to be invertible.
寻找特征值的关键是矩阵的特征多项式。该多项式对值进行编码 矩阵 $A - \lambda I$ 不可逆，其中 $\lambda$ 。

### Definition
定义

For an $n \times n$ matrix $A$, the characteristic polynomial is
对于 $n \times n$ 矩阵 $A$ ，特征多项式为

$$
p_A(\lambda) = \det(A - \lambda I).
$$

The roots of $p_A(\lambda)$ are the eigenvalues of $A$.
$p_A(\lambda)$ 的根是 $A$ 的特征值。

### Examples
示例

Example 8.3.1. Let
例 8.3.1. 设

$$
A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}.
$$

Then
然后

$$
p_A(\lambda) = \det\!\begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix}= (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3.
$$

Thus eigenvalues are $\lambda = 1, 3$.
因此特征值为 $\lambda = 1, 3$ 。

Example 8.3.2. For
例 8.3.2. 对于

$$
A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
$$

(rotation by 90°),
（旋转 90°），

$$
p_A(\lambda) = \det\!\begin{bmatrix} -\lambda & -1 \\ 1 & -\lambda \end{bmatrix}= \lambda^2 + 1.
$$

Eigenvalues are $\lambda = \pm i$. No real eigenvalues exist, consistent with pure rotation.
特征值为 $\lambda = \pm i$ 。不存在实数特征值，与纯旋转一致。

Example 8.3.3. For a triangular matrix
例 8.3.3. 对于三角矩阵

$$
A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 3 & 5 \\ 0 & 0 & 4 \end{bmatrix},
$$

the determinant is simply the product of diagonal entries minus $\lambda$:
行列式仅仅是对角线项的乘积减去 $\lambda$ ：

$$
p_A(\lambda) = (2-\lambda)(3-\lambda)(4-\lambda).
$$

So eigenvalues are 2,3,4.
所以特征值为 2,3,4 。

### Properties
特性

1.  The characteristic polynomial of an $n \times n$ matrix has degree $n$.
    $n \times n$ 矩阵的特征多项式的度为 $n$ 。
    
2.  The sum of the eigenvalues (counted with multiplicity) equals the trace of $A$:
    特征值（按重数计算）的和等于 $A$ 的迹：
    
    $$
    \text{tr}(A) = \lambda_1 + \cdots + \lambda_n.
    $$
    
3.  The product of the eigenvalues equals the determinant of $A$:
    特征值的乘积等于 $A$ 的行列式：
    
    $$
    \det(A) = \lambda_1 \cdots \lambda_n.
    $$
    
4.  Similar matrices have the same characteristic polynomial, hence the same eigenvalues.
    相似的矩阵具有相同的特征多项式，因此具有相同的特征值。
    

### Geometric Interpretation
几何解释

The characteristic polynomial captures when $A - \lambda I$ collapses space: its determinant is zero precisely when the transformation $A - \lambda I$ is singular. Thus, eigenvalues mark the critical scalings where the matrix loses invertibility.
特征多项式捕捉了 $A - \lambda I$ 何时使空间坍缩：当变换 $A - \lambda I$ 为奇异时，其行列式恰好为零。因此，特征值标记了矩阵失去可逆性的临界尺度。

### Why this matters
为什么这很重要

Characteristic polynomials provide the computational tool to extract eigenvalues. They connect matrix invariants (trace and determinant) with geometry, and form the foundation for diagonalization, spectral theorems, and stability analysis in dynamical systems.
特征多项式提供了提取特征值的计算工具。它们将矩阵不变量（迹和行列式）与几何联系起来，并构成了动力系统中对角化、谱定理和稳定性分析的基础。

### Exercises 8.3
练习 8.3

1.  Compute the characteristic polynomial of
    计算特征多项式
    
    $$
    A = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}.
    $$
    
2.  Verify that the sum of the eigenvalues of $\begin{bmatrix} 5 & 0 \\ 0 & -2 \end{bmatrix}$ equals its trace, and their product equals its determinant.
    验证特征值之和 $\begin{bmatrix} 5 & 0 \\ 0 & -2 \end{bmatrix}$ 等于它的迹，它们的乘积等于它的行列式。
    
3.  Show that for any triangular matrix, the eigenvalues are just the diagonal entries.
    证明对于任何三角矩阵，特征值只是对角线项。
    
4.  Prove that if $A$ and $B$ are similar matrices, then $p_A(\lambda) = p_B(\lambda)$.
    证明如果 $A$ 和 $B$ 是相似矩阵，则 $p_A(\lambda) = p_B(\lambda)$ 。
    
5.  Compute the characteristic polynomial of $\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$.
    计算特征多项式 \[ 1 1 0 0 1 1 0 0 1 \] ​ 1 0 0 ​ 1 1 0 ​ 0 1 1 ​ ​ .
    

## 8.4 Applications (Differential Equations, Markov Chains)
8.4 应用（微分方程、马尔可夫链）

Eigenvalues and eigenvectors are not only central to the theory of linear algebra-they are indispensable tools across mathematics and applied science. Two classic applications are solving systems of differential equations and analyzing Markov chains.
特征值和特征向量不仅是线性代数理论的核心，也是数学和应用科学领域中不可或缺的工具。两个经典的应用是求解微分方程组和分析马尔可夫链。

### Linear Differential Equations
线性微分方程

Consider the system
考虑系统

$$
\frac{d\mathbf{x}}{dt} = A \mathbf{x},
$$

where $A$ is an $n \times n$ matrix and $\mathbf{x}(t)$ is a vector-valued function.
其中 $A$ 是 $n \times n$ 矩阵， $\mathbf{x}(t)$ 是矢量值函数。

If $\mathbf{v}$ is an eigenvector of $A$ with eigenvalue $\lambda$, then the function
如果 $\mathbf{v}$ 是 $A$ 的特征向量，其特征值为 $\lambda$ ，则函数

$$
\mathbf{x}(t) = e^{\lambda t}\mathbf{v}
$$

is a solution.
是一个解决方案。

*   Eigenvalues determine the growth or decay rate:
    特征值决定增长率或衰减率：
    
    *   If $\lambda < 0$, solutions decay (stable).
        如果 $\lambda < 0$ ，则解决方案衰减（稳定）。
    *   If $\lambda > 0$, solutions grow (unstable).
        如果 $\lambda > 0$ ，则解决方案会增长（不稳定）。
    *   If $\lambda$ is complex, oscillations occur.
        如果 $\lambda$ 是复数，则会发生振荡。

By combining eigenvector solutions, we can solve general initial conditions.
通过结合特征向量解，我们可以解决一般的初始条件。

Example 8.4.1. Let
例 8.4.1. 设

$$
A = \begin{bmatrix}2 & 0 \\0 & -1 \end{bmatrix}.
$$

Then eigenvalues are $2, -1$with eigenvectors$(1,0)$, $(0,1)$. Solutions are
则特征值为 $2, -1 $with eigenvectors$ (1,0) $, $ (0,1)$。解为

$$
\mathbf{x}(t) = c_1 e^{2t}(1,0) + c_2 e^{-t}(0,1).
$$

Thus one component grows exponentially, the other decays.
因此，一个部分呈指数增长，另一个部分则衰减。

### Markov Chains
马尔可夫链

A Markov chain is described by a stochastic matrix $P$, where each column sums to 1 and entries are nonnegative. If $\mathbf{x}_k$ represents the probability distribution after $k$ steps, then
马尔可夫链可以用随机矩阵 $P$ 来描述，其中每列和为 1，且元素为非负值。如果 𝑥 𝑘 x k ​ 表示 $k$ 步后的概率分布，则

$$
\mathbf{x}_{k+1} = P \mathbf{x}_k.
$$

Iterating gives
迭代得到

$$
\mathbf{x}_k = P^k \mathbf{x}_0.
$$

Understanding long-term behavior reduces to analyzing powers of $P$.
理解长期行为可以归结为分析 $P$ 的力量。

*   The eigenvalue $\lambda = 1$ always exists. Its eigenvector gives the steady-state distribution.
    特征值 $\lambda = 1$ 始终存在。其特征向量给出了稳态分布。
*   All other eigenvalues satisfy $|\lambda| \leq 1$. Their influence decays as $k \to \infty$.
    所有其他特征值都满足 $|\lambda| \leq 1$ 。它们的影响衰减为 $k \to \infty$ 。

Example 8.4.2. Consider
例 8.4.2. 考虑

$$
P = \begin{bmatrix}0.9 & 0.5 \\0.1 & 0.5 \end{bmatrix}.
$$

Eigenvalues are $\lambda_1 = 1$, $\lambda_2 = 0.4$. The eigenvector for $\lambda = 1$ is proportional to $(5,1)$. Normalizing gives the steady state
特征值为 $\lambda_1 = 1$ , $\lambda_2 = 0.4$ 。 $\lambda = 1$ 的特征向量与 $(5,1)$ 成正比。归一化后可得到稳态

$$
\pi = \left(\tfrac{5}{6}, \tfrac{1}{6}\right).
$$

Thus, regardless of the starting distribution, the chain converges to $\pi$.
因此，无论起始分布如何，链都会收敛到 $\pi$ 。

### Geometric Interpretation
几何解释

*   In differential equations, eigenvalues determine the time evolution: exponential growth, decay, or oscillation.
    在微分方程中，特征值决定时间的演变：指数增长、衰减或振荡。
*   In Markov chains, eigenvalues determine the long-term equilibrium of stochastic processes.
    在马尔可夫链中，特征值决定了随机过程的长期均衡。

### Why this matters
为什么这很重要

Eigenvalue methods turn complex iterative or dynamical systems into tractable problems. In physics, engineering, and finance, they describe stability and resonance. In computer science and statistics, they power algorithms from Google’s PageRank to modern machine learning.
特征值方法将复杂的迭代或动态系统转化为易于处理的问题。在物理学、工程学和金融学领域，它们描述稳定性和共振。在计算机科学和统计学领域，它们为从谷歌的 PageRank 到现代机器学习等各种算法提供支持。

### Exercises 8.4
练习 8.4

1.  Solve $\tfrac{d}{dt}\mathbf{x} = \begin{bmatrix} 3 & 0 \\ 0 & -2 \end{bmatrix}\mathbf{x}$.
    解出 $\tfrac{d}{dt}\mathbf{x} = \begin{bmatrix} 3 & 0 \\ 0 & -2 \end{bmatrix}\mathbf{x}$ 。
    
2.  Show that if $A$ has a complex eigenvalue $\alpha \pm i\beta$, then solutions of $\tfrac{d}{dt}\mathbf{x} = A\mathbf{x}$ involve oscillations of frequency $\beta$.
    证明如果 $A$ 具有复特征值 $\alpha \pm i\beta$ ，则 $\tfrac{d}{dt}\mathbf{x} = A\mathbf{x}$ 的解涉及频率 $\beta$ 的振荡。
    
3.  Find the steady-state distribution of
    找到稳态分布
    
    $$
    P = \begin{bmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{bmatrix}.
    $$
    
4.  Prove that for any stochastic matrix $P$, 1 is always an eigenvalue.
    证明对于任何随机矩阵 $P$ ， 1 始终是特征值。
    
5.  Explain why all eigenvalues of a stochastic matrix satisfy $|\lambda| \leq 1$.
    解释为什么随机矩阵的所有特征值都满足 $|\lambda| \leq 1$ 。
    