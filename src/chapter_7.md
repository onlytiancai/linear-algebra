# Chapter 7. Inner Product Spaces

第 7 章内积空间

## 7.1 Inner Products and Norms

7.1 内积和范数

To extend the geometric ideas of length, distance, and angle beyond $\mathbb{R}^2$ and $\mathbb{R}^3$, we introduce inner products. Inner products provide a way of measuring similarity between vectors, while norms derived from them measure length. These concepts are the foundation of geometry inside vector spaces.

为了将长度、距离和角度的几何概念扩展到 $\mathbb{R}^2$ 和 $\mathbb{R}^3$ 之外，我们引入了内积。内积提供了一种度量向量之间相似性的方法，而由内积导出的范数则用于度量长度。这些概念是向量空间几何的基础。

### Inner Product

内积

An inner product on a real vector space $V$ is a function

实向量空间 $V$ 上的内积是一个函数

$$
\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}
$$

that assigns to each pair of vectors $(\mathbf{u}, \mathbf{v})$ a real number, subject to the following properties:

为每对向量 $(\mathbf{u}, \mathbf{v})$ 分配一个实数，并遵循以下属性：

1.  Symmetry: $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle.$

    对称性： $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle.$
    
2.  Linearity in the first argument: $\langle a\mathbf{u} + b\mathbf{w}, \mathbf{v} \rangle = a \langle \mathbf{u}, \mathbf{v} \rangle + b \langle \mathbf{w}, \mathbf{v} \rangle.$

    第一个参数的线性： $\langle a\mathbf{u} + b\mathbf{w}, \mathbf{v} \rangle = a \langle \mathbf{u}, \mathbf{v} \rangle + b \langle \mathbf{w}, \mathbf{v} \rangle.$
    
3.  Positive-definiteness: $\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$, and equality holds if and only if $\mathbf{v} = \mathbf{0}$.

    正定性： $\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$ ，且仅当 $\mathbf{v} = \mathbf{0}$ 时等式成立。
    

The standard inner product on $\mathbb{R}^n$ is the dot product:

$\mathbb{R}^n$ 上的标准内积是点积：

$$
\langle \mathbf{u}, \mathbf{v} \rangle = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n.
$$

### Norms
范数

The norm of a vector is its length, defined in terms of the inner product:

向量的范数是其长度，根据内积定义：

$$
\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}.
$$

For the dot product in $\mathbb{R}^n$:

对于 $\mathbb{R}^n$ 中的点积：

$$
\|(x_1, x_2, \dots, x_n)\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}.
$$

### Angles Between Vectors

向量之间的角度

The inner product allows us to define the angle $\theta$ between two nonzero vectors $\mathbf{u}, \mathbf{v}$ by

通过内积，我们可以定义两个非零向量 $\mathbf{u}, \mathbf{v}$ 之间的角度 $\theta$ ，即

$$
\cos \theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\| \, \|\mathbf{v}\|}.
$$

Thus, two vectors are orthogonal if $\langle \mathbf{u}, \mathbf{v} \rangle = 0$.

因此，若 $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ ，则两个向量正交。

### Examples

示例

Example 7.1.1. In $\mathbb{R}^2$, with $\mathbf{u} = (1,2)$, $\mathbf{v} = (3,4)$:

例 7.1.1。 在 $\mathbb{R}^2$ 中，使用 $\mathbf{u} = (1,2)$ 、 $\mathbf{v} = (3,4)$ ：

$$
\langle \mathbf{u}, \mathbf{v} \rangle = 1\cdot 3 + 2\cdot 4 = 11.
$$

 

$$
\|\mathbf{u}\| = \sqrt{1^2 + 2^2} = \sqrt{5}, \quad \|\mathbf{v}\| = \sqrt{3^2 + 4^2} = 5.
$$

So,

所以，

$$
\cos \theta = \frac{11}{\sqrt{5}\cdot 5}.
$$

Example 7.1.2. In the function space $C[0,1]$, the inner product

例 7.1.2。 在函数空间 $C[0,1]$ 中，内积

$$
\langle f, g \rangle = \int_0^1 f(x) g(x)\, dx
$$

defines a length

定义长度

$$
\|f\| = \sqrt{\int_0^1 f(x)^2 dx}.
$$

This generalizes geometry to infinite-dimensional spaces.

这将几何学推广到无限维空间。

### Geometric Interpretation
几何解释

*   Inner product: measures similarity between vectors.

    内积：测量向量之间的相似性。
*   Norm: length of a vector.

    范数：向量的长度。
*   Angle: measure of alignment between two directions.

    角度：两个方向之间的对齐度量。

These concepts unify algebraic operations with geometric intuition.

这些概念将代数运算与几何直觉统一起来。

### Why this matters
为什么这很重要

Inner products and norms allow us to extend geometry into abstract vector spaces. They form the basis of orthogonality, projections, Fourier series, least squares approximation, and many applications in physics and machine learning.

内积和范数使我们能够将几何扩展到抽象向量空间。它们构成了正交性、投影、傅里叶级数、最小二乘近似以及物理学和机器学习中许多应用的基础。

### Exercises 7.1
练习 7.1

1.  Compute $\langle (2,-1,3), (1,4,0) \rangle$. Then find the angle between them.

    计算 $\langle (2,-1,3), (1,4,0) \rangle$ 。然后求出它们之间的角度。
    
2.  Show that $\|(x,y)\| = \sqrt{x^2+y^2}$ satisfies the properties of a norm.

    证明$\|(x,y)\| = \sqrt{x^2+y^2}$​ 满足范数的性质。
    
3.  In $\mathbb{R}^3$, verify that $(1,1,0)$ and $(1,-1,0)$ are orthogonal.

    在 $\mathbb{R}^3$ 中，验证 $(1,1,0)$ 和 $(1,-1,0)$ 是否正交。
    
4.  In $C[0,1]$, compute $\langle f,g \rangle$ for $f(x)=x$, $g(x)=1$.

    在 $C[0,1]$ 中，计算 $f(x)=x$ 、 $g(x)=1$ 的 $\langle f,g \rangle$ 。
    
5.  Prove the Cauchy–Schwarz inequality:

    证明柯西-施瓦茨不等式：
    
    $$
    |\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\| \, \|\mathbf{v}\|.
    $$
    

## 7.2 Orthogonal Projections

7.2 正交投影

One of the most useful applications of inner products is the notion of orthogonal projection. Projection allows us to approximate a vector by another lying in a subspace, minimizing error in the sense of distance. This idea underpins geometry, statistics, and numerical analysis.

内积最有用的应用之一是正交投影的概念。投影使我们能够用子空间中的另一个向量来近似一个向量，从而最小化距离方向上的误差。这一思想是几何、统计学和数值分析的基础。

### Projection onto a Line

投影到线上

Let $\mathbf{u} \in \mathbb{R}^n$ be a nonzero vector. The line spanned by $\mathbf{u}$ is

令 $\mathbf{u} \in \mathbb{R}^n$ 为非零向量。 $\mathbf{u}$ 所张成的直线为

$$
L = \{ c\mathbf{u} \mid c \in \mathbb{R} \}.
$$

Given a vector $\mathbf{v}$, the projection of $\mathbf{v}$ onto $\mathbf{u}$ is the vector in $L$ closest to $\mathbf{v}$. Geometrically, it is the shadow of $\mathbf{v}$ on the line.

给定向量 $\mathbf{v}$ ， $\mathbf{v}$ 在 $\mathbf{u}$ 上的投影是 $L$ 中距离 $\mathbf{v}$ 最近的向量。从几何学上讲，它是 $\mathbf{v}$ 在线上的阴影。

The formula is

公式是

$$
\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \, \mathbf{u}.
$$

The error vector $\mathbf{v} - \text{proj}_{\mathbf{u}}(\mathbf{v})$ is orthogonal to $\mathbf{u}$.

误差向量 $\mathbf{v} - \text{proj}_{\mathbf{u}}(\mathbf{v})$ 与 $\mathbf{u}$ 正交。

### Example 7.2.1
例 7.2.1

Let $\mathbf{u} = (1,2)$, $\mathbf{v} = (3,1)$.

令 $\mathbf{u} = (1,2)$ ， $\mathbf{v} = (3,1)$ 。

$$
\langle \mathbf{v}, \mathbf{u} \rangle = 3\cdot 1 + 1\cdot 2 = 5, \quad\langle \mathbf{u}, \mathbf{u} \rangle = 1^2 + 2^2 = 5.
$$

So

所以

$$
\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{5}{5}(1,2) = (1,2).
$$

The error vector is $(3,1) - (1,2) = (2,-1)$, which is orthogonal to $(1,2)$.

误差向量为 $(3,1) - (1,2) = (2,-1)$ ，与 $(1,2)$ 正交。

### Projection onto a Subspace

投影到子空间

Suppose $W \subseteq \mathbb{R}^n$ is a subspace with orthonormal basis $\{ \mathbf{w}_1, \dots, \mathbf{w}_k \}$. The projection of a vector $\mathbf{v}$ onto $W$ is

假设 $W \subseteq \mathbb{R}^n$ 是一个具有正交基 $\{ \mathbf{w}_1, \dots, \mathbf{w}_k \}$ 的子空间。向量 $\mathbf{v}$ 在 $W$ 上的投影为

$$
\text{proj}_{W}(\mathbf{v}) = \langle \mathbf{v}, \mathbf{w}_1 \rangle \mathbf{w}_1 + \cdots + \langle \mathbf{v}, \mathbf{w}_k \rangle \mathbf{w}_k.
$$

This is the unique vector in $W$ closest to $\mathbf{v}$. The difference $\mathbf{v} - \text{proj}_{W}(\mathbf{v})$ is orthogonal to all of $W$.

这是 $W$ 中与 $\mathbf{v}$ 最接近的唯一向量。差值 $\mathbf{v} - \text{proj}_{W}(\mathbf{v})$ 与所有 $W$ 正交。

### Least Squares Approximation

最小二乘近似

Orthogonal projection explains the method of least squares. To solve an overdetermined system $A\mathbf{x} \approx \mathbf{b}$, we seek the $\mathbf{x}$ that makes $A\mathbf{x}$ the projection of $\mathbf{b}$ onto the column space of $A$. This gives the normal equations

正交投影解释了最小二乘法。为了解决超定问题 系统 $A\mathbf{x} \approx \mathbf{b}$ ，我们寻找 $\mathbf{x}$ ，使得 $A\mathbf{x}$ 成为 $\mathbf{b}$ 在 $A$ 的列空间上的投影。这给出了正则方程

$$
A^T A \mathbf{x} = A^T \mathbf{b}.
$$

Thus, least squares is just projection in disguise.

因此，最小二乘法只是伪装的投影。

### Geometric Interpretation

几何解释

*   Projection finds the closest point in a subspace to a given vector.

    投影找到子空间中距离给定向量最近的点。

*   It minimizes distance (error) in the sense of Euclidean norm.

    它按照欧几里得范数的意义最小化距离（误差）。
*   Orthogonality ensures the error vector points directly away from the subspace.

    正交性确保误差向量直接指向远离子空间的方向。

### Why this matters

为什么这很重要

Orthogonal projection is central in both pure and applied mathematics. It underlies the geometry of subspaces, the theory of Fourier series, regression in statistics, and approximation methods in numerical linear algebra. Whenever we fit data with a simpler model, projection is at work.

正交投影在纯数学和应用数学中都至关重要。它是子空间几何、傅里叶级数理论、统计学中的回归以及数值线性代数中的近似方法的基础。每当我们用更简单的模型拟合数据时，投影就会发挥作用。

### Exercises 7.2
练习 7.2

1.  Compute the projection of $(2,3)$ onto the vector $(1,1)$.

    计算 $(2,3)$ 到向量 $(1,1)$ 的投影。
2.  Show that $\mathbf{v} - \text{proj}_{\mathbf{u}}(\mathbf{v})$ is orthogonal to $\mathbf{u}$.

    证明 $\mathbf{v} - \text{proj}_{\mathbf{u}}(\mathbf{v})$ 与 $\mathbf{u}$ 正交。
3.  Let $W = \text{span}\{(1,0,0), (0,1,0)\} \subseteq \mathbb{R}^3$. Find the projection of $(1,2,3)$ onto $W$.

    令 $W = \text{span}\{(1,0,0), (0,1,0)\} \subseteq \mathbb{R}^3$ 。求 $(1,2,3)$ 到 $W$ 的投影。
4.  Explain why least squares fitting corresponds to projection onto the column space of $A$.

    解释为什么最小二乘拟合对应于 $A$ 的列空间上的投影。
5.  Prove that projection onto a subspace $W$ is unique: there is exactly one closest vector in $W$ to a given $\mathbf{v}$.

    证明投影到子空间 $W$ 是唯一的：在 $W$ 中，有且仅有一个与给定 $\mathbf{v}$ 最接近的向量。

## 7.3 Gram–Schmidt Process

7.3 格拉姆-施密特过程

The Gram–Schmidt process is a systematic way to turn any linearly independent set of vectors into an orthonormal basis. This is especially useful because orthonormal bases simplify computations: inner products become simple coordinate comparisons, and projections take clean forms.

格拉姆-施密特过程是一种将任意线性无关的向量集转化为正交基的系统方法。这种方法尤其有用，因为正交基可以简化计算：内积变成了简单的坐标比较，并且投影呈现出清晰的形式。

### The Idea
理念

Given a linearly independent set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}$ in an inner product space, we want to construct an orthonormal set $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ that spans the same subspace.

给定内积空间中一组线性无关的向量 $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}$ ，我们想要构建一个张成同一子空间的正交集 $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ 。

We proceed step by step:
我们一步步来：

1.  Start with $\mathbf{v}_1$, normalize it to get $\mathbf{u}_1$.

    从 $\mathbf{v}_1$ 开始，将其标准化得到$\mathbf{u}_1$​ .
2.  Subtract from $\mathbf{v}_2$ its projection onto $\mathbf{u}_1$, leaving a vector orthogonal to $\mathbf{u}_1$. Normalize to get $\mathbf{u}_2$.

    从 $\mathbf{v}_2$ 中减去它在$\mathbf{u}_1$上的投影，留下一个与 $\mathbf{u}_1$ 正交的向量，标准化得到 $\mathbf{u}_2$​ .
3.  For each $\mathbf{v}_k$, subtract projections onto all previously constructed $\mathbf{u}_1, \dots, \mathbf{u}_{k-1}$, then normalize.

    对于每个$\mathbf{v}_k$ ​ ，减去所有先前构建的𝑢上的投影 $\mathbf{u}_1, \dots, \mathbf{u}_{k-1}$ ​ ，然后标准化。

### The Algorithm

算法

For $k = 1, 2, \dots, n$:

对于 $k = 1, 2, \dots, n$ ：

$$
\mathbf{w}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \langle \mathbf{v}_k, \mathbf{u}_j \rangle \mathbf{u}_j,
$$

 

$$
\mathbf{u}_k = \frac{\mathbf{w}_k}{\|\mathbf{w}_k\|}.
$$

The result $\{\mathbf{u}_1, \dots, \mathbf{u}_n\}$ is an orthonormal basis of the span of the original vectors.

结果 $\{\mathbf{u}_1, \dots, \mathbf{u}_n\}$ 是原始向量跨度的正交基。

### Example 7.3.1

例 7.3.1

Take $\mathbf{v}_1 = (1,1,0), \ \mathbf{v}_2 = (1,0,1), \ \mathbf{v}_3 = (0,1,1)$ in $\mathbb{R}^3$.

在 $\mathbb{R}^3$ 中 $\mathbf{v}_1 = (1,1,0), \ \mathbf{v}_2 = (1,0,1), \ \mathbf{v}_3 = (0,1,1)$ 。

1.  Normalize $\mathbf{v}_1$:

    标准化$\mathbf{v}_1$​ :

$$
\mathbf{u}_1 = \frac{1}{\sqrt{2}}(1,1,0).
$$

2.  Subtract projection of $\mathbf{v}_2$ on $\mathbf{u}_1$:

    减去 $\mathbf{v}_2$ 在$\mathbf{u}_1$ 的投影 :

    $$
    \mathbf{w}_2 = \mathbf{v}_2 - \langle \mathbf{v}_2,\mathbf{u}_1 \rangle \mathbf{u}_1.
    $$

    

    $$
    \langle \mathbf{v}_2,\mathbf{u}_1 \rangle = \frac{1}{\sqrt{2}}(1\cdot 1 + 0\cdot 1 + 1\cdot 0) = \tfrac{1}{\sqrt{2}}.
    $$

    So

    所以

    $$
    \mathbf{w}_2 = (1,0,1) - \tfrac{1}{\sqrt{2}}\cdot \tfrac{1}{\sqrt{2}}(1,1,0)= (1,0,1) - \tfrac{1}{2}(1,1,0)= \left(\tfrac{1}{2}, -\tfrac{1}{2}, 1\right).
    $$

    Normalize:

    规范化：

    $$
    \mathbf{u}_2 = \frac{1}{\sqrt{\tfrac{1}{4}+\tfrac{1}{4}+1}} \left(\tfrac{1}{2}, -\tfrac{1}{2}, 1\right)= \frac{1}{\sqrt{\tfrac{3}{2}}}\left(\tfrac{1}{2}, -\tfrac{1}{2}, 1\right).
    $$

3.  Subtract projections from $\mathbf{v}_3$:

    从$\mathbf{v}_3$中减去投影:

    $$
    \mathbf{w}_3 = \mathbf{v}_3 - \langle \mathbf{v}_3,\mathbf{u}_1 \rangle \mathbf{u}_1 - \langle \mathbf{v}_3,\mathbf{u}_2 \rangle \mathbf{u}_2.
    $$

    After computing, normalize to obtain $\mathbf{u}_3$.

    计算后，归一化得到$\mathbf{u}_3$​ .

    The result is an orthonormal basis of the span of $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3\}$.

    结果是 $\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3\}$ 张成的正交基。

### Geometric Interpretation
几何解释

Gram–Schmidt is like straightening out a set of vectors: you start with the original directions and adjust each new vector to be perpendicular to all previous ones. Then you scale to unit length. The process ensures orthogonality while preserving the span.

格拉姆-施密特变换就像拉直一组向量：从原始方向开始，调整每个新向量使其与所有先前的向量垂直。然后缩放到单位长度。这个过程确保了正交性，同时保留了跨度。

### Why this matters

为什么这很重要

Orthonormal bases simplify inner products, projections, and computations in general. They make coordinate systems easier to work with and are crucial in numerical methods, QR decomposition, Fourier analysis, and statistics (orthogonal polynomials, principal component analysis).

正交基可以简化内积、投影和一般计算。它们使坐标系更易于使用，并且在数值方法、QR 分解、傅里叶分析和统计学（正交多项式、主成分分析）中至关重要。

### Exercises 7.3
练习 7.3

1.  Apply Gram–Schmidt to $(1,0), (1,1)$ in $\mathbb{R}^2$.

    对 $\mathbb{R}^2$ 中的 $(1,0), (1,1)$ 应用 Gram–Schmidt 公式。
2.  Orthogonalize $(1,1,1), (1,0,1)$ in $\mathbb{R}^3$.

    在 $\mathbb{R}^3$ 中对 $(1,1,1), (1,0,1)$ 进行正交化。
3.  Prove that each step of Gram–Schmidt yields a vector orthogonal to all previous ones.

    证明 Gram-Schmidt 的每一步都会产生一个与所有前面的向量正交的向量。
4.  Show that Gram–Schmidt preserves the span of the original vectors.

    证明 Gram–Schmidt 保留了原始向量的跨度。
5.  Explain how Gram–Schmidt leads to the QR decomposition of a matrix.

    解释 Gram-Schmidt 如何导致矩阵的 QR 分解。

## 7.4 Orthonormal Bases
7.4 正交基

An orthonormal basis is a basis of a vector space in which all vectors are both orthogonal to each other and have unit length. Such bases are the most convenient possible coordinate systems: computations involving inner products, projections, and norms become exceptionally simple.

正交基是向量空间中的一种基，其中所有向量彼此正交且具有单位长度。这样的基是最方便的坐标系：涉及内积、投影和范数的计算变得异常简单。

### Definition
定义

A set of vectors $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ in an inner product space $V$ is called an orthonormal basis if

内积空间 $V$ 中的一组向量 $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ 称为正交基，若

1.  $\langle \mathbf{u}_i, \mathbf{u}_j \rangle = 0$ whenever $i \neq j$ (orthogonality),

    $\langle \mathbf{u}_i, \mathbf{u}_j \rangle = 0$ 每当 $i \neq j$ （正交性）
2.  $\|\mathbf{u}_i\| = 1$ for all $i$ (normalization),

    对所有 $i$ 进行 $\|\mathbf{u}_i\| = 1$ （规范化），
3.  The set spans $V$.

    该集合张成 $V$ 。

### Examples
示例

Example 7.4.1. In $\mathbb{R}^2$, the standard basis

例 7.4.1. 在 $\mathbb{R}^2$ 中，标准基础

$$
\mathbf{e}_1 = (1,0), \quad \mathbf{e}_2 = (0,1)
$$

is orthonormal under the dot product.

在点积下是正交的。

Example 7.4.2. In $\mathbb{R}^3$, the standard basis

例 7.4.2. 在 $\mathbb{R}^3$ 中，标准基础

$$
\mathbf{e}_1 = (1,0,0), \quad \mathbf{e}_2 = (0,1,0), \quad \mathbf{e}_3 = (0,0,1)
$$

is orthonormal.

是正交的。

Example 7.4.3. Fourier basis on functions:

例 7.4.3. 函数的傅里叶基：

$$
\{1, \cos x, \sin x, \cos 2x, \sin 2x, \dots\}
$$

is an orthogonal set in the space of square-integrable functions on $[-\pi,\pi]$ with inner product

是 $[-\pi,\pi]$ 上平方可积函数空间中的正交集，具有内积

$$
\langle f,g \rangle = \int_{-\pi}^{\pi} f(x) g(x)\, dx.
$$

After normalization, it becomes an orthonormal basis.

经过归一化之后，它就变成了正交基。

### Properties
特性

1.  Coordinate simplicity: If $\{\mathbf{u}_1,\dots,\mathbf{u}_n\}$ is an orthonormal basis of $V$, then any vector $\mathbf{v}\in V$ has coordinates

    坐标简单性：如果 $\{\mathbf{u}_1,\dots,\mathbf{u}_n\}$ 是 $V$ 的正交基，则任何向量 $\mathbf{v}\in V$ 都有坐标
    
    $$
    [\mathbf{v}] = \begin{bmatrix} \langle \mathbf{v}, \mathbf{u}_1 \rangle \\ \vdots \\ \langle \mathbf{v}, \mathbf{u}_n \rangle \end{bmatrix}.
    $$
    
    That is, coordinates are just inner products.

    也就是说，坐标只是内积。
    
2.  Parseval’s identity: For any $\mathbf{v} \in V$,

    帕塞瓦尔的 identity： 对于任意的 $\mathbf{v} \in V$ ，
    
    $$
    \|\mathbf{v}\|^2 = \sum_{i=1}^n |\langle \mathbf{v}, \mathbf{u}_i \rangle|^2.
    $$
    
3.  Projections: The orthogonal projection onto the span of $\mathbf{u}_1,\dots,\mathbf{u}_k$ is
    
    投影： $ \mathbf{u}_1,\dots,\mathbf{u}_k$ 张成的正交投影​ 是
    
    $$
    \text{proj}(\mathbf{v}) = \sum_{i=1}^k \langle \mathbf{v}, \mathbf{u}_i \rangle \mathbf{u}_i.
    $$
    

### Constructing Orthonormal Bases
构造正交基

*   Start with any linearly independent set, then apply the Gram–Schmidt process to obtain an orthonormal set spanning the same subspace.

    从任意线性无关集开始，然后应用 Gram-Schmidt 过程来获取张成相同子空间的正交集。

*   In practice, orthonormal bases are often chosen for numerical stability and simplicity of computation.

    在实践中，通常选择正交基来实现数值稳定性和计算简单性。

### Geometric Interpretation
几何解释

An orthonormal basis is like a perfectly aligned and equally scaled coordinate system. Distances and angles are computed directly using coordinates without correction factors. They are the ideal rulers of linear algebra.

正交基就像一个完美对齐且等比例缩放的坐标系。距离和角度直接使用坐标计算，无需校正因子。它们是线性代数的理想标尺。

### Why this matters
为什么这很重要

Orthonormal bases simplify every aspect of linear algebra: solving systems, computing projections, expanding functions, diagonalizing symmetric matrices, and working with Fourier series. In data science, principal component analysis produces orthonormal directions capturing maximum variance.

正交基简化了线性代数的各个方面：求解系统、计算投影、展开函数、对角化对称矩阵以及处理傅里叶级数。在数据科学中，主成分分析可以生成正交方向，从而捕捉最大方差。

### Exercises 7.4
练习 7.4

1.  Verify that $(1/\sqrt{2})(1,1)$ and $(1/\sqrt{2})(1,-1)$ form an orthonormal basis of $\mathbb{R}^2$.

    验证 $(1/\sqrt{2})(1,1)$ 和 $(1/\sqrt{2})(1,-1)$ 是否构成 $\mathbb{R}^2$ 的正交基。
2.  Express $(3,4)$ in terms of the orthonormal basis $\{(1/\sqrt{2})(1,1), (1/\sqrt{2})(1,-1)\}$.
    
    用正交基 $\{(1/\sqrt{2})(1,1), (1/\sqrt{2})(1,-1)\}$ 表示 $(3,4)$ 。
3.  Prove Parseval’s identity for $\mathbb{R}^n$ with the dot product.
    
    使用点积证明 $\mathbb{R}^n$ 的帕塞瓦尔恒等式。
4.  Find an orthonormal basis for the plane $x+y+z=0$ in $\mathbb{R}^3$.

    在 $\mathbb{R}^3$ 中找出平面 $x+y+z=0$ 的正交基。
5.  Explain why orthonormal bases are numerically more stable than arbitrary bases in computations.

    解释为什么正交基在计算中比任意基在数值上更稳定。