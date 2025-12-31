# Chapter 4. Vector Spaces
第 4 章 向量空间

## 4.1 Definition of a Vector Space
4.1 向量空间的定义

Up to now we have studied vectors and matrices concretely in $\mathbb{R}^n$. The next step is to move beyond coordinates and define vector spaces in full generality. A vector space is an abstract setting where the familiar rules of addition and scalar multiplication hold, regardless of whether the elements are geometric vectors, polynomials, functions, or other objects.

到目前为止，我们已经在 $\mathbb{R}^n$ 中具体学习了向量和矩阵。下一步是超越坐标，全面定义向量空间。向量空间是一个抽象的场景，其中熟悉的加法和标量乘法规则始终成立，无论元素是几何向量、多项式、函数还是其他对象。

### Formal Definition
正式定义

A vector space over the real numbers $\mathbb{R}$ is a set $V$ equipped with two operations:

实数 $\mathbb{R}$ 上的向量空间是具有两个运算的集合 $V$ ：

1.  Vector addition: For any $\mathbf{u}, \mathbf{v} \in V$, there is a vector $\mathbf{u} + \mathbf{v} \in V$.

    向量加法：对于任何 $\mathbf{u}, \mathbf{v} \in V$ ，都有向量 $\mathbf{u} + \mathbf{v} \in V$ 。
2.  Scalar multiplication: For any scalar $c \in \mathbb{R}$ and any $\mathbf{v} \in V$, there is a vector $c\mathbf{v} \in V$.

    标量乘法：对于任何标量 $c \in \mathbb{R}$ 和任何 $\mathbf{v} \in V$ ，都有一个向量 $c\mathbf{v} \in V$ 。

These operations must satisfy the following axioms (for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and all scalars $a,b \in \mathbb{R}$):

这些运算必须满足以下公理（对于所有 $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ 和所有标量 $a,b \in \mathbb{R}$ ）：

1.  Commutativity of addition: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$.

    加法的交换性： $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ 。
2.  Associativity of addition: $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$.

    加法的结合性： $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ 。
3.  Additive identity: There exists a zero vector $\mathbf{0} \in V$ such that $\mathbf{v} + \mathbf{0} = \mathbf{v}$.

    加法恒等式：存在零向量 $\mathbf{0} \in V$ 使得 $\mathbf{v} + \mathbf{0} = \mathbf{v}$ 。
4.  Additive inverses: For each $\mathbf{v} \in V$, there exists $(-\mathbf{v} \in V$ such that $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$.

    加法逆元：对于每个 $\mathbf{v} \in V$ ，存在 $(-\mathbf{v} \in V$ 使得 $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$ 。
5.  Compatibility of scalar multiplication: $a(b\mathbf{v}) = (ab)\mathbf{v}$.

    标量乘法的兼容性： $a(b\mathbf{v}) = (ab)\mathbf{v}$ 。
6.  Identity element of scalars: 1⋅v\=v.

    标量的单位元： 1⋅v\=v 。
7.  Distributivity over vector addition: $a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$.

    向量加法的分配律： $a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$ 。
8.  Distributivity over scalar addition: $(a+b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$.

    标量加法的分配律： $(a+b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$ 。

If a set $V$ with operations satisfies all eight axioms, we call it a vector space.

如果一个集合 $V$ 满足所有八个公理，我们称它为向量空间。

### Examples
示例

Example 4.1.1. Standard Euclidean space $\mathbb{R}^n$ with ordinary addition and scalar multiplication is a vector space. This is the model case from which the axioms are abstracted.

例 4.1.1. 标准欧几里得空间 $\mathbb{R}^n$ 进行普通的加法和标量乘法运算后，是一个向量空间。这是抽象出公理的典型例子。

Example 4.1.2. Polynomials The set of all polynomials with real coefficients, denoted $\mathbb{R}[x]$, forms a vector space. Addition and scalar multiplication are defined term by term.

例 4.1.2. 多项式 所有实系数多项式的集合，记为 $\mathbb{R}[x]$ ，构成一个向量空间。加法和标量乘法是逐项定义的。

Example 4.1.3. Functions The set of all real-valued functions on an interval, e.g. $f: [0,1] \to \mathbb{R}$, forms a vector space, since functions can be added and scaled pointwise.

例 4.1.3. 函数区间上的所有实值函数的集合，例如 $f: [0,1] \to \mathbb{R}$ ，形成一个向量空间，因为函数可以逐点添加和缩放。


---
### Non-Examples
非示例

Not every set with operations qualifies. For instance, the set of positive real numbers under usual addition is not a vector space, because additive inverses (negative numbers) are missing. The axioms must all hold.

并非所有包含运算的集合都符合条件。例如，通常加法运算下的正实数集不是向量空间，因为缺少加法逆元（负数）。公理必须全部成立。

### Geometric Interpretation
几何解释

In familiar cases like $\mathbb{R}^2$ or $\mathbb{R}^3$, vector spaces provide the stage for geometry: vectors can be added, scaled, and combined to form lines, planes, and higher-dimensional structures. In abstract settings like function spaces, the same algebraic rules let us apply geometric intuition to infinite-dimensional problems.

在像 $\mathbb{R}^2$ 或 $\mathbb{R}^3$ 这样常见的情形下，向量空间为几何学提供了舞台：向量可以相加、缩放和组合，从而形成线、平面和更高维度的结构。在像函数空间这样的抽象环境中，同样的代数规则让我们能够将几何直觉应用于无限维问题。

### Why this matters
为什么这很重要

The concept of vector space unifies seemingly different mathematical objects under a single framework. Whether dealing with forces in physics, signals in engineering, or data in machine learning, the common language of vector spaces allows us to use the same techniques everywhere.

向量空间的概念将看似不同的数学对象统一在一个框架下。无论是处理物理学中的力、工程学中的信号，还是机器学习中的数据，向量空间的通用语言使我们能够在任何地方使用相同的技术。

### Exercises 4.1
练习4.1

1.  Verify that $\mathbb{R}^2$ with standard addition and scalar multiplication satisfies all eight vector space axioms.

    验证 $\mathbb{R}^2$ 通过标准加法和标量乘法满足所有八个向量空间公理。
2.  Show that the set of integers $\mathbb{Z}$ with ordinary operations is not a vector space over $\mathbb{R}$. Which axiom fails?

    证明：具有普通运算的整数集 $\mathbb{Z}$ 不是 $\mathbb{R}$ 上的向量空间。哪条公理不成立？
3.  Consider the set of all polynomials of degree at most 3. Show it forms a vector space over $\mathbb{R}$. What is its dimension?

    考虑所有次数最多为3的多项式的集合。证明它构成一个 $\mathbb{R}$ 上的向量空间。它的维度是多少？
4.  Give an example of a vector space where the vectors are not geometric objects.

    给出一个向量空间的例子，其中的向量不是几何对象。
5.  Prove that in any vector space, the zero vector is unique.

    证明在任何向量空间中，零向量都是唯一的。

## 4.2 Subspaces
4.2 子空间

A subspace is a smaller vector space living inside a larger one. Just as lines and planes naturally sit inside three-dimensional space, subspaces generalize these ideas to higher dimensions and more abstract settings.

子空间是位于较大向量空间中的较小向量空间。正如线和平面自然地存在于三维空间中一样，子空间将这些概念推广到更高维度和更抽象的场景。

### Definition
定义

Let $V$ be a vector space. A subset $W \subseteq V$ is called a subspace of $V$ if:

令 $V$ 为向量空间。若满足以下条件，则子集 $W \subseteq V$ 称为 $V$ 的子空间：

1.  $\mathbf{0} \in W$ (contains the zero vector),

    $\mathbf{0} \in W$ （包含零向量），
2.  For all $\mathbf{u}, \mathbf{v} \in W$, the sum $\mathbf{u} + \mathbf{v} \in W$ (closed under addition),

    对于所有 $\mathbf{u}, \mathbf{v} \in W$ ，总和为 $\mathbf{u} + \mathbf{v} \in W$ （加法封闭），
3.  For all scalars $c \in \mathbb{R}$ and vectors $\mathbf{v} \in W$, the product $c\mathbf{v} \in W$ (closed under scalar multiplication).

    对于所有标量 $c \in \mathbb{R}$ 和向量 $\mathbf{v} \in W$ ，乘积 $c\mathbf{v} \in W$ （在标量乘法下封闭）。

If these hold, then $W$ is itself a vector space with the inherited operations.

如果这些成立，那么 $W$ 本身就是具有继承操作的向量空间。

### Examples
示例

Example 4.2.1. Line through the origin in $\mathbb{R}^2$ The set

例 4.2.1. 穿过 $\mathbb{R}^2$ 中的原点的线 该集合

$$
W = \{ (t, 2t) \mid t \in \mathbb{R} \}
$$

is a subspace of $\mathbb{R}^2$. It contains the zero vector, is closed under addition, and is closed under scalar multiplication.

是 $\mathbb{R}^2$ 的一个子空间。它包含零向量，在加法运算下封闭，在标量乘法运算下封闭。

Example 4.2.2. The x–y plane in $\mathbb{R}^3$ The set

例 4.2.2. $\mathbb{R}^3$ 中的 x-y 平面 该集合

$$
W = \{ (x, y, 0) \mid x,y \in \mathbb{R} \}
$$

is a subspace of $\mathbb{R}^3$. It is the collection of all vectors lying in the plane through the origin parallel to the x–y plane.

是 $\mathbb{R}^3$ 的一个子空间。它是位于通过原点并平行于 x-y 平面的平面内的所有向量的集合。

Example 4.2.3. Null space of a matrix For a matrix $A \in \mathbb{R}^{m \times n}$, the null space

例 4.2.3. 矩阵的零空间 对于矩阵 $A \in \mathbb{R}^{m \times n}$ ，零空间

$$
\{ \mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0} \}
$$

is a subspace of $\mathbb{R}^n$. This subspace represents all solutions to the homogeneous system.

是 $\mathbb{R}^n$ 的一个子空间。该子空间表示齐次系统的所有解。

### Non-Examples
非示例

Not every subset is a subspace.

并非每个子集都是子空间。

*   The set ${ (x,y) \in \mathbb{R}^2 \mid x \geq 0 }$ is not a subspace: it is not closed under scalar multiplication (a negative scalar breaks the condition).

    集合 ${ (x,y) \in \mathbb{R}^2 \mid x \geq 0 }$ 不是子空间：它在标量乘法下不封闭（负标量会破坏该条件）。
*   Any line in $\mathbb{R}^2$ that does not pass through the origin is not a subspace, because it does not contain $\mathbf{0}$.

    $\mathbb{R}^2$ 中任何不经过原点的线都不是子空间，因为它不包含 $\mathbf{0}$ 。

### Geometric Interpretation
几何解释

Subspaces are the linear structures inside vector spaces.

子空间是向量空间内的线性结构。

*   In $\mathbb{R}^2$, the subspaces are: the zero vector, any line through the origin, or the entire plane.

    在 $\mathbb{R}^2$ 中，子空间是：零向量、过原点的任意直线或整个平面。
*   In $\mathbb{R}^3$, the subspaces are: the zero vector, any line through the origin, any plane through the origin, or the entire space.

    在 $\mathbb{R}^3$ 中，子空间是：零向量、过原点的任意直线、过原点的任意平面或整个空间。
*   In higher dimensions, the same principle applies: subspaces are the flat linear pieces through the origin.

    在更高的维度中，同样的原理适用：子空间是通过原点的平坦线性部分。

### Why this matters
为什么这很重要

Subspaces capture the essential structure of linear problems. Column spaces, row spaces, and null spaces are all subspaces. Much of linear algebra consists of understanding how these subspaces intersect, span, and complement each other.

子空间捕捉了线性问题的本质结构。列空间、行空间和零空间都是子空间。线性代数的大部分内容都在于理解这些子空间如何相互交叉、延伸和互补。

### Exercises 4.2
练习 4.2

1.  Prove that the set $W = { (x,0) \mid x \in \mathbb{R} } \subseteq \mathbb{R}^2$ is a subspace.

    证明集合 $W = { (x,0) \mid x \in \mathbb{R} } \subseteq \mathbb{R}^2$ 是一个子空间。
2.  Show that the line ${ (1+t, 2t) \mid t \in \mathbb{R} }$ is not a subspace of $\mathbb{R}^2$. Which condition fails?

    证明行 ${ (1+t, 2t) \mid t \in \mathbb{R} }$ 不是 $\mathbb{R}^2$ 的子空间。哪个条件不成立？
3.  Determine whether the set of all vectors $(x,y,z) \in \mathbb{R}^3$ satisfying $x+y+z=0$ is a subspace.

    确定满足 $x+y+z=0$ 的所有向量 $(x,y,z) \in \mathbb{R}^3$ 的集合是否为子空间。
4.  For the matrix

    对于矩阵

    $$
    A = \begin{bmatrix}1 & 2 & 3 \\4 & 5 & 6\end{bmatrix}
    $$

    Describe the null space of $A$ as a subspace of $\mathbb{R}^3$.

    将 $A$ 的零空间描述为 $\mathbb{R}^3$ 的子空间。

5.  List all possible subspaces of $\mathbb{R}^2$.

    列出 $\mathbb{R}^2$ 所有可能的子空间。

## 4.3 Span, Basis, Dimension
4.3 张成、基、维度

The ideas of span, basis, and dimension provide the language for describing the size and structure of subspaces. Together, they tell us how a vector space is generated, how many building blocks it requires, and how those blocks can be chosen.

张成、基和维数的概念提供了描述子空间大小和结构的语言。它们共同告诉我们向量空间是如何生成的，它需要多少个构建块，以及如何选择这些构建块。

### Span
张成

Given a set of vectors ${\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k} \subseteq V$, the span is the collection of all linear combinations:

给定一组向量 ${\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k} \subseteq V$ ，张成是所有线性组合的集合：

$$
\text{span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\} = \{ c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k \mid c_i \in \mathbb{R} \}.
$$

The span is always a subspace of $V$, namely the smallest subspace containing those vectors.

张成的空间始终是 $V$ 的子空间，即包含这些向量的最小子空间。

Example 4.3.1. In $\mathbb{R}^2$, $ \text{span}{(1,0)} = \{(x,0) \mid x \in \mathbb{R}\},$ the x-axis. Similarly, $\text{span}\{(1,0),(0,1)\} = \mathbb{R}^2.$

例 4.3.1。 在 $\mathbb{R}^2$ 中， $ \text{span}{(1,0)} = \{(x,0) \mid x \in \mathbb{R}\},$ x 轴。同样， $\text{span}\{(1,0),(0,1)\} = \mathbb{R}^2.$

### Basis
基

A basis of a vector space $V$ is a set of vectors that:

向量空间 $V$ 的基是一组向量，其：

1.  Span $V$.

    张成 $V$ 。
2.  Are linearly independent (no vector in the set is a linear combination of the others).

    是线性独立的（集合中没有向量是其他向量的线性组合）。

If either condition fails, the set is not a basis.

如果任一条件不成立，则该集合不作为基。

Example 4.3.2. In $\mathbb{R}^3$, the standard unit vectors

例 4.3.2。 在 $\mathbb{R}^3$ 中，标准单位向量

$$
\mathbf{e}_1 = (1,0,0), \quad \mathbf{e}_2 = (0,1,0), \quad \mathbf{e}_3 = (0,0,1)
$$

form a basis. Every vector $(x,y,z)$ can be uniquely written as

构成基。每个向量 $(x,y,z)$ 都可以唯一地写成

$$
x\mathbf{e}_1 + y\mathbf{e}_2 + z\mathbf{e}_3.
$$

### Dimension
维度

The dimension of a vector space $V$, written $\dim(V)$, is the number of vectors in any basis of $V$. This number is well-defined: all bases of a vector space have the same cardinality.

向量空间 $V$ 的维数，记作 $\dim(V)$ ，是任意 $V$ 的基中向量的数量。这个维数定义明确：向量空间的所有基都具有相同的基数。

Examples 4.3.3.

示例 4.3.3。

*   $\dim(\mathbb{R}^2) = 2$, with basis $(1,0), (0,1)$.

    $\dim(\mathbb{R}^2) = 2$ ，依据是 $(1,0), (0,1)$ 。
*   $\dim(\mathbb{R}^3) = 3$, with basis $(1,0,0), (0,1,0), (0,0,1)$.

    $\dim(\mathbb{R}^3) = 3$ ，依据是 $(1,0,0), (0,1,0), (0,0,1)$ 。
*   The set of polynomials of degree at most 3 has dimension 4, with basis $(1, x, x^2, x^3)$.

    次数最多为 3 的多项式集的维度为 4，基为 $(1, x, x^2, x^3)$ 。

### Geometric Interpretation
几何解释

*   The span is like the reach of a set of vectors.

    张成的空间就像一组向量的范围。
*   A basis is the minimal set of directions needed to reach everything in the space.

    基是到达空间中所有事物所需的最小方向集。
*   The dimension is the count of those independent directions.

    维度是这些独立方向的数量。

Lines, planes, and higher-dimensional flats can all be described in terms of span, basis, and dimension.

线、平面和高维平面都可以用张成、基和维度来描述。

### Why this matters
为什么这很重要

These concepts classify vector spaces and subspaces in terms of size and structure. Many theorems in linear algebra-such as the Rank–Nullity Theorem-are consequences of understanding span, basis, and dimension. In practical terms, bases are how we encode data in coordinates, and dimension tells us how much freedom a system truly has.

这些概念根据大小和结构对向量空间和子空间进行分类。线性代数中的许多定理，例如秩零定理，都是理解张成、基和维数的结果。实际上，基是我们在坐标系中编码数据的方式，而维数则告诉我们一个系统真正拥有多少自由度。

### Exercises 4.3
练习 4.3

1.  Show that $(1,0,0)$, $(0,1,0)$, $(1,1,0)$ span the $xy$\-plane in $\mathbb{R}^3$. Are they a basis?

    证明 $(1,0,0)$ , $(0,1,0)$ , $(1,1,0)$ 在 $\mathbb{R}^3$ 中张成 $xy$ -平面。它们是基吗？
2.  Find a basis for the line $\{(2t,-3t,t) : t \in \mathbb{R}\}$ in $\mathbb{R}^3$.

    找出 $\mathbb{R}^3$ 中直线 $\{(2t,-3t,t) : t \in \mathbb{R}\}$ 的基。
3.  Determine the dimension of the subspace of $\mathbb{R}^3$ defined by $x+y+z=0$.

    确定由 $x+y+z=0$ 定义的 $\mathbb{R}^3$ 子空间的维数。
4.  Prove that any two different bases of $\mathbb{R}^n$ must contain exactly $n$ vectors.

    证明 $\mathbb{R}^n$ 的任意两个不同基必定包含恰好 $n$ 个向量。
5.  Give a basis for the set of polynomials of degree $\leq 2$. What is its dimension?

    给出次数为 $\leq 2$ 的多项式集的基。它的维数是多少？

## 4.4 Coordinates
4.4 坐标

Once a basis for a vector space is chosen, every vector can be expressed uniquely as a linear combination of the basis vectors. The coefficients in this combination are called the coordinates of the vector relative to that basis. Coordinates allow us to move between the abstract world of vector spaces and the concrete world of numbers.

一旦选定了向量空间的基，每个向量都可以唯一地表示为基向量的线性组合。该组合中的系数称为向量相对于该基的坐标。坐标使我们能够在向量空间的抽象世界和具体的数字世界之间移动。

### Coordinates Relative to a Basis
相对于基的坐标

Let $V$ be a vector space, and let

令 $V$ 为向量空间，然后

$$
\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}
$$

be an ordered basis for $V$. Every vector $\mathbf{u} \in V$ can be written uniquely as

是 $V$ 的有序基。每个向量 $\mathbf{u} \in V$ 都可以唯一地写成

$$
\mathbf{u} = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n.
$$

The scalars $(c_1, c_2, \dots, c_n)$ are the coordinates of $\mathbf{u}$ relative to $\mathcal{B}$, written

标量 $(c_1, c_2, \dots, c_n)$ 是 $\mathbf{u}$ 相对于 $\mathcal{B}$ 的坐标，写为

$$
[\mathbf{u}]_{\mathcal{B}} = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}.
$$

### Example in $\mathbb{R}^2$
$\mathbb{R}^2$ 中的示例

Example 4.4.1. Let the basis be

例 4.4.1. 设基为

$$
\mathcal{B} = \{ (1,1), (1,-1) \}.
$$

To find the coordinates of $\mathbf{u} = (3,1)$ relative to $\mathcal{B}$, solve

要找 $\mathbf{u} = (3,1)$ 相对于 $\mathcal{B}$ 的坐标，求解

$$
(3,1) = c_1(1,1) + c_2(1,-1).
$$

This gives the system

得方程组

$$
\begin{cases}c_1 + c_2 = 3, \\c_1 - c_2 = 1.\end{cases}
$$

Adding: $2c_1 = 4 \implies c_1 = 2$. Then $c_2 = 1$.

两式相加：$2c_1 = 4 \implies c_1 = 2 $. 则 $ c_2 = 1$。

So,

所以，

$$
[\mathbf{u}]_{\mathcal{B}} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}.
$$

### Standard Coordinates
标准坐标

In $\mathbb{R}^n$, the standard basis is

在 $\mathbb{R}^n$ 中，标准依据是

$$
\mathbf{e}_1 = (1,0,\dots,0), \quad \mathbf{e}_2 = (0,1,0,\dots,0), \dots, \mathbf{e}_n = (0,\dots,0,1).
$$

Relative to this basis, the coordinates of a vector are simply its entries. Thus, column vectors are coordinate representations by default.

相对于此基，向量的坐标仅仅是它的元素。因此，列向量默认为坐标表示。

### Change of Basis
变基

If $\mathcal{B} = {\mathbf{v}_1, \dots, \mathbf{v}_n}$ is a basis of $\mathbb{R}^n$, the change of basis matrix is

如果 $\mathcal{B} = {\mathbf{v}_1, \dots, \mathbf{v}_n}$  ​ 是 $\mathbb{R}^n$ 的基，基矩阵的变化是

$$
P = \begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \cdots & \mathbf{v}_n \end{bmatrix},
$$

with basis vectors as columns. For any vector $\mathbf{u}$,

以基向量为列。对于任意向量 $\mathbf{u}$ ，

$$
\mathbf{u} = P [\mathbf{u}]_{\mathcal{B}}, \qquad [\mathbf{u}]_{\mathcal{B}} = P^{-1}\mathbf{u}.
$$

Thus, switching between bases reduces to matrix multiplication.

因此，基之间的切换就简化为矩阵乘法。

### Geometric Interpretation
几何解释

Coordinates are the address of a vector relative to a chosen set of directions. Different bases are like different coordinate systems: Cartesian, rotated, skewed, or scaled. The same vector may look very different numerically depending on the basis, but its geometric identity is unchanged.

坐标是向量相对于一组选定方向的地址。不同的基就像不同的坐标系：笛卡尔坐标系、旋转坐标系、倾斜坐标系或缩放坐标系。同一个向量在不同基上可能呈现出截然不同的数值，但其几何恒等式保持不变。

### Why this matters
为什么这很重要

Coordinates turn abstract vectors into concrete numerical data. Changing basis is the algebraic language for rotations of axes, diagonalization of matrices, and principal component analysis in data science. Mastery of coordinates is essential for moving fluidly between geometry, algebra, and computation.

坐标将抽象向量转化为具体的数值数据。变换基是数据科学中轴旋转、矩阵对角化和主成分分析的代数语言。掌握坐标系对于在几何、代数和计算之间流畅切换至关重要。

### Exercises 4.4
练习 4.4

1.  Express $(4,2)$ in terms of the basis $(1,1), (1,-1)$.

    根据基础 $(1,1), (1,-1)$ 表达 $(4,2)$ 。
2.  Find the coordinates of $(1,2,3)$ relative to the standard basis of $\mathbb{R}^3$.

    找出 $(1,2,3)$ 相对于 $\mathbb{R}^3$ 标准基的坐标。
3.  If $\mathcal{B} = \{(2,0), (0,3)\}$, compute $[ (4,6) ]_{\mathcal{B}}$.

    如果 $\mathcal{B} = \{(2,0), (0,3)\}$ ，则计算 $[ (4,6) ]_{\mathcal{B}}$ ​ .
4.  Construct the change of basis matrix from the standard basis of $\mathbb{R}^2$ to $\mathcal{B} = \{(1,1), (1,-1)\}$.

    构建从标准基 $\mathbb{R}^2$ 到 $\mathcal{B} = \{(1,1), (1,-1)\}$ 的基变换矩阵。
5.  Prove that coordinate representation with respect to a basis is unique.

    证明关于基的坐标表示是唯一的。
