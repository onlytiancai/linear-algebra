# Chapter 1. Vectors
第 1 章 向量

## 1.1 Scalars and Vectors
1.1 标量和矢量

A scalar is a single numerical quantity, most often taken from the real numbers, denoted by $\mathbb{R}$. Scalars are the fundamental building blocks of arithmetic: they can be added, subtracted, multiplied, and, except in the case of zero, divided. In linear algebra, scalars play the role of coefficients, scaling factors, and entries of larger structures such as vectors and matrices. They provide the weights by which more complex objects are measured and combined. A vector is an ordered collection of scalars, arranged either in a row or a column. When the scalars are real numbers, the vector is said to belong to *real* $n$\-dimensional space, written


标量是一个单一的数值，通常取自实数，用 $\mathbb{R}$ 表示。标量是算术的基本组成部分：它们可以进行加、减、乘和除（零除外）。在线性代数中，标量充当系数、比例因子以及向量和矩阵等更大结构中的元素。它们提供权重，用于测量和组合更复杂的对象。向量是按行或列排列的标量的有序集合。当标量为实数时，该向量被称为属于*实* $n$ 维空间，写为

$$
\mathbb{R}^n = \{ (x_1, x_2, \dots, x_n) \mid x_i \in \mathbb{R} \}.
$$

An element of $\mathbb{R}^n$ is called a vector of dimension $n$ or an *n*\-vector. The number $n$ is called the dimension of the vector space. Thus $\mathbb{R}^2$ is the space of all ordered pairs of real numbers, $\mathbb{R}^3$ the space of all ordered triples, and so on.

$\mathbb{R}^n$ 中的一个元素称为维度为 $n$ 的向量或 *n* 向量。数字 $n$ 称为向量空间的维数。因此， $\mathbb{R}^2$ 是所有有序实数对的空间， $\mathbb{R}^3$ 是所有有序三元组的空间，等等。

Example 1.1.1.
例 1.1.1。

*   A 2-dimensional vector: $(3, -1) \in \mathbb{R}^2$.

    二维向量： $(3, -1) \in \mathbb{R}^2$ 。
*   A 3-dimensional vector: $(2, 0, 5) \in \mathbb{R}^3$.

    三维向量： $(2, 0, 5) \in \mathbb{R}^3$ 。
*   A 1-dimensional vector: $(7) \in \mathbb{R}^1$, which corresponds to the scalar 7 itself.

    一维向量： $(7) \in \mathbb{R}^1$ ，对应于标量 7 本身。

Vectors are often written vertically in column form, which emphasizes their role in matrix multiplication:

向量通常以列的形式垂直书写，这强调了它们在矩阵乘法中的作用：

$$
\mathbf{v} = \begin{bmatrix}2 \\0 \\5 \end{bmatrix} \in \mathbb{R}^3.
$$

The vertical layout makes the structure clearer when we consider linear combinations or multiply matrices by vectors.

当我们考虑线性组合或矩阵乘以向量时，垂直布局使结构更加清晰。

### Geometric Interpretation
几何解释

In $\mathbb{R}^2$, a vector $(x_1, x_2)$ can be visualized as an arrow starting at the origin $(0,0)$ and ending at the point $(x_1, x_2)$. Its length corresponds to the distance from the origin, and its orientation gives a direction in the plane. In $\mathbb{R}^3$, the same picture extends into three dimensions: a vector is an arrow from the origin to $(x_1, x_2, x_3)$. Beyond three dimensions, direct visualization is no longer possible, but the algebraic rules of vectors remain identical. Even though we cannot draw a vector in $\mathbb{R}^{10}$, it behaves under addition, scaling, and transformation exactly as a 2- or 3-dimensional vector does. This abstract point of view is what allows linear algebra to apply to data science, physics, and machine learning, where data often lives in very high-dimensional spaces. Thus a vector may be regarded in three complementary ways:

在 $\mathbb{R}^2$ 中，向量 $(x_1, x_2)$ 可以可视化为一个从原点 $(0,0)$ 开始到点 $(x_1, x_2)$ 结束的箭头。它的长度对应于与原点的距离，其方向给出了平面内的方向。在 $\mathbb{R}^3$ 中，同样的图像延伸到三维空间：向量是一个从原点指向 $(x_1, x_2, x_3)$ 的箭头。超过三维空间后，直接可视化就不再可能，但向量的代数规则保持不变。即使我们无法在 $\mathbb{R}^{10}$ 中绘制向量，它在加法、缩放和变换下的行为与二维或三维向量完全相同。这种抽象的观点使得线性代数能够应用于数据科学、物理学和机器学习，这些领域的数据通常存在于非​​常高维的空间中。因此，向量可以从三个互补的角度来看待：

1.  As a point in space, described by its coordinates.

    作为空间中的一个点，由其坐标描述。
2.  As a displacement or arrow, described by a direction and a length.

    作为位移或箭头，由方向和长度描述。
3.  As an abstract element of a vector space, whose properties follow algebraic rules independent of geometry.

    作为向量空间的抽象元素，其属性遵循与几何无关的代数规则。

### Notation
符号

*   Vectors are written in boldface lowercase letters: $\mathbf{v}, \mathbf{w}, \mathbf{x}$.

    向量以粗体小写字母表示： $\mathbf{v}, \mathbf{w}, \mathbf{x}$ 。
*   The *i*\-th entry of a vector $\mathbf{v}$ is written $v_i$, where indices begin at 1.

    向量 $\mathbf{v}$ 的第 *i* 个元素写为 $v_i$​ ，其中索引从 1 开始。
*   The set of all *n*\-dimensional vectors over $\mathbb{R}$ is denoted $\mathbb{R}^n$.

    $\mathbb{R}$ 上的所有 *n* 维向量的集合记为 $\mathbb{R}^n$ 。
*   Column vectors will be the default form unless otherwise stated.

    除非另有说明，列向量将是默认形式。

### Why begin here?
为什么从这里开始？

Scalars and vectors form the atoms of linear algebra. Every structure we will build-vector spaces, linear transformations, matrices, eigenvalues-relies on the basic notions of number and ordered collection of numbers. Once vectors are understood, we can define operations such as addition and scalar multiplication, then generalize to subspaces, bases, and coordinate systems. Eventually, this framework grows into the full theory of linear algebra, with powerful applications to geometry, computation, and data.

标量和向量构成了线性代数的原子。我们将要构建的每一个结构——向量空间、线性变换、矩阵、特征值——都依赖于数和有序数集的基本概念。一旦理解了向量，我们就可以定义诸如加法和标量乘法之类的运算，然后推广到子空间、基和坐标系。最终，这个框架将发展成为完整的线性代数理论，并在几何、计算和数据领域拥有强大的应用。

### Exercises 1.1
练习 1.1

1.  Write three different vectors in $\mathbb{R}^2$ and sketch them as arrows from the origin. Identify their coordinates explicitly.

    在 $\mathbb{R}^2$ 中写出三个不同的向量，并将它们画成从原点出发的箭头。明确指出它们的坐标。
2.  Give an example of a vector in $\mathbb{R}^4$. Can you visualize it directly? Explain why high-dimensional visualization is challenging.

    给出 $\mathbb{R}^4$ 中一个向量的例子。你能直接将其可视化吗？解释为什么高维可视化具有挑战性。
3.  Let $\mathbf{v} = (4, -3, 2)$. Write $\mathbf{v}$ in column form and state $v_1, v_2, v_3$.

    令 $\mathbf{v} = (4, -3, 2)$ 。将 $\mathbf{v}$ 写成列形式，并说明 $v_1, v_2, v_3$.
4.  In what sense is the set $\mathbb{R}^1$ both a line and a vector space? Illustrate with examples.

    在什么意义上集合 $\mathbb{R}^1$ 既是线空间又是向量空间？请举例说明。
5.  Consider the vector $\mathbf{u} = (1,1,\dots,1) \in \mathbb{R}^n$. What is special about this vector when $n$ is large? What might it represent in applications?

    考虑向量 $\mathbf{u} = (1,1,\dots,1) \in \mathbb{R}^n$ 。当 $n$ 很大时，这个向量有什么特殊之处？它在应用中可能代表什么？

## 1.2 Vector Addition and Scalar Multiplication
1.2 向量加法和标量乘法

Vectors in linear algebra are not static objects; their power comes from the operations we can perform on them. Two fundamental operations define the structure of vector spaces: addition and scalar multiplication. These operations satisfy simple but far-reaching rules that underpin the entire subject.

线性代数中的向量并非静态对象；它们的力量源于我们可以对它们执行的运算。两个基本运算定义了向量空间的结构：加法和标量乘法。这两个运算满足一些简单却影响深远的规则，这些规则构成了整个线性代数学科的基础。

### Vector Addition
向量加法

Given two vectors of the same dimension, their sum is obtained by adding corresponding entries. Formally, if

给定两个相同维度的向量，它们的和可以通过添加相应的元素来获得。形式上，如果

$$
\mathbf{u} = (u_1, u_2, \dots, u_n), \quad\mathbf{v} = (v_1, v_2, \dots, v_n),
$$

then their sum is

那么它们的总和是

$$
\mathbf{u} + \mathbf{v} = (u_1+v_1, u_2+v_2, \dots, u_n+v_n).
$$

Example 1.2.1. Let $\mathbf{u} = (2, -1, 3)$ and $\mathbf{v} = (4, 0, -5)$. Then

例 1.2.1。 设 $\mathbf{u} = (2, -1, 3)$ 和 $\mathbf{v} = (4, 0, -5)$ 。则

$$
\mathbf{u} + \mathbf{v} = (2+4, -1+0, 3+(-5)) = (6, -1, -2).
$$

Geometrically, vector addition corresponds to the *parallelogram rule*. If we draw both vectors as arrows from the origin, then placing the tail of one vector at the head of the other produces the sum. The diagonal of the parallelogram they form represents the resulting vector.

从几何学上讲，向量加法对应于*平行四边形法则* 。如果我们将两个向量都画成从原点出发的箭头，那么将一个向量的尾部放在另一个向量的头部，就能得到向量的和。它们构成的平行四边形的对角线代表最终的向量。

### Scalar Multiplication
标量乘法

Multiplying a vector by a scalar stretches or shrinks the vector while preserving its direction, unless the scalar is negative, in which case the vector is also reversed. If $c \in \mathbb{R}$ and

将矢量乘以标量会拉伸或收缩矢量，同时保持其方向，除非标量 负数，在这种情况下向量也会反转。如果 $c \in \mathbb{R}$ 和

$$
\mathbf{v} = (v_1, v_2, \dots, v_n),
$$

then

然后

$$
c \mathbf{v} = (c v_1, c v_2, \dots, c v_n).
$$

Example 1.2.2. Let $\mathbf{v} = (3, -2)$ and $c = -2$. Then

例 1.2.2。 设 $\mathbf{v} = (3, -2)$ 和 $c = -2$ 。则

$$
c\mathbf{v} = -2(3, -2) = (-6, 4).
$$

This corresponds to flipping the vector through the origin and doubling its length.

这相当于通过原点翻转向量并使其长度加倍。

### Linear Combinations
线性组合

The interaction of addition and scalar multiplication allows us to form *linear combinations*. A linear combination of vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k$ is any vector of the form

加法和标量乘法的相互作用使我们能够形成 *线性组合* 。向量 $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k$ 的线性组合如下

$$
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k, \quad c_i \in \mathbb{R}.
$$

Linear combinations are the mechanism by which we generate new vectors from existing ones. The span of a set of vectors-the collection of all their linear combinations-will later lead us to the idea of a subspace.

线性组合是一种从现有向量生成新向量的机制。一组向量张成的空间是它们所有线性组合的集合——稍后会引出子空间的概念。

Example 1.2.3. Let $\mathbf{v}_1 = (1,0)$ and $\mathbf{v}_2 = (0,1)$. Then any vector $(a,b)\in\mathbb{R}^2$ can be expressed as

例 1.2.3。 设 $\mathbf{v}_1 = (1,0)$ 和 $\mathbf{v}_2 = (0,1)$ 。则任意向量 $(a,b)\in\mathbb{R}^2$ 可以表示为

$$
a\mathbf{v}_1 + b\mathbf{v}_2.
$$

Thus $(1,0)$ and $(0,1)$ form the basic building blocks of the plane.

因此 $(1,0)$ 和 $(0,1)$ 构成了平面的基本构造块。

### Notation
符号

*   Addition: $\mathbf{u} + \mathbf{v}$ means component-wise addition.

    加法： $\mathbf{u} + \mathbf{v}$ 表示逐个组件的加法。
*   Scalar multiplication: $c\mathbf{v}$ scales each entry of $\mathbf{v}$ by $c$.

    标量乘法： $c\mathbf{v}$ 将 $\mathbf{v}$ 的每个条目乘以 $c$ 。
*   Linear combination: a sum of the form $c_1 \mathbf{v}_1 + \cdots + c_k \mathbf{v}_k$.

    线性组合： $c_1 \mathbf{v}_1 + \cdots + c_k \mathbf{v}_k$ 形式的和 .

### Why this matters
为什么这很重要

Vector addition and scalar multiplication are the defining operations of linear algebra. They give structure to vector spaces, allow us to describe geometric phenomena like translation and scaling, and provide the foundation for solving systems of equations. Everything that follows-basis, dimension, transformations-builds on these simple but profound rules.

向量加法和标量乘法是线性代数的定义运算。它们赋予向量空间结构，使我们能够描述平移和缩放等几何现象，并为方程组的求解奠定基础。之后的一切——基、维度、变换——都建立在这些简单而深刻的规则之上。

### Exercises 1.2
练习 1.2

1.  Compute $\mathbf{u} + \mathbf{v}$ where $\mathbf{u} = (1,2,3)$ and $\mathbf{v} = (4, -1, 0)$.

    计算 $\mathbf{u} + \mathbf{v}$ ，其中 $\mathbf{u} = (1,2,3)$ 和 $\mathbf{v} = (4, -1, 0)$ 。
2.  Find $3\mathbf{v}$ where $\mathbf{v} = (-2,5)$. Sketch both vectors to illustrate the scaling.

    求 $3\mathbf{v} $ 其中 $ \mathbf{v} = (-2,5)$。画出两个向量的示意图，以说明缩放关系。
3.  Show that $(5,7)$ can be written as a linear combination of $(1,0)$ and $(0,1)$.

    证明 $(5,7)$ 可以写成 $(1,0)$ 和 $(0,1)$ 的线性组合。
4.  Write $(4,4)$ as a linear combination of $(1,1)$ and $(1,-1)$.

    将 $(4,4)$ 写为 $(1,1)$ 和 $(1,-1)$ 的线性组合。
5.  Prove that if $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, then $(c+d)(\mathbf{u}+\mathbf{v}) = c\mathbf{u} + c\mathbf{v} + d\mathbf{u} + d\mathbf{v}$ for scalars $c,d \in \mathbb{R}$.

    证明如果 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ ，则对于标量 $c,d \in \mathbb{R}$ 有 $(c+d)(\mathbf{u}+\mathbf{v}) = c\mathbf{u} + c\mathbf{v} + d\mathbf{u} + d\mathbf{v}$ 。

## 1.3 Dot Product, Norms, and Angles
1.3 点积、范数和角

The dot product is the fundamental operation that links algebra and geometry in vector spaces. It allows us to measure lengths, compute angles, and determine orthogonality. From this single definition flow the notions of *norm* and *angle*, which give geometry to abstract vector spaces.

点积是向量空间中连接代数和几何的基本运算。它使我们能够测量长度、计算角度并确定正交性。从这个单一定义中衍生出*范*数和 *角度* ，它为抽象向量空间提供几何形状。

### The Dot Product
点积

For two vectors in $\mathbb{R}^n$, the dot product (also called the inner product) is defined by

对于 $\mathbb{R}^n$ 中的两个向量，点积（也称为内积）定义为

$$
\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n.
$$

Equivalently, in matrix notation:

等效地，用矩阵表示法表示：

$$
\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T \mathbf{v}.
$$

Example 1.3.1. Let $\mathbf{u} = (2, -1, 3)$ and $\mathbf{v} = (4, 0, -2)$. Then

例 1.3.1。 设 $\mathbf{u} = (2, -1, 3)$ 和 $\mathbf{v} = (4, 0, -2)$ 。则

$$
\mathbf{u} \cdot \mathbf{v} = 2\cdot 4 + (-1)\cdot 0 + 3\cdot (-2) = 8 - 6 = 2.
$$

The dot product outputs a single scalar, not another vector.

点积输出单个标量，而不是另一个向量。

### Norms (Length of a Vector)
范数（向量的长度）

The *Euclidean norm* of a vector is the square root of its dot product with itself:

向量的*欧几里得范数*是其与自身的点积的平方根：

$$
\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}.
$$

This generalizes the Pythagorean theorem to arbitrary dimensions.

这将勾股定理推广到任意维度。

Example 1.3.2. For $\mathbf{v} = (3, 4)$,

例 1.3.2。 对于 $\mathbf{v} = (3, 4)$ ，

$$
\|\mathbf{v}\| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5.
$$

This is exactly the length of the vector as an arrow in the plane.

这正是平面中箭头所指的矢量的长度。

### Angles Between Vectors
向量之间的角度

The dot product also encodes the angle between two vectors. For nonzero vectors $\mathbf{u}, \mathbf{v}$,

点积也编码了两个向量之间的角度。对于非零向量 $\mathbf{u}, \mathbf{v}$ ，

$$
\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \, \|\mathbf{v}\| \cos \theta,
$$

where $\theta$ is the angle between them. Thus,

其中 $\theta$ 是它们之间的角度。因此，

$$
\cos \theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}.
$$

Example 1.3.3. Let $\mathbf{u} = (1,0)$ and $\mathbf{v} = (0,1)$. Then

例 1.3.3。 设 $\mathbf{u} = (1,0)$ 和 $\mathbf{v} = (0,1)$ 。则

$$
\mathbf{u} \cdot \mathbf{v} = 0, \quad \|\mathbf{u}\| = 1, \quad \|\mathbf{v}\| = 1.
$$

Hence

因此

$$
\cos \theta = \frac{0}{1\cdot 1} = 0 \quad \Rightarrow \quad \theta = \frac{\pi}{2}.
$$

The vectors are perpendicular.

这些向量是垂直的。

### Orthogonality
正交性

Two vectors are said to be orthogonal if their dot product is zero:

如果两个向量的点积为零，则称它们正交：

$$
\mathbf{u} \cdot \mathbf{v} = 0.
$$

Orthogonality generalizes the idea of perpendicularity from geometry to higher dimensions.

正交性将垂直性的概念从几何学推广到更高维度。

### Notation
符号

*   Dot product: $\mathbf{u} \cdot \mathbf{v}$.

    点积： $\mathbf{u} \cdot \mathbf{v}$ 。
*   Norm (length): $|\mathbf{v}|$.

    范数（长度）： $|\mathbf{v}|$ 。
*   Orthogonality: $\mathbf{u} \perp \mathbf{v}$ if $\mathbf{u} \cdot \mathbf{v} = 0$.

    正交性：如果为 $\mathbf{u} \cdot \mathbf{v} = 0$ ，则为 $\mathbf{u} \perp \mathbf{v}$ 。

### Why this matters
为什么这很重要

The dot product turns vector spaces into geometric objects: vectors gain lengths, angles, and notions of perpendicularity. This foundation will later support the study of orthogonal projections, Gram–Schmidt orthogonalization, eigenvectors, and least squares problems.

点积将向量空间转化为几何对象：向量获得长度、角度和垂直度的概念。这一基础将为后续的正交投影、格拉姆-施密特正交化、特征向量和最小二乘问题的研究奠定基础。

### Exercises 1.3
练习 1.3

1.  Compute $\mathbf{u} \cdot \mathbf{v}$ for $\mathbf{u} = (1,2,3)$, $\mathbf{v} = (4,5,6)$.

    计算 $\mathbf{u} = (1,2,3)$ 、 $\mathbf{v} = (4,5,6)$ 的 $\mathbf{u} \cdot \mathbf{v}$ 。
2.  Find the norm of $\mathbf{v} = (2, -2, 1)$.

    求出 $\mathbf{v} = (2, -2, 1)$ 的范数。
3.  Determine whether $\mathbf{u} = (1,1,0)$ and $\mathbf{v} = (1,-1,2)$ are orthogonal.

    确定 $\mathbf{u} = (1,1,0)$ 和 $\mathbf{v} = (1,-1,2)$ 是否正交。
4.  Let $\mathbf{u} = (3,4)$, $\mathbf{v} = (4,3)$. Compute the angle between them.

    令 $\mathbf{u} = (3,4)$ , $\mathbf{v} = (4,3)$ 。计算它们之间的角度。
5.  Prove that $|\mathbf{u} + \mathbf{v}|^2 = |\mathbf{u}|^2 + |\mathbf{v}|^2 + 2\mathbf{u}\cdot \mathbf{v}$. This identity is the algebraic version of the Law of Cosines.

    证明 $|\mathbf{u} + \mathbf{v}|^2 = |\mathbf{u}|^2 + |\mathbf{v}|^2 + 2\mathbf{u}\cdot \mathbf{v}$ 。这个恒等式是余弦定理的代数形式。

## 1.4 Orthogonality
1.4 正交性

Orthogonality captures the notion of perpendicularity in vector spaces. It is one of the most important geometric ideas in linear algebra, allowing us to decompose vectors, define projections, and construct special bases with elegant properties.

正交性捕捉了向量空间中垂直性的概念。它是线性代数中最重要的几何概念之一，它使我们能够分解向量、定义投影，并构造具有优雅性质的特殊基。

### Definition
定义

Two vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ are said to be orthogonal if their dot product is zero:

如果两个向量 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ 的点积为零，则称它们正交：

$$
\mathbf{u} \cdot \mathbf{v} = 0.
$$

This condition ensures that the angle between them is $\pi/2$ radians (90 degrees).

此条件确保它们之间的角度为 $\pi/2$ 弧度（90 度）。

Example 1.4.1. In $\mathbb{R}^2$, the vectors $(1,2)$ and $(2,-1)$ are orthogonal since

例 1.4.1。 在 $\mathbb{R}^2$ 中，向量 $(1,2)$ 和 $(2,-1)$ 是正交的，因为

$$
(1,2) \cdot (2,-1) = 1\cdot 2 + 2\cdot (-1) = 0.
$$

### Orthogonal Sets
正交集

A collection of vectors is called orthogonal if every distinct pair of vectors in the set is orthogonal. If, in addition, each vector has norm 1, the set is called orthonormal.

如果一组向量中每对不同的向量都是正交的，则称该集合为正交向量。此外，如果每个向量的范数均为 1，则该集合称为标准正交向量集。

Example 1.4.2. In $\mathbb{R}^3$, the standard basis vectors

例 1.4.2。 在 $\mathbb{R}^3$ 中，标准基向量

$$
\mathbf{e}_1 = (1,0,0), \quad \mathbf{e}_2 = (0,1,0), \quad \mathbf{e}_3 = (0,0,1)
$$

form an orthonormal set: each has length 1, and their dot products vanish when the indices differ.

形成一个正交集：每个集的长度为 1，并且当索引不同时，它们的点积消失。

### Projections
投影

Orthogonality makes possible the decomposition of a vector into two components: one parallel to another vector, and one orthogonal to it. Given a nonzero vector $\mathbf{u}$ and any vector $\mathbf{v}$, the projection of $\mathbf{v}$ onto $\mathbf{u}$ is

正交性使得将一个向量分解为两个分量成为可能：一个与另一个向量平行，另一个 与其正交。给定一个非零向量 $\mathbf{u}$ 和任意向量 $\mathbf{v}$ ，则 $\mathbf{v}$ 的投影 到 $\mathbf{u}$ 是

$$
\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{u} \cdot \mathbf{u}} \mathbf{u}.
$$

The difference

差

$$
\mathbf{v} - \text{proj}_{\mathbf{u}}(\mathbf{v})
$$

is orthogonal to $\mathbf{u}$. Thus every vector can be decomposed uniquely into a parallel and perpendicular part with respect to another vector.

与 $\mathbf{u}$ 正交。因此，每个向量都可以唯一地分解为相对于另一个向量平行和垂直的部分。

Example 1.4.3. Let $\mathbf{u} = (1,0)$, $\mathbf{v} = (2,3)$. Then

例 1.4.3。 令 $\mathbf{u} = (1,0)$ ， $\mathbf{v} = (2,3)$ 。然后

$$
\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{(1,0)\cdot(2,3)}{(1,0)\cdot(1,0)} (1,0)= \frac{2}{1}(1,0) = (2,0).
$$

Thus
因此

$$
\mathbf{v} = (2,3) = (2,0) + (0,3),
$$

where $(2,0)$ is parallel to $(1,0)$ and $(0,3)$ is orthogonal to it.

其中 $(2,0)$ 与 $(1,0)$ 平行， $(0,3)$ 与 $(1,0)$ 正交。

### Orthogonal Decomposition
正交分解

In general, if $\mathbf{u} \neq \mathbf{0}$ and $\mathbf{v} \in \mathbb{R}^n$, then

一般来说，如果 $\mathbf{u} \neq \mathbf{0}$ 和 $\mathbf{v} \in \mathbb{R}^n$ ，那么

$$
\mathbf{v} = \text{proj}\_{\mathbf{u}}(\mathbf{v}) + \big(\mathbf{v} - \text{proj}\_{\mathbf{u}}(\mathbf{v})\big),
$$

where the first term is parallel to $\mathbf{u}$ and the second term is orthogonal. This decomposition underlies methods such as least squares approximation and the Gram–Schmidt process.

其中第一项平行于 $\mathbf{u}$ ，第二项正交。这种分解是最小二乘近似和格拉姆-施密特过程等方法的基础。

### Notation
符号

*   $\mathbf{u} \perp \mathbf{v}$: vectors $\mathbf{u}$ and $\mathbf{v}$ are orthogonal.

    $\mathbf{u} \perp \mathbf{v}$ ：向量 $\mathbf{u}$ 和 $\mathbf{v}$ 正交。
*   An orthogonal set: vectors pairwise orthogonal.

    正交集：向量两两正交。
*   An orthonormal set: pairwise orthogonal, each of norm 1.

    标准正交集：两两正交，每组范数为 1。

### Why this matters
为什么这很重要

Orthogonality gives structure to vector spaces. It provides a way to separate independent directions cleanly, simplify computations, and minimize errors in approximations. Many powerful algorithms in numerical linear algebra and data science (QR decomposition, least squares regression, PCA) rely on orthogonality.

正交性赋予向量空间结构。它提供了一种清晰地分离独立方向、简化计算并最小化近似误差的方法。数值线性代数和数据科学中许多强大的算法（例如 QR 分解、最小二乘回归、主成分分析）都依赖于正交性。

### Exercises 1.4
练习 1.4

1.  Verify that the vectors $(1,2,2)$ and $(2,0,-1)$ are orthogonal.

    验证向量 $(1,2,2)$ 和 $(2,0,-1)$ 是否正交。
2.  Find the projection of $(3,4)$ onto $(1,1)$.

    找到 $(3,4)$ 到 $(1,1)$ 的投影。
3.  Show that any two distinct standard basis vectors in $\mathbb{R}^n$ are orthogonal.

    证明 $\mathbb{R}^n$ 中的任意两个不同的标准基向量都是正交的。
4.  Decompose $(5,2)$ into components parallel and orthogonal to $(2,1)$.

    将 $(5,2)$ 分解为与 $(2,1)$ 平行且正交的分量。
5.  Let $\mathbf{u}, \mathbf{v}$ be orthogonal nonzero vectors. (a) Show that $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})=\lVert \mathbf{u}\rVert^2-\lVert \mathbf{v}\rVert^2.$ (b) For what condition on $\mathbf{u}$ and $\mathbf{v}$ does $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})=0$?

    令 $\mathbf{u}, \mathbf{v}$ 为正交非零向量。
    
    （a）证明 $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})=\lVert \mathbf{u}\rVert^2-\lVert \mathbf{v}\rVert^2.$ 
    
    （b） $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})=0$ 对 $\mathbf{u}$ 和 $\mathbf{v}$ 满足什么条件？