# Chapter 9. Quadratic Forms and Spectral Theorems
第九章二次型和谱定理

## 9.1 Quadratic Forms
9.1 二次型

A quadratic form is a polynomial of degree two in several variables, expressed neatly using matrices. Quadratic forms appear throughout mathematics: in optimization, geometry of conic sections, statistics (variance), and physics (energy functions).
二次型是多元二次多项式，可以用矩阵简洁地表示。二次型在数学中随处可见：优化、圆锥曲线几何、统计学（方差）和物理学（能量函数）。

### Definition
定义

Let $A$ be an $n \times n$ symmetric matrix and $\mathbf{x} \in \mathbb{R}^n$. The quadratic form associated with $A$ is
令 $A$ 为 $n \times n$ 对称矩阵， $\mathbf{x} \in \mathbb{R}^n$ 。与 $A$ 相关的二次式为

$$
Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}.
$$

Expanded,
扩展，

$$
Q(\mathbf{x}) = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j.
$$

Because $A$ is symmetric ($a_{ij} = a_{ji}$), the cross-terms can be grouped naturally.
因为 $A$ 是对称的 (𝑎 𝑖 𝑗 = 𝑎 𝑗 𝑖 a 伊奇 ​ =a 姬 ​ )，交叉项可以自然分组。

### Examples
示例

Example 9.1.1. For
例 9.1.1. 对于

$$
A = \begin{bmatrix}2 & 1 \\1 & 3 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix}x \\y \end{bmatrix},
$$

 

$$
Q(x,y) = \begin{bmatrix} x & y \end{bmatrix}\begin{bmatrix}2 & 1 \\1 & 3 \end{bmatrix}\begin{bmatrix}x \\y \end{bmatrix}= 2x^2 + 2xy + 3y^2.
$$

Example 9.1.2. The quadratic form
例 9.1.2. 二次型

$$
Q(x,y) = x^2 + y^2
$$

corresponds to the matrix $A = I_2$. It measures squared Euclidean distance from the origin.
对应于矩阵𝐴 = 𝐼 2 A=I 2 ​ . 它测量距离原点的平方欧几里得距离。

Example 9.1.3. The conic section equation
例 9.1.3 圆锥曲线方程

$$
4x^2 + 2xy + 5y^2 = 1
$$

is described by the quadratic form $\mathbf{x}^T A \mathbf{x} = 1$ with
由二次型 $\mathbf{x}^T A \mathbf{x} = 1$ 描述

$$
A = \begin{bmatrix}4 & 1 \\1 & 5\end{bmatrix}.
$$

### Diagonalization of Quadratic Forms
二次型的对角化

By choosing a new basis consisting of eigenvectors of $A$, we can rewrite the quadratic form without cross terms. If $A = PDP^{-1}$ with $D$ diagonal, then
通过选择由 $A$ 的特征向量组成的新基，我们可以重写没有交叉项的二次型。如果 $A = PDP^{-1}$ 以 $D$ 为对角线，则

$$
Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} = (P^{-1}\mathbf{x})^T D (P^{-1}\mathbf{x}).
$$

Thus quadratic forms can always be expressed as a sum of weighted squares:
因此二次型总是可以表示为加权平方和：

$$
Q(\mathbf{y}) = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2,
$$

where $\lambda_i$ are the eigenvalues of $A$.
其中𝜆 𝑖 λ i ​ 是 $A$ 的特征值。

### Geometric Interpretation
几何解释

Quadratic forms describe geometric shapes:
二次型描述几何形状：

*   In 2D: ellipses, parabolas, hyperbolas.
    二维：椭圆、抛物线、双曲线。
*   In 3D: ellipsoids, paraboloids, hyperboloids.
    在 3D 中：椭圆体、抛物面、双曲面。
*   In higher dimensions: generalizations of ellipsoids.
    在更高维度中：椭圆体的概括。

Diagonalization aligns the coordinate axes with the principal axes of the shape.
对角化将坐标轴与形状的主轴对齐。

### Why this matters
为什么这很重要

Quadratic forms unify geometry and algebra. They are central in optimization (minimizing energy functions), statistics ( covariance matrices and variance), mechanics (kinetic energy), and numerical analysis. Understanding quadratic forms leads directly to the spectral theorem.
二次型统一了几何和代数。它们在优化（最小化能量函数）、统计学（协方差矩阵和方差）、力学（动能）和数值分析中都至关重要。理解二次型可以直接引出谱定理。

### Exercises 9.1
练习 9.1

1.  Write the quadratic form $Q(x,y) = 3x^2 + 4xy + y^2$ as $\mathbf{x}^T A \mathbf{x}$ for some symmetric matrix $A$.
    对于某些对称矩阵 $A$ ，将二次型 $Q(x,y) = 3x^2 + 4xy + y^2$ 写为 $\mathbf{x}^T A \mathbf{x}$ 。
2.  For $A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$, compute $Q(x,y)$ explicitly.
    对于 $A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$ ，明确计算 $Q(x,y)$ 。
3.  Diagonalize the quadratic form $Q(x,y) = 2x^2 + 2xy + 3y^2$.
    将二次型 $Q(x,y) = 2x^2 + 2xy + 3y^2$ 对角化。
4.  Identify the conic section given by $Q(x,y) = x^2 - y^2$.
    确定由 $Q(x,y) = x^2 - y^2$ 给出的圆锥截面。
5.  Show that if $A$ is symmetric, quadratic forms defined by $A$ and $A^T$ are identical.
    证明如果 $A$ 是对称的，则由 $A$ 和 $A^T$ 定义的二次型是相同的。

## 9.2 Positive Definite Matrices
9.2 正定矩阵

Quadratic forms are especially important when their associated matrices are positive definite, since these guarantee positivity of energy, distance, or variance. Positive definiteness is a cornerstone in optimization, numerical analysis, and statistics.
当二次型的相关矩阵为正定矩阵时，它们尤为重要，因为它们可以保证能量、距离或方差的正性。正定性是优化、数值分析和统计学的基石。

### Definition
定义

A symmetric matrix $A \in \mathbb{R}^{n \times n}$ is called:
对称矩阵 $A \in \mathbb{R}^{n \times n}$ 称为：

*   Positive definite if
    正定如果
    
    $$
    \mathbf{x}^T A \mathbf{x} > 0 \quad \text{for all nonzero } \mathbf{x} \in \mathbb{R}^n.
    $$
    
*   Positive semidefinite if
    正半定的，如果
    
    $$
    \mathbf{x}^T A \mathbf{x} \geq 0 \quad \text{for all } \mathbf{x}.
    $$
    

Similarly, negative definite (always < 0) and indefinite (can be both < 0 and > 0) matrices are defined.
类似地，定义了负定（始终 < 0）和不定（可以同时 < 0 和 > 0）矩阵。

### Examples
示例

Example 9.2.1.
例 9.2.1。

$$
A = \begin{bmatrix}2 & 0 \\0 & 3 \end{bmatrix}
$$

is positive definite, since
是正定的，因为

$$
Q(x,y) = 2x^2 + 3y^2 > 0
$$

for all $(x,y) \neq (0,0)$.
对于所有 $(x,y) \neq (0,0)$ 。

Example 9.2.2.
例 9.2.2。

$$
A = \begin{bmatrix}1 & 2 \\2 & 1 \end{bmatrix}
$$

has quadratic form
具有二次形式

$$
Q(x,y) = x^2 + 4xy + y^2.
$$

This matrix is not positive definite, since $Q(1,-1) = -2 < 0$.
该矩阵不是正定的，因为 $Q(1,-1) = -2 < 0$ 。

### Characterizations
特征

For a symmetric matrix $A$:
对于对称矩阵 $A$ ：

1.  Eigenvalue test: $A$ is positive definite if and only if all eigenvalues of $A$ are positive.
    特征值检验：当且仅当 $A$ 的所有特征值都为正时， $A$ 才是正定的。
    
2.  Principal minors test (Sylvester’s criterion): $A$ is positive definite if and only if all leading principal minors ( determinants of top-left $k \times k$ submatrices) are positive.
    主子式检验（西尔维斯特标准）：当且仅当所有首项主子式（左上角 $k \times k$ 子矩阵的行列式）均为正时， $A$ 才是正定的。
    
3.  Cholesky factorization: $A$ is positive definite if and only if it can be written as
    Cholesky 分解： $A$ 为正定当且仅当它可以写成
    
    $$
    A = R^T R,
    $$
    
    where $R$ is an upper triangular matrix with positive diagonal entries.
    其中 $R$ 是具有正对角线项的上三角矩阵。
    

### Geometric Interpretation
几何解释

*   Positive definite matrices correspond to quadratic forms that define ellipsoids centered at the origin.
    正定矩阵对应于定义以原点为中心的椭圆体的二次型。
*   Positive semidefinite matrices define flattened ellipsoids (possibly degenerate).
    正半定矩阵定义扁平的椭球体（可能是退化的）。
*   Indefinite matrices define hyperbolas or saddle-shaped surfaces.
    不定矩阵定义双曲线或马鞍形曲面。

### Applications
应用

*   Optimization: Hessians of convex functions are positive semidefinite; strict convexity corresponds to positive definite Hessians.
    优化：凸函数的 Hessian 矩阵是正半定的；严格凸性对应于正定的 Hessian 矩阵。
*   Statistics: Covariance matrices are positive semidefinite.
    统计：协方差矩阵是正半定的。
*   Numerical methods: Cholesky decomposition is widely used to solve systems with positive definite matrices efficiently.
    数值方法：Cholesky 分解被广泛用于有效地解决具有正定矩阵的系统。

### Why this matters
为什么这很重要

Positive definiteness provides stability and guarantees in mathematics and computation. It ensures energy functions are bounded below, optimization problems have unique solutions, and statistical models are meaningful.
正定性在数学和计算中提供了稳定性和保证。它确保能量函数有界，优化问题有唯一解，统计模型有意义。

### Exercises 9.2
练习 9.2

1.  Use Sylvester’s criterion to check whether
    使用 Sylvester 标准检查
    
    $$
    A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
    $$
    
    is positive definite.
    是正定的。
    
2.  Determine whether
    确定是否
    
    $$
    A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
    $$
    
    is positive definite, semidefinite, or indefinite.
    是正定的、半定的或不定的。
    
3.  Find the eigenvalues of
    找到特征值
    
    $$
    A = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix},
    $$
    
    and use them to classify definiteness.
    并用它们来对确定性进行分类。
    
4.  Prove that all diagonal matrices with positive entries are positive definite.
    证明所有具有正项的对角矩阵都是正定的。
    
5.  Show that if $A$ is positive definite, then so is $P^T A P$ for any invertible matrix $P$.
    证明如果 $A$ 为正定矩阵，则对于任何可逆矩阵 $P$ ， $P^T A P$ 也为正定矩阵。
    

## 9.3 Spectral Theorem
9.3 谱定理

The spectral theorem is one of the most powerful results in linear algebra. It states that symmetric matrices can always be diagonalized by an orthogonal basis of eigenvectors. This links algebra (eigenvalues), geometry (orthogonal directions), and applications (stability, optimization, statistics).
谱定理是线性代数中最有力的结论之一。它指出对称矩阵总是可以通过特征向量的正交基对角化。这连接了代数（特征值）、几何（正交方向）和应用（稳定性、优化、统计）。

### Statement of the Spectral Theorem
谱定理表述

If $A \in \mathbb{R}^{n \times n}$ is symmetric ($A^T = A$), then:
如果 $A \in \mathbb{R}^{n \times n}$ 是对称的（ $A^T = A$ ），则：

1.  All eigenvalues of $A$ are real.
    $A$ 的所有特征值都是实数。
    
2.  There exists an orthonormal basis of $\mathbb{R}^n$ consisting of eigenvectors of $A$.
    存在由 $A$ 的特征向量组成的 $\mathbb{R}^n$ 正交基。
    
3.  Thus, $A$ can be written as
    因此， $A$ 可以写成
    
    $$
    A = Q \Lambda Q^T,
    $$
    
    where $Q$ is an orthogonal matrix ($Q^T Q = I$) and $\Lambda$ is diagonal with eigenvalues of $A$ on the diagonal.
    其中 $Q$ 是正交矩阵 ( $Q^T Q = I$ )， $\Lambda$ 是对角矩阵，其特征值 $A$ 位于对角线上。
    

### Consequences
结果

*   Symmetric matrices are always diagonalizable, and the diagonalization is numerically stable.
    对称矩阵总是可对角化的，并且对角化在数值上是稳定的。
*   Quadratic forms $\mathbf{x}^T A \mathbf{x}$ can be expressed in terms of eigenvalues and eigenvectors, showing ellipsoids aligned with eigen-directions.
    二次型 $\mathbf{x}^T A \mathbf{x}$ 可以用特征值和特征向量来表示，显示与特征方向对齐的椭圆体。
*   Positive definiteness can be checked by confirming that all eigenvalues are positive.
    可以通过确认所有特征值都为正来检查正定性。

### Example 9.3.1
例 9.3.1

Let
让

$$
A = \begin{bmatrix}2 & 1 \\1 & 2 \end{bmatrix}.
$$

1.  Characteristic polynomial:
    特征多项式：

$$
p(\lambda) = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3.
$$

Eigenvalues: $\lambda_1 = 1, \ \lambda_2 = 3$.
特征值： $\lambda_1 = 1, \ \lambda_2 = 3$ 。

2.  Eigenvectors:
    特征向量：

*   For $\lambda=1$: solve $(A-I)\mathbf{v} = 0$, giving $(1,-1)$.
    对于 $\lambda=1$ ：求解 $(A-I)\mathbf{v} = 0$ ，得到 $(1,-1)$ 。
*   For $\lambda=3$: solve $(A-3I)\mathbf{v} = 0$, giving $(1,1)$.
    对于 $\lambda=3$ ：求解 $(A-3I)\mathbf{v} = 0$ ，得到 $(1,1)$ 。

3.  Normalize eigenvectors:
    归一化特征向量：

$$
\mathbf{u}_1 = \tfrac{1}{\sqrt{2}}(1,-1), \quad \mathbf{u}_2 = \tfrac{1}{\sqrt{2}}(1,1).
$$

4.  Then
    然后

$$
Q =\begin{bmatrix}\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} \\[6pt] -\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}}\end{bmatrix}, \quad\Lambda =\begin{bmatrix}1 & 0 \\0 & 3\end{bmatrix}.
$$

So
所以

$$
A = Q \Lambda Q^T.
$$

### Geometric Interpretation
几何解释

The spectral theorem says every symmetric matrix acts like independent scaling along orthogonal directions. In geometry, this corresponds to stretching space along perpendicular axes.
谱定理指出，每个对称矩阵都像沿正交方向的独立缩放一样。在几何学中，这相当于沿垂直轴拉伸空间。

*   Ellipses, ellipsoids, and quadratic surfaces can be fully understood via eigenvalues and eigenvectors.
    通过特征值和特征向量可以充分理解椭圆、椭圆体和二次曲面。
*   Orthogonality ensures directions remain perpendicular after transformation.
    正交性确保方向在变换后保持垂直。

### Applications
应用

*   Optimization: The spectral theorem underlies classification of critical points via eigenvalues of the Hessian.
    优化：谱定理是通过 Hessian 的特征值对临界点进行分类的基础。
*   PCA (Principal Component Analysis): Data covariance matrices are symmetric, and PCA finds orthogonal directions of maximum variance.
    PCA（主成分分析）：数据协方差矩阵是对称的，PCA 找到最大方差的正交方向。
*   Differential equations & physics: Symmetric operators correspond to measurable quantities with real eigenvalues ( stability, energy).
    微分方程和物理学：对称算子对应于具有实特征值（稳定性、能量）的可测量量。

### Why this matters
为什么这很重要

The spectral theorem guarantees that symmetric matrices are as simple as possible: they can always be analyzed in terms of real, orthogonal eigenvectors. This provides both deep theoretical insight and powerful computational tools.
谱定理保证对称矩阵尽可能简单：它们总是可以用实数正交特征向量来分析。这既提供了深刻的理论见解，也提供了强大的计算工具。

### Exercises 9.3
练习 9.3

1.  Diagonalize
    对角化
    
    $$
    A = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}
    $$
    
    using the spectral theorem.
    使用谱定理。
    
2.  Prove that all eigenvalues of a real symmetric matrix are real.
    证明实对称矩阵的所有特征值都是实数。
    
3.  Show that eigenvectors corresponding to distinct eigenvalues of a symmetric matrix are orthogonal.
    证明对称矩阵的不同特征值对应的特征向量是正交的。
    
4.  Explain geometrically how the spectral theorem describes ellipsoids defined by quadratic forms.
    从几何角度解释谱定理如何描述由二次型定义的椭球体。
    
5.  Apply the spectral theorem to the covariance matrix
    将谱定理应用于协方差矩阵
    
    $$
    \Sigma = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix},
    $$
    
    and interpret the eigenvectors as principal directions of variance.
    并将特征向量解释为方差的主方向。
    

## 9.4 Principal Component Analysis (PCA)
9.4 主成分分析（PCA）

Principal Component Analysis (PCA) is a widely used technique in data science, machine learning, and statistics. At its core, PCA is an application of the spectral theorem to covariance matrices: it finds orthogonal directions (principal components) that capture the maximum variance in data.
主成分分析 (PCA) 是数据科学、机器学习和统计学中广泛使用的技术。PCA 的核心是谱定理在协方差矩阵中的应用：它找到能够捕捉数据中最大方差的正交方向（主成分）。

### The Idea
理念

Given a dataset of vectors $\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_m \in \mathbb{R}^n$:
给定向量数据集 $\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_m \in \mathbb{R}^n$ ：

1.  Center the data by subtracting the mean vector $\bar{\mathbf{x}}$.
    通过减去平均向量 $\bar{\mathbf{x}}$ 使数据居中。
    
2.  Form the covariance matrix
    形成协方差矩阵
    
    $$
    \Sigma = \frac{1}{m} \sum_{i=1}^m (\mathbf{x}_i - \bar{\mathbf{x}})(\mathbf{x}_i - \bar{\mathbf{x}})^T.
    $$
    
3.  Apply the spectral theorem: $\Sigma = Q \Lambda Q^T$.
    应用谱定理： $\Sigma = Q \Lambda Q^T$ 。
    
    *   Columns of $Q$ are orthonormal eigenvectors (principal directions).
        $Q$ 的列是正交特征向量（主方向）。
    *   Eigenvalues in $\Lambda$ measure variance explained by each direction.
        $\Lambda$ 中的特征值测量每个方向解释的方差。

The first principal component is the eigenvector corresponding to the largest eigenvalue; it is the direction of maximum variance.
第一个主成分是最大特征值对应的特征向量，是方差最大的方向。

### Example 9.4.1
例 9.4.1

Suppose we have two-dimensional data points roughly aligned along the line $y = x$. The covariance matrix is approximately
假设我们有二维数据点大致沿着直线 $y = x$ 排列。协方差矩阵大约为

$$
\Sigma =\begin{bmatrix}2 & 1.9 \\1.9 & 2\end{bmatrix}.
$$

Eigenvalues are about $3.9 and \\0.1$. The eigenvector for $\\lambda = 3.9$is approximately$(1,1)/\\sqrt{2}$.
特征值约为 $3.9 和 \\ 0.1 $. The eigenvector for $ \\lambda = 3.9 $is approximately$ (1,1)/\\sqrt{2}$。

*   First principal component: the line $y = x$.
    第一个主成分：线 $y = x$ 。
*   Most variance lies along this direction.
    大部分差异都发生在这个方向。
*   Second component is nearly orthogonal ($y = -x$), but variance there is tiny.
    第二个成分几乎正交（ $y = -x$ ），但那里的方差很小。

Thus PCA reduces the data to essentially one dimension.
因此，PCA 将数据简化为一个维度。

### Applications of PCA
PCA 的应用

1.  Dimensionality reduction: Represent data with fewer features while retaining most variance.
    降维：用较少的特征表示数据，同时保留大部分的方差。
2.  Noise reduction: Small eigenvalues correspond to noise; discarding them filters data.
    降噪：较小的特征值对应噪声；丢弃它们可以过滤数据。
3.  Visualization: Projecting high-dimensional data onto top 2 or 3 principal components reveals structure.
    可视化：将高维数据投影到前 2 个或 3 个主成分上可以揭示结构。
4.  Compression: PCA is used in image and signal compression.
    压缩：PCA 用于图像和信号压缩。

### Connection to the Spectral Theorem
与谱定理的联系

The covariance matrix $\Sigma$ is always symmetric and positive semidefinite. Hence by the spectral theorem, it has an orthonormal basis of eigenvectors and nonnegative real eigenvalues. PCA is nothing more than re-expressing data in this eigenbasis.
协方差矩阵 $\Sigma$ 始终是对称的，且为半正定矩阵。因此，根据谱定理，它有一个由特征向量和非负实特征值组成的正交基。PCA 只不过是在这个特征基上重新表达数据。

### Why this matters
为什么这很重要

PCA demonstrates how abstract linear algebra directly powers modern applications. Eigenvalues and eigenvectors give a practical method for simplifying data, revealing patterns, and reducing complexity. It is one of the most important algorithms derived from the spectral theorem.
PCA 展示了抽象线性代数如何直接驱动现代应用。特征值和特征向量提供了一种简化数据、揭示模式和降低复杂性的实用方法。它是从谱定理中推导出的最重要的算法之一。

### Exercises 9.4
练习 9.4

1.  Show that the covariance matrix is symmetric and positive semidefinite.
    证明协方差矩阵是对称的和半正定的。
2.  Compute the covariance matrix of the dataset $(1,2), (2,3), (3,4)$, and find its eigenvalues and eigenvectors.
    计算数据集 $(1,2), (2,3), (3,4)$ 的协方差矩阵，并找到其特征值和特征向量。
3.  Explain why the first principal component captures the maximum variance.
    解释为什么第一个主成分捕获最大方差。
4.  In image compression, explain how PCA can reduce storage by keeping only the top $k$ principal components.
    在图像压缩中，解释 PCA 如何通过仅保留前 $k$ 个主成分来减少存储。
5.  Prove that the sum of the eigenvalues of the covariance matrix equals the total variance of the dataset.
    证明协方差矩阵的特征值之和等于数据集的总方差。