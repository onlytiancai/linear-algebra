# Chapter 5. Linear Transformations
第 5 章线性变换

## 5.1 Functions that Preserve Linearity
5.1 保持线性的函数

A central theme of linear algebra is understanding linear transformations: functions between vector spaces that preserve their algebraic structure. These transformations generalize the idea of matrix multiplication and capture the essence of linear behavior.

线性代数的核心主题是理解线性变换：向量空间之间保持其代数结构的函数。这些变换推广了矩阵乘法的概念，并抓住了线性行为的本质。

### Definition
定义

Let $V$ and $W$ be vector spaces over $\mathbb{R}$. A function

令 $V$ 和 $W$ 为 $\mathbb{R}$ 上的向量空间。函数

$$
T : V \to W
$$

is called a linear transformation (or linear map) if for all vectors $\mathbf{u}, \mathbf{v} \in V$ and all scalars $c \in \mathbb{R}$:

如果对于所有向量 $\mathbf{u}, \mathbf{v} \in V$ 和所有标量 $c \in \mathbb{R}$ ，则称为线性变换（或线性映射）：

1.  Additivity:

    可加性：

$$
T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}),
$$

2.  Homogeneity:

    齐次性：

$$
T(c\mathbf{u}) = cT(\mathbf{u}).
$$

If both conditions hold, then $T$ automatically respects linear combinations:

如果两个条件都成立，则 $T$ 自动遵循线性组合：

$$
T(c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k) = c_1 T(\mathbf{v}_1) + \cdots + c_k T(\mathbf{v}_k).
$$

### Examples
示例

Example 5.1.1. Scaling in $\mathbb{R}^2$. Let $T:\mathbb{R}^2 \to \mathbb{R}^2$ be defined by

例 5.1.1. 缩放 $\mathbb{R}^2$ 。令 $T:\mathbb{R}^2 \to \mathbb{R}^2$ 定义为

$$
T(x,y) = (2x, 2y).
$$

This doubles the length of every vector, preserving direction. It is linear.

这会使每个向量的长度加倍，同时保持方向不变。它是线性的。

Example 5.1.2. Rotation.
例 5.1.2. 旋转。

Let $R_\theta: \mathbb{R}^2 \to \mathbb{R}^2$ be

令 $R_\theta: \mathbb{R}^2 \to \mathbb{R}^2$ 为

$$
R_\theta(x,y) = (x\cos\theta - y\sin\theta, \; x\sin\theta + y\cos\theta).
$$

This rotates vectors by angle $\theta$. It satisfies additivity and homogeneity, hence is linear.

这将向量旋转角度 $\theta$ 。它满足可加性和齐次性，因此是线性的。

Example 5.1.3. Differentiation.

例 5.1.3. 区分。

Let $D: \mathbb{R}[x] \to \mathbb{R}[x]$ be differentiation: $D(p(x)) = p'(x)$.

令 $D: \mathbb{R}[x] \to \mathbb{R}[x]$ 为微分： $D(p(x)) = p'(x)$ 。

Since derivatives respect addition and scalar multiples, differentiation is a linear transformation.

由于导数尊重加法和标量倍数，因此微分是一种线性变换。

### Non-Example
非示例

The map $S:\mathbb{R}^2 \to \mathbb{R}^2$ defined by

映射 $S:\mathbb{R}^2 \to \mathbb{R}^2$ 定义为

$$
S(x,y) = (x^2, y^2)
$$

is not linear, because $S(\mathbf{u} + \mathbf{v}) \neq S(\mathbf{u}) + S(\mathbf{v})$ in general.

不是线性的，因为一般来说 $S(\mathbf{u} + \mathbf{v}) \neq S(\mathbf{u}) + S(\mathbf{v})$ 。

### Geometric Interpretation
几何解释

Linear transformations are exactly those that preserve the origin, lines through the origin, and proportions along those lines. They include familiar operations: scaling, rotations, reflections, shears, and projections. Nonlinear transformations bend or curve space, breaking these properties.

线性变换正是那些保留原点、过原点的直线以及沿这些直线的比例的变换。它们包括我们熟悉的操作：缩放、旋转、反射、剪切和投影。非线性变换会弯曲空间，从而破坏这些属性。

### Why this matters
为什么这很重要

Linear transformations unify geometry, algebra, and computation. They explain how matrices act on vectors, how data can be rotated or projected, and how systems evolve under linear rules. Much of linear algebra is devoted to understanding these transformations, their representations, and their invariants.

线性变换统一了几何、代数和计算。它解释了矩阵如何作用于向量，数据如何旋转或投影，以及系统如何在线性规则下演化。线性代数的大部分内容致力于理解这些变换、它们的表示及其不变量。

### Exercises 5.1
练习 5.1

1.  Verify that $T(x,y) = (3x-y, 2y)$ is a linear transformation on $\mathbb{R}^2$.

    验证 $T(x,y) = (3x-y, 2y)$ 是否是 $\mathbb{R}^2$ 的线性变换。
2.  Show that $T(x,y) = (x+1, y)$ is not linear. Which axiom fails?

    证明 $T(x,y) = (x+1, y)$ 不是线性的。哪条公理不成立？
3.  Prove that if $T$ and $S$ are linear transformations, then so is $T+S$.

    证明如果 $T$ 和 $S$ 是线性变换，那么 $T+S$ 也是线性变换。
4.  Give an example of a linear transformation from $\mathbb{R}^3$ to $\mathbb{R}^2$.

    给出一个从 $\mathbb{R}^3$ 到 $\mathbb{R}^2$ 的线性变换的例子。
5.  Let $T:\mathbb{R}[x] \to \mathbb{R}[x]$ be integration:

    令 $T:\mathbb{R}[x] \to \mathbb{R}[x]$ 为积分：

$$
T(p(x)) = \int_0^x p(t)\\,dt.
$$

Prove that $T$ is a linear transformation.

证明 $T$ 是线性变换。

## 5.2 Matrix Representation of Linear Maps
5.2 线性映射的矩阵表示

Every linear transformation between finite-dimensional vector spaces can be represented by a matrix. This correspondence is one of the central insights of linear algebra: it lets us use the tools of matrix arithmetic to study abstract transformations.

有限维向量空间之间的所有线性变换都可以用矩阵表示。这种对应关系是线性代数的核心洞见之一：它让我们能够利用矩阵运算工具来研究抽象的变换。

### From Linear Map to Matrix
从线性映射到矩阵

Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation. Choose the standard basis $\{ \mathbf{e}_1, \dots, \mathbf{e}_n \}$ of $\mathbb{R}^n$, where $\mathbf{e}_i$ has a 1 in the $i$\-th position and 0 elsewhere.

令 $T: \mathbb{R}^n \to \mathbb{R}^m$ 为线性变换。选取 $\mathbb{R}^n$ 的标准基 $\{ \mathbf{e}_1, \dots, \mathbf{e}_n \}$ ，其中 $\mathbf{e}_i$  ​ 第 $i$ 个位置为 1，其他地方为 0。

The action of $T$ on each basis vector determines the entire transformation:

$T$ 对每个基向量的作用决定了整个变换：

$$
T(\mathbf{e}\_j) = \begin{bmatrix}a_{1j} \\a_{2j} \\\vdots \\a_{mj} \end{bmatrix}.
$$

Placing these outputs as columns gives the matrix of $T$:

将这些输出作为列放置，得到矩阵 $T$ ：

$$
[T] = A = \begin{bmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\a_{21} & a_{22} & \cdots & a_{2n} \\\vdots & \vdots & \ddots & \vdots \\a_{m1} & a_{m2} & \cdots & a_{mn}\end{bmatrix}.
$$

Then for any vector $\mathbf{x} \in \mathbb{R}^n$:

然后对于任意向量 $\mathbf{x} \in \mathbb{R}^n$ ：

$$
T(\mathbf{x}) = A\mathbf{x}.
$$

### Examples
示例

Example 5.2.1. Scaling in $\mathbb{R}^2$. Let $T(x,y) = (2x, 3y)$. Then

例 5.2.1. 缩放 $\mathbb{R}^2$ 。设 $T(x,y) = (2x, 3y)$ 。然后

$$
T(\mathbf{e}_1) = (2,0), \quad T(\mathbf{e}_2) = (0,3).
$$

So the matrix is

所以矩阵是

$$
[T] = \begin{bmatrix}2 & 0 \\0 & 3\end{bmatrix}.
$$

Example 5.2.2. Rotation in the plane. The rotation transformation $R_\theta(x,y) = (x\cos\theta - y\sin\theta, \; x\sin\theta + y\cos\theta)$ has matrix

例5.2.2. 平面旋转。 旋转变换 $R_\theta(x,y) = (x\cos\theta - y\sin\theta, \; x\sin\theta + y\cos\theta)$ 具有矩阵

$$
[R_\theta] = \begin{bmatrix}\cos\theta & -\sin\theta \\\sin\theta & \cos\theta\end{bmatrix}.
$$

Example 5.2.3. Projection onto the x-axis. The map $P(x,y) = (x,0)$ corresponds to

例 5.2.3. 投影到 x 轴。 映射 $P(x,y) = (x,0)$ 对应于

$$
[P] = \begin{bmatrix}1 & 0 \\0 & 0\end{bmatrix}.
$$

### Change of Basis
基变换

Matrix representations depend on the chosen basis. If $\mathcal{B}$ and $\mathcal{C}$ are bases of $\mathbb{R}^n$ and $\mathbb{R}^m$, then the matrix of $T: \mathbb{R}^n \to \mathbb{R}^m$ with respect to these bases is obtained by expressing $T(\mathbf{v}_j)$ in terms of $\mathcal{C}$ for each $\mathbf{v}_j \in \mathcal{B}$. Changing bases corresponds to conjugating the matrix by the appropriate change-of-basis matrices.

矩阵表示取决于所选的基。如果 $\mathcal{B}$ 和 $\mathcal{C}$ 是 $\mathbb{R}^n$ 和 $\mathbb{R}^m$ 的基  ，则 $T: \mathbb{R}^n \to \mathbb{R}^m$ 关于这些基的矩阵，可以通过将 $T(\mathbf{v}_j)$ 表示为 $\mathcal{C}$ 来获得，其中 $\mathbf{v}_j \in \mathcal{B}$ 表示为 $T(\mathbf{v}_j)$。改变基相当于将矩阵与适当的基变换矩阵共轭。

### Geometric Interpretation
几何解释

Matrices are not just convenient notation-they *are* linear maps once a basis is fixed. Every rotation, reflection, projection, shear, or scaling corresponds to multiplying by a specific matrix. Thus, studying linear transformations reduces to studying their matrices.

矩阵不仅仅是方便的符号——一旦基确定，它们*就是*线性映射。所有旋转、反射、投影、剪切或缩放都对应于乘以一个特定的矩阵。因此，研究线性变换可以归结为研究它们的矩阵。

### Why this matters
为什么这很重要

Matrix representations make linear transformations computable. They connect abstract definitions to explicit calculations, enabling algorithms for solving systems, finding eigenvalues, and performing decompositions. Applications from graphics to machine learning depend on this translation.

矩阵表示使线性变换可计算。它们将抽象定义与明确的计算联系起来，从而支持求解方程组、查找特征值和执行分解的算法。从图形到机器学习等各种应用都依赖于这种转换。

### Exercises 5.2
练习 5.2

1.  Find the matrix representation of $T:\mathbb{R}^2 \to \mathbb{R}^2$, $T(x,y) = (x+y, x-y)$.

    找到 $T:\mathbb{R}^2 \to \mathbb{R}^2$ , $T(x,y) = (x+y, x-y)$ 的矩阵表示。
2.  Determine the matrix of the linear transformation $T:\mathbb{R}^3 \to \mathbb{R}^2$, $T(x,y,z) = (x+z, y-2z)$.

    确定线性变换矩阵 $T:\mathbb{R}^3 \to \mathbb{R}^2$ ， $T(x,y,z) = (x+z, y-2z)$ 。
3.  What matrix represents reflection across the line $y=x$ in $\mathbb{R}^2$?

    哪个矩阵表示 $\mathbb{R}^2$ 中沿线 $y=x$ 的反射？
4.  Show that the matrix of the identity transformation on $\mathbb{R}^n$ is $I_n$.

    证明 $\mathbb{R}^n$ 上的恒等变换矩阵是 $I_n$​ .
5.  For the differentiation map $D:\mathbb{R}_2[x] \to \mathbb{R}_1[x]$, where $\mathbb{R}_k[x]$ is the space of polynomials of degree at most $k$, find the matrix of $D$ relative to the bases $\{1,x,x^2\}$ and $\{1,x\}$.

    对于微分映射 $D:\mathbb{R}_2[x] \to \mathbb{R}_1[x]$ ，其中 $\mathbb{R}_k[x]$ 是次数最多为 $k$ 的多项式空间，求出 $D$ 相对于基数 $\{1,x,x^2\}$ 和 $\{1,x\}$ 的矩阵。

## 5.3 Kernel and Image
5.3 内核和镜像

To understand a linear transformation deeply, we must examine what it kills and what it produces. These ideas are captured by the kernel and the image, two fundamental subspaces associated with any linear map.

要深入理解线性变换，我们必须考察它消除了什么，又产生了什么。这些概念可以通过核和像来理解，它们是任何线性映射都相关的两个基本子空间。

### The Kernel
核

The kernel (or null space) of a linear transformation $T: V \to W$ is the set of all vectors in $V$ that map to the zero vector in $W$:

线性变换 $T: V \to W$ 的核（或零空间）是 $V$ 中映射到 $W$ 中的零向量的所有向量的集合：

$$
\ker(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0} \}.
$$

The kernel is always a subspace of $V$. It measures the degeneracy of the transformation-directions that collapse to nothing.

核始终是 $V$ 的子空间。它衡量的是坍缩为零的变换方向的退化程度。

Example 5.3.1. Let $T:\mathbb{R}^3 \to \mathbb{R}^2$ be defined by

例 5.3.1。 让 $T:\mathbb{R}^3 \to \mathbb{R}^2$ 定义为

$$
T(x,y,z) = (x+y, y+z).
$$

In matrix form,

以矩阵形式，

$$
[T] = \begin{bmatrix}1 & 1 & 0 \\0 & 1 & 1\end{bmatrix}.
$$

To find the kernel, solve

要找到核，请解决

$$
\begin{bmatrix}1 & 1 & 0 \\0 & 1 & 1\end{bmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix}= \begin{bmatrix} 0 \\ 0 \end{bmatrix}.
$$

This gives the equations $x + y = 0$, $y + z = 0$. Hence $x = -y, z = -y$. The kernel is

由此得到方程 $x + y = 0$ ， $y + z = 0$ 。因此 $x = -y, z = -y$ 。核为

$$
\ker(T) = \{ (-t, t, -t) \mid t \in \mathbb{R} \},
$$

a line in $\mathbb{R}^3$.

$\mathbb{R}^3$ 中的一行。

### The Image
像

The image (or range) of a linear transformation $T: V \to W$ is the set of all outputs:

线性变换 $T: V \to W$ 的像（或范围）是所有输出的集合：

$$
\text{im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \} \subseteq W.
$$

Equivalently, it is the span of the columns of the representing matrix. The image is always a subspace of $W$.

等效地，它是表示矩阵的列的跨度。像始终是 $W$ 的子空间。

Example 5.3.2. For the same transformation as above,

例 5.3.2. 对于与上述相同的变换，

$$
[T] = \begin{bmatrix}1 & 1 & 0 \\0 & 1 & 1\end{bmatrix},
$$

the columns are $(1,0)$, $(1,1)$, and $(0,1)$. Since $(1,1) = (1,0) + (0,1)$, the image is

列为 $(1,0)$ 、 $(1,1)$ 和 $(0,1)$ 。由于 $(1,1) = (1,0) + (0,1)$ ，因此像为

$$
\text{im}(T) = \text{span}\{ (1,0), (0,1) \} = \mathbb{R}^2.
$$

### Dimension Formula (Rank–Nullity Theorem)
维度公式（秩-零度定理）

For a linear transformation $T: V \to W$ with $V$ finite-dimensional,

对于线性变换 $T: V \to W$ 且 $V$ 为有限维，

$$
\dim(\ker(T)) + \dim(\text{im}(T)) = \dim(V).
$$

This fundamental result connects the lost directions (kernel) with the achieved directions (image).

这个基本结果将丢失的方向（核）与实现的方向（像）联系起来。

### Geometric Interpretation
几何解释

*   The kernel describes how the transformation flattens space (e.g., projecting a 3D object onto a plane).

    核描述了变换如何使空间变平坦（例如，将 3D 对象投影到平面上）。
*   The image describes the target subspace reached by the transformation.

    图像描述了变换所达到的目标子空间。
*   The rank–nullity theorem quantifies the tradeoff: the more dimensions collapse, the fewer remain in the image.

    秩零定理量化了这种权衡：维度崩溃得越多，图像中剩余的维度就越少。

### Why this matters
为什么这很重要

Kernel and image capture the essence of a linear map. They classify transformations, explain when systems have unique or infinite solutions, and form the backbone of important results like the Rank–Nullity Theorem, diagonalization, and spectral theory.

核和图像捕捉了线性映射的本质。它们对变换进行分类，解释线性方程组何时具有唯一或无限解，并构成秩零定理、对角化和谱理论等重要结果的支柱。

### Exercises 5.3
练习 5.3

1.  Find the kernel and image of $T:\mathbb{R}^2 \to \mathbb{R}^2$, $T(x,y) = (x-y, x+y)$.

    查找 $T:\mathbb{R}^2 \to \mathbb{R}^2$ 、 $T(x,y) = (x-y, x+y)$ 的核和像。
2.  Let
    令

    $$
    A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \end{bmatrix}
    $$

    Find bases for $\ker(A)$ and $\text{im}(A)$. 

    找到 $\ker(A)$ 和 $\text{im}(A)$ 的基。

3. For the projection map $P(x,y,z) = (x,y,0)$, describe the kernel and image. 
   
    对于投影图 $P(x,y,z) = (x,y,0)$ ，描述其核和图像。

4. Prove that $\ker(T)$ and $\text{im}(T)$ are always subspaces. 

    证明 $\ker(T)$ 和 $\text{im}(T)$ 始终是子空间。

5. Verify the Rank–Nullity Theorem for the transformation in Example 5.3.1.

    验证示例5.3.1中变换的秩零性定理。

## 5.4 Change of Basis
5.4 基变换

Linear transformations can look very different depending on the coordinate system we use. The process of rewriting vectors and transformations relative to a new basis is called a change of basis. This concept lies at the heart of diagonalization, orthogonalization, and many computational techniques.

根据我们使用的坐标系，线性变换看起来可能非常不同。相对于新的基重写向量和变换的过程称为基变换。这个概念是对角化、正交化以及许多计算技术的核心。

### Coordinate Change
坐标变换

Suppose $V$ is an $n$\-dimensional vector space, and let $\mathcal{B} = \{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ be a basis. Every vector $\mathbf{x} \in V$ has a coordinate vector $[\mathbf{x}]_{\mathcal{B}} \in \mathbb{R}^n$.

假设 $V$ 是一个 $n$ 维向量空间，设 $\mathcal{B} = \{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ 为基。每个向量 $\mathbf{x} \in V$ 都有一个坐标向量 $[\mathbf{x}]_{\mathcal{B}} \in \mathbb{R}^n$ 。

If $P$ is the change-of-basis matrix from $\mathcal{B}$ to the standard basis, then

如果 $P$ 是从 $\mathcal{B}$ 到标准基的基变换矩阵，则

$$
\mathbf{x} = P [\mathbf{x}]_{\mathcal{B}}.
$$

Equivalently,

等价地，

$$
[\mathbf{x}]_{\mathcal{B}} = P^{-1} \mathbf{x}.
$$

Here, $P$ has the basis vectors of $\mathcal{B}$ as its columns:

这里， $P$ 以 $\mathcal{B}$ 的基向量作为其列：

$$
P = \begin{bmatrix}\mathbf{v}_1 & \mathbf{v}_2 & \cdots & \mathbf{v}_n\end{bmatrix}.
$$

### Transformation of Matrices
矩阵变换

Let $T: V \to V$ be a linear transformation. Suppose its matrix in the standard basis is $A$. In the basis $\mathcal{B}$, the representing matrix becomes

令 $T: V \to V$ 为线性变换。假设其在标准基中的矩阵为 $A$ 。在基 $\mathcal{B}$ 中，表示矩阵变为

$$
[T]_{\mathcal{B}} = P^{-1} A P.
$$

Thus, changing basis corresponds to a similarity transformation of the matrix.

因此，改变基对应于矩阵的相似变换。

### Example
例子

Example 5.4.1. Let $T:\mathbb{R}^2 \to \mathbb{R}^2$ be given by

例 5.4.1。 令 $T:\mathbb{R}^2 \to \mathbb{R}^2$ 为

$$
T(x,y) = (3x + y, x + y).
$$

In the standard basis, its matrix is

在标准基上，其矩阵为

$$
A = \begin{bmatrix}3 & 1 \\1 & 1\end{bmatrix}.
$$

Now consider the basis $\mathcal{B} = \{ (1,1), (1,-1) \}$. The change-of-basis matrix is

现在考虑基 $\mathcal{B} = \{ (1,1), (1,-1) \}$ 。基变换矩阵为

$$
P = \begin{bmatrix}1 & 1 \\1 & -1\end{bmatrix}.
$$

Then

然后

$$
[T]_{\mathcal{B}} = P^{-1} A P.
$$

Computing gives

计算得出

$$
[T]_{\mathcal{B}} =\begin{bmatrix}4 & 0 \\0 & 0\end{bmatrix}.
$$

In this new basis, the transformation is diagonal: one direction is scaled by 4, the other collapsed to 0.

在这个新的基础上，变换是对角的：一个方向缩放 4，另一个方向折叠为 0。

### Geometric Interpretation
几何解释

Change of basis is like rotating or skewing your coordinate grid. The underlying transformation does not change, but its description in numbers becomes simpler or more complicated depending on the basis. Finding a basis that simplifies a transformation (often a diagonal basis) is a key theme in linear algebra.

基变换就像旋转或倾斜坐标网格。底层变换本身不会改变，但其数值描述会根据基的变化而变得更简单或更复杂。寻找能够简化变换的基（通常是对角基）是线性代数的一个关键主题。

### Why this matters
为什么这很重要

Change of basis connects the abstract notion of similarity to practical computation. It is the tool that allows us to diagonalize matrices, compute eigenvalues, and simplify complex transformations. In applications, it corresponds to choosing a more natural coordinate system-whether in geometry, physics, or machine learning.

基变换将相似性的抽象概念与实际计算联系起来。它使我们能够对矩阵进行对角化、计算特征值并简化复杂的变换。在实际应用中，它相当于选择一个更自然的坐标系——无论是在几何、物理还是机器学习领域。

### Exercises 5.4
练习 5.4

1.  Let

    令

    $$
    A = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}
    $$

    Compute its representation in the basis $\{(1,0),(1,1)\}$. 

    计算其在基 $\{(1,0),(1,1)\}$ 中的表示。

2. Find the change-of-basis matrix from the standard basis of $\mathbb{R}^2$ to $\{(2,1),(1,1)\}$. 

   求出从 $\mathbb{R}^2$ 到 $\{(2,1),(1,1)\}$ 的标准基变换矩阵。

3. Prove that similar matrices (related by $P^{-1}AP$) represent the same linear transformation under different bases. 

   证明相似的矩阵（由 $P^{-1}AP$ 关联）在不同基下表示相同的线性变换。

4. Diagonalize the matrix
    对角化矩阵
  

    $$
    A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
    $$

    in the basis $\{(1,1),(1,-1)\}$. 

    在基 $\{(1,1),(1,-1)\}$ 中。


5. In $\mathbb{R}^3$, let $\mathcal{B} = \{(1,0,0),(1,1,0),(1,1,1)\}$. Construct the change-of-basis matrix $P$ and compute $P^{-1}$.

    在 $\mathbb{R}^3$ 中，令 $\mathcal{B} = \{(1,0,0),(1,1,0),(1,1,1)\}$ 。构造基变换矩阵 $P$ 并计算 $P^{-1}$ 。
