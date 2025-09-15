# Chapter 2. Matrices
第 2 章矩阵

## 2.1 Definition and Notation
2.1 定义和符号

Matrices are the central objects of linear algebra, providing a compact way to represent and manipulate linear transformations, systems of equations, and structured data. A matrix is a rectangular array of numbers arranged in rows and columns.

矩阵是线性代数的核心对象，它提供了一种简洁的方式来表示和操作线性变换、方程组和结构化数据。矩阵是由按行和列排列的数字组成的矩形阵列。

### Formal Definition
正式定义

An $m \times n$ matrix is an array with $m$ rows and $n$ columns, written

$m \times n$ 矩阵是具有 $m$ 行和 $n$ 列的数组，写为

$$
A =\begin{bmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\a_{21} & a_{22} & \cdots & a_{2n} \\\vdots & \vdots & \ddots & \vdots \\a_{m1} & a_{m2} & \cdots & a_{mn}\end{bmatrix}.
$$

Each entry $a_{ij}$ is a scalar, located in the *i*\-th row and *j*\-th column. The size (or dimension) of the matrix is denoted by $m \times n$.

每个条目$a_{ij}$ 是一个标量，位于第 *i* 行和第 *j* 列。矩阵的大小（或维度）用 $m \times n$ 表示。

*   If $m = n$, the matrix is square.

    如果为 $m = n$ ，则矩阵为方阵。
*   If $m = 1$, the matrix is a row vector.

    如果为 $m = 1$ ，则该矩阵为行向量。
*   If $n = 1$, the matrix is a column vector.

    如果为 $n = 1$ ，则矩阵为列向量。

Thus, vectors are simply special cases of matrices.
因此，向量只是矩阵的特殊情况。

### Examples
示例

Example 2.1.1. A 2×3 matrix:

例 2.1.1. 2×3 矩阵：

$$
A = \begin{bmatrix}1 & -2 & 4 \\0 & 3 & 5\end{bmatrix}.
$$

Here, $a_{12} = -2$, $a_{23} = 5$, and the matrix has 2 rows, 3 columns.

这里， $a_{12} = -2$ ， $a_{23} = 5$ ，矩阵有 2 行，3 列。

Example 2.1.2. A 3×3 square matrix:

例 2.1.2. 3×3 方阵：

$$
B = \begin{bmatrix}2 & 0 & 1 \\-1 & 3 & 4 \\0 & 5 & -2\end{bmatrix}.
$$

This will later serve as the representation of a linear transformation on $\mathbb{R}^3$.

这稍后将作为 $\mathbb{R}^3$ 的线性变换的表示。

### Indexing and Notation
索引和符号

*   Matrices are denoted by uppercase bold letters: $A, B, C$.

    矩阵用大写粗体字母表示： $A, B, C$ 。
*   Entries are written as $a_{ij}$, with the row index first, column index second.

    条目写为$a_{ij}$ ​ ，其中行索引在前，列索引在后。
*   The set of all real $m \times n$ matrices is denoted $\mathbb{R}^{m \times n}$.

    所有实数 $m \times n$ 矩阵的集合表示为 $\mathbb{R}^{m \times n}$ 。

Thus, a matrix is a function $A: {1,\dots,m} \times {1,\dots,n} \to \mathbb{R}$, assigning a scalar to each row-column position.

因此，矩阵是一个函数 $A: {1,\dots,m} \times {1,\dots,n} \to \mathbb{R}$ ，为每个行列位置分配一个标量。

### Why this matters
为什么这很重要

Matrices generalize vectors and give us a language for describing linear operations systematically. They encode systems of equations, rotations, projections, and transformations of data. With matrices, algebra and geometry come together: a single compact object can represent both numerical data and functional rules.

矩阵推广了向量，并为我们提供了一种系统地描述线性运算的语言。它们对方程组、旋转、投影和数据变换进行编码。矩阵将代数和几何结合在一起：一个紧凑的对象既可以表示数值数据，又可以表示函数规则。

### Exercises 2.1
练习 2.1

1.  Write a $3 \times 2$ matrix of your choice and identify its entries $a_{ij}$.

    写一个你选定的 $3 \times 2$ 行方阵，并确定其各元素 $a_{ij}$。
2.  Is every vector a matrix? Is every matrix a vector? Explain.
    每个向量都是矩阵吗？每个矩阵都是向量吗？请解释。
3.  Which of the following are square matrices: $A \in \mathbb{R}^{4\times4}$, $B \in \mathbb{R}^{3\times5}$, $C \in \mathbb{R}^{1\times1}$?

    下列哪些是正方形 矩阵： $A \in \mathbb{R}^{4\times4}$ ， $B \in \mathbb{R}^{3\times5}$ ， $C \in \mathbb{R}^{1\times1}$ ？
4.  Let
    让

$$
D = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix}
$$

What kind of matrix is this? 

这是什么类型的矩阵？

5. Consider the matrix

考虑矩阵

$$
E = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

Express $e_{11}, e_{12}, e_{21}, e_{22}$ explicitly.

明确表示$e_{11}, e_{12}, e_{21}, e_{22}$。

## 2.2 Matrix Addition and Multiplication
2.2 矩阵加法和乘法

Once matrices are defined, the next step is to understand how they combine. Just as vectors gain meaning through addition and scalar multiplication, matrices become powerful through two operations: addition and multiplication.

定义好矩阵后，下一步就是理解它们是如何组合的。正如向量通过加法和标量乘法获得意义一样，矩阵也通过两种运算变得强大：加法和乘法。

### Matrix Addition
矩阵加法

Two matrices of the same size are added by adding corresponding entries. If

两个大小相同的矩阵可以通过添加相应的元素来相加。如果

$$
A = [a_{ij}] \in \mathbb{R}^{m \times n}, \quad B = [b_{ij}] \in \mathbb{R}^{m \times n},
$$

then
则

$$
A + B = [a_{ij} + b_{ij}] \in \mathbb{R}^{m \times n}.
$$

Example 2.2.1. Let

例 2.2.1. 设

$$
A = \begin{bmatrix}1 & 2 \\3 & 4\end{bmatrix}, \quad B = \begin{bmatrix}-1 & 0 \\5 & 2\end{bmatrix}.
$$

Then
则

$$
A + B = \begin{bmatrix}1 + (-1) & 2 + 0 \\3 + 5 & 4 + 2\end{bmatrix} =\begin{bmatrix}0 & 2 \\8 & 6\end{bmatrix}.
$$

Matrix addition is commutative ($A+B = B+A$) and associative ($(A+B)+C = A+(B+C)$). The zero matrix, with all entries 0, acts as the additive identity.

矩阵加法满足交换律 ( $A+B = B+A$ ) 和结合律 ( $(A+B)+C = A+(B+C)$ )。零矩阵（所有元素均为 0）充当加法恒等式。

### Scalar Multiplication
标量乘法

For a scalar $c \in \mathbb{R}$ and a matrix $A = [[a_{ij}]$, we define

对于标量 $c \in \mathbb{R}$ 和矩阵 $A = [[a_{ij}]$ ，我们定义

$$
cA = [c \cdot a_{ij}].
$$

This stretches or shrinks all entries of the matrix uniformly.

这会均匀地拉伸或收缩矩阵的所有条目。

Example 2.2.2. If

例 2.2.2. 如果

$$
A = \begin{bmatrix}2 & -1 \\0 & 3\end{bmatrix}, \quad c = -2,
$$

then

则

$$
cA = \begin{bmatrix}-4 & 2 \\0 & -6\end{bmatrix}.
$$

### Matrix Multiplication
矩阵乘法

The defining operation of matrices is multiplication. If

矩阵的定义运算是乘法。如果

$$
A \in \mathbb{R}^{m \times n}, \quad B \in \mathbb{R}^{n \times p},
$$

then their product is the $m \times p$ matrix

那么它们的乘积就是 $m \times p$ 矩阵

$$
AB = C = [c_{ij}], \quad c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}.
$$

Thus, the entry in the $i$\-th row and $j$\-th column of $AB$ is the dot product of the $i$\-th row of $A$ with the $j$\-th column of $B$.

因此， $AB$ 第 $i$ 行、第 $j$ 列的条目是 $A$ 第 $i$ 行与 $B$ 第 $j$ 列的点积。

Example 2.2.3. Let

例 2.2.3. 设

$$
A = \begin{bmatrix}1 & 2 \\0 & 3\end{bmatrix}, \quad B = \begin{bmatrix}4 & -1 \\2 & 5\end{bmatrix}.
$$

Then

则

$$
AB = \begin{bmatrix}1\cdot4 + 2\cdot2 & 1\cdot(-1) + 2\cdot5 \\0\cdot4 + 3\cdot2 & 0\cdot(-1) + 3\cdot5\end{bmatrix} =\begin{bmatrix}8 & 9 \\6 & 15\end{bmatrix}.
$$

Notice that matrix multiplication is not commutative in general: $AB \neq BA$. Sometimes $BA$ may not even be defined if dimensions do not align.

请注意，矩阵乘法通常不满足交换律： $AB \neq BA$ 。如果维度不一致，有时甚至可能无法定义 $BA$ 。

### Geometric Meaning
几何意义

Matrix multiplication corresponds to the composition of linear transformations. If $A$ transforms vectors in $\mathbb{R}^n$ and $B$ transforms vectors in $\mathbb{R}^p$, then $AB$ represents applying $B$ first, then $A$. This makes matrices the algebraic language of transformations.

矩阵乘法对应于线性变换的复合。如果 $A$ 变换 $\mathbb{R}^n$ 中的向量， $B$ 变换 $\mathbb{R}^p$ 中的向量，那么 $AB$ 表示先应用 $B$ ，然后再应用 $A$ 。这使得矩阵成为变换的代数语言。

### Notation
符号

*   Matrix sum: $A+B$.

    矩阵和： $A+B$ 。
*   Scalar multiple: $cA$.

    标量倍数： $cA$ 。
*   Product: $AB$, defined only when the number of columns of $A$ equals the number of rows of $B$.

    乘积： $AB$ ，仅当 $A$ 的列数等于 $B$ 的行数时才定义。

### Why this matters
为什么这很重要

Matrix multiplication is the core mechanism of linear algebra: it encodes how transformations combine, how systems of equations are solved, and how data flows in modern algorithms. Addition and scalar multiplication make matrices into a vector space, while multiplication gives them an algebraic structure rich enough to model geometry, computation, and networks.

矩阵乘法是线性代数的核心机制：它编码了变换的组合方式、方程组的求解方式以及现代算法中数据流动的方式。加法和标量乘法将矩阵转化为向量空间，而乘法则赋予矩阵丰富的代数结构，使其能够对几何、计算和网络进行建模。

### Exercises 2.2
练习 2.2

1.  Compute $A+B$ for

    计算 $A+B$

$$
A = \begin{bmatrix} 2 & 3 \\-1 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 4 & -2 \\5 & 7 \end{bmatrix}.
$$

2.  Find 3A where

    查找 3A

$$
A = \begin{bmatrix} 1 & -4 \\2 & 6 \end{bmatrix}.
$$

3.  Multiply

    乘

$$
A = \begin{bmatrix} 1 & 0 & 2 \\-1 & 3 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 1 \\0 & -1 \\3 & 4 \end{bmatrix}.
$$

4.  Verify with an explicit example that $AB \neq BA$.

    通过明确的例子来验证 $AB \neq BA$ 。
5.  Prove that matrix multiplication is distributive: $A(B+C) = AB + AC$.

    证明矩阵乘法是分配的： $A(B+C) = AB + AC$ 。

## 2.3 Transpose and Inverse
2.3 转置和逆

Two special operations on matrices-the transpose and the inverse-give rise to deep algebraic and geometric properties. The transpose rearranges a matrix by flipping it across its main diagonal, while the inverse, when it exists, acts as the undo operation for matrix multiplication.

矩阵的两种特殊运算——转置和逆——引出了深刻的代数和几何性质。转置通过沿矩阵主对角线翻转来重新排列矩阵，而逆（如果存在）则充当矩阵乘法的撤消操作。

### The Transpose
转置

The transpose of an $m \times n$ matrix $A = [a_{ij}]$ is the $n \times m$ matrix $A^T = [a_{ji}]$, obtained by swapping rows and columns.

$m \times n$ 矩阵 $A = [a_{ij}]$ 的转置是通过交换行和列获得的 $n \times m$ 矩阵 $A^T = [a_{ji}]$ 。

Formally,

正式地，

$$
(A^T)\_{ij} = a\_{ji}.
$$

Example 2.3.1. If

例 2.3.1. 如果

$$
A = \begin{bmatrix}1 & 4 & -2 \\0 & 3 & 5\end{bmatrix},
$$

then

然后

$$
A^T = \begin{bmatrix}1 & 0 \\4 & 3 \\-2 & 5\end{bmatrix}.
$$

Properties of the Transpose.

转置的属性。

1.  $(A^T)^T = A$.
2.  $(A+B)^T = A^T + B^T$.
3.  $(cA)^T = cA^T$, for scalar $c$.

    $(cA)^T = cA^T$ ，对于标量 $c$ 。
4.  $(AB)^T = B^T A^T$.

The last rule is crucial: the order reverses.

最后一条规则至关重要：顺序反转。

### The Inverse
逆

A square matrix $A \in \mathbb{R}^{n \times n}$ is said to be invertible (or nonsingular) if there exists another matrix $A^{-1}$ such that

如果存在另一个矩阵 $A^{-1}$ 满足以下条件，则称方阵 $A \in \mathbb{R}^{n \times n}$ 可逆（或非奇异）

$$
AA^{-1} = A^{-1}A = I_n,
$$

where $I_n$ is the $n \times n$ identity matrix. In this case, $A^{-1}$ is called the inverse of $A$.

其中 $I_n$ ​ 是 $n \times n$ 单位矩阵。在这种情况下， $A^{-1}$ 被称为 $A$ 的逆。

Not every matrix is invertible. A necessary condition is that $\det(A) \neq 0$, a fact that will be developed in Chapter 6.

并非所有矩阵都是可逆的。必要条件是 $\det(A) \neq 0$ ，我们将在第 6 章中进一步阐述。

Example 2.3.2. Let

例 2.3.2. 设

$$
A = \begin{bmatrix}1 & 2 \\3 & 4\end{bmatrix}.
$$

Its determinant is $\det(A) = (1)(4) - (2)(3) = -2 \neq 0$. The inverse is

它的行列式是 $\det(A) = (1)(4) - (2)(3) = -2 \neq 0$ 。逆是

$$
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix}4 & -2 \\-3 & 1\end{bmatrix} =\begin{bmatrix}-2 & 1 \\1.5 & -0.5\end{bmatrix}.
$$

Verification:

确认：

$$
AA^{-1} = \begin{bmatrix}1 & 2 \\3 & 4\end{bmatrix}\begin{bmatrix}-2 & 1 \\1.5 & -0.5\end{bmatrix} =\begin{bmatrix}1 & 0 \\0 & 1\end{bmatrix}.
$$

### Geometric Meaning
几何意义

*   The transpose corresponds to reflecting a linear transformation across the diagonal. For vectors, it switches between row and column forms.

    转置对应于沿对角线反映线性变换。对于向量，它在行和列形式之间切换。
*   The inverse, when it exists, corresponds to reversing a linear transformation. For example, if $A$ scales and rotates vectors, $A^{-1}$ rescales and rotates them back.

    如果存在逆变换，则它对应于线性变换的逆变换。例如，如果 $A$ 缩放并旋转了矢量，则 $A^{-1}$ 会将其重新缩放并旋转回去。

### Notation
符号

*   Transpose: $A^T$.

    转置： $A^T$ 。
*   Inverse: $A^{-1}$, defined only for invertible square matrices.

    逆： $A^{-1}$ ，仅为可逆方阵定义。
*   Identity: $I_n$, acts as the multiplicative identity.

    身份：$I_n$ ​ ，充当乘法恒等式。

### Why this matters
为什么这很重要

The transpose allows us to define symmetric and orthogonal matrices, central to geometry and numerical methods. The inverse underlies the solution of linear systems, encoding the idea of undoing a transformation. Together, these operations set the stage for determinants, eigenvalues, and orthogonalization.

转置使我们能够定义对称矩阵和正交矩阵，这是几何和数值方法的核心。逆矩阵是线性系统解的基础，它蕴含着撤销变换的思想。这些运算共同为行列式、特征值和正交化奠定了基础。

### Exercises 2.3
练习 2.3

1.  Compute the transpose of

    计算转置

$$
A = \begin{bmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \end{bmatrix}.
$$

2.  Verify that $(AB)^T = B^T A^T$ for

    验证 $(AB)^T = B^T A^T$

$$
A = \begin{bmatrix}1 & 2 \\0 & 1 \end{bmatrix}, \quad B = \begin{bmatrix}3 & 4 \\5 & 6 \end{bmatrix}.
$$

3.  Determine whether

    确定是否

$$
C = \begin{bmatrix}2 & 1 \\4 & 2 \end{bmatrix}
$$

is invertible. If so, find $C^{-1}$.
可逆。如果可逆，则求 $C^{-1}$ 。

4.  Find the inverse of
    求逆

$$
D = \begin{bmatrix}0 & 1 \\-1 & 0 \end{bmatrix},
$$

and explain its geometric action on vectors in the plane.

并解释其对平面向量的几何作用。

5.  Prove that if $A$ is invertible, then so is $A^T$, and $(A^T)^{-1} = (A^{-1})^T$.

    证明如果 $A$ 可逆，则 $A^T$ 和 $(A^T)^{-1} = (A^{-1})^T$ 也可逆。

## 2.4 Special Matrices

2.4 特殊矩阵

Certain matrices occur so frequently in theory and applications that they are given special names. Recognizing their properties allows us to simplify computations and understand the structure of linear transformations more clearly.

某些矩阵在理论和应用中出现频率很高，因此被赋予了特殊的名称。了解它们的性质可以简化计算，并更清楚地理解线性变换的结构。

### The Identity Matrix
单位矩阵

The identity matrix $I_n$ is the $n \times n$ matrix with ones on the diagonal and zeros elsewhere:

单位矩阵$I_n$​ 是 $n \times n$ 矩阵，对角线上为 1，其他位置为 0：

$$
I_n = \begin{bmatrix}1 & 0 & \cdots & 0 \\0 & 1 & \cdots & 0 \\\vdots & \vdots & \ddots & \vdots \\0 & 0 & \cdots & 1\end{bmatrix}.
$$

It acts as the multiplicative identity:

它充当乘法恒等式：

$$
AI_n = I_nA = A, \quad \text{for all } A \in \mathbb{R}^{n \times n}.
$$

Geometrically, $I_n$ represents the transformation that leaves every vector unchanged.

从几何学上讲，$I_n$ 表示保持每个向量不变的变换。

### Diagonal Matrices
对角矩阵

A diagonal matrix has all off-diagonal entries zero:

对角矩阵的所有非对角元素均为零：

$$
D = \begin{bmatrix}d_{11} & 0 & \cdots & 0 \\0 & d_{22} & \cdots & 0 \\\vdots & \vdots & \ddots & \vdots \\0 & 0 & \cdots & d_{nn}\end{bmatrix}.
$$

Multiplication by a diagonal matrix scales each coordinate independently:

与对角矩阵相乘可独立缩放每个坐标：

$$
D\mathbf{x} = (d_{11}x_1, d_{22}x_2, \dots, d_{nn}x_n).
$$

Example 2.4.1. Let

例 2.4.1. 设

$$
D = \begin{bmatrix} 2 & 0 & 0 \\0 & 3 & 0 \\0 & 0 & -1 \end{bmatrix}, \quad\mathbf{x} = \begin{bmatrix}1 \\4 \\-2 \end{bmatrix}.
$$

Then

则

$$
D\mathbf{x} = \begin{bmatrix}2 \\12 \\2 \end{bmatrix}.
$$

### Permutation Matrices
置换矩阵

A permutation matrix is obtained by permuting the rows of the identity matrix. Multiplying a vector by a permutation matrix reorders its coordinates.

置换矩阵是通过对单位矩阵的行进行置换而得到的。将向量乘以置换矩阵会重新排序其坐标。

Example 2.4.2. Let
例 2.4.2. 设

$$
P = \begin{bmatrix}0 & 1 & 0 \\1 & 0 & 0 \\0 & 0 & 1\end{bmatrix}.
$$

Then

则


$$
P\begin{bmatrix}a \\b \\c \end{bmatrix} =\begin{bmatrix} b \\a \\c \end{bmatrix}.
$$

Thus, $P$ swaps the first two coordinates.

因此， $P$ 交换前两个坐标。

Permutation matrices are always invertible; their inverses are simply their transposes.

置换矩阵总是可逆的；它们的逆只是它们的转置。

### Symmetric and Skew-Symmetric Matrices
对称矩阵和斜对称矩阵

A matrix is symmetric if

如果矩阵是对称的

$$
A^T = A,
$$

and skew-symmetric if Symmetric matrices appear in quadratic forms and optimization, while skew-symmetric matrices describe rotations and cross products in geometry.

如果对称矩阵出现在二次形式和优化中，则为斜对称，而斜对称矩阵描述几何中的旋转和叉积。

### Orthogonal Matrices
正交矩阵

A square matrix $Q$ is orthogonal if

方阵 $Q$ 是正交的，如果

$$
Q^T Q = QQ^T = I.
$$

Equivalently, the rows (and columns) of $Q$ form an orthonormal set. Orthogonal matrices preserve lengths and angles; they represent rotations and reflections.

等价地， $Q$ 的行（和列）构成一个正交集。正交矩阵保留长度和角度；它们表示旋转和反射。

Example 2.4.3. The rotation matrix in the plane:

例2.4.3. 平面内的旋转矩阵:

$$
R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta \\\sin\theta & \cos\theta\end{bmatrix}
$$

is orthogonal, since

是正交的，因为

$$
R(\theta)^T R(\theta) = I_2.
$$

---

把

$$
R(\theta)=\begin{bmatrix}\cos\theta & -\sin\theta\\[4pt]\sin\theta & \cos\theta\end{bmatrix}
$$

先求转置

$$
R(\theta)^T=\begin{bmatrix}\cos\theta & \sin\theta\\[4pt]-\sin\theta & \cos\theta\end{bmatrix}.
$$

现在相乘（逐项计算）：

* 第一行第一列：

  $$
  (\cos\theta)(\cos\theta)+(\sin\theta)(-\sin\theta)=\cos^2\theta+\sin^2\theta=1.
  $$
* 第一行第二列：

  $$
  (\cos\theta)(-\sin\theta)+(\sin\theta)(\cos\theta)=-\cos\theta\sin\theta+\sin\theta\cos\theta=0.
  $$
* 第二行第一列：

  $$
  (-\sin\theta)(\cos\theta)+(\cos\theta)(-\sin\theta)=-\sin\theta\cos\theta+\cos\theta(-\sin\theta)=0.
  $$

  （同上，等于 0）
* 第二行第二列：

  $$
  (-\sin\theta)(-\sin\theta)+(\cos\theta)(\cos\theta)=\sin^2\theta+\cos^2\theta=1.
  $$

因此

$$
R(\theta)^T R(\theta)=\begin{bmatrix}1&0\\[4pt]0&1\end{bmatrix}=I.
$$

这正符合正交矩阵的定义，所以 $R(\theta)$ 是正交矩阵。

---

### Why this matters
为什么这很重要

Special matrices serve as the building blocks of linear algebra. Identity matrices define the neutral element, diagonal matrices simplify computations, permutation matrices reorder data, symmetric and orthogonal matrices describe fundamental geometric structures. Much of modern applied mathematics reduces complex problems to operations involving these simple forms.

特殊矩阵是线性代数的基石。单位矩阵定义中性元素，对角矩阵简化计算，置换矩阵重新排序数据，对称矩阵和正交矩阵描述基本几何结构。许多现代应用数学将复杂问题简化为涉及这些简单形式的运算。

### Exercises 2.4
练习 2.4

1.  Show that the product of two diagonal matrices is diagonal, and compute an example.

    证明两个对角矩阵的乘积是对角的，并计算一个例子。
2.  Find the permutation matrix that cycles $(a,b,c)$ into $(b,c,a)$.

    找到将 $(a,b,c)$ 循环到 $(b,c,a)$ 的置换矩阵。
3.  Prove that every permutation matrix is invertible and its inverse is its transpose.

    证明每个置换矩阵都是可逆的，并且它的逆是它的转置。
4.  Verify that

    验证

$$
Q = \begin{bmatrix}0 & 1 \\-1 & 0 \end{bmatrix}
$$

is orthogonal. What geometric transformation does it represent? 

是正交的。它代表什么几何变换？

5. Determine whether
判断

$$
A = \begin{bmatrix}2 & 3 \\3 & 2 \end{bmatrix}, \quad B = \begin{bmatrix}0 & 5 \\-5 & 0 \end{bmatrix}
$$

are symmetric, skew-symmetric, or neither.

是对称的、斜对称的，或者都不是。