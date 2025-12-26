# 矩阵特征值的实际应用

## 1、高斯消元（初等行变换）解方程

原方程如下:

$$
\begin{cases}
-x_1 + x_2 = 0 \\
x_1 - x_2 = 0
\end{cases}
$$

写成矩阵形式 $Ax=0$：
$$
\begin{pmatrix}
-1 & 1 \\
1 & -1
\end{pmatrix}
\mathbf{x}=0
$$

写成增广矩阵（右边是 0）：
$$
\left[
\begin{array}{cc|c}
-1 & 1 & 0\\
1 & -1 & 0
\end{array}
\right]
$$


第一步，交换两行（方便一点）：
$$
R_1 \leftrightarrow R_2
\Rightarrow
\left[
\begin{array}{cc|c}
1 & -1 & 0\\
-1 & 1 & 0
\end{array}
\right]
$$


第二步，用第一行消去第二行：
$$
R_2 \leftarrow R_2 + R_1
$$

得到：
$$
\left[
\begin{array}{cc|c}
1 & -1 & 0\\
0 & 0 & 0
\end{array}
\right]
$$

现在已经是行阶梯形矩阵了，对应的方程是：
$$
x_1 - x_2 = 0
$$

令自由变量：$x_2 = t \quad (t\in\mathbb{R})$ 则：$x_1 = t$，所以解集为：$\mathbf{x}=\begin{pmatrix}t\\t\end{pmatrix}=t\begin{pmatrix}1\\1\end{pmatrix},\quad t\in\mathbb{R}$

## 2、特征值和特征向量

一句话版的直觉：**特征向量是在线性变换作用下，方向不变（只被拉伸或压缩）的向量。**

先从**代数角度**来看。

给定一个方阵 $A$，如果存在一个 **非零向量** $\mathbf v$ 和一个数 $\lambda$，满足$A\mathbf v = \lambda \mathbf v$ 那么：

* $\lambda$ 叫做 **特征值**
* $\mathbf v$ 叫做 **对应的特征向量**

这句话的代数含义是：
矩阵 $A$ 作用在 $\mathbf v$ 上，结果并没有“换方向”，只是变成了原来的 $\lambda$ 倍。

把式子挪一下：$(A - \lambda I)\mathbf v = 0$

这说明一件关键的事：
**特征向量就是齐次线性方程组的非零解**。

所以代数上的流程是：

1. 解方程 $\det(A - \lambda I) = 0$，得到特征值 (TODO:这里介绍下行列式)
2. 对每个特征值 $\lambda$，解 $(A - \lambda I)\mathbf v = 0$
3. 解空间（零空间）里所有非零向量，都是对应的特征向量(TODO:这里介绍下子空间，零空间)

从代数结构上看，特征向量形成的是一个**线性子空间**，称为特征子空间。

---

接着从**几何角度**来看，这里是理解的关键。

矩阵可以看成一个**线性变换**：

* 在二维里：平面 → 平面
* 在三维里：空间 → 空间

一般情况下，一个向量经过变换后：

* 长度变了
* 方向也变了（被“旋转 + 拉伸”）

但**特征向量很特殊**。

如果 $\mathbf v$ 是特征向量，那么：$A\mathbf v = \lambda \mathbf v$

几何上意味着：

* 向量仍然落在**原来的那条直线**上
* 只发生了缩放：

  * $\lambda > 1$：拉长
  * $0 < \lambda < 1$：压缩
  * $\lambda < 0$：反向再缩放
  * $\lambda = 0$：被压到原点

所以你可以这样理解：
**特征向量指出了这个线性变换“最稳定的方向”**。

在二维平面里：

* 特征向量对应的是**不被扭转的直线**
* 整个平面被“压扁 / 拉伸 / 翻折”，但这些直线方向保持不变

---

把代数和几何连起来看，会非常清晰。

* 代数上：
  $(A - \lambda I)\mathbf v = 0$ 有非零解
* 几何上：
  线性变换在某些方向上，只做伸缩，不做旋转

这也是为什么**对角矩阵**那么简单：
$$
\begin{pmatrix}
\lambda_1 & 0 \\
0 & \lambda_2
\end{pmatrix}
$$

它的特征向量就是坐标轴方向，因为：

* x 轴方向只被 $\lambda_1$ 缩放
* y 轴方向只被 $\lambda_2$ 缩放
  完全没有“混合方向”

而一般矩阵能否对角化，本质上就在问一句话：
**能不能找到一组方向，使得变换在这些方向上只是缩放？**

总结:

* 代数定义：
  特征向量是满足 $A\mathbf v = \lambda \mathbf v$ 的非零向量
* 几何意义：
  特征向量是线性变换下方向不变、只发生伸缩的向量方向
* 本质作用：
  它们揭示了矩阵最“本征”的变换方向，是对角化和很多应用的基础


## 3、一个 n 维方阵，最多有几个特征值和特征向量，最少有几个？

这是一个线性代数里的经典问题，可以从“代数重数”和“几何重数”两个层面来理解。

先说**特征值的个数**。

对一个 $n \times n$ 的方阵，特征值来自它的特征多项式，而特征多项式是一个 **n 次多项式**。

在复数域 $\mathbb C$ 上：
- 最多有 $n$ 个特征值（都不相同的情况）。
- 最少也有 **1 个特征值**（比如全部重合，只有一个不同的特征值）。

在实数域 $\mathbb R$ 上：
- 最多仍然是 $n$ 个实特征值。
- 最少可以是 **0 个实特征值**（例如二维旋转矩阵，特征值是共轭复数对）。

接下来说**特征向量的个数**。这里要特别注意：
- “特征向量的个数”如果按严格意义来讲，其实是**无穷多个**（因为一个特征向量乘以任意非零标量还是特征向量）。
- 所以通常我们讨论的是 **线性无关的特征向量个数**，也就是特征子空间的维数。

对于每一个特征值：
- 至少有 **1 个**线性无关的特征向量。
- 至多有 **该特征值的代数重数** 个线性无关特征向量。

对整个矩阵来说：
- 线性无关特征向量的**最多个数是 (n)**，此时矩阵可对角化。
- 线性无关特征向量的**最少个数是 1**（所有特征值都一样，而且只有一个方向的特征向量，比如一个 Jordan 块）。

可以简单总结成一句话，方便记忆：

* 特征值（复数域）：最多 $n$，最少 1
* 线性无关特征向量：最多 $n$，最少 1



---

**总结一下行变换视角：**

* 有一行化成了全 0 → 方程不独立
* 主元只有 1 个 → 秩为 1
* 一个自由变量 → 解空间是一条直线


## 4、特征分解（对角化）


先看一个 2×2 的矩阵：

$$
A =
\begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}
$$

这是一个很典型、而且**一定可以对角化**的矩阵。

第一步：求特征值
解特征方程
$$
\det(A - \lambda I) = 0
$$

- $I$ 是单位矩阵，指其主对角线上的元素都为 1，其余所有元素都为 0 的正方矩阵。2 维单位矩阵就是 $\begin{pmatrix} 1 & 0\\ 0&1 \end{pmatrix}$
- $\lambda I$ 就是用标量乘单位矩阵，最终得 $\begin{pmatrix} \lambda & 0\\ 0&\lambda \end{pmatrix}$
- $A - \lambda I$ 是两个相同形状矩阵的各对应元素相减 

    $\begin{pmatrix} 2 & 1\\ 1&2 \end{pmatrix} - \begin{pmatrix} \lambda & 0\\ 0&\lambda \end{pmatrix}$
    $=\begin{pmatrix} 2-\lambda & 1-0\\ 1-0 & 2-\lambda \end{pmatrix} $
    $=\begin{pmatrix} 2-\lambda & 1\\ 1 & 2-\lambda \end{pmatrix}$

- $\begin{vmatrix} \end{vmatrix}$ 这两个竖线是行列式操作，2 维方阵$\begin{pmatrix} a & b\\ c&d \end{pmatrix}$的行列式计算就是主对角线乘积减去副对角线乘积 $ad-bc$

列方程得：

$$
\begin{vmatrix}
2-\lambda & 1 \\
1 & 2-\lambda
\end{vmatrix}
= (2-\lambda)^2 - 1 = 0
$$


整理：
$$
(2-\lambda)^2 - 1 = 0\\

2^2- 2 * 2 * \lambda + \lambda ^2-1=0\\

\lambda^2-4\lambda-3=0\\

$$




解这个二次方程：

- 十字相乘法：因为二次项系数是 1
    - 直接找两个数乘积等于常数项 3，和等于一次项系数 -4
    - −1 和 −3 满足条件
    - 得 $(\lambda - 3)(\lambda - 1) = 0$
    - 得 $\lambda_1 = 3,\quad \lambda_2 = 1$
- 配方：
    $$
    \lambda^2 - 4\lambda + 3 = 0\\
    (λ^2 − 4λ + 4) − 4 + 3 = 0 \\
    (λ − 2)^2-1 = 0 \\
    (λ − 2 − 1)(λ − 2 + 1)= 0\\
    (λ − 3)(λ − 1)=0
    $$
     - 得 $\lambda_1 = 3,\quad \lambda_2 = 1$


这一步告诉我们：
矩阵 (A) 在两个“特殊方向”上，只做拉伸（不发生旋转或剪切）。

第二步：求特征向量

由特征值的定义 $Av=λv$，得 $Av-λv=0$，简化得 $(A-λI)v=0$

对 $\lambda_1 = 3$，解
$$
(A - 3I)\mathbf{x} = 0
$$

$$
\left[\begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}
- 3\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}\right]
\mathbf{x} = 0
$$

$$
\left[\begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}
- \begin{pmatrix}
3 & 0 \\
0 & 3
\end{pmatrix}\right]
\mathbf{x} = 0
$$

$$
\begin{pmatrix}
2-3 & 1-0 \\
1-0 & 2-3
\end{pmatrix}
\mathbf{x} = 0
$$

$$
\begin{pmatrix}
-1 & 1 \\
1 & -1
\end{pmatrix}
\mathbf{x} = 0
$$

解特征向量 x：

设
$$
\mathbf{x}=\begin{pmatrix}x_1\\ x_2\end{pmatrix}
$$

那么

$$
\begin{pmatrix}
-1 & 1 \\
1 & -1
\end{pmatrix}
\begin{pmatrix}x_1\\ x_2\end{pmatrix}
=

\begin{pmatrix}
-x_1 + x_2 \\
x_1 - x_2
\end{pmatrix}
=

\begin{pmatrix}0\\0\end{pmatrix}
$$

得到方程组：
$$
\begin{cases}
-x_1 + x_2 = 0 \\
x_1 - x_2 = 0
\end{cases}
$$

用高斯消元得
$$
\mathbf{x}=\mathbf{v}_1 =
\begin{pmatrix}
1 \\
1
\end{pmatrix}
$$

对 $ \lambda_2 = 1$，解

$$
(A - I)\mathbf{x} = 0
$$

$$
\begin{pmatrix}
1 & 1 \\
1 & 1
\end{pmatrix}
\mathbf{x} = 0
$$

解特征向量：
$$
\mathbf{v}_2 =
\begin{pmatrix}
1 \\
-1
\end{pmatrix}
$$

第三步：写出特征分解（对角化）

把特征向量按列放在一起，组成矩阵
$$
P =
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
$$

把对应的特征值放在对角线上：
$$
D =
\begin{pmatrix}
3 & 0 \\
0 & 1
\end{pmatrix}
$$

这时就可以写出： $A = P D P^{-1}$

这一步就是**特征分解 / 对角化**。

直观理解一下

- 在标准坐标系里，矩阵 $A$ 做的是“混合的拉伸 + 旋转”。
- 但如果我们换到由特征向量 $(1,1)$、$(1,-1)$ 组成的新坐标系里：

* 在第一个方向上，所有向量都被放大 3 倍
* 在第二个方向上，所有向量都被放大 1 倍

所以在这个坐标系下，矩阵的作用就变成了一个**纯粹的对角矩阵 (D)**。

为什么对角化很重要？
比如计算 $A^{10}$：

$$
A^{10} = P D^{10} P^{-1}
$$

而
$$
D^{10} =
\begin{pmatrix}
3^{10} & 0 \\
0 & 1^{10}
\end{pmatrix}
$$

这比直接算 $A^{10}$ 要简单得多。这也是特征分解在微分方程、PCA、图算法、物理系统里特别常见的原因。