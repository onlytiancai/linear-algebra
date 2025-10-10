# Chapter 6. Determinants
第六章 行列式

## 6.1 Motivation and Geometric Meaning
6.1 动机和几何意义

Determinants are numerical values associated with square matrices. At first they may appear as a complicated formula, but their importance comes from what they measure: determinants encode scaling, orientation, and invertibility of linear transformations. They bridge algebra and geometry.

行列式是与方阵相关的数值。乍一看，它们可能看起来像一个复杂的公式，但它们的重要性在于它们所测量的内容：行列式编码了线性变换的缩放、方向和可逆性。它们连接了代数和几何。

### Determinants of 2×2 Matrices
2×2 矩阵的行列式

For a 2×2 matrix

对于 2×2 矩阵

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix},
$$

the determinant is defined as

行列式定义为

$$
\det(A) = ad - bc.
$$

Geometric meaning: If $A$ represents a linear transformation of the plane, then $|\det(A)|$ is the area scaling factor. For example, if $\det(A) = 2$, areas of shapes are doubled. If $\det(A) = 0$, the transformation collapses the plane to a line: all area is lost.

几何含义：如果 $A$ 表示平面的线性变换，则 $|\det(A)|$ 是面积缩放因子。例如，如果 $\det(A) = 2$ ，形状的面积将加倍。如果 $\det(A) = 0$ ，变换将平面折叠成一条线：所有面积都将丢失。

### Determinants of 3×3 Matrices
3×3 矩阵的行列式

For

对于

$$
A = \begin{bmatrix}a & b & c \\d & e & f \\g & h & i\end{bmatrix},
$$

the determinant can be computed as

行列式可以计算为

$$
\det(A) = a(ei - fh) - b(di - fg) + c(dh - eg).
$$

Geometric meaning: In $\mathbb{R}^3$, $|\det(A)|$ is the volume scaling factor. If $\det(A) < 0$, orientation is reversed (a handedness flip), such as turning a right-handed coordinate system into a left-handed one.

几何含义：在 $\mathbb{R}^3$ 中， $|\det(A)|$ 是体积缩放因子。如果为 $\det(A) < 0$ ，则方向反转（即手性翻转），例如将右手坐标系转换为左手坐标系。

### General Case
一般情况

For $A \in \mathbb{R}^{n \times n}$, the determinant is a scalar that measures how the linear transformation given by $A$ scales n-dimensional volume.

对于 $A \in \mathbb{R}^{n \times n}$ ，行列式是一个标量，它衡量 $A$ 给出的线性变换如何缩放 n 维体积。

*   If $\det(A) = 0$: the transformation squashes space into a lower dimension, so $A$ is not invertible.

    如果 $\det(A) = 0$ ：变换将空间压缩到较低维度，因此 $A$ 不可逆。
*   If $\det(A) > 0$: volume is scaled by $\det(A)$, orientation preserved.

    如果是 $\det(A) > 0$ ：体积按 $\det(A)$ 缩放，方向保持不变。
*   If $\det(A) < 0$: volume is scaled by $|\det(A)|$, orientation reversed.

    如果是 $\det(A) < 0$ ：体积按 $|\det(A)|$ 缩放，方向反转。

### Visual Examples
视觉示例

1.  Shear in $\mathbb{R}^2$: $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$. Then $\det(A) = 1$. The transformation slants the unit square into a parallelogram but preserves area.

    $\mathbb{R}^2$ 的剪切： $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ 。然后是 $\det(A) = 1$ 。变换将单位正方形倾斜为平行四边形，但保留面积。
    
2.  Projection in $\mathbb{R}^2$: $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$. Then $\det(A) = 0$. The unit square collapses into a line segment: area vanishes.

    $\mathbb{R}^2$ 中的投影： $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ 。然后 $\det(A) = 0$ 。单位正方形坍缩成一条线段：面积消失。
    
3.  Rotation in $\mathbb{R}^2$: $R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$. Then $\det(R_\theta) = 1$. Rotations preserve area and orientation.

    $\mathbb{R}^2$ 中的旋转： $R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ 。然后 $\det(R_\theta) = 1$ 。旋转保留面积和方向。
    

### Why this matters
为什么这很重要

The determinant is not just a formula-it is a measure of transformation. It tells us whether a matrix is invertible, how it distorts space, and whether it flips orientation. This geometric insight makes the determinant indispensable in analysis, geometry, and applied mathematics.

行列式不仅仅是一个公式，它还是一种变换的度量。它告诉我们一个矩阵是否可逆，它如何扭曲空间，以及它是否会翻转方向。这种几何学上的洞察力使得行列式在分析、几何和应用数学中不可或缺。

### Exercises 6.1
练习 6.1

1.  Compute the determinant of

    计算行列式
$$
\begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}
$$

What area scaling factor does it represent? 

它代表什么面积比例因子？

2. Find the determinant of the shear matrix

   求剪切矩阵的行列式

$$
\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}
$$

What happens to the area of the unit square? 

单位正方形的面积会发生什么变化？ 

3. For the $3 \times 3$ matrix

   对于 $3 \times 3$ 矩阵

$$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}$$

Compute the determinant. How does it scale volume in $\mathbb{R}^3$?

计算行列式。它如何在$\mathbb{R}^3$中缩放体积？

4. Show that any rotation matrix in $\mathbb{R}^2$ has determinant $1$.

   证明$\mathbb{R}^2$中任意旋转矩阵的行列式均为$1$。

5. Give an example of a $2 \times 2$ matrix with determinant $-1$. What geometric action does it represent?

   举一个行列式为$-1$的$2 \times 2$矩阵的例子。它代表什么几何作用？



## 6.2 Properties of Determinants

行列式的性质

Beyond their geometric meaning, determinants satisfy a collection of algebraic rules that make them powerful tools in linear algebra. These properties allow us to compute efficiently, test invertibility, and understand how determinants behave under matrix operations.

除了几何意义之外，行列式还满足一系列代数规则，使其成为线性代数中强大的工具。这些性质使我们能够高效计算、测试可逆性，并理解行列式在矩​​阵运算下的行为。

### Basic Properties

基本属性

Let $A, B \in \mathbb{R}^{n \times n}$, and let $c \in \mathbb{R}$. Then:

令 $A, B \in \mathbb{R}^{n \times n}$ ，令 $c \in \mathbb{R}$ 。则：

1.  Identity:

    单位矩阵的行列式为 1：

$$
\det(I_n) = 1.
$$

2.  Triangular matrices: If $A$ is upper or lower triangular, then

    三角矩阵： 如果 $A$ 是上三角矩阵或下三角矩阵，则

$$
\det(A) = a_{11} a_{22} \cdots a_{nn}.
$$

3.  Row/column swap: Interchanging two rows (or columns) multiplies the determinant by $-1$.

    行/列交换： 交换两行（或列）将行列式乘以 $-1$ 。
    
4.  Row/column scaling: Multiplying a row (or column) by a scalar $c$ multiplies the determinant by $c$.

    行/列缩放： 将行（或列）乘以标量 $c$ 会将行列式乘以 $c$ 。
    
5.  Row/column addition: Adding a multiple of one row to another does not change the determinant.

    行/列加法：将一行的倍数添加到另一行不会改变行列式。
    
6.  Transpose:

    转置：
    

$$
\det(A^T) = \det(A).
$$

7.  Multiplicativity:

    乘法性：

$$
\det(AB) = \det(A)\det(B).
$$

8.  Invertibility: $A$ is invertible if and only if $\det(A) \neq 0$.

    可逆性： 当且仅当 $\det(A) \neq 0$ 时， $A$ 才是可逆的。

### Example Computations
计算示例

Example 6.2.1. For

例 6.2.1. 对于

$$
A = \begin{bmatrix}2 & 0 & 0 \\1 & 3 & 0 \\-1 & 4 & 5\end{bmatrix},
$$

$A$ is lower triangular, so

$A$ 是下三角，所以

$$
\det(A) = 2 \cdot 3 \cdot 5 = 30.
$$

Example 6.2.2. Let

例 6.2.2. 设

$$
B = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}.
$$

Then

则

$$
\det(B) = 1\cdot 4 - 2\cdot 3 = -2, \quad \det(C) = -1.
$$

Since $CB$ is obtained by swapping rows of $B$,

由于 $CB$ 是通过交换 $B$ 的行获得的，

$$
\det(CB) = -\det(B) = 2.
$$

This matches the multiplicativity rule: $\det(CB) = \det(C)\det(B) = (-1)(-2) = 2.$

这符合乘法规则： $\det(CB) = \det(C)\det(B) = (-1)(-2) = 2.$

### Geometric Insights
几何洞察

*   Row swaps: flipping orientation of space.

    行交换：翻转空间的方向。
*   Scaling a row: stretching space in one direction.

    缩放一行：朝一个方向拉伸空间。
*   Row replacement: sliding hyperplanes without altering volume.

    行替换：滑动超平面而不改变体积。
*   Multiplicativity: performing two transformations multiplies their scaling factors.

    乘法性：执行两个变换会将它们的比例因子相乘。

These properties make determinants both computationally manageable and geometrically interpretable.

这些性质使得行列式既易于计算管理，又易于几何解释。

### Why this matters
为什么这很重要

Determinant properties connect computation with geometry and theory. They explain why Gaussian elimination works, why invertibility is equivalent to nonzero determinant, and why determinants naturally arise in areas like volume computation, eigenvalue theory, and differential equations.
行列式的性质将计算与几何和理论联系起来。它们解释了高斯消元法为何有效，可逆性为何等价于非零行列式，以及行列式为何自然地出现在体积计算、特征值理论和微分方程等领域。

### Exercises 6.2
练习 6.2

1.  Compute the determinant of
    计算行列式

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 2 \end{bmatrix}.
$$

2.  Show that if two rows of a square matrix are identical, then its determinant is zero.
    证明如果方阵的两行相同，则其行列式为零。
    
3.  Verify $\det(A^T) = \det(A)$ for
    验证 $\det(A^T) = \det(A)$
    

$$
A = \begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix}.
$$

4.  If $A$ is invertible, prove that
    如果 $A$ 可逆，则证明

$$
\det(A^{-1}) = \frac{1}{\det(A)}.
$$

5.  Suppose $A$ is a $3\\times 3$matrix with$\\det(A) = 5$. What is $\\det(2A)$?
    假设 $A$ 是 $3\\times 3 $matrix with$ \\det(A) = 5 $. What is $ \\det(2A)$？

## 6.3 Cofactor Expansion
6.3 辅因子展开

While determinants of small matrices can be computed directly from formulas, larger matrices require a systematic method. The cofactor expansion (also known as Laplace expansion) provides a recursive way to compute determinants by breaking them into smaller ones.
虽然小矩阵的行列式可以直接通过公式计算，但较大的矩阵则需要系统的方法。余因子展开式（也称为拉普拉斯展开式）通过将行列式分解为更小的矩阵，提供了一种递归计算行列式的方法。

### Minors and Cofactors
小式和辅因子

For an $n \times n$ matrix $A = [a_{ij}]$:
对于 $n \times n$ 矩阵 $A = [a_{ij}]$ ：

*   The minor $M_{ij}$ is the determinant of the $(n-1) \times (n-1)$ matrix obtained by deleting the $i$\-th row and $j$ -th column of $A$.
    小调𝑀 𝑖 𝑗 M 伊奇 ​ 是删除第 $i$ 行和 $j$ 后得到的 $(n-1) \times (n-1)$ 矩阵的行列式 $A$ 的第列。
*   The cofactor $C_{ij}$ is defined by
    辅因子𝐶 𝑖 𝑗 C 伊奇 ​ 定义为

$$
C_{ij} = (-1)^{i+j} M_{ij}.
$$

The sign factor $(-1)^{i+j}$ alternates in a checkerboard pattern:
符号因子 $(-1)^{i+j}$ 以棋盘格图案交替出现：

$$
\begin{bmatrix}+ & - & + & - & \cdots \\- & + & - & + & \cdots \\+ & - & + & - & \cdots \\\vdots & \vdots & \vdots & \vdots & \ddots\end{bmatrix}.
$$

### Cofactor Expansion Formula
辅因式展开公式

The determinant of $A$ can be computed by expanding along any row or any column:
$A$ 的行列式可以通过沿任意行或任意列展开来计算：

$$
\det(A) = \sum_{j=1}^n a_{ij} C_{ij} \quad \text{(expansion along row \(i\))},
$$

 

$$
\det(A) = \sum_{i=1}^n a_{ij} C_{ij} \quad \text{(expansion along column \(j\))}.
$$

### Example
例子

Example 6.3.1. Compute
例 6.3.1. 计算

$$
A = \begin{bmatrix}1 & 2 & 3 \\0 & 4 & 5 \\1 & 0 & 6\end{bmatrix}.
$$

Expand along the first row:
沿第一行展开：

$$
\det(A) = 1 \cdot C_{11} + 2 \cdot C_{12} + 3 \cdot C_{13}.
$$

*   For $C_{11}$:
    对于𝐶 11 C 11 ​ :

$$
M_{11} = \det \begin{bmatrix} 4 & 5 \\ 0 & 6 \end{bmatrix} = 24
$$

so $C_{11} = (+1)(24) = 24$.
所以 $C_{11} = (+1)(24) = 24$ 。

*   For $C_{12}$:
    对于𝐶 12 C 12 ​ :

$$
M_{12} = \det \begin{bmatrix} 0 & 5 \\ 1 & 6 \end{bmatrix} = 0 - 5 = -5
$$

so $C_{12} = (-1)(-5) = 5$.
所以 $C_{12} = (-1)(-5) = 5$ 。

*   For $C_{13}$:
    对于𝐶 13 C 13 ​ :

$$
M_{13} = \det \begin{bmatrix} 0 & 4 \\ 1 & 0 \end{bmatrix} = 0 - 4 = -4
$$

so $C_{13} = (+1)(-4) = -4$.
所以 $C_{13} = (+1)(-4) = -4$ 。

Thus,
因此，

$$
\det(A) = 1(24) + 2(5) + 3(-4) = 24 + 10 - 12 = 22.
$$

### Properties of Cofactor Expansion
辅因子展开的性质

1.  Expansion along any row or column yields the same result.
    沿任意行或列扩展都会产生相同的结果。
2.  The cofactor expansion provides a recursive definition of determinant: a determinant of size $n$ is expressed in terms of determinants of size $n-1$.
    余因子展开提供了行列式的递归定义：大小为 $n$ 的行列式可以用大小为 $n-1$ 的行列式来表示。
3.  Cofactors are fundamental in constructing the adjugate matrix, which gives a formula for inverses:
    余因子是构造伴随矩阵的基础，它给出了逆的公式：

$$
A^{-1} = \frac{1}{\det(A)} \, \text{adj}(A), \quad \text{where adj}(A) = [C_{ji}].
$$

### Geometric Interpretation
几何解释

Cofactor expansion breaks down the determinant into contributions from sub-volumes defined by fixing one row or column at a time. Each cofactor measures how that row/column influences the overall volume scaling.
余因子展开将行列式分解为由每次固定一行或一列定义的子体积的贡献。每个余因子衡量该行/列对整体体积缩放的影响。

### Why this matters
为什么这很重要

Cofactor expansion generalizes the small-matrix formulas and provides a conceptual definition of determinants. While not the most efficient way to compute determinants for large matrices, it is essential for theory, proofs, and connections to adjugates, Cramer’s rule, and classical geometry.
余因子展开式推广了小矩阵公式，并提供了行列式的概念定义。虽然它并非计算大矩阵行列式的最有效方法，但它对于理论、证明以及与伴随项、克莱姆规则和古典几何的联系至关重要。

### Exercises 6.3
练习 6.3

1.  Compute the determinant of
    计算行列式

$$
\begin{bmatrix}2 & 0 & 1 \\3 & -1 & 4 \\1 & 2 & 0\end{bmatrix}
$$

by cofactor expansion along the first column.
通过沿第一列的余因子展开。

2.  Verify that expanding along the second row of Example 6.3.1 gives the same determinant.
    验证沿示例 6.3.1 的第二行展开是否给出相同的行列式。
    
3.  Prove that expansion along any row gives the same value.
    证明沿任何行展开都会给出相同的值。
    
4.  Show that if a row of a matrix is zero, then its determinant is zero.
    证明如果矩阵的某一行是零，那么它的行列式也是零。
    
5.  Use cofactor expansion to prove that $\det(A) = \det(A^T)$.
    使用余因子展开来证明 $\det(A) = \det(A^T)$ 。
    

## 6.4 Applications (Volume, Invertibility Test)
6.4 应用（体积、可逆性测试）

Determinants are not merely algebraic curiosities; they have concrete geometric and computational uses. Two of the most important applications are measuring volumes and testing invertibility of matrices.
行列式不仅仅是代数上的奇闻；它们有着具体的几何和计算用途。其中最重要的两个应用是测量体积和检验矩阵的可逆性。

### Determinants as Volume Scalers
决定因素作为体积标量

Given vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \in \mathbb{R}^n$, arrange them as columns of a matrix:
给定向量 $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \in \mathbb{R}^n$ ，将它们排列为矩阵的列：

$$
A = \begin{bmatrix}| & | & & | \\\mathbf{v}_1 & \mathbf{v}_2 & \cdots & \mathbf{v}_n \\| & | & & |\end{bmatrix}.
$$

Then $|\det(A)|$ equals the volume of the parallelepiped spanned by these vectors.
那么 $|\det(A)|$ 等于这些向量所跨越的平行六面体的体积。

*   In $\mathbb{R}^2$, $|\det(A)|$ gives the area of the parallelogram spanned by $\mathbf{v}_1, \mathbf{v}_2$.
    在 $\mathbb{R}^2$ 中， $|\det(A)|$ 给出由 𝑣 构成的平行四边形的面积 1 , 𝑣 2 v 1 ​ ，v 2 ​ .
*   In $\mathbb{R}^3$, $|\det(A)|$ gives the volume of the parallelepiped spanned by $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$.
    在 $\mathbb{R}^3$ 中， $|\det(A)|$ 给出平行六面体的体积，跨度为 𝑣 1 , 𝑣 2 , 𝑣 3 v 1 ​ ，v 2 ​ ，v 3 ​ .
*   In higher dimensions, it generalizes to $n$\-dimensional volume (hypervolume).
    在更高维度中，它可以推广到 $n$ 维体积（超体积）。

Example 6.4.1. Let
例 6.4.1. 设

$$
\mathbf{v}_1 = (1,0,0), \quad \mathbf{v}_2 = (1,1,0), \quad \mathbf{v}_3 = (1,1,1).
$$

Then
然后

$$
A = \begin{bmatrix}1 & 1 & 1 \\0 & 1 & 1 \\0 & 0 & 1\end{bmatrix}, \quad \det(A) = 1.
$$

So the parallelepiped has volume 1, even though the vectors are not orthogonal.
因此，即使向量不正交，平行六面体的体积也是 1 。

### Invertibility Test
可逆性测试

A square matrix $A$ is invertible if and only if $\det(A) \neq 0$.
方阵 $A$ 可逆当且仅当 $\det(A) \neq 0$ 。

*   If $\det(A) = 0$: the transformation collapses space into a lower dimension (area/volume is zero). No inverse exists.
    如果 $\det(A) = 0$ ：变换将空间塌缩至较低维度（面积/体积为零）。不存在逆变换。
*   If $\det(A) \neq 0$: the transformation scales volume by $|\det(A)|$, and is reversible.
    如果 $\det(A) \neq 0$ ：变换将体积缩放 $|\det(A)|$ ，并且是可逆的。

Example 6.4.2. The matrix
例 6.4.2. 矩阵

$$
B = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}
$$

has determinant $\det(B) = 2 \cdot 2 - 4 \cdot 1 = 0$. Thus, $B$ is not invertible. Geometrically, the two column vectors are collinear, spanning only a line in $\mathbb{R}^2$.
行列式为 $\det(B) = 2 \cdot 2 - 4 \cdot 1 = 0$ 。因此， $B$ 不可逆。几何上，这两个列向量共线，在 $\mathbb{R}^2$ 中仅延伸一条线。

### Cramer’s Rule
克莱默规则

Determinants also provide an explicit formula for solving systems of linear equations when the matrix is invertible. For $A\mathbf{x} = \mathbf{b}$ with $A \in \mathbb{R}^{n \times n}$:
当矩阵可逆时，行列式还提供了求解线性方程组的明确公式。 对于带有 $A \in \mathbb{R}^{n \times n}$ 的 $A\mathbf{x} = \mathbf{b}$ ：

$$
x_i = \frac{\det(A_i)}{\det(A)},
$$

where $A_i$ is obtained by replacing the $i$\-th column of $A$ with $\mathbf{b}$. While inefficient computationally, Cramer’s rule highlights the determinant’s role in solutions and uniqueness.
其中𝐴 𝑖 A i ​ 通过将 $A$ 的第 $i$ 列替换为 $\mathbf{b}$ 得到。克莱姆规则虽然计算效率低下，但它凸显了行列式在解和唯一性方面的作用。

### Orientation
方向

The sign of $\det(A)$ indicates whether a transformation preserves or reverses orientation. For example, a reflection in the plane has determinant $-1$, flipping handedness.
$\det(A)$ 的符号表示变换是保持方向还是反转方向。例如，平面上的反射具有行列式 $-1$ ，即翻转旋向性。

### Why this matters
为什么这很重要

Determinants condense key information: they measure scaling, test invertibility, and track orientation. These insights are indispensable in geometry (areas and volumes), analysis (Jacobian determinants in calculus), and computation ( solving systems and checking singularity).
行列式浓缩了关键信息：它们测量缩放比例、检验可逆性并追踪方向。这些洞见在几何学（面积和体积）、分析学（微积分中的雅可比行列式）和计算学（求解系统和检查奇点）中都不可或缺。

### Exercises 6.4
练习 6.4

1.  Compute the area of the parallelogram spanned by $(2,1)$ and $(1,3)$.
    计算 $(2,1)$ 和 $(1,3)$ 所构成的平行四边形的面积。
    
2.  Find the volume of the parallelepiped spanned by $(1,0,0), (1,1,0), (1,1,1)$.
    求出 $(1,0,0), (1,1,0), (1,1,1)$ 所跨度的平行六面体的体积。
    
3.  Determine whether the matrix
    确定矩阵
    

$$
\begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}
$$

is invertible. Justify using determinants. 4. Use Cramer’s rule to solve
是可逆的。用行列式证明。4. 使用克莱姆规则求解

$$
\begin{cases}x + y = 3, \\2x - y = 0.\end{cases}
$$

5.  Explain geometrically why a determinant of zero implies no inverse exists.
    从几何角度解释为什么行列式为零意味着不存在逆元。