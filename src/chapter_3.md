# Chapter 3. Systems of Linear Equations
第 3 章线性方程组

## 3.1 Linear Systems and Solutions
3.1 线性系统及其解

One of the central motivations for linear algebra is solving systems of linear equations. These systems arise naturally in science, engineering, and data analysis whenever multiple constraints interact. Matrices provide a compact language for expressing and solving them.

线性代数的核心动机之一是求解线性方程组。在科学、工程和数据分析领域，当多个约束相互作用时，这类方程组自然而然地出现。矩阵提供了一种简洁的语言来表达和求解它们。

### Linear Systems
线性系统

A linear system consists of equations where each unknown appears only to the first power and with no products between variables. A general system of $m$ equations in $n$ unknowns can be written as:

线性系统由方程组成，其中每个未知数仅出现一次方，并且之间没有乘积 变量。包含 $n$ 个未知数的 $m$ 个方程的一般系统可以写成：

$$
\begin{aligned}a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1, \\a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2, \\&\vdots \\a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m.\end{aligned}
$$

Here the coefficients $a_{ij}$ and constants $b_i$ are scalars, and the unknowns are $x_1, x_2, \dots, x_n$.

这里系数$a_{ij}$  ​ 和常数$b_i$​ 是标量，未知数是$x_1, x_2, \dots, x_n$。

### Matrix Form
矩阵形式

The system can be expressed compactly as:

该系统可以简洁地表示为：

$$
A\mathbf{x} = \mathbf{b},
$$

where

其中


*   $A \in \mathbb{R}^{m \times n}$ is the coefficient matrix $[a_{ij}]$,

    $A \in \mathbb{R}^{m \times n}$ 是系数矩阵 $[a_{ij}]$ ，
*   $\mathbf{x} \in \mathbb{R}^n$ is the column vector of unknowns,

    $\mathbf{x} \in \mathbb{R}^n$ 是未知数的列向量，
*   $\mathbf{b} \in \mathbb{R}^m$ is the column vector of constants.

    $\mathbf{b} \in \mathbb{R}^m$ 是常数列向量。

This formulation turns the problem of solving equations into analyzing the action of a matrix.

这个公式将解方程的问题转化为分析矩阵的作用。

Example 3.1.1. The system

例 3.1.1. 系统

$$
\begin{cases}x + 2y = 5, \\3x - y = 4\end{cases}
$$


可以写成

$$
\begin{bmatrix} 1 & 2 \\ 3 & -1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix}=\begin{bmatrix} 5 \\ 4 \end{bmatrix}.
$$

### Types of Solutions
解决方案类型

A linear system may have:

线性系统可能有：

1.  No solution (inconsistent): The equations conflict. Example:

    无解（不一致）：方程式相互矛盾。例如：

$$
\begin{cases}x + y = 1 \\x + y = 2\end{cases}
$$

This system has no solution.

这个系统没有解决方案。

2.  Exactly one solution (unique): The system’s equations intersect at a single point.

    只有一个解（唯一）：系统方程在一个点相交。

    Example: The following coefficient matrix:

    例如：以下系数矩阵：

$$
\begin{bmatrix}1 & 2 \\3 & -1\end{bmatrix}
$$

has a unique solution.

有一个独特的解决方案。

3.  Infinitely many solutions: The equations describe overlapping constraints (e.g., multiple equations representing the same line or plane).

    无数个解：方程描述重叠的约束（例如，表示同一条线或平面的多个方程）。

The nature of the solution depends on the rank of $A$ and its relation to the augmented matrix $(A|\mathbf{b})$, which we will study later.

解的性质取决于 $A$ 的秩及其与增广矩阵 $(A|\mathbf{b})$ 的关系，我们稍后会研究。

### Geometric Interpretation
几何解释

*   In $\mathbb{R}^2$, each linear equation represents a line. Solving a system means finding intersection points of lines.

    在 $\mathbb{R}^2$ 中，每个线性方程代表一条直线。求解方程组意味着找到直线的交点。
*   In $\mathbb{R}^3$, each equation represents a plane. A system may have no solution (parallel planes), one solution (a unique intersection point), or infinitely many (a line of intersection).

    在 $\mathbb{R}^3$ 中，每个方程代表一个平面。一个方程组可能没有解（平行平面），可能有一个解（唯一的交点），也可能有无数个解（一条交线）。    
*   In higher dimensions, the picture generalizes: solutions form intersections of hyperplanes.

    在更高维度中，该图概括为：解决方案形成超平面的交点。

### Why this matters
为什么这很重要

Linear systems are the practical foundation of linear algebra. They appear in balancing chemical reactions, circuit analysis, least-squares regression, optimization, and computer graphics. Understanding how to represent and classify their solutions is the first step toward systematic solution methods like Gaussian elimination.

线性系统是线性代数的实践基础。它们出现在平衡化学反应、电路分析、最小二乘回归、优化和计算机图形学中。了解如何表示和分类它们的解是迈向高斯消元法等系统求解方法的第一步。

### Exercises 3.1
练习3.1

1.  Write the following system in matrix form:

    将以下系统写成矩阵形式：

$$
\begin{cases}2x + 3y - z = 7, \\x - y + 4z = 1, \\3x + 2y + z = 5\end{cases}
$$

2.  Determine whether the system

    确定系统是否

$$
\begin{cases}x + y = 1, \\2x + 2y = 2\end{cases}
$$

has no solution, one solution, or infinitely many solutions.

有无解、有一个解或有无数个解。

3.  Geometrically interpret the system

    在平面上对方程组进行几何解释。

$$
\begin{cases}x + y = 3, \\x - y = 1\end{cases}
$$

in the plane.

4.  Solve the system

    解方程组

$$
\begin{cases}2x + y = 1, \\x - y = 4\end{cases}
$$

and check your solution.

并检查您的解。

5.  In $\mathbb{R}^3$, describe the solution set of

    在 $\mathbb{R}^3$ 中，描述

$$
\begin{cases}x + y + z = 0, \\2x + 2y + 2z = 0\end{cases}
$$

What geometric object does it represent?

它代表什么几何对象？

## 3.2 Gaussian Elimination
3.2 高斯消元法

To solve linear systems efficiently, we use Gaussian elimination: a systematic method of transforming a system into a simpler equivalent one whose solutions are easier to see. The method relies on elementary row operations that preserve the solution set.

为了高效地求解线性方程组，我们使用高斯消元法：这是一种将方程组转化为更简单、更易解的等效方程的系统方法。该方法依赖于保留解集的基本行运算。

### Elementary Row Operations
初等行运算

On an augmented matrix $(A|\mathbf{b})$, we are allowed three operations:

对于增广矩阵 $(A|\mathbf{b})$ ，我们可以进行三种运算：

1.  Row swapping: interchange two rows.

    换行：交换两行。
2.  Row scaling: multiply a row by a nonzero scalar.

    行缩放：将一行乘以非零标量。
3.  Row replacement: replace one row by itself plus a multiple of another row.

    行替换：用一行本身加上另一行的倍数来替换一行。

These operations correspond to re-expressing equations in different but equivalent forms.

这些运算对应于以不同但等效的形式重新表达方程。

### Row Echelon Form
行梯队形式

A matrix is in row echelon form (REF) if:

如果满足以下条件，则矩阵为行阶梯形矩阵（REF）：

1.  All nonzero rows are above any zero rows.

    所有非零行均位于任何零行之上。
2.  Each leading entry (the first nonzero number from the left in a row) is to the right of the leading entry in the row above.

    每个前导条目（一行中从左边开始的第一个非零数字）位于上一行前导条目的右侧。
3.  All entries below a leading entry are zero.

    前导条目下面的所有条目都为零。

Further, if each leading entry is 1 and is the only nonzero entry in its column, the matrix is in reduced row echelon form (RREF).

此外，如果每个前导项都是 1，并且是其列中唯一的非零项，则矩阵为简化行阶梯形式 (RREF)。

### Algorithm of Gaussian Elimination
高斯消元法

1.  Write the augmented matrix for the system.

    写出系统的增广矩阵。
2.  Use row operations to create zeros below each pivot (the leading entry in a row).

    使用行运算在每个主元（一行中的前导条目）下方创建零。
3.  Continue column by column until the matrix is in echelon form.

    继续逐列进行，直到矩阵呈阶梯形式。
4.  Solve by back substitution: starting from the last pivot equation and working upward.

    通过反向代入来求解：从最后一个主元方程开始向上求解。

If we continue to RREF, the solution can be read off directly.
如果我们继续 RREF，则可以直接读出解决方案。

### Example
例子



Example 3.2.1. Solve

例 3.2.1. 求解

$$
\begin{cases}x + 2y - z = 3, \\2x + y + z = 7, \\3x - y + 2z = 4.\end{cases}
$$

Step 1. Augmented matrix

步骤1.增广矩阵

$$
\left[\begin{array}{ccc|c}1 & 2 & -1 & 3 \\2 & 1 & 1 & 7 \\3 & -1 & 2 & 4\end{array}\right].
$$

Step 2. Eliminate below the first pivot

步骤 2. 消除第一个主元以下的元（置0）

Subtract 2 times row 1 from row 2, and 3 times row 1 from row 3:

从第 2 行减去第 1 行的 2 倍，从第 3 行减去第 1 行的 3 倍：

$$
\left[\begin{array}{ccc|c}1 & 2 & -1 & 3 \\0 & -3 & 3 & 1 \\0 & -7 & 5 & -5\end{array}\right].
$$

Step 3. Pivot in column 2

步骤 3. 在第 2 列中选取主元

Divide row 2 by -3:

将第 2 行除以 -3：

$$
\left[\begin{array}{ccc|c}1 & 2 & -1 & 3 \\0 & 1 & -1 & -\tfrac{1}{3} \\0 & -7 & 5 & -5\end{array}\right].
$$

Add 7 times row 2 to row 3:

将第 2 行的 7 倍加到第 3 行：

$$
\left[\begin{array}{ccc|c}1 & 2 & -1 & 3 \\0 & 1 & -1 & -\tfrac{1}{3} \\0 & 0 & -2 & -\tfrac{22}{3}\end{array}\right].
$$

Step 4. Pivot in column 3

步骤 4. 在第 3 列中选取主元

Divide row 3 by -2:

将第 3 行除以 -2：

$$
\left[\begin{array}{ccc|c}1 & 2 & -1 & 3 \\0 & 1 & -1 & -\tfrac{1}{3} \\0 & 0 & 1 & \tfrac{11}{3}\end{array}\right].
$$

Step 5. Back substitution

步骤 5. 回代

From the last row:

从最后一行开始：

$$
z = \tfrac{11}{3}.
$$

Second row:

第二行：

$$
y - z = -\tfrac{1}{3} \implies y = -\tfrac{1}{3} + \tfrac{11}{3} = \tfrac{10}{3}.
$$

First row:

第一行：

$$
x + 2y - z = 3 \implies x + 2\cdot\tfrac{10}{3} - \tfrac{11}{3} = 3.
$$

So

所以

$$
x + \tfrac{20}{3} - \tfrac{11}{3} = 3 \implies x + 3 = 3 \implies x = 0.
$$

Solution:

解：

$$
(x,y,z) = \big(0, \tfrac{10}{3}, \tfrac{11}{3}\big).
$$

### Why this matters
为什么这很重要

Gaussian elimination is the foundation of computational linear algebra. It reduces complex systems to a form where solutions are visible, and it forms the basis for algorithms used in numerical analysis, scientific computing, and machine learning.

高斯消元法是计算线性代数的基础。它将复杂系统简化为可见解的形式，并构成数值分析、科学计算和机器学习中使用的算法的基础。

### Exercises 3.2
练习 3.2

1.  Solve by Gaussian elimination:

    通过高斯消元法求解：

$$
\begin{cases}x + y = 2, \\2x - y = 0.\end{cases}
$$

2.  Reduce the following augmented matrix to REF:

    将以下增广矩阵简化为 REF：

$$
\left[\begin{array}{ccc|c}1 & 1 & 1 & 6 \\2 & -1 & 3 & 14 \\1 & 4 & -2 & -2\end{array}\right].
$$

3.  Show that Gaussian elimination always produces either:

    证明高斯消元法总是产生以下结果：

*   a unique solution,

    一个独特的解决方案，
*   infinitely many solutions, or

    无穷多个解，或者
*   a contradiction (no solution).

    矛盾（无解）。

4.  Use Gaussian elimination to find all solutions of

    使用高斯消元法找到所有解

$$
\begin{cases}x + y + z = 0, \\2x + y + z = 1.\end{cases}
$$

5.  Explain why pivoting (choosing the largest available pivot element) is useful in numerical computation.

    解释为什么枢轴旋转（选择最大的可用主元元素）在数值计算中很有用。

## 3.3 Rank and Consistency
3.3 秩和一致性

Gaussian elimination not only provides solutions but also reveals the structure of a linear system. Two key ideas are the rank of a matrix and the consistency of a system. Rank measures the amount of independent information in the equations, while consistency determines whether the system has at least one solution.

高斯消元法不仅能提供解，还能揭示线性系统的结构。两个关键概念是矩阵的秩和系统的一致性。秩衡量方程中独立信息的数量，而一致性则决定系统是否至少有一个解。

### Rank of a Matrix
矩阵的秩

The rank of a matrix is the number of leading pivots in its row echelon form. Equivalently, it is the maximum number of linearly independent rows or columns.

矩阵的秩是其行阶梯形中前导主元的个数。换句话说，它是线性无关的行或列的最大数量。

Formally,
正式地，

$$
\text{rank}(A) = \dim(\text{row space of } A) = \dim(\text{column space of } A).
$$

The rank tells us the effective dimension of the space spanned by the rows (or columns).

秩告诉我们行（或列）所跨越的空间的有效维度。

Example 3.3.1. For

例 3.3.1. 对于

$$
A = \begin{bmatrix}1 & 2 & 3 \\2 & 4 & 6 \\3 & 6 & 9\end{bmatrix},
$$

row reduction gives

行减少给出

$$
\begin{bmatrix}1 & 2 & 3 \\0 & 0 & 0 \\0 & 0 & 0\end{bmatrix}.
$$

Thus, $\text{rank}(A) = 1$, since all rows are multiples of the first.

因此， $\text{rank}(A) = 1$ ，因为所有行都是第一行的倍数。

### Consistency of Linear Systems

线性系统的一致性

Consider the system $A\mathbf{x} = \mathbf{b}$. The system is consistent (has at least one solution) if and only if

考虑系统 $A\mathbf{x} = \mathbf{b}$ 。该系统是一致的（至少有一个解），当且仅当

$$
\text{rank}(A) = \text{rank}(A|\mathbf{b}),
$$

where $(A|\mathbf{b})$ is the augmented matrix. If the ranks differ, the system is inconsistent.

其中 $(A|\mathbf{b})$ 是增广矩阵。如果秩不同，则系统不一致。

*   If $\text{rank}(A) = \text{rank}(A|\mathbf{b}) = n$ (number of unknowns), the system has a unique solution.

    如果 $\text{rank}(A) = \text{rank}(A|\mathbf{b}) = n$ （未知数），则系统有一个唯一的解。
*   If $\text{rank}(A) = \text{rank}(A|\mathbf{b}) < n$, the system has infinitely many solutions.

    如果 $\text{rank}(A) = \text{rank}(A|\mathbf{b}) < n$ ，则系统有无数个解。

### Example
例子

Example 3.3.2. Consider

例 3.3.2. 考虑

$$
\begin{cases}x + y + z = 1, \\2x + 2y + 2z = 2, \\x + y + z = 3.\end{cases}
$$

The augmented matrix is

增广矩阵是

$$
\left[\begin{array}{ccc|c}1 & 1 & 1 & 1 \\2 & 2 & 2 & 2 \\1 & 1 & 1 & 3\end{array}\right].
$$

Row reduction gives

行减少给出

$$
\left[\begin{array}{ccc|c}1 & 1 & 1 & 1 \\0 & 0 & 0 & 0 \\0 & 0 & 0 & 2\end{array}\right].
$$

Here, $\text{rank}(A) = 1$, but $\text{rank}(A|\mathbf{b}) = 2$. Since the ranks differ, the system is inconsistent: no solution exists.

这里， $\text{rank}(A) = 1$ ，但 $\text{rank}(A|\mathbf{b}) = 2$ 。由于秩不同，系统不一致：不存在解。

### Example with Infinite Solutions
无限解的例子

Example 3.3.3. For

例 3.3.3. 对于

$$
\begin{cases}x + y = 2, \\2x + 2y = 4,\end{cases}
$$

the augmented matrix reduces to

增广矩阵简化为

$$
\left[\begin{array}{cc|c}1 & 1 & 2 \\0 & 0 & 0\end{array}\right].
$$

Here, $\text{rank}(A) = \text{rank}(A|\mathbf{b}) = 1 < 2$. Thus, infinitely many solutions exist, forming a line.

这里， $\text{rank}(A) = \text{rank}(A|\mathbf{b}) = 1 < 2$ 。因此，存在无数个解，形成一条线。

### Why this matters
为什么这很重要

Rank is a measure of independence: it tells us how many truly distinct equations or directions are present. Consistency explains when equations align versus when they contradict. These concepts connect linear systems to vector spaces and prepare for the ideas of dimension, basis, and the Rank–Nullity Theorem.

秩是独立性的度量：它告诉我们有多少个真正不同的方程或方向。一致性解释了方程何时一致，何时矛盾。这些概念将线性系统与向量空间联系起来，并为维度、基和秩零定理的概念做好准备。

### Exercises 3.3
练习 3.3

1.  Compute the rank of

    计算下面矩阵的秩

$$
A = \begin{bmatrix}1 & 2 & 1 \\0 & 1 & -1 \\2 & 5 & -1\end{bmatrix}.
$$

2.  Determine whether the system

    确定方程组是一致的

$$
\begin{cases}x + y + z = 1, \\2x + 3y + z = 2, \\3x + 5y + 2z = 3\end{cases}
$$

is consistent.


3.  Show that the rank of the identity matrix $I_n$ is $n$.

    证明单位矩阵 $I_n$ 的秩   ​ 是 $n$ 。
    
4.  Give an example of a system in $\mathbb{R}^3$ with infinitely many solutions, and explain why it satisfies the rank condition.

    给出 $\mathbb{R}^3$ 中具有无穷多个解的系统的例子，并解释它为什么满足秩条件。
    
5.  Prove that for any matrix $A \in \mathbb{R}^{m \times n}$, $\text{rank}(A) \leq \min(m,n).$

    证明对于任意矩阵 $A \in \mathbb{R}^{m \times n}$ ， $\text{rank}(A) \leq \min(m,n).$
    

## 3.4 Homogeneous Systems
3.4 齐次方程组

A homogeneous system is a linear system in which all constant terms are zero:

齐次方程组是所有常数项都为零的线性系统：

$$
A\mathbf{x} = \mathbf{0},
$$

where $A \in \mathbb{R}^{m \times n}$, and $\mathbf{0}$ is the zero vector in $\mathbb{R}^m$.

其中 $A \in \mathbb{R}^{m \times n}$ ，且 $\mathbf{0}$ 是 $\mathbb{R}^m$ 中的零向量。

### The Trivial Solution
简单的解决方案

Every homogeneous system has at least one solution:

每个齐次方程组至少有一个解：

$$
\mathbf{x} = \mathbf{0}.
$$

This is called the trivial solution. The interesting question is whether *nontrivial solutions* (nonzero vectors) exist.

这被称为平凡解。有趣的问题是是否存在*非平凡解* （非零向量）。

### Existence of Nontrivial Solutions
非平凡解的存在性

Nontrivial solutions exist precisely when the number of unknowns exceeds the rank of the coefficient matrix:

当未知数的数量超过系数矩阵的秩时，就会存在非平凡解：

$$
\text{rank}(A) < n.
$$

In this case, there are infinitely many solutions, forming a subspace of $\mathbb{R}^n$. The dimension of this solution space is

在这种情况下，有无穷多个解，形成一个 $\mathbb{R}^n$ 的子空间。这个解空间的维度是

$$
\dim(\text{null}(A)) = n - \text{rank}(A),
$$

where null(A) is the set of all solutions to $A\mathbf{x} = 0$. This set is called the null space or kernel of $A$.

其中 null(A) 是 $A\mathbf{x} = 0$ 所有解的集合。该集合称为 $A$ 的零空间或零核。

### Example
例子

Example 3.4.1. Consider

例 3.4.1. 考虑

$$
\begin{cases}x + y + z = 0, \\2x + y - z = 0.\end{cases}
$$

The augmented matrix is

增广矩阵是

$$
\left[\begin{array}{ccc|c}1 & 1 & 1 & 0 \\2 & 1 & -1 & 0\end{array}\right].
$$

Row reduction:

行减少：

$$
\left[\begin{array}{ccc|c}1 & 1 & 1 & 0 \\0 & -1 & -3 & 0\end{array}\right]\quad\to\quad\left[\begin{array}{ccc|c}1 & 1 & 1 & 0 \\0 & 1 & 3 & 0\end{array}\right].
$$

So the system is equivalent to:

因此该系统等同于：

$$
\begin{cases}x + y + z = 0, \\y + 3z = 0.\end{cases}
$$

From the second equation, $y = -3z$. Substituting into the first: $x - 3z + z = 0 \implies x = 2z.$

从第二个方程得出 $y = -3z$ 。代入第一个方程： $x - 3z + z = 0 \implies x = 2z.$

Thus solutions are:

因此解决方案是：

$$
(x,y,z) = z(2, -3, 1), \quad z \in \mathbb{R}.
$$

The null space is the line spanned by the vector $(2, -3, 1)$.

零空间是向量 $(2, -3, 1)$ 所跨越的线。

### Geometric Interpretation
几何解释

The solution set of a homogeneous system is always a subspace of $\mathbb{R}^n$.

同质系统的解集始终是 $\mathbb{R}^n$ 的子空间。

*   If $\text{rank}(A) = n$, the only solution is the zero vector.

    如果为 $\text{rank}(A) = n$ ，则唯一的解就是零向量。
*   If $\text{rank}(A) = n-1$, the solution set is a line through the origin.

    如果为 $\text{rank}(A) = n-1$ ，则解集是一条过原点的线。
*   If $\text{rank}(A) = n-2$, the solution set is a plane through the origin.

    如果为 $\text{rank}(A) = n-2$ ，则解集是通过原点的平面。

More generally, the null space has dimension $n - \text{rank}(A)$, known as the nullity.

更一般地，零空间的维度为 $n - \text{rank}(A)$ ，称为零度。

### Why this matters
为什么这很重要

Homogeneous systems are central to understanding vector spaces, subspaces, and dimension. They lead directly to the concepts of kernel, null space, and linear dependence. In applications, homogeneous systems appear in equilibrium problems, eigenvalue equations, and computer graphics transformations.

齐次系统是理解向量空间、子空间和维度的核心。它们直接引出核、零空间和线性相关性的概念。在实际应用中，齐次系统出现在平衡问题、特征值方程和计算机图形变换中。

### Exercises 3.4
练习 3.4

1.  Solve the homogeneous system

    解齐次方程组

$$
\begin{cases}x + 2y - z = 0, \\2x + 4y - 2z = 0.\end{cases}
$$

What is the dimension of its solution space?

其解空间的维数是多少？

2.  Find all solutions of

    找到所有解

$$
\begin{cases}x - y + z = 0, \\2x + y - z = 0.\end{cases}
$$

3.  Show that the solution set of any homogeneous system is a subspace of $\mathbb{R}^n$.

    证明任何线性方程组的解集都是 $\mathbb{R}^n$ 的子空间。
    
4.  Suppose $A$ is a $3 \times 3$ matrix with $\text{rank}(A) = 2$. What is the dimension of the null space of $A$?

    设 $A$ 是 $3 \times 3$ 矩阵，且 $\text{rank}(A) = 2$。则 $A$ 的零空间维数是多少？
    
5.  For

    为
    

$$
A = \begin{bmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{bmatrix},
$$

compute a basis for the null space of $A$.

计算 $A$ 的零空间的基础。