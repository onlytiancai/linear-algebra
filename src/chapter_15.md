# 问题 1

> 线性变化和线性组合有什么区别？

线性变换和线性组合是**线性代数**中两个核心且紧密相关的概念，但它们描述的是不同的操作。简单来说，**线性组合**是构建向量的一种方法，而**线性变换**是一种作用于向量的函数。

---

### 线性组合 (Linear Combination)

**线性组合**是将一组向量通过**缩放**和**相加**来创建一个新向量的过程。

想象你有一组向量 $v_1, v_2, \ldots, v_n$。它们的线性组合就是将每个向量乘以一个标量（数字），然后把结果加起来，得到一个新的向量 $v$。

公式形式为：
$v = c_1v_1 + c_2v_2 + \ldots + c_nv_n$

这里的 $c_1, c_2, \ldots, c_n$ 是**标量**（实数）。

**举个例子：**
在二维平面上，如果你有两个向量 $v_1 = (1, 0)$ 和 $v_2 = (0, 1)$。
它们的线性组合可以是 $3v_1 + 2v_2 = 3(1, 0) + 2(0, 1) = (3, 0) + (0, 2) = (3, 2)$。
这里，我们通过**线性组合**的方式，用 $v_1$ 和 $v_2$ **构造**出了一个新的向量 $(3, 2)$。

---

### 线性变换 (Linear Transformation)

**线性变换**是一种特殊的函数，它将一个向量**空间**中的向量**映射**到另一个（或同一个）向量空间中的向量。它本质上是一种对向量进行操作的“规则”或“过程”。

一个变换 $T$ 如果满足以下两个条件，就被称为线性变换：

1.  **加法可分配性 (Additivity)：**
    $T(u + v) = T(u) + T(v)$
    对任意向量 $u, v$ 都成立。这意味着先将两个向量相加再进行变换，与先分别变换再相加，结果是一样的。

2.  **齐次性 (Homogeneity)：**
    $T(cu) = cT(u)$
    对任意向量 $u$ 和任意标量 $c$ 都成立。这意味着先对向量进行缩放再变换，与先变换再缩放，结果是一样的。

**举个例子：**
一个二维向量的旋转操作就是一个线性变换。
假设有一个变换 $T$ 将一个向量 $(x, y)$ 旋转90度。
$T(x, y) = (-y, x)$
你可以验证它是否满足上述两个条件。
如果你有一个向量 $v = (3, 2)$，对其进行线性变换 $T$，得到的结果是 $T(3, 2) = (-2, 3)$。

---

### 核心区别总结

| 特性 | 线性组合 (Linear Combination) | 线性变换 (Linear Transformation) |
| :--- | :--- | :--- |
| **作用** | 将一组向量通过缩放和相加**构造**成一个新的向量。 | 将一个向量**映射**或**转换**成一个新的向量。 |
| **主体** | 多个向量（以及一些标量）。 | 一个函数或操作（通常用矩阵表示）。 |
| **输入/输出** | 输入是**一组向量**和**一组标量**，输出是**一个向量**。 | 输入是**一个向量**，输出是**一个向量**。 |
| **目的** | 描述如何用基本向量**构建**出所有其他向量。 | 描述如何**改变**或**移动**向量空间中的向量。 |

**简单类比：**
* **线性组合**就像是“配方”：用不同的基本“原料”（向量）和“用量”（标量）来制作一道新“菜”（新向量）。
* **线性变换**就像是“工具”：一个能对任何“菜”（向量）进行特殊处理（比如切片、搅拌、旋转）的机器。

# 问题 2

> Let $D: \mathbb{R}[x] \to \mathbb{R}[x]$ be differentiation: $D(p(x)) = p'(x)$.
> 
> 令 $D: \mathbb{R}[x] \to \mathbb{R}[x]$ 为微分： $D(p(x)) = p'(x)$ 。
> 
> Since derivatives respect addition and scalar multiples, differentiation is a linear transformation.
> 
> 由于导数尊重加法和标量倍数，因此微分是一种线性变换。

这是一段非常经典的线性代数例子，它用一个你熟悉的微积分概念——**求导**，来解释**线性变换**。

我们来一步步拆解这句话：

### 1. 什么是 $D: \mathbb{R}[x] \to \mathbb{R}[x]$？

* **$\mathbb{R}[x]$**：这是所有**实系数多项式**组成的集合。例如，$x^2 + 2x - 5$ 和 $4x^3$ 都是这个集合里的元素。
* **$D$**：这是一个**函数**或**变换**，它的名字叫 $D$。
* **$D: \mathbb{R}[x] \to \mathbb{R}[x]$**：这句话的意思是，这个函数 $D$ 的**输入**是一个实系数多项式，**输出**也是一个实系数多项式。

### 2. 什么是 $D(p(x)) = p'(x)$？

* $p(x)$ 是 $\mathbb{R}[x]$ 里的一个多项式。
* $p'(x)$ 是 $p(x)$ 的**导数**。
* 这句话定义了 $D$ 的具体操作：**输入一个多项式 $p(x)$，输出它的导数 $p'(x)$。**
    * 例如，如果 $p(x) = x^2 + 3x$，那么 $D(x^2 + 3x) = 2x + 3$。

---

### 3. 如何理解“Since derivatives respect addition and scalar multiples, differentiation is a linear transformation.”？

**“respect addition and scalar multiples”** 是理解核心。这句话翻译过来就是“导数运算遵守加法和标量乘法”。

这正是**线性变换**的两个核心条件：

1.  **尊重加法 (Respects Addition)**：
    * 在微积分中，我们知道两个函数的和的导数，等于它们各自导数的和。用公式表示就是：
        $(f(x) + g(x))' = f'(x) + g'(x)$
    * 如果我们将求导操作看作是 $D$，那么这个性质可以写成：
        $D(f(x) + g(x)) = D(f(x)) + D(g(x))$
    * 这完全符合线性变换的第一个条件：**$T(u + v) = T(u) + T(v)$**。

2.  **尊重标量乘法 (Respects Scalar Multiples)**：
    * 在微积分中，一个函数乘以常数的导数，等于这个常数乘以函数的导数。用公式表示就是：
        $(c \cdot f(x))' = c \cdot f'(x)$
    * 用 $D$ 来表示，这个性质就是：
        $D(c \cdot f(x)) = c \cdot D(f(x))$
    * 这完全符合线性变换的第二个条件：**$T(cu) = cT(u)$**。

因为求导操作 $D$ **同时满足这两个条件**，所以它是一个**线性变换**。

总而言之，这段话巧妙地将你熟悉的求导规则（和的导数是导数的和，常数倍的导数是常数倍的导数）提升到了线性代数的抽象层面，告诉你**求导本身就是一个线性变换**。

# 问题 3

> Linear transformations are exactly those that preserve the origin, lines through the origin, and proportions along those lines. They include familiar operations: scaling, rotations, reflections, shears, and projections. Nonlinear transformations bend or curve space, breaking these properties.
> 
> 线性变换正是那些保留原点、过原点的直线以及沿这些直线的比例的变换。它们包括我们熟悉的操作：缩放、旋转、反射、剪切和投影。非线性变换会弯曲空间，从而破坏这些属性。

这句话非常精辟，它用直观的几何概念描述了**线性变换**的核心特征，并将其与**非线性变换**做了对比。我们可以从几个关键点来理解它。

---

### 1. 核心特征：保留原点、过原点的直线和沿直线的比例

**a) 保留原点 (Preserves the Origin)**
线性变换 $T$ 必须满足 $T(\mathbf{0}) = \mathbf{0}$。
* **几何意义**：空间中的原点 $(0, 0, \ldots)$ 经过线性变换后，**位置不会改变**。
* **为什么？**：因为线性变换的齐次性 $T(c\mathbf{v}) = cT(\mathbf{v})$。如果让 $c=0$，我们得到 $T(0 \cdot \mathbf{v}) = 0 \cdot T(\mathbf{v})$，即 $T(\mathbf{0}) = \mathbf{0}$。
* **类比**：一个线性变换就像是在一张纸上拉伸、旋转、倾斜，但纸上的“钉子”——原点——始终固定不动。

**b) 保留过原点的直线 (Preserves Lines Through the Origin)**
* **几何意义**：如果空间中有一条穿过原点的直线，经过线性变换后，这条线**依然是直线**，并且**仍然穿过原点**。它可能被旋转或拉伸，但不会变成曲线。
* **为什么？**：一条过原点的直线可以表示为所有向量 $c\mathbf{v}$ 的集合，其中 $\mathbf{v}$ 是直线上的一个方向向量，$c$ 是任意标量。因为线性变换满足 $T(c\mathbf{v}) = cT(\mathbf{v})$，变换后的所有点 $T(c\mathbf{v})$ 依然在同一条由 $T(\mathbf{v})$ 定义的直线上。

**c) 保留沿直线的比例 (Preserves Proportions Along These Lines)**
* **几何意义**：想象一条直线上的三个点 $A, B, C$。如果 $B$ 位于 $A$ 和 $C$ 的中点，那么经过线性变换后，变换后的点 $A', B', C'$，**$B'$ 仍然位于 $A'$ 和 $C'$ 的中点**。
* **为什么？**：这再次源于齐次性。如果向量 $\mathbf{v}$ 是向量 $\mathbf{u}$ 的两倍长（$\mathbf{v} = 2\mathbf{u}$），那么经过线性变换后，变换后的向量 $T(\mathbf{v})$ 仍然是 $T(\mathbf{u})$ 的两倍长（$T(\mathbf{v}) = T(2\mathbf{u}) = 2T(\mathbf{u})$）。变换**不会改变向量之间的相对长度关系**。

---

### 2. 具体的线性变换操作

这句话列举了几个我们熟悉的线性变换例子：
* **缩放 (Scaling)**：将所有向量按比例拉长或缩短。
* **旋转 (Rotation)**：围绕原点旋转向量。
* **反射 (Reflection)**：将向量像照镜子一样翻转。
* **剪切 (Shear)**：将一个方向上的所有点沿另一个方向移动，就像把一本厚书的封面推向一边，书页向外倾斜一样。
* **投影 (Projection)**：将所有向量投影到一个子空间（例如，将三维空间中的所有点都压平到二维平面上）。

这些操作的共同点是它们都**符合**上面提到的三条核心性质。

---

### 3. 非线性变换的对比

**非线性变换会“弯曲空间”**。这意味着：
* **不保留直线**：一条直线经过非线性变换后可能会变成一条**曲线**。
* **不保留比例**：变换后，向量的相对长度关系会被**扭曲**。
* **不保留原点**：非线性变换可以把原点移动到其他位置。

**例如**：
* **平移 (Translation)**：将所有点移动一段固定的距离。这**不是**线性变换，因为它**不保留原点**。
* **sin(x) 函数**：这是一个典型的非线性函数，它会把一条直线“弯曲”成波浪线。

**总结**：这句话提供了一个强大的几何直觉：**线性变换就是那些“硬邦邦”的变换**，它们不会弯曲、扭曲或撕裂空间。它们只对空间进行拉伸、旋转和倾斜，但始终保持其基础的网格结构。相比之下，非线性变换则更具“柔性”，可以随意弯曲和变形空间。

# 问题 4

> Verify that $T(x,y) = (3x-y, 2y)$ is a linear transformation on $\mathbb{R}^2$.
> 
> 验证 $T(x,y) = (3x-y, 2y)$ 是否是 $\mathbb{R}^2$ 的线性变换。

要验证一个变换是否是线性变换，需要检查它是否满足两个核心条件：**加法可分配性**和**齐次性**。

这个变换 $T$ 将 $\mathbb{R}^2$ 中的向量 $(x,y)$ 映射到另一个向量 $(3x-y, 2y)$。

让我们来验证这两个条件。

---

### 条件一：加法可分配性 (Additivity)

这个条件要求，对于任意两个向量 $\mathbf{u}$ 和 $\mathbf{v}$，都满足 $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$。

设两个向量为 $\mathbf{u} = (x_1, y_1)$ 和 $\mathbf{v} = (x_2, y_2)$。

1.  **计算 $T(\mathbf{u} + \mathbf{v})$**：
    首先，将两个向量相加：
    $\mathbf{u} + \mathbf{v} = (x_1 + x_2, y_1 + y_2)$
    然后，对这个新向量进行变换 $T$：
    $T(\mathbf{u} + \mathbf{v}) = T(x_1 + x_2, y_1 + y_2) = (3(x_1+x_2) - (y_1+y_2), 2(y_1+y_2))$
    $= (3x_1 + 3x_2 - y_1 - y_2, 2y_1 + 2y_2)$

2.  **计算 $T(\mathbf{u}) + T(\mathbf{v})$**：
    首先，分别对 $\mathbf{u}$ 和 $\mathbf{v}$ 进行变换：
    $T(\mathbf{u}) = T(x_1, y_1) = (3x_1 - y_1, 2y_1)$
    $T(\mathbf{v}) = T(x_2, y_2) = (3x_2 - y_2, 2y_2)$
    然后，将变换后的向量相加：
    $T(\mathbf{u}) + T(\mathbf{v}) = (3x_1 - y_1, 2y_1) + (3x_2 - y_2, 2y_2)$
    $= (3x_1 - y_1 + 3x_2 - y_2, 2y_1 + 2y_2)$
    $= (3x_1 + 3x_2 - y_1 - y_2, 2y_1 + 2y_2)$

由于 $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$，第一个条件**成立**。

---

### 条件二：齐次性 (Homogeneity)

这个条件要求，对于任意向量 $\mathbf{u}$ 和任意标量 $c$，都满足 $T(c\mathbf{u}) = cT(\mathbf{u})$。

设向量为 $\mathbf{u} = (x, y)$。

1.  **计算 $T(c\mathbf{u})$**：
    首先，对向量进行标量乘法：
    $c\mathbf{u} = c(x, y) = (cx, cy)$
    然后，对这个新向量进行变换 $T$：
    $T(c\mathbf{u}) = T(cx, cy) = (3(cx) - (cy), 2(cy)) = (3cx - cy, 2cy)$

2.  **计算 $cT(\mathbf{u})$**：
    首先，对 $\mathbf{u}$ 进行变换：
    $T(\mathbf{u}) = T(x, y) = (3x - y, 2y)$
    然后，用标量 $c$ 乘以变换后的向量：
    $cT(\mathbf{u}) = c(3x - y, 2y) = (c(3x-y), c(2y)) = (3cx - cy, 2cy)$

由于 $T(c\mathbf{u}) = cT(\mathbf{u})$，第二个条件也**成立**。

---

**结论**：
因为变换 $T(x,y) = (3x-y, 2y)$ **同时满足加法可分配性和齐次性**这两个条件，所以它是一个**线性变换**。

# 问题 5

> 证明 $T(x,y) = (x+1, y)$ 不是线性的。哪条公理不成立？
> 
> Prove that if $T$ and $S$ are linear transformations, then so is $T+S$.

要证明一个变换不是线性的，我们只需要找到一个反例，证明它不满足线性变换的两个核心公理中的**任意一个**即可。这两个公理是：

1.  **加法可分配性**：$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2.  **齐次性**：$T(c\mathbf{u}) = cT(\mathbf{u})$

我们来验证变换 $T(x,y) = (x+1, y)$。这是一个**平移**变换，将所有点向右平移一个单位。

### 验证不成立的公理

**最简单的方法是检查线性变换的隐藏公理：$T(\mathbf{0}) = \mathbf{0}$。**
一个线性变换必须将原点 $(0,0)$ 映射到它自身。
对于 $T(x,y) = (x+1, y)$，我们计算 $T(0,0)$：
$T(0,0) = (0+1, 0) = (1, 0)$

由于 $T(0,0) = (1,0) \ne (0,0)$，变换**不保留原点**。因此，它不是一个线性变换。

---

### 详细验证：加法可分配性

即使不使用上面这个简单的验证方法，我们也可以直接使用加法公理来证明。
设两个向量 $\mathbf{u} = (x_1, y_1)$ 和 $\mathbf{v} = (x_2, y_2)$。

1.  **计算 $T(\mathbf{u} + \mathbf{v})$**
    首先将两个向量相加：
    $\mathbf{u} + \mathbf{v} = (x_1 + x_2, y_1 + y_2)$
    然后进行变换：
    $T(\mathbf{u} + \mathbf{v}) = T(x_1 + x_2, y_1 + y_2) = ((x_1+x_2)+1, y_1+y_2) = (x_1+x_2+1, y_1+y_2)$

2.  **计算 $T(\mathbf{u}) + T(\mathbf{v})$**
    首先分别进行变换：
    $T(\mathbf{u}) = T(x_1, y_1) = (x_1+1, y_1)$
    $T(\mathbf{v}) = T(x_2, y_2) = (x_2+1, y_2)$
    然后将变换后的向量相加：
    $T(\mathbf{u}) + T(\mathbf{v}) = (x_1+1, y_1) + (x_2+1, y_2) = ((x_1+1) + (x_2+1), y_1+y_2) = (x_1+x_2+2, y_1+y_2)$

由于 $T(\mathbf{u} + \mathbf{v}) \ne T(\mathbf{u}) + T(\mathbf{v})$（因为 $x_1+x_2+1 \ne x_1+x_2+2$），加法可分配性**不成立**。

---

### 详细验证：齐次性

我们也可以用齐次性来证明。
设向量 $\mathbf{u} = (x, y)$，取一个标量 $c=2$。

1.  **计算 $T(c\mathbf{u})$**
    首先进行标量乘法：
    $c\mathbf{u} = 2(x, y) = (2x, 2y)$
    然后进行变换：
    $T(c\mathbf{u}) = T(2x, 2y) = (2x+1, 2y)$

2.  **计算 $cT(\mathbf{u})$**
    首先进行变换：
    $T(\mathbf{u}) = T(x, y) = (x+1, y)$
    然后进行标量乘法：
    $cT(\mathbf{u}) = 2T(x,y) = 2(x+1, y) = (2(x+1), 2y) = (2x+2, 2y)$

由于 $T(c\mathbf{u}) \ne cT(\mathbf{u})$（因为 $2x+1 \ne 2x+2$），齐次性**也不成立**。

### 结论

**$T(x,y) = (x+1, y)$ 不满足线性变换的任一公理，所以它不是一个线性变换。**

在几何上，这个变换是**平移**，它将所有点移动了一个单位。正如我们之前所讨论的，线性变换必须保留原点和过原点的直线，但平移变换会移动原点，因此从直觉上就知道它不是线性的。

# 问题 6

> Give an example of a linear transformation from $\mathbb{R}^3$ to $\mathbb{R}^2$.
> 
> 给出一个从 $\mathbb{R}^3$ 到 $\mathbb{R}^2$ 的线性变换的例子。

为了给出一个从 $\mathbb{R}^3$ 到 $\mathbb{R}^2$ 的线性变换的例子，我们可以使用一个 $2 \times 3$ **矩阵**来定义这个变换。

一个从 $\mathbb{R}^3$ 到 $\mathbb{R}^2$ 的线性变换 $T$ 可以用一个 $2 \times 3$ 矩阵 $A$ 来表示。如果一个向量 $\mathbf{v} = (x, y, z)$ 属于 $\mathbb{R}^3$，那么它经过变换后的向量 $T(\mathbf{v})$ 可以通过矩阵乘法 $A\mathbf{v}$ 来得到。

### 例子：

让我们选择一个简单的 $2 \times 3$ 矩阵 $A$：
$$
A = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0
\end{pmatrix}
$$

这个矩阵代表了一个**投影**变换。它将三维空间中的一个点 $(x, y, z)$ 投影到二维平面上的点 $(x, y)$。

这个线性变换 $T$ 可以定义为：
$$
T(\mathbf{v}) = A\mathbf{v} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
= \begin{pmatrix}
1 \cdot x + 0 \cdot y + 0 \cdot z \\
0 \cdot x + 1 \cdot y + 0 \cdot z
\end{pmatrix}
= \begin{pmatrix}
x \\
y
\end{pmatrix}
$$

或者用函数形式表示为：
$T(x, y, z) = (x, y)$

### 为什么它是一个线性变换？

我们可以快速验证它是否满足线性变换的两个条件：

1.  **加法可分配性**：
    设 $\mathbf{u} = (x_1, y_1, z_1)$ 和 $\mathbf{v} = (x_2, y_2, z_2)$。
    $T(\mathbf{u} + \mathbf{v}) = T(x_1+x_2, y_1+y_2, z_1+z_2) = (x_1+x_2, y_1+y_2)$
    $T(\mathbf{u}) + T(\mathbf{v}) = (x_1, y_1) + (x_2, y_2) = (x_1+x_2, y_1+y_2)$
    由于两者相等，条件成立。

2.  **齐次性**：
    设 $\mathbf{u} = (x, y, z)$ 和标量 $c$。
    $T(c\mathbf{u}) = T(cx, cy, cz) = (cx, cy)$
    $cT(\mathbf{u}) = c(x, y) = (cx, cy)$
    由于两者相等，条件成立。

因此，$T(x, y, z) = (x, y)$ 是一个从 $\mathbb{R}^3$ 到 $\mathbb{R}^2$ 的线性变换。在几何上，这个变换将三维空间中的每个点**垂直投影**到 $xy$ 平面上。

# 问题 7

> Let $T:\mathbb{R}[x] \to \mathbb{R}[x]$ be integration:
>
> 令 $T:\mathbb{R}[x] \to \mathbb{R}[x]$ 为积分：
> 
> $$
T(p(x)) = \int_0^x p(t)dt
$$
>  
> Prove that $T$ is a linear transformation.
> 
> 证明 $T$ 是线性变换。

要证明变换 $T$ 是一个线性变换，我们必须验证它是否满足线性变换的两个核心公理：**加法可分配性**和**齐次性**。

这个变换 $T$ 的定义是将一个多项式 $p(x)$ 积分，得到一个新的多项式。这个积分的下限是固定的 $0$，所以它总是返回一个多项式，而不是一个常数。

让我们来验证这两个公理。

---

### 条件一：加法可分配性 (Additivity)

这个条件要求，对于任意两个多项式 $p(x)$ 和 $q(x)$，都满足 $T(p(x) + q(x)) = T(p(x)) + T(q(x))$。

根据定积分的性质，两个函数和的积分等于它们各自积分的和。我们可以用这个性质来验证：

$$T(p(x) + q(x)) = \int_0^x (p(t) + q(t))\,dt$$

利用积分的加法性质，可以将右边的积分拆开：

$$= \int_0^x p(t)\,dt + \int_0^x q(t)\,dt$$

根据 $T$ 的定义，右边的两项正好是 $T(p(x))$ 和 $T(q(x))$：

$$= T(p(x)) + T(q(x))$$

因此，加法可分配性**成立**。

---

### 条件二：齐次性 (Homogeneity)

这个条件要求，对于任意多项式 $p(x)$ 和任意标量 $c$，都满足 $T(c \cdot p(x)) = c \cdot T(p(x))$。

根据定积分的性质，一个常数乘以函数的积分，等于这个常数乘以函数的积分。

$$T(c \cdot p(x)) = \int_0^x (c \cdot p(t))\,dt$$

利用积分的齐次性，可以将常数 $c$ 提到积分号外面：

$$= c \int_0^x p(t)\,dt$$

根据 $T$ 的定义，右边的积分项正好是 $T(p(x))$：

$$= c \cdot T(p(x))$$

因此，齐次性**成立**。

---

### 结论

因为变换 $T$ **同时满足加法可分配性（尊重加法）和齐次性（尊重标量乘法）**这两个条件，所以它是一个**线性变换**。这个例子和微分是线性变换的例子相辅相成，共同说明了微积分中的核心运算本身就是线性代数中的线性变换。

# 问题 8

> Find the matrix representation of $T:\mathbb{R}^2 \to \mathbb{R}^2$, $T(x,y) = (x+y, x-y)$.
>
>    找到 $T:\mathbb{R}^2 \to \mathbb{R}^2$ , $T(x,y) = (x+y, x-y)$ 的矩阵表示。

要找到一个线性变换的矩阵表示，你需要确定变换对标准基向量的作用。在 $\mathbb{R}^2$ 中，标准基向量是：
* $e_1 = (1, 0)$
* $e_2 = (0, 1)$

这个矩阵的**列**就是变换后的基向量。

---

### 1. 变换第一个基向量 $e_1$

将 $e_1 = (1, 0)$ 代入变换 $T(x,y) = (x+y, x-y)$：
$T(1, 0) = (1+0, 1-0) = (1, 1)$
这就是矩阵的第一列。

### 2. 变换第二个基向量 $e_2$

将 $e_2 = (0, 1)$ 代入变换 $T(x,y) = (x+y, x-y)$：
$T(0, 1) = (0+1, 0-1) = (1, -1)$
这就是矩阵的第二列。

---

### 3. 构建矩阵

将变换后的向量作为矩阵的列，我们得到变换的矩阵表示 $A$：
$$
A = \begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
$$

### 4. 验证

我们可以用这个矩阵来验证它是否能得到原始的变换。对于任意向量 $(x, y)$，我们应该有 $T(x, y) = A\begin{pmatrix} x \\ y \end{pmatrix}$。
$$
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
= \begin{pmatrix}
1 \cdot x + 1 \cdot y \\
1 \cdot x - 1 \cdot y
\end{pmatrix}
= \begin{pmatrix}
x+y \\
x-y
\end{pmatrix}
$$
这与变换 $T(x,y) = (x+y, x-y)$ 的定义完全一致。

因此，这个变换的矩阵表示就是 $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$。

# 问题 9

> Determine the matrix of the linear transformation $T:\mathbb{R}^3 \to \mathbb{R}^2$, $T(x,y,z) = (x+z, y-2z)$.
>
> 确定线性变换矩阵 $T:\mathbb{R}^3 \to \mathbb{R}^2$ ， $T(x,y,z) = (x+z, y-2z)$ 。

要确定这个从 $\mathbb{R}^3$ 到 $\mathbb{R}^2$ 的线性变换的矩阵，我们需要找出变换作用在 $\mathbb{R}^3$ 的标准基向量上会得到什么结果。

$\mathbb{R}^3$ 的标准基向量是：
* $e_1 = (1, 0, 0)$
* $e_2 = (0, 1, 0)$
* $e_3 = (0, 0, 1)$

这个线性变换的矩阵的**列**就是变换后的基向量。

### 1. 变换第一个基向量 $e_1$
将 $e_1 = (1, 0, 0)$ 代入变换 $T(x,y,z) = (x+z, y-2z)$：
$T(1, 0, 0) = (1+0, 0-2(0)) = (1, 0)$
这构成了矩阵的第一列。

### 2. 变换第二个基向量 $e_2$
将 $e_2 = (0, 1, 0)$ 代入变换 $T(x,y,z) = (x+z, y-2z)$：
$T(0, 1, 0) = (0+0, 1-2(0)) = (0, 1)$
这构成了矩阵的第二列。

### 3. 变换第三个基向量 $e_3$
将 $e_3 = (0, 0, 1)$ 代入变换 $T(x,y,z) = (x+z, y-2z)$：
$T(0, 0, 1) = (0+1, 0-2(1)) = (1, -2)$
这构成了矩阵的第三列。

---

### 4. 构建矩阵
将这三个变换后的向量作为矩阵的列，我们得到变换的矩阵表示 $A$：
$$
A = \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & -2
\end{pmatrix}
$$

### 5. 验证
我们可以用这个矩阵来验证它是否能得到原始的变换。对于任意向量 $(x, y, z)$，我们应该有 $T(x, y, z) = A\begin{pmatrix} x \\ y \\ z \end{pmatrix}$。
$$
\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & -2
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
= \begin{pmatrix}
1 \cdot x + 0 \cdot y + 1 \cdot z \\
0 \cdot x + 1 \cdot y - 2 \cdot z
\end{pmatrix}
= \begin{pmatrix}
x+z \\
y-2z
\end{pmatrix}
$$
这与变换 $T(x,y,z) = (x+z, y-2z)$ 的定义完全一致。

因此，该线性变换的矩阵表示是 $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & -2 \end{pmatrix}$。

# 问题 10

> What matrix represents reflection across the line $y=x$ in $\mathbb{R}^2$?
> 
> 哪个矩阵表示 $\mathbb{R}^2$ 中沿线 $y=x$ 的反射？

这个线性变换的矩阵可以通过作用在 $\mathbb{R}^2$ 的标准基向量上来确定。

$\mathbb{R}^2$ 的标准基向量是：
* $e_1 = (1, 0)$
* $e_2 = (0, 1)$

### 1. 变换第一个基向量 $e_1 = (1, 0)$

点 $(1, 0)$ 在 $y=x$ 线上方的右侧。当它关于 $y=x$ 反射时，它的新位置是 $(0, 1)$。
* $T(1, 0) = (0, 1)$

### 2. 变换第二个基向量 $e_2 = (0, 1)$

点 $(0, 1)$ 在 $y=x$ 线上方的左侧。当它关于 $y=x$ 反射时，它的新位置是 $(1, 0)$。
* $T(0, 1) = (1, 0)$

### 3. 构建矩阵

将变换后的向量作为矩阵的列，我们得到变换的矩阵表示 $A$：
$$
A = \begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
$$

### 4. 验证

我们可以用这个矩阵来验证。对于任意向量 $(x, y)$，我们应该有 $T(x, y) = A\begin{pmatrix} x \\ y \end{pmatrix}$。
$$
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
= \begin{pmatrix}
0 \cdot x + 1 \cdot y \\
1 \cdot x + 0 \cdot y
\end{pmatrix}
= \begin{pmatrix}
y \\
x
\end{pmatrix}
$$
变换后的向量是 $(y, x)$，这正是点 $(x, y)$ 关于直线 $y=x$ 反射后的坐标。

因此，矩阵 $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ 表示 $\mathbb{R}^2$ 中沿直线 $y=x$ 的反射。

# 问题 11

学不懂线性代数？用动画来拯救（一）：线性变换
https://zhuanlan.zhihu.com/p/1896368529332237603

# 问题 12

> For the differentiation map $D:\mathbb{R}_2[x] \to \mathbb{R}_1[x]$, where $\mathbb{R}_k[x]$ is the space of polynomials of degree at most $k$, find the matrix of $D$ relative to the bases $\{1,x,x^2\}$ and $\{1,x\}$.
> 
> 对于微分映射 $D:\mathbb{R}_2[x] \to \mathbb{R}_1[x]$ ，其中 $\mathbb{R}_k[x]$ 是次数最多为 $k$ 的多项式空间，求出 $D$ 相对于基数 $\{1,x,x^2\}$ 和 $\{1,x\}$ 的矩阵。

对于微分映射 $D:\mathbb{R}_2[x] \to \mathbb{R}_1[x]$，我们需要找到它相对于给定基的矩阵表示。

---

### 1. 确定基

* **输入空间** $\mathbb{R}_2[x]$ 的基为 $B_1 = \{1, x, x^2\}$。
    这个基中的任何多项式 $p(x) = a+bx+cx^2$ 都可以表示为向量 $\begin{pmatrix} a \\ b \\ c \end{pmatrix}$。
* **输出空间** $\mathbb{R}_1[x]$ 的基为 $B_2 = \{1, x\}$。
    这个基中的任何多项式 $q(x) = d+ex$ 都可以表示为向量 $\begin{pmatrix} d \\ e \end{pmatrix}$。

### 2. 对输入基向量进行微分

微分映射 $D$ 的作用是 $D(p(x)) = p'(x)$。我们将对输入空间 $\mathbb{R}_2[x]$ 的每个基向量进行微分：

* **对 $1$ 进行微分**:
    $D(1) = 0$
    在输出基 $B_2$ 中，这个结果可以表示为 $0 \cdot 1 + 0 \cdot x$。
    它的坐标向量是 $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$。

* **对 $x$ 进行微分**:
    $D(x) = 1$
    在输出基 $B_2$ 中，这个结果可以表示为 $1 \cdot 1 + 0 \cdot x$。
    它的坐标向量是 $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$。

* **对 $x^2$ 进行微分**:
    $D(x^2) = 2x$
    在输出基 $B_2$ 中，这个结果可以表示为 $0 \cdot 1 + 2 \cdot x$。
    它的坐标向量是 $\begin{pmatrix} 0 \\ 2 \end{pmatrix}$。

---

### 3. 构建矩阵

线性变换的矩阵表示是**将变换后基向量的坐标向量作为矩阵的列**。

将上面得到的三个坐标向量作为矩阵的列，我们得到矩阵 $A$：
$$
A = \begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 2
\end{pmatrix}
$$

### 4. 验证

我们可以用这个矩阵来验证。例如，多项式 $p(x) = 3+4x+5x^2$ 在基 $B_1$ 下的坐标向量为 $\begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix}$。

用矩阵 $A$ 乘以这个向量：
$$
\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 2
\end{pmatrix}
\begin{pmatrix}
3 \\ 4 \\ 5
\end{pmatrix}
= \begin{pmatrix}
0 \cdot 3 + 1 \cdot 4 + 0 \cdot 5 \\
0 \cdot 3 + 0 \cdot 4 + 2 \cdot 5
\end{pmatrix}
= \begin{pmatrix}
4 \\ 10
\end{pmatrix}
$$

这个结果 $\begin{pmatrix} 4 \\ 10 \end{pmatrix}$ 是微分后多项式在基 $B_2$ 下的坐标向量。
它表示的多项式是 $4 \cdot 1 + 10 \cdot x = 4+10x$。

直接对 $p(x)$ 进行微分，得到 $p'(x) = (3+4x+5x^2)' = 4+10x$，结果完全一致。

因此，矩阵 $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$ 正确地表示了微分映射 $D$ 相对于给定基的矩阵。

# 问题 13

> Find the kernel and image of $T:\mathbb{R}^2 \to \mathbb{R}^2$, $T(x,y) = (x-y, x+y)$.
>
> 查找 $T:\mathbb{R}^2 \to \mathbb{R}^2$ 、 $T(x,y) = (x-y, x+y)$ 的核和图像。

该线性变换的**核（Kernel）**是只包含零向量的集合 $\{ (0,0) \}$，而**像（Image）**是整个 $\mathbb{R}^2$ 空间。

***

### 1. 找到核（Kernel）

一个线性变换的**核**是输入空间中所有被映射到零向量的向量的集合。对于给定的变换 $T(x,y) = (x-y, x+y)$，我们需要找到所有满足 $T(x,y) = (0,0)$ 的向量 $(x,y)$。

这相当于求解以下线性方程组：
$$
\begin{cases}
x - y = 0 \\
x + y = 0
\end{cases}
$$

* 将两个方程相加：
    $(x - y) + (x + y) = 0 + 0$
    $2x = 0$
    $x = 0$

* 将 $x=0$ 代入第一个方程：
    $0 - y = 0$
    $y = 0$

唯一的解是 $x=0, y=0$。这意味着只有零向量 $(0,0)$ 被映射到零向量 $(0,0)$。
所以，**核**为 $\text{ker}(T) = \{ (0,0) \}$。

***

### 2. 找到像（Image）

一个线性变换的**像**是输入空间中所有向量经过变换后所能生成的输出向量的集合。为了找到像，我们可以考察变换矩阵的列空间。

首先，找到变换 $T$ 的矩阵表示。我们考察标准基向量 $e_1=(1,0)$ 和 $e_2=(0,1)$ 的变换结果：
* $T(1,0) = (1-0, 1+0) = (1,1)$
* $T(0,1) = (0-1, 0+1) = (-1,1)$

因此，变换的矩阵为：
$$
A = \begin{pmatrix}
1 & -1 \\
1 & 1
\end{pmatrix}
$$
像**等于**这个矩阵的列空间，它由矩阵的列向量 $(1,1)$ 和 $(-1,1)$ 的所有线性组合组成。

这两个列向量是**线性无关**的，因为它们不是彼此的常数倍。两个线性无关的向量在 $\mathbb{R}^2$ 空间中能张成整个空间。
所以，**像**为 $\text{Im}(T) = \mathbb{R}^2$。

***

### 补充：秩-零化度定理

这个结果与**秩-零化度定理**相符。该定理指出，对于一个线性变换 $T:V \to W$，有：
$$\text{dim}(\text{ker}(T)) + \text{dim}(\text{Im}(T)) = \text{dim}(V)$$
在本例中：
* $\text{dim}(\text{ker}(T)) = 0$ （因为核中只有一个零向量）
* $\text{dim}(V) = \text{dim}(\mathbb{R}^2) = 2$
因此：
$$0 + \text{dim}(\text{Im}(T)) = 2$$
所以 $\text{dim}(\text{Im}(T)) = 2$，这再次确认了像的维度为 2，即整个 $\mathbb{R}^2$ 空间。

# 问题 14

> Matrix representations depend on the chosen basis. If $\mathcal{B}$ and $\mathcal{C}$ are bases of $\mathbb{R}^n$ and $\mathbb{R}^m$, then the matrix of $T: \mathbb{R}^n \to \mathbb{R}^m$ with respect to these bases is obtained by expressing $T(\mathbf{v}_j)$ in terms of $\mathcal{C}$ for each $\mathbf{v}_j \in \mathcal{B}$. Changing bases corresponds to conjugating the matrix by the appropriate change-of-basis matrices.
>
> 矩阵表示取决于所选的基。如果 $\mathcal{B}$ 和 $\mathcal{C}$ 是 $\mathbb{R}^n$ 和 $\mathbb{R}^m$ 的基  ，则 $T: \mathbb{R}^n \to \mathbb{R}^m$ 关于这些基的矩阵，可以通过将 $T(\mathbf{v}_j)$ 表示为 $\mathcal{C}$ 来获得，其中 $\mathbf{v}_j \in \mathcal{B}$ 表示为 $T(\mathbf{v}_j)$。改变基相当于将矩阵与适当的基变换矩阵共轭。

这句话阐述了线性变换的矩阵表示与基选择之间的关系。我们可以分三部分来理解它：

---

### 1. 矩阵表示的依赖性

**"Matrix representations depend on the chosen basis."**

这句话是核心思想。一个线性变换本身是一个抽象的操作，比如旋转或投影，它不依赖于任何坐标系。但当我们想用矩阵来描述这个操作时，我们必须先选择一个坐标系（即一组**基**）。不同的基会产生不同的矩阵来表示同一个线性变换。

例如，在 $\mathbb{R}^2$ 中，旋转 $90^\circ$ 的变换是固定的。如果我们用标准基 $\{(1,0), (0,1)\}$，矩阵是 $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$。但如果我们选择另一组基，比如 $\{(1,1), (-1,1)\}$，这个旋转变换的矩阵会是不同的。

### 2. 构建矩阵的方法

**"...the matrix of $T: \mathbb{R}^n \to \mathbb{R}^m$ with respect to these bases is obtained by expressing $T(\mathbf{v}_j)$ in terms of $\mathcal{C}$ for each $\mathbf{v}_j \in \mathcal{B}$."**

这部分解释了如何具体构建矩阵。假设你有：
* **输入空间** $\mathbb{R}^n$ 的基 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$。
* **输出空间** $\mathbb{R}^m$ 的基 $\mathcal{C} = \{\mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_m\}$。

矩阵构建的步骤是：
1.  对**输入基**中的每一个向量 $\mathbf{v}_j$ 应用线性变换 $T$，得到新向量 $T(\mathbf{v}_j)$。
2.  这个新向量 $T(\mathbf{v}_j)$ 属于输出空间 $\mathbb{R}^m$。你需要将它表示成**输出基** $\mathcal{C}$ 的线性组合。
3.  将这个线性组合的**坐标系数**写成一列，这就是变换矩阵的第 $j$ 列。

重复这个过程，直到你处理完输入基中的所有向量，你就得到了完整的变换矩阵。

### 3. 改变基底与矩阵共轭

**"Changing bases corresponds to conjugating the matrix by the appropriate change-of-basis matrices."**

这部分解释了当基发生变化时，矩阵如何变化。它给出了一个重要的关系式：
$A' = P^{-1}AP$
其中：
* $A$ 是变换 $T$ 在旧基下的矩阵。
* $A'$ 是变换 $T$ 在新基下的矩阵。
* $P$ 是**从新基到旧基**的过渡矩阵（change-of-basis matrix）。

这个关系称为**矩阵的相似变换**（similarity transformation）或**共轭**（conjugation）。它的几何意义是：
1.  用 $P$ 将新基下的向量**转换**到旧基下的坐标（$P$ 的列是新基向量在旧基下的表示）。
2.  用旧矩阵 $A$ **执行**线性变换。
3.  用 $P^{-1}$ 将结果**转换回**新基下的坐标。



通过这个公式，我们可以方便地在不同基下的矩阵表示之间进行转换，而无需重新计算每个基向量的变换。这个特性是**特征值和特征向量**理论的基础，因为特征向量所组成的基可以使线性变换的矩阵表示成为最简单的形式——对角矩阵。

# 问题 15

> Let
>
> 令
>
> $$
A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \end{bmatrix}
$$
>
 >Find bases for $\ker(A)$ and $\text{im}(A)$. 
>
> 找到 $\ker(A)$ 和 $\text{im}(A)$ 的基。

首先，矩阵 $A$ 描述了一个从 $\mathbb{R}^3$ 到 $\mathbb{R}^2$ 的线性变换。我们需要找到这个变换的**零空间（核）**和**列空间（像）**的基。

---

### 1. 找到零空间（核）$\ker(A)$ 的基

**零空间**是所有被 $A$ 映射为零向量的向量 $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}$ 的集合。这等价于求解方程 $A\mathbf{x} = \mathbf{0}$：

$$\begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

这对应于以下方程组：
1.  $x_1 + 2x_2 + 3x_3 = 0$
2.  $x_2 + 4x_3 = 0$

从第二个方程，我们可以用 $x_3$ 来表示 $x_2$：

$x_2 = -4x_3$

将这个结果代入第一个方程：

$x_1 + 2(-4x_3) + 3x_3 = 0$

$x_1 - 8x_3 + 3x_3 = 0$

$x_1 - 5x_3 = 0$

$x_1 = 5x_3$

我们可以用自由变量 $x_3$ 来表示所有解。设 $x_3 = t$，其中 $t$ 是任意实数。那么：
$$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 5t \\ -4t \\ t \end{bmatrix} = t \begin{bmatrix} 5 \\ -4 \\ 1 \end{bmatrix}$$

因此，**零空间**是由向量 $\begin{bmatrix} 5 \\ -4 \\ 1 \end{bmatrix}$ 张成的。这个向量构成了零空间的一个基。

$\ker(A)$ 的基是：$\left\{ \begin{bmatrix} 5 \\ -4 \\ 1 \end{bmatrix} \right\}$

---

### 2. 找到列空间（像）$\text{im}(A)$ 的基

**列空间**是矩阵 $A$ 的列向量的所有线性组合的集合。矩阵 $A$ 的列向量是：
$$\mathbf{a}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \mathbf{a}_2 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}, \quad \mathbf{a}_3 = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$$

为了找到列空间的基，我们需要找到这些列向量中的**线性无关**的向量。因为矩阵 $A$ 已经是**行阶梯形式**，我们可以很容易地识别出主元（pivot）列。主元是行阶梯形式中每行第一个非零元素。

* 第一行的主元是 $1$（在第一列）。
* 第二行的主元是 $1$（在第二列）。

矩阵 $A$ 的主元位于**第一列**和**第二列**。这些列向量构成了列空间的一组基。

因此，$\text{im}(A)$ 的基是：$\left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 1 \end{bmatrix} \right\}$

注意，虽然 $\mathbf{a}_3 = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$ 也是列向量，但它是前两个向量的线性组合，因此不是基的一部分。

我们可以验证：

$1 \cdot \begin{bmatrix} 1 \\ 0 \end{bmatrix} + 1 \cdot \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} \ne \begin{bmatrix} 3 \\ 4 \end{bmatrix}$。

实际上 $\mathbf{a}_3 = -5\mathbf{a}_1 + 4\mathbf{a}_2$ 吗？

$4\mathbf{a}_2 = \begin{bmatrix} 8 \\ 4 \end{bmatrix}$， 
$-5\mathbf{a}_1 = \begin{bmatrix} -5 \\ 0 \end{bmatrix}$。

$（-5）\begin{bmatrix} 1 \\ 0 \end{bmatrix} + (4)\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -5 \\ 0 \end{bmatrix} + \begin{bmatrix} 8 \\ 4 \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$。


让我们重新看一下方程：$x_1+2x_2+3x_3=0$。 

$x_3$ 是自由变量。 

$x_2 = -4x_3$, 

$x_1 = -2x_2-3x_3 = -2(-4x_3) - 3x_3 = 8x_3-3x_3=5x_3$。

是的，没错。

根据秩-零化度定理（Rank-Nullity Theorem），我们有：

$\text{dim}(\ker(A)) + \text{dim}(\text{im}(A)) = \text{dim}(\text{domain})$

$1 + 2 = 3$

这与我们找到的结果一致，进一步验证了答案的正确性。

### Chatgpt

我们解线性方程 $A x=0$。设 $x=(x_1,x_2,x_3)^T$，由

$$
\begin{cases}
x_1+2x_2+3x_3=0,\\[4pt]
x_2+4x_3=0
\end{cases}
$$

得 $x_2=-4x_3$，代入第一式得 $x_1=5x_3$。于是

$$
x=x_3(5,-4,1)^T.
$$

因此

$$
\ker(A)=\operatorname{span}\{(5,-4,1)^T\}.
$$

再看像空间。取矩阵的列向量

$$
c_1=(1,0)^T,\quad c_2=(2,1)^T,\quad c_3=(3,4)^T.
$$

容易看出 $c_1$ 与 $c_2$ 线性无关（因此秩为 2），所以像空间是整个 $\mathbb{R}^2$，且例如

$$
\operatorname{im}(A)=\operatorname{span}\{(1,0)^T,(2,1)^T\}=\mathbb{R}^2.
$$

总结：

* $\displaystyle \ker(A)=\operatorname{span}\{(5,-4,1)^T\}$.
* $\displaystyle \operatorname{im}(A)=\operatorname{span}\{(1,0)^T,(2,1)^T\}=\mathbb{R}^2$。

把 $c_1=(1,0)^T,\;c_2=(2,1)^T,\;c_3=(3,4)^T$。要证明 $c_3$ 是 $c_1,c_2$ 的线性组合，只需找出常数 $a,b$ 使得

$$
a c_1 + b c_2 = c_3.
$$

写成分量方程：

$$
a(1,0)^T + b(2,1)^T = (3,4)^T
\quad\Longrightarrow\quad
\begin{cases}
a+2b=3,\\
0\cdot a + b =4.
\end{cases}
$$

由第二式得到 $b=4$，代入第一式得 $a=3-2\cdot4= -5$。于是

$$
c_3 = -5c_1 + 4c_2,
$$

并且验算：$-5(1,0)^T+4(2,1)^T=(3,4)^T$。因此 $c_3$ 确实是 $c_1,c_2$ 的线性组合。


# 问题 16


> For the projection map $P(x,y,z) = (x,y,0)$, describe the kernel and image. 
>   
> 对于投影图 $P(x,y,z) = (x,y,0)$ ，描述其核和图像。

这个投影映射的**核**是 z 轴，而**像**是 xy 平面。

---

### 1. 核 (Kernel)

**核**是所有被映射到零向量的向量的集合。对于给定的投影映射 $P(x,y,z) = (x,y,0)$，我们需要找到所有满足 $P(x,y,z) = (0,0,0)$ 的向量 $(x,y,z)$。

这相当于求解以下方程：
$P(x,y,z) = (x,y,0) = (0,0,0)$

这意味着：
* $x = 0$
* $y = 0$
* $z$ 可以是任何实数。

因此，所有满足条件的向量都形如 $(0,0,z)$，它们构成了三维空间中的 z 轴。

所以，**核**为 $\ker(P) = \{ (0,0,z) \mid z \in \mathbb{R} \}$。它的维度是1。

---

### 2. 像 (Image)

**像**是输入空间中所有向量经过变换后所能生成的输出向量的集合。对于 $P(x,y,z) = (x,y,0)$，输出向量总是形如 $(x,y,0)$。

这意味着，无论你选择哪个三维向量，它的投影结果都将是第三个分量为零的向量。所有这些向量的集合构成了三维空间中的 xy 平面。

所以，**像**为 $\text{im}(P) = \{ (x,y,0) \mid x,y \in \mathbb{R} \}$。它的维度是2。

***

**几何直觉**：
* 投影**将所有点压平到 xy 平面**。
* **核**包含了所有“消失”的点，即那些被压平后变成原点的点。在三维空间中，只有位于 z 轴上的点才能满足这个条件。
* **像**是所有投影结果的集合，也就是 xy 平面本身。

# 问题 17

> Prove that $\ker(T)$ and $\text{im}(T)$ are always subspaces. 
> 
> 证明 $\ker(T)$ 和 $\text{im}(T)$ 始终是子空间。

要证明**核 (kernel)** 和**像 (image)** 始终是**子空间 (subspace)**，我们需要验证它们是否满足子空间定义中的三个条件。

一个集合 $W$ 是向量空间 $V$ 的子空间，如果它满足：
1.  **零向量闭合**：零向量 $\mathbf{0}$ 属于 $W$。
2.  **加法闭合**：如果向量 $\mathbf{u}$ 和 $\mathbf{v}$ 属于 $W$，那么它们的和 $\mathbf{u} + \mathbf{v}$ 也属于 $W$。
3.  **标量乘法闭合**：如果向量 $\mathbf{u}$ 属于 $W$，那么对于任意标量 $c$，向量 $c\mathbf{u}$ 也属于 $W$。

我们用这些条件来分别证明 $\ker(T)$ 和 $\text{im}(T)$。

---

### 证明 $\ker(T)$ 是子空间

假设 $T: V \to W$ 是一个线性变换。**核 $\ker(T)$** 是 $V$ 中所有被 $T$ 映射到 $W$ 中零向量的向量的集合。即 $\ker(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W \}$。

1.  **零向量闭合**
    我们需要证明 $V$ 的零向量 $\mathbf{0}_V$ 属于 $\ker(T)$。
    根据线性变换的性质，我们知道 $T(\mathbf{0}_V) = \mathbf{0}_W$。
    因此，$\mathbf{0}_V$ 满足核的定义，它属于 $\ker(T)$。

2.  **加法闭合**
    设 $\mathbf{u}$ 和 $\mathbf{v}$ 是 $\ker(T)$ 中的任意两个向量。
    根据定义，我们有 $T(\mathbf{u}) = \mathbf{0}_W$ 和 $T(\mathbf{v}) = \mathbf{0}_W$。
    因为 $T$ 是一个线性变换，它满足加法可分配性：
    $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W$
    因此，向量 $\mathbf{u} + \mathbf{v}$ 也被映射到零向量，所以它属于 $\ker(T)$。

3.  **标量乘法闭合**
    设 $\mathbf{u}$ 是 $\ker(T)$ 中的一个向量，而 $c$ 是任意标量。
    根据定义，我们有 $T(\mathbf{u}) = \mathbf{0}_W$。
    因为 $T$ 是一个线性变换，它满足齐次性：
    $T(c\mathbf{u}) = cT(\mathbf{u}) = c \cdot \mathbf{0}_W = \mathbf{0}_W$
    因此，向量 $c\mathbf{u}$ 也被映射到零向量，所以它属于 $\ker(T)$。

所有三个条件都满足，因此 $\ker(T)$ 是 $V$ 的一个子空间。

---

### 证明 $\text{im}(T)$ 是子空间

**像 $\text{im}(T)$** 是 $W$ 中所有由 $T$ 变换而来的向量的集合。即 $\text{im}(T) = \{ \mathbf{w} \in W \mid \mathbf{w} = T(\mathbf{v}) \text{ for some } \mathbf{v} \in V \}$。

1.  **零向量闭合**
    我们需要证明 $W$ 的零向量 $\mathbf{0}_W$ 属于 $\text{im}(T)$。
    我们知道 $T(\mathbf{0}_V) = \mathbf{0}_W$。这意味着存在一个向量（即 $\mathbf{0}_V$），它经过 $T$ 的变换后得到了 $\mathbf{0}_W$。
    因此，$\mathbf{0}_W$ 属于 $\text{im}(T)$。

2.  **加法闭合**
    设 $\mathbf{w}_1$ 和 $\mathbf{w}_2$ 是 $\text{im}(T)$ 中的任意两个向量。
    根据定义，存在向量 $\mathbf{v}_1, \mathbf{v}_2 \in V$，使得 $T(\mathbf{v}_1) = \mathbf{w}_1$ 和 $T(\mathbf{v}_2) = \mathbf{w}_2$。
    我们想证明 $\mathbf{w}_1 + \mathbf{w}_2$ 属于 $\text{im}(T)$。
    利用 $T$ 的加法可分配性：
    $\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{v}_1) + T(\mathbf{v}_2) = T(\mathbf{v}_1 + \mathbf{v}_2)$
    因为 $\mathbf{v}_1 + \mathbf{v}_2$ 属于 $V$，所以 $\mathbf{w}_1 + \mathbf{w}_2$ 是 $V$ 中某个向量经过 $T$ 变换后的结果。
    因此，$\mathbf{w}_1 + \mathbf{w}_2$ 属于 $\text{im}(T)$。

3.  **标量乘法闭合**
    设 $\mathbf{w}$ 是 $\text{im}(T)$ 中的一个向量，而 $c$ 是任意标量。
    根据定义，存在向量 $\mathbf{v} \in V$，使得 $T(\mathbf{v}) = \mathbf{w}$。
    我们想证明 $c\mathbf{w}$ 属于 $\text{im}(T)$。
    利用 $T$ 的齐次性：
    $c\mathbf{w} = cT(\mathbf{v}) = T(c\mathbf{v})$
    因为 $c\mathbf{v}$ 属于 $V$，所以 $c\mathbf{w}$ 是 $V$ 中某个向量经过 $T$ 变换后的结果。
    因此，$c\mathbf{w}$ 属于 $\text{im}(T)$。

所有三个条件都满足，因此 $\text{im}(T)$ 是 $W$ 的一个子空间。

# 问题 18

> Linear transformations can look very different depending on the coordinate system we use. The process of rewriting vectors and transformations relative to a new basis is called a change of basis. This concept lies at the heart of diagonalization, orthogonalization, and many computational techniques.
> 
> 根据我们使用的坐标系，线性变换看起来可能非常不同。相对于新的基重写向量和变换的过程称为基变换。这个概念是对角化、正交化以及许多计算技术的核心。

这段话的核心思想是：**线性变换的矩阵表示不是唯一的，它取决于我们选择的坐标系（基）。理解基的变换，能帮助我们简化复杂的数学问题。**

---

### 1. 线性变换的“变脸”

**“Linear transformations can look very different depending on the coordinate system we use.”**

一个线性变换本身是一个几何操作，比如旋转或拉伸，它在空间中是固定的。但当我们用矩阵来描述它时，这个矩阵的**形式**会随着我们选择的基不同而改变。这就像一个物体在不同的光照下，看起来颜色深浅不一，但物体本身没有变。矩阵就是这个“光照”，它提供了我们观察线性变换的视角。

### 2. 什么是基变换？

**“The process of rewriting vectors and transformations relative to a new basis is called a change of basis.”**

**基变换**就是将一个向量或一个线性变换的矩阵，从一个旧的坐标系（旧基）转换到另一个新的坐标系（新基）的过程。这个过程通常通过一个**过渡矩阵**（change-of-basis matrix）来实现。

* **向量的基变换**：一个向量在旧基下的坐标，可以通过乘以过渡矩阵来得到在新基下的坐标。
* **矩阵的基变换**：一个线性变换在旧基下的矩阵，可以通过一个称为“相似变换”或“共轭”的操作，来得到在新基下的矩阵。它的形式是 $A' = P^{-1}AP$，其中 $A$ 是旧矩阵，$A'$ 是新矩阵，$P$ 是过渡矩阵。

### 3. 基变换的重要性

**“This concept lies at the heart of diagonalization, orthogonalization, and many computational techniques.”**

这段话指出了基变换的实际应用价值。我们之所以要做基变换，不是为了好玩，而是为了**简化问题**。

* **对角化 (Diagonalization)**：这是一种特殊的基变换。如果一个线性变换可以用对角矩阵表示，那么它的计算会变得极其简单。对角矩阵只在主对角线上有非零元素，这使得求幂、求逆等操作变得轻而易举。对角化的关键是找到一组**特征向量**作为新的基。在这个新的坐标系中，变换只是简单的拉伸或压缩，没有旋转或剪切。
* **正交化 (Orthogonalization)**：这是另一种重要的基变换。通过将一组向量转换为正交基（向量两两垂直），我们可以简化投影、最小二乘法等计算。
* **计算技术**：在机器学习、信号处理、计算机图形学等领域，基变换被广泛应用。例如，**主成分分析 (PCA)** 就是通过基变换找到数据的主要变化方向，从而实现降维和数据压缩。

总而言之，这段话告诉我们，矩阵的表示是相对的，而基变换是寻找**最优**矩阵表示的方法。这个最优的矩阵（例如对角矩阵）能让我们更容易地理解和操作线性变换。

# 问题 19

> 基变换矩阵必须是可逆的吗？

是的，这里的矩阵 $P$ 必须是**可逆**的。


$P$ 是从基 $\mathcal{B} = \{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ 到标准基的**基变换矩阵**。根据定义，它的列就是基向量 $\mathbf{v}_1, \dots, \mathbf{v}_n$。

一个矩阵可逆的充分必要条件是其**列向量是线性无关的**。由于 $\mathcal{B}$ 是一个**基**，其定义本身就保证了集合中的所有向量是线性无关的。因此，矩阵 $P$ 的列向量 $\mathbf{v}_1, \dots, \mathbf{v}_n$ 必定是线性无关的。

因为 $P$ 的列是线性无关的，所以 $P$ 是可逆的。这确保了从一个坐标系到另一个坐标系的转换是**一对一**的，并且是可逆的。如果 $P$ 不可逆，那么不同的向量在 $\mathcal{B}$ 下可能有相同的坐标，这与基的唯一性定义相矛盾。

# 问题 20

> $$
\mathbf{x} = P [\mathbf{x}]_{\mathcal{B}}.
$$


让我们来详细解释这个等式的含义。

### 等式左侧：$\mathbf{x}$
这里的 $\mathbf{x}$ 是向量本身。它是在**标准基**下的坐标向量。例如，在 $\mathbb{R}^2$ 中，向量 $\mathbf{x} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ 就表示“从原点开始，向右走 3 个单位，向上走 4 个单位”。这里的 3 和 4 就是它在标准基 $\{(1,0), (0,1)\}$ 下的坐标。

### 等式右侧：$P [\mathbf{x}]_{\mathcal{B}}$
* **$P$**：这是一个**过渡矩阵**（change-of-basis matrix），它的列是新基 $\mathcal{B}$ 的向量。这个矩阵的作用是把新基下的坐标**转换回**标准基下的坐标。
* **$[\mathbf{x}]_{\mathcal{B}}$**：这是向量 $\mathbf{x}$ 在**新基** $\mathcal{B}$ 下的**坐标向量**。

### 总结

所以，等式 $\mathbf{x} = P [\mathbf{x}]_{\mathcal{B}}$ 的真正含义是：

> **一个向量在标准基下的坐标，等于它的新基坐标向量乘以一个过渡矩阵。**

这个等式描述了从一个坐标系（新基 $\mathcal{B}$）转换到另一个坐标系（标准基）的过程。它告诉我们，要找到一个向量在标准基下的坐标，我们只需知道它在新基下的坐标，然后用矩阵 $P$ 转换即可。

> $$
[\mathbf{x}]_{\mathcal{B}} = P^{-1} \mathbf{x}.
$$

这个等式描述了将一个向量的**标准基坐标**转换成**新基坐标**的过程。

---

### 等式各部分的含义

* **$\mathbf{x}$**：向量 $\mathbf{x}$ 在**标准基**下的坐标向量。例如，在 $\mathbb{R}^n$ 中，它就是向量本身。
* **$[\mathbf{x}]_{\mathcal{B}}$**：向量 $\mathbf{x}$ 在**新基** $\mathcal{B}$ 下的坐标向量。
* **$P$**：这是一个**过渡矩阵**（change-of-basis matrix），它的列是新基 $\mathcal{B}$ 的向量。它将新基坐标转换回标准基坐标，即 $\mathbf{x} = P [\mathbf{x}]_{\mathcal{B}}$。
* **$P^{-1}$**：矩阵 $P$ 的逆矩阵。它的作用正好相反，它将标准基坐标转换成新基坐标。

---

### 转换过程的逻辑

理解这个等式，可以从矩阵 $P$ 的作用来思考：
* $P$ 是一个“**新到旧**”的转换器。它把新基下的坐标（$[\mathbf{x}]_{\mathcal{B}}$）转换成旧基（标准基）下的坐标（$\mathbf{x}$）。
* 因此，它的逆矩阵 $P^{-1}$ 自然就是一个“**旧到新**”的转换器。它把旧基（标准基）下的坐标（$\mathbf{x}$）转换成新基下的坐标（$[\mathbf{x}]_{\mathcal{B}}$）。

---

### 类比

想象你有两个坐标系：一个是我们熟悉的南北-东西坐标系（标准基），另一个是东北-西北-西南-东南坐标系（新基）。

* $P$ 就像一个“**翻译**”工具，它能把东北-西北坐标系下的指示（例如，向东北方向走 5 步）转换成南北-东西坐标系下的指示（向东 3.5 步，向北 3.5 步）。
* $P^{-1}$ 就是这个工具的“**逆向翻译**”版本，它能把南北-东西坐标系下的指示（例如，向东 5 步）转换成东北-西北坐标系下的指示（向东南方向走 3.5 步，向东北方向走 3.5 步）。

等式 $ [\mathbf{x}]_{\mathcal{B}} = P^{-1} \mathbf{x}$ 描述的就是这个**从旧坐标系到新坐标系**的转换过程。

# 问题 21

> ### Transformation of Matrices
> 矩阵变换
> 
> Let $T: V \to V$ be a linear transformation. Suppose its matrix in the standard basis is $A$. In the basis $\mathcal{B}$, the representing matrix becomes
> 
> 令 $T: V \to V$ 为线性变换。假设其在标准基中的矩阵为 $A$ 。在基 $\mathcal{B}$ 中，表示矩阵变为
> 
> $$
[T]_{\mathcal{B}} = P^{-1} A P.
$$
> 
> Thus, changing basis corresponds to a similarity transformation of the matrix.
> 
> 因此，改变基对应于矩阵的相似变换。


这段话的核心是解释**线性变换的矩阵表示**如何随着**基的变化**而改变。它指出了一个关键的公式：$A' = P^{-1}AP$。

我们可以分三部分来理解这个概念。

---

### 1. 不同的基，不同的矩阵

**“Let $T: V \to V$ be a linear transformation. Suppose its matrix in the standard basis is $A$. In the basis $\mathcal{B}$, the representing matrix becomes $[T]_{\mathcal{B}}$.”**

* **线性变换 $T$** 是一个抽象的几何操作（如旋转、缩放），它本身不依赖于任何坐标系。
* **矩阵表示**是这个操作在特定坐标系中的“坐标”。例如，矩阵 $A$ 是 $T$ 在标准基（我们最熟悉的直角坐标系）下的表示。
* **基 $\mathcal{B}$** 是一个新的坐标系。在新的坐标系下，同一个变换 $T$ 会有一个新的矩阵表示，我们称之为 $[T]_{\mathcal{B}}$ 或 $A'$。

想象一下你站在不同的角度看一个物体，物体本身没变，但它在你的视野中的样子变了。矩阵就是这个“视野中的样子”。

---

### 2. 基变换的公式

**“$$[T]_{\mathcal{B}} = P^{-1} A P$$”**

这个公式是连接新旧矩阵的关键。它描述了如何用旧矩阵 $A$ 来计算新矩阵 $[T]_{\mathcal{B}}$。这里的核心是**过渡矩阵 $P$**：

* **$P$** 是从**新基 $\mathcal{B}$** 到**旧基（标准基）**的过渡矩阵。它的列是新基向量在旧基下的坐标。
* **$P^{-1}$** 是 $P$ 的逆矩阵，它将旧基下的坐标转换回新基下的坐标。

**理解公式的几何意义**：$P^{-1}AP$ 描述了一个三步走的“绕道”操作：
1.  **$P$**：将一个向量从新基坐标系**转换到**旧基坐标系。
2.  **$A$**：在旧基坐标系下**执行**线性变换 $T$。
3.  **$P^{-1}$**：将变换后的结果**转换回**新基坐标系。

这三个步骤合起来，就相当于直接在新基坐标系中执行了变换 $T$。因此，矩阵 $[T]_{\mathcal{B}}$ 实现了直接的转换。

### 3. 相似变换

**“Thus, changing basis corresponds to a similarity transformation of the matrix.”**

矩阵 $A$ 和 $[T]_{\mathcal{B}}$ 是**相似**的（similar）。相似矩阵代表**同一个线性变换**，只是在**不同的基**下。

**相似变换** $A' = P^{-1}AP$ 在线性代数中至关重要。它的主要目的就是寻找一个**最简单**的矩阵表示，通常是对角矩阵。如果一个矩阵可以被对角化（即可找到一个可逆矩阵 $P$ 使得 $P^{-1}AP$ 是对角矩阵），那么在这个对角矩阵所对应的基下，线性变换就是简单的拉伸或压缩，没有旋转或剪切。这极大地简化了矩阵运算，也是**特征值和特征向量**理论的核心。

# 问题 22

> Let
> 
> 令
> 
> $$
A = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}
$$
> 
> Compute its representation in the basis $\{(1,0),(1,1)\}$. 
> 
> 计算其在基 $\{(1,0),(1,1)\}$ 中的表示。

该问题的目标是找到一个线性变换在**新基**下的矩阵表示。这个线性变换由矩阵 $A$ 在**标准基**下定义。

我们可以使用**相似变换**公式来解决这个问题：
$$A' = P^{-1}AP$$
其中：
* $A$ 是在标准基下的旧矩阵。
* $A'$ 是在新基下的新矩阵。
* $P$ 是从新基到标准基的过渡矩阵。

### 1. 找到过渡矩阵 $P$

过渡矩阵 $P$ 的列是新基向量在标准基下的坐标。
新基为 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2\}$, 其中 $\mathbf{v}_1 = (1,0)$ 和 $\mathbf{v}_2 = (1,1)$。
所以，
$$
P = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

### 2. 计算 $P$ 的逆矩阵 $P^{-1}$

对于一个 $2 \times 2$ 矩阵 $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$，其逆矩阵为 $M^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$。
对于矩阵 $P$，行列式为 $\det(P) = (1)(1) - (1)(0) = 1$。
$$
P^{-1} = \frac{1}{1} \begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}
= \begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}
$$

### 3. 计算新矩阵 $A' = P^{-1}AP$

现在，我们将所有矩阵相乘：
$$
\begin{aligned}
A' &= \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \\
&= \begin{bmatrix} (1)(2)+(-1)(0) & (1)(1)+(-1)(2) \\ (0)(2)+(1)(0) & (0)(1)+(1)(2) \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \\
&= \begin{bmatrix} 2 & -1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \\
&= \begin{bmatrix} (2)(1)+(-1)(0) & (2)(1)+(-1)(1) \\ (0)(1)+(2)(0) & (0)(1)+(2)(1) \end{bmatrix} \\
&= \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}
\end{aligned}
$$

### 结论

因此，在基 $\{(1,0),(1,1)\}$ 中，矩阵 $A = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$ 的表示仍然是它本身，即 $A' = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$。

**这有点出人意料，因为通常基变换会改变矩阵。** 让我们验证一下。

我们也可以用另一种方法验证。我们需要找出变换作用在新基向量上的结果，并用新基来表示这些结果。

* **对新基向量 $\mathbf{v}_1=(1,0)$ 进行变换**：

    $A\mathbf{v}_1 = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}$

    我们需要用新基 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2\}$ 来表示结果 $\begin{bmatrix} 2 \\ 0 \end{bmatrix}$：

    $\begin{bmatrix} 2 \\ 0 \end{bmatrix} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 = c_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ 1 \end{bmatrix} \Rightarrow \begin{cases} c_1+c_2=2 \\ c_2=0 \end{cases}$

    解得 $c_1=2, c_2=0$。所以，结果在新基下的坐标是 $\begin{pmatrix} 2 \\ 0 \end{pmatrix}$。这是新矩阵的第一列。

* **对新基向量 $\mathbf{v}_2=(1,1)$ 进行变换**：
    $A\mathbf{v}_2 = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$

    我们需要用新基 $\mathcal{B}$ 来表示结果 $\begin{bmatrix} 3 \\ 2 \end{bmatrix}$：

    $\begin{bmatrix} 3 \\ 2 \end{bmatrix} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 = c_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ 1 \end{bmatrix} \Rightarrow \begin{cases} c_1+c_2=3 \\ c_2=2 \end{cases}$

    解得 $c_1=1, c_2=2$。所以，结果在新基下的坐标是 $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$。这是新矩阵的第二列。

将这两列组合起来，得到新矩阵：
$$A' = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$$
这与我们使用相似变换公式得到的结果完全一致。

# 问题 23

> Find the change-of-basis matrix from the standard basis of $\mathbb{R}^2$ to $\{(2,1),(1,1)\}$. 
> 
> 求出从 $\mathbb{R}^2$ 到 $\{(2,1),(1,1)\}$ 的标准基变换矩阵。

好的，我们来求从 $\mathbb{R}^2$ 的标准基到新基 $\mathcal{B} = \{(2,1), (1,1)\}$ 的变换矩阵。

---

### 1. 理解基变换

首先，我们需要明确两种基变换矩阵：
1.  **从新基到标准基**的矩阵（我们称之为 $P$）。
2.  **从标准基到新基**的矩阵（我们称之为 $P^{-1}$）。

问题要求的是**从标准基到新基**的变换矩阵。这个矩阵的作用是，如果你有一个向量在标准基下的坐标，用它乘以这个矩阵，就能得到它在新基下的坐标。

### 2. 构建从新基到标准基的矩阵 $P$

根据定义，**从新基到标准基的过渡矩阵 $P$** 的列就是新基的向量。
新基为 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2\}$, 其中 $\mathbf{v}_1 = (2,1)$ 和 $\mathbf{v}_2 = (1,1)$。
所以，
$$
P = \begin{pmatrix}
2 & 1 \\
1 & 1
\end{pmatrix}
$$

### 3. 求 $P$ 的逆矩阵 $P^{-1}$

我们要求的是**从标准基到新基**的变换矩阵，这正是 $P$ 的逆矩阵 $P^{-1}$。

对于一个 $2 \times 2$ 矩阵 $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$，其逆矩阵为 $M^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$。

对于矩阵 $P$，行列式为 $\det(P) = (2)(1) - (1)(1) = 1$。

因此，
$$
P^{-1} = \frac{1}{1} \begin{pmatrix}
1 & -1 \\
-1 & 2
\end{pmatrix}
= \begin{pmatrix}
1 & -1 \\
-1 & 2
\end{pmatrix}
$$

### 4. 结论

这个矩阵 $P^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$ 就是**从标准基到新基 $\mathcal{B}$ 的基变换矩阵**。

**验证**
让我们用一个向量来验证。例如，标准基下的向量 $\mathbf{x} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$。

用 $P^{-1}$ 变换它：
$$
\begin{pmatrix}
1 & -1 \\
-1 & 2
\end{pmatrix}
\begin{pmatrix}
3 \\
2
\end{pmatrix}
= \begin{pmatrix}
1(3) + (-1)(2) \\
-1(3) + 2(2)
\end{pmatrix}
= \begin{pmatrix}
1 \\
1
\end{pmatrix}
$$
这意味着向量 $(3,2)$ 在新基下的坐标是 $(1,1)$。我们可以用新基来检验这个结果：
$1 \cdot (2,1) + 1 \cdot (1,1) = (2+1, 1+1) = (3,2)$

结果正确。

# 问题 24

> Prove that similar matrices (related by $P^{-1}AP$) represent the same linear transformation under different bases. 
> 
> 证明相似的矩阵（由 $P^{-1}AP$ 关联）在不同基下表示相同的线性变换。

我们来证明这个核心概念：**相似矩阵表示相同的线性变换**。

为了证明这一点，我们不需要使用任何特定的矩阵或基，只需要使用**基变换的定义**和**矩阵乘法**的性质。

### 1. 设定情境

假设我们有一个线性变换 $T: V \to V$。
* 在标准基 $\mathcal{E}$ 下，这个变换由矩阵 $A$ 表示。也就是说，对于任意向量 $\mathbf{x}$，我们有 $T(\mathbf{x}) = A\mathbf{x}$。这里的 $\mathbf{x}$ 和 $T(\mathbf{x})$ 都是在标准基下的坐标。
* 我们有一个新的基 $\mathcal{B}$。
* $P$ 是从新基 $\mathcal{B}$ 到标准基 $\mathcal{E}$ 的过渡矩阵。
* 我们想证明，在新基 $\mathcal{B}$ 下，这个变换由矩阵 $A' = P^{-1}AP$ 表示。

### 2. 证明过程

要证明 $A'$ 是 $T$ 在新基 $\mathcal{B}$ 下的矩阵，我们必须证明对于任何在新基 $\mathcal{B}$ 下表示为 $[\mathbf{x}]_{\mathcal{B}}$ 的向量，应用 $A'$ 得到的向量就是 $T(\mathbf{x})$ 在新基 $\mathcal{B}$ 下的表示。

即，我们必须证明：
$$A' [\mathbf{x}]_{\mathcal{B}} = [T(\mathbf{x})]_{\mathcal{B}}$$

现在，我们用基变换的公式来逐步推导：

1.  **将 $[\mathbf{x}]_{\mathcal{B}}$ 转换到标准基**
    向量 $\mathbf{x}$ 在新基下的坐标是 $[\mathbf{x}]_{\mathcal{B}}$。要将它转换到标准基，我们使用过渡矩阵 $P$：
    $$\mathbf{x} = P [\mathbf{x}]_{\mathcal{B}}$$

2.  **在标准基下应用线性变换**
    现在，向量 $\mathbf{x}$ 在标准基下。我们可以使用标准基下的矩阵 $A$ 来进行变换：
    $$T(\mathbf{x}) = A\mathbf{x}$$
    将上一步的结果代入，我们得到：
    $$T(\mathbf{x}) = A(P[\mathbf{x}]_{\mathcal{B}}) = AP[\mathbf{x}]_{\mathcal{B}}$$
    这个结果 $T(\mathbf{x})$ 仍然在标准基下。

3.  **将结果转换回新基**
    我们想要的是变换结果在**新基**下的坐标，也就是 $[T(\mathbf{x})]_{\mathcal{B}}$。要做到这一点，我们使用 $P$ 的逆矩阵 $P^{-1}$：
    $$[T(\mathbf{x})]_{\mathcal{B}} = P^{-1} T(\mathbf{x})$$
    将上一步的结果代入，我们得到：
    $$[T(\mathbf{x})]_{\mathcal{B}} = P^{-1} (AP[\mathbf{x}]_{\mathcal{B}}) = (P^{-1}AP) [\mathbf{x}]_{\mathcal{B}}$$

### 4. 结论

我们最终推导出了：
$$[T(\mathbf{x})]_{\mathcal{B}} = (P^{-1}AP) [\mathbf{x}]_{\mathcal{B}}$$

这证明了矩阵 $P^{-1}AP$ 确实将新基下的向量 $[\mathbf{x}]_{\mathcal{B}}$ 转换成了变换后的向量在新基下的坐标 $[T(\mathbf{x})]_{\mathcal{B}}$。

因此，矩阵 $A' = P^{-1}AP$ **就是**线性变换 $T$ 在新基 $\mathcal{B}$ 下的矩阵表示。这证明了**相似矩阵在不同基下表示相同的线性变换**。

# 问题 25

> Diagonalize the matrix
> 
> 对角化矩阵
> 
> $$
A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
$$
> 
> in the basis $\{(1,1),(1,-1)\}$. 
> 
> 在基 $\{(1,1),(1,-1)\}$ 中。

为了找到矩阵 $A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ 在新基 $\mathcal{B} = \{(1,1), (1,-1)\}$ 中的表示，我们可以使用**相似变换**公式：
$$A' = P^{-1}AP$$
其中：
* $A$ 是在标准基下的旧矩阵。
* $A'$ 是在新基 $\mathcal{B}$ 下的新矩阵。
* $P$ 是从新基 $\mathcal{B}$ 到标准基的过渡矩阵。

---

### 1. 找到过渡矩阵 $P$

过渡矩阵 $P$ 的列就是新基向量在标准基下的坐标。
新基为 $\mathbf{v}_1 = (1,1)$ 和 $\mathbf{v}_2 = (1,-1)$。
所以，
$$
P = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

---

### 2. 找到 $P$ 的逆矩阵 $P^{-1}$

对于一个 $2 \times 2$ 矩阵 $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$，其逆矩阵为 $M^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$。
对于矩阵 $P$，行列式为 $\det(P) = (1)(-1) - (1)(1) = -1 - 1 = -2$。
$$
P^{-1} = \frac{1}{-2} \begin{bmatrix}
-1 & -1 \\
-1 & 1
\end{bmatrix}
= \begin{bmatrix}
1/2 & 1/2 \\
1/2 & -1/2
\end{bmatrix}
$$

---

### 3. 计算新矩阵 $A' = P^{-1}AP$

现在，我们将所有矩阵相乘：
$$
\begin{aligned}
A' &= P^{-1}AP \\
&= \begin{bmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \\
&= \begin{bmatrix} 1/2 & -1/2 \\ 1/2 & 1/2 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \\
&= \begin{bmatrix} (1/2)(1)+(-1/2)(1) & (1/2)(1)+(-1/2)(-1) \\ (1/2)(1)+(1/2)(1) & (1/2)(1)+(1/2)(-1) \end{bmatrix} \\
&= \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
\end{aligned}
$$

---

### 结论

在基 $\{(1,1),(1,-1)\}$ 中，矩阵 $A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ 的表示是 $A' = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$。

**思考一下这个结果的几何意义。**（TODO：没看懂）
* 矩阵 $A$ 在标准基下表示的是**沿 y 轴的反射**。
* 矩阵 $A'$ 是一种**基变换**后的表示。它表示在新基 $\mathcal{B}$ 下的同样一个变换。
* 矩阵 $A'$ 恰好是**沿线 $y=x$ 的反射矩阵**。这表明，在某种意义上，沿 y 轴的反射和沿线 $y=x$ 的反射是“等价”的，它们通过基变换相互关联。
* 更有趣的是，如果我们将新基中的向量看作特征向量，那么 $A\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix} = -1 \cdot \mathbf{v}_2$ 和 $A\mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} = 1 \cdot \mathbf{v}_1$，这表明这两个向量是**特征向量**，而新基下的矩阵 $A'$ 应该是一个对角矩阵。但这里的结果不是对角矩阵。这说明，虽然这两个基向量是特征向量，但它们与特征值不是简单的对应关系，我们需要重新审视。
* 让我们再看一下：$A\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$。$A\mathbf{v}_1 = \mathbf{v}_2$。
    $A\mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$。$A\mathbf{v}_2 = \mathbf{v}_1$。
    那么在基 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2\}$ 下，
    * $T(\mathbf{v}_1)$ 的坐标是 $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$（因为 $T(\mathbf{v}_1) = 0 \cdot \mathbf{v}_1 + 1 \cdot \mathbf{v}_2$）。这是新矩阵的第一列。
    * $T(\mathbf{v}_2)$ 的坐标是 $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$（因为 $T(\mathbf{v}_2) = 1 \cdot \mathbf{v}_1 + 0 \cdot \mathbf{v}_2$）。这是新矩阵的第二列。
    所以，新矩阵是 $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$。这与我们的计算结果完全一致。这个矩阵**确实**表示了沿 $y=x$ 的反射。

因此，矩阵 $A = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ 在基 $\{(1,1),(1,-1)\}$ 中的表示是 $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$。

# 问题 26

> In $\mathbb{R}^3$, let $\mathcal{B} = \{(1,0,0),(1,1,0),(1,1,1)\}$. Construct the change-of-basis matrix $P$ and compute $P^{-1}$.
> 
> 在 $\mathbb{R}^3$ 中，令 $\mathcal{B} = \{(1,0,0),(1,1,0),(1,1,1)\}$ 。构造基变换矩阵 $P$ 并计算 $P^{-1}$ 。

首先，我们需要确定基变换矩阵 $P$ 和它的逆矩阵 $P^{-1}$。

### 1. 构造基变换矩阵 $P$
根据定义，从新基 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ 到标准基的过渡矩阵 $P$ 的列就是新基的向量。
这里，新基向量是 $\mathbf{v}_1 = (1,0,0)$, $\mathbf{v}_2 = (1,1,0)$, 和 $\mathbf{v}_3 = (1,1,1)$。
因此，矩阵 $P$ 为：
$$
P = \begin{bmatrix}
1 & 1 & 1 \\
0 & 1 & 1 \\
0 & 0 & 1
\end{bmatrix}
$$

### 2. 计算 $P$ 的逆矩阵 $P^{-1}$
我们可以使用增广矩阵 $[P | I]$ 并通过行简化来求出 $P^{-1}$。
$$
[P | I] = \left[
\begin{array}{ccc|ccc}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 & 0 & 1
\end{array}
\right]
$$
**步骤 1：** 将第一行与第二行相减，并将第一行与第三行相减。
* $R_1 \to R_1 - R_2$：
$$
\left[
\begin{array}{ccc|ccc}
1 & 0 & 0 & 1 & -1 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 & 0 & 1
\end{array}
\right]
$$
**步骤 2：** 将第二行与第三行相减。
* $R_2 \to R_2 - R_3$：

$$
\left[
\begin{array}{ccc|ccc}
1 & 0 & 0 & 1 & -1 & 0 \\
0 & 1 & 0 & 0 & 1 & -1 \\
0 & 0 & 1 & 0 & 0 & 1
\end{array}
\right]
$$

左侧的矩阵现在是单位矩阵，所以右侧的矩阵就是 $P^{-1}$。

$$
P^{-1} = \begin{bmatrix}
1 & -1 & 0 \\
0 & 1 & -1 \\
0 & 0 & 1
\end{bmatrix}
$$

**验证**

我们可以通过计算 $P P^{-1}$ 来验证结果是否正确。
$$
P P^{-1} = \begin{bmatrix}
1 & 1 & 1 \\
0 & 1 & 1 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & -1 & 0 \\
0 & 1 & -1 \\
0 & 0 & 1
\end{bmatrix} = \begin{bmatrix}
1\cdot 1+1\cdot 0+1\cdot 0 & 1\cdot (-1)+1\cdot 1+1\cdot 0 & 1\cdot 0+1\cdot (-1)+1\cdot 1 \\
0\cdot 1+1\cdot 0+1\cdot 0 & 0\cdot (-1)+1\cdot 1+1\cdot 0 & 0\cdot 0+1\cdot (-1)+1\cdot 1 \\
0\cdot 1+0\cdot 0+1\cdot 0 & 0\cdot (-1)+0\cdot 1+1\cdot 0 & 0\cdot 0+0\cdot (-1)+1\cdot 1
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$
结果是单位矩阵，所以 $P^{-1}$ 计算正确。

### Chatgpt

先把基向量按列写成矩阵（这是从 $ \mathcal B$-坐标到标准坐标的变换矩阵）：

$$
P=\begin{bmatrix}
1 & 1 & 1\\[4pt]
0 & 1 & 1\\[4pt]
0 & 0 & 1
\end{bmatrix},
$$

因为 $(1,0,0)^T,(1,1,0)^T,(1,1,1)^T$ 分别为 $P$ 的第1、2、3 列。

计算逆矩阵（也可以通过解线性方程或分块/回代法得到）：

$$
P^{-1}=\begin{bmatrix}
1 & -1 & 0\\[4pt]
0 & 1 & -1\\[4pt]
0 & 0 & 1
\end{bmatrix}.
$$

检验：$P P^{-1}=I_3$（可逐项乘开验证），因此以上 $P$ 与 $P^{-1}$ 正确。

说明：若 $v$ 为任意标准坐标下的列向量，则 $P^{-1}v$ 给出 $v$ 在基 $\mathcal B$ 下的坐标。
