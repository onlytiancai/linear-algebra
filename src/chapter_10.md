# Chapter 10. Linear Algebra in Practice
第 10 章 线性代数实践

## 10.1 Computer Graphics (Rotations, Projections)
10.1 计算机图形学（旋转、投影）

Linear algebra is the language of modern computer graphics. Every image rendered on a screen, every 3D model rotated or projected, is ultimately the result of applying matrices to vectors. Rotations, reflections, scalings, and projections are all linear transformations, making matrices the natural tool for manipulating geometry.
线性代数是现代计算机图形学的语言。屏幕上渲染的每一幅图像，以及旋转或投影的每一个 3D 模型，最终都是将矩阵应用于向量的结果。旋转、反射、缩放和投影都是线性变换，这使得矩阵成为处理几何图形的天然工具。

### Rotations in 2D
二维旋转

A counterclockwise rotation by an angle $\theta$ in the plane is represented by
在平面上逆时针旋转角度 $\theta$ 表示为

$$
R_\theta =\begin{bmatrix}\cos\theta & -\sin\theta \\\sin\theta & \cos\theta\end{bmatrix}.
$$

For any vector $\mathbf{v} \in \mathbb{R}^2$, the rotated vector is
对于任意向量 $\mathbf{v} \in \mathbb{R}^2$ ，旋转后的向量为

$$
\mathbf{v}' = R_\theta \mathbf{v}.
$$

This preserves lengths and angles, since $R_\theta$ is orthogonal with determinant 1.
这保留了长度和角度，因为𝑅 𝜃 R θ ​ 与行列式 1 正交。

### Rotations in 3D
3D 旋转

In three dimensions, rotations are represented by $3 \\times 3 orthogonal matrices with determinant \\1$. For example, arotation about the $z$-axis is
在三维空间中，旋转由$3 \\times 3 正交矩阵表示，其行列式为 \\ 1 $. For example, arotation about the $ z$轴为

$$
R_z(\theta) =\begin{bmatrix}\cos\theta & -\sin\theta & 0 \\\sin\theta & \cos\theta & 0 \\0 & 0 & 1\end{bmatrix}.
$$

Similar formulas exist for rotations about the $x$\- and $y$\-axes.
对于绕 $x$ 轴和 $y$ 轴的旋转也存在类似的公式。

More general 3D rotations can be described by axis–angle representation or quaternions, but the underlying idea is still linear transformations represented by matrices.
更一般的 3D 旋转可以用轴角表示或四元数来描述，但其基本思想仍然是矩阵表示的线性变换。

### Projections
预测

To display 3D objects on a 2D screen, we use projections:
为了在 2D 屏幕上显示 3D 对象，我们使用投影：

1.  Orthogonal projection: drops the $z$\-coordinate, mapping $(x,y,z) \mapsto (x,y)$.
    正交投影：删除 $z$ 坐标，映射 $(x,y,z) \mapsto (x,y)$ 。
    
    $$
    P = \begin{bmatrix}1 & 0 & 0 \\0 & 1 & 0\end{bmatrix}.
    $$
    
2.  Perspective projection: mimics the effect of a camera. A point $(x,y,z)$ projects to
    透视投影：模拟相机的效果。点 $(x,y,z)$ 投影到
    
    $$
    \left(\frac{x}{z}, \frac{y}{z}\right),
    $$
    
    capturing how distant objects appear smaller.
    捕捉远处物体如何显得更小。
    

These operations are linear (orthogonal projection) or nearly linear (perspective projection becomes linear in homogeneous coordinates).
这些操作是线性的（正交投影）或近似线性的（透视投影在齐次坐标中变为线性）。

### Homogeneous Coordinates
齐次坐标

To unify translations and projections with linear transformations, computer graphics uses homogeneous coordinates. A 3D point $(x,y,z)$ is represented as a 4D vector $(x,y,z,1)$. Transformations are then 4×4 matrices, which can represent rotations, scalings, and translations in a single framework.
为了将平移和投影与线性变换统一起来，计算机图形学使用齐次坐标。3D 点 $(x,y,z)$ 表示为四维向量 $(x,y,z,1)$ 。变换则表示为矩阵 4×4 ，可以在单个框架中表示旋转、缩放和平移。

Example: Translation by $(a,b,c)$:
例如： $(a,b,c)$ 翻译：

$$
T = \begin{bmatrix}1 & 0 & 0 & a \\0 & 1 & 0 & b \\0 & 0 & 1 & c \\0 & 0 & 0 & 1\end{bmatrix}.
$$

### Geometric Interpretation
几何解释

*   Rotations preserve shape and size, only changing orientation.
    旋转保持形状和大小，仅改变方向。
*   Projections reduce dimension: from 3D world space to 2D screen space.
    投影减少维度：从 3D 世界空间到 2D 屏幕空间。
*   Homogeneous coordinates allow us to combine multiple transformations (rotation + translation + projection) into a single matrix multiplication.
    齐次坐标允许我们将多个变换（旋转+平移+投影）组合成单个矩阵乘法。

### Why this matters
为什么这很重要

Linear algebra enables all real-time graphics: video games, simulations, CAD software, and movie effects. By chaining simple matrix operations, complex transformations are applied efficiently to millions of points per second.
线性代数支持所有实时图形：视频游戏、模拟、CAD 软件和电影特效。通过链接简单的矩阵运算，复杂的变换可以高效地应用于每秒数百万个点。

### Exercises 10.1
练习10.1

1.  Write the rotation matrix for a 90° counterclockwise rotation in $\mathbb{R}^2$. Apply it to $(1,0)$.
    在 $\mathbb{R}^2$ 中写出逆时针旋转 90° 的旋转矩阵。将其应用到 $(1,0)$ 。
2.  Rotate the point $(1,1,0)$ about the $z$\-axis by 180°.
    将点 $(1,1,0)$ 绕 $z$ 轴旋转 180°。
3.  Show that the determinant of any 2D or 3D rotation matrix is 1.
    证明任何二维或三维旋转矩阵的行列式为 1。
4.  Derive the orthogonal projection matrix from $\mathbb{R}^3$ to the $xy$\-plane.
    推导从 $\mathbb{R}^3$ 到 $xy$ 平面的正交投影矩阵。
5.  Explain how homogeneous coordinates allow translations to be represented as matrix multiplications.
    解释齐次坐标如何允许平移表示为矩阵乘法。

## 10.2 Data Science (Dimensionality Reduction, Least Squares)
10.2 数据科学（降维、最小二乘）

Linear algebra provides the foundation for many data science techniques. Two of the most important are dimensionality reduction, where high-dimensional datasets are compressed while preserving essential information, and the least squares method, which underlies regression and model fitting.
线性代数为许多数据科学技术奠定了基础。其中最重要的两个技术是降维（在保留基本信息的同时压缩高维数据集）和最小二乘法（回归和模型拟合的基础）。

### Dimensionality Reduction
降维

High-dimensional data often contains redundancy: many features are correlated, meaning the data essentially lies near a lower-dimensional subspace. Dimensionality reduction identifies these subspaces.
高维数据通常包含冗余：许多特征相互关联，这意味着数据本质上位于低维子空间附近。降维可以识别这些子空间。

*   PCA (Principal Component Analysis): As introduced earlier, PCA diagonalizes the covariance matrix of the data.
    PCA（主成分分析）：如前所述，PCA 将数据的协方差矩阵对角化。
    
    *   Eigenvectors (principal components) define orthogonal directions of maximum variance.
        特征向量（主成分）定义最大方差的正交方向。
    *   Eigenvalues measure how much variance lies along each direction.
        特征值衡量每个方向上的方差。
    *   Keeping only the top $k$ components reduces data from $n$\-dimensional space to $k$\-dimensional space while retaining most variability.
        仅保留前 $k$ 个成分可将数据从 $n$ 维空间减少到 $k$ 维空间，同时保留大部分可变性。

Example 10.2.1. A dataset of 1000 images, each with 1024 pixels, may have most variance captured by just 50 eigenvectors of the covariance matrix. Projecting onto these components compresses the data while preserving essential features.
例 10.2.1。一个包含 1000 幅图像的数据集，每幅图像有 1024 个像素，其大部分方差可能仅由协方差矩阵的 50 个特征向量捕获。投影到这些分量上可以压缩数据，同时保留基本特征。

### Least Squares
最小二乘法

Often, we have more equations than unknowns-an overdetermined system:
通常，我们的方程比未知数还多——一个超定系统：

$$
A\mathbf{x} \approx \mathbf{b}, \quad A \in \mathbb{R}^{m \times n}, \ m > n.
$$

An exact solution may not exist. Instead, we seek $\mathbf{x}$ that minimizes the error
精确解可能不存在。因此，我们寻求最小化误差的 $\mathbf{x}$

$$
\|A\mathbf{x} - \mathbf{b}\|^2.
$$

This leads to the normal equations:
这导致了正规方程：

$$
A^T A \mathbf{x} = A^T \mathbf{b}.
$$

The solution is the orthogonal projection of $\mathbf{b}$ onto the column space of $A$.
解决方案是将 $\mathbf{b}$ 正交投影到 $A$ 的列空间上。

### Example 10.2.2
例 10.2.2

Fit a line $y = mx + c$ to data points $(x_i, y_i)$.
将线 $y = mx + c$ 与数据点 $(x_i, y_i)$ 拟合。

Matrix form:
矩阵形式：

$$
A = \begin{bmatrix}x_1 & 1 \\x_2 & 1 \\\vdots & \vdots \\x_m & 1\end{bmatrix},\quad\mathbf{b} =\begin{bmatrix}y_1 \\y_2 \\\vdots \\y_m \end{bmatrix},\quad\mathbf{x} =\begin{bmatrix}m \\c \end{bmatrix}.
$$

Solve $A^T A \mathbf{x} = A^T \mathbf{b}$. This yields the best-fit line in the least squares sense.
求解 $A^T A \mathbf{x} = A^T \mathbf{b}$ 。这将得出最小二乘意义上的最佳拟合线。

### Geometric Interpretation
几何解释

*   Dimensionality reduction: Find the best subspace capturing most variance.
    降维：找到捕获最多方差的最佳子空间。
*   Least squares: Project the target vector onto the subspace spanned by predictors.
    最小二乘：将目标向量投影到预测变量所跨越的子空间上。

Both are projection problems, solved using inner products and orthogonality.
两者都是投影问题，使用内积和正交性来解决。

### Why this matters
为什么这很重要

Dimensionality reduction makes large datasets tractable, filters noise, and reveals structure. Least squares fitting powers regression, statistics, and machine learning. Both rely directly on eigenvalues, eigenvectors, and projections-core tools of linear algebra.
降维使大型数据集更易于处理，过滤噪声并揭示结构。最小二乘拟合为回归、统计和机器学习提供支持。两者都直接依赖于特征值、特征向量和投影——线性代数的核心工具。

### Exercises 10.2
练习10.2

1.  Explain why PCA reduces noise in datasets by discarding small eigenvalue components.
    解释为什么 PCA 通过丢弃较小的特征值分量来减少数据集中的噪声。
2.  Compute the least squares solution to fitting a line through $(0,0), (1,1), (2,2)$.
    计算通过 $(0,0), (1,1), (2,2)$ 拟合直线的最小二乘解。
3.  Show that the least squares solution is unique if and only if $A^T A$ is invertible.
    证明最小二乘解是唯一的当且仅当 $A^T A$ 可逆。
4.  Prove that the least squares solution minimizes the squared error by projection arguments.
    证明最小二乘解通过投影参数最小化平方误差。
5.  Apply PCA to the data points $(1,0), (2,1), (3,2)$ and find the first principal component.
    将 PCA 应用于数据点 $(1,0), (2,1), (3,2)$ 并找到第一个主成分。

## 10.3 Networks and Markov Chains
10.3 网络和马尔可夫链

Graphs and networks provide a natural setting where linear algebra comes to life. From modeling flows and connectivity to predicting long-term behavior, matrices translate network structure into algebraic form. Markov chains, already introduced in Section 8.4, are a central example of networks evolving over time.
图和网络为线性代数的运用提供了自然的平台。从建模流和连接到预测长期行为，矩阵将网络结构转化为代数形式。马尔可夫链（已在 8.4 节介绍）是网络随时间演化的一个典型例子。

### Adjacency Matrices
邻接矩阵

A network (graph) with $n$ nodes can be represented by an adjacency matrix $A \in \mathbb{R}^{n \times n}$:
具有 $n$ 个节点的网络（图）可以用邻接矩阵 $A \in \mathbb{R}^{n \times n}$ 表示：

$$
A_{ij} =\begin{cases}1 & \text{if there is an edge from node \(i\) to node \(j\)} \\0 & \text{otherwise.}\end{cases}
$$

For weighted graphs, entries may be positive weights instead of 0/1.
对于加权图，条目可能是正权重而不是 0/1 。

*   The number of walks of length $k$ from node $i$ to node $j$ is given by the entry $(A^k)_{ij}$.
    从节点 $i$ 到节点 $j$ 的长度为 $k$ 的步行次数由条目 ( 𝐴 𝑘 ) 𝑖 𝑗 （一个 k ) 伊奇 ​ .
*   Powers of adjacency matrices thus encode connectivity over time.
    因此，邻接矩阵的幂可以对随时间变化的连通性进行编码。

### Laplacian Matrices
拉普拉斯矩阵

Another important matrix is the graph Laplacian:
另一个重要的矩阵是图拉普拉斯矩阵：

$$
L = D - A,
$$

where $D$ is the diagonal degree matrix ( $D_{ii} = \text{degree}(i)$ ).
其中 $D$ 是对角度矩阵 ( $D_{ii} = \text{degree}(i)$ )。

*   $L$ is symmetric and positive semidefinite.
    $L$ 是对称的并且是正半定的。
*   The smallest eigenvalue is always $0$, with eigenvector $(1,1,\\dots,1)$.
    最小特征值始终是 $0 $, with eigenvector $ (1,1,\\dots,1)$。
*   The multiplicity of eigenvalue 0 equals the number of connected components in the graph.
    特征值 0 的多重性等于图中连通分量的数量。

This connection between eigenvalues and connectivity forms the basis of spectral graph theory.
特征值和连通性之间的这种联系构成了谱图理论的基础。

### Markov Chains on Graphs
图上的马尔可夫链

A Markov chain can be viewed as a random walk on a graph. If $P$ is the transition matrix where $P_{ij}$ is the probability of moving from node $i$ to node $j$, then
马尔可夫链可以看作图上的随机游动。设 $P$ 为转移矩阵，其中 𝑃 𝑖 𝑗 P 伊奇 ​ 是从节点 $i$ 移动到节点 $j$ 的概率，那么

$$
\mathbf{x}_{k+1} = P \mathbf{x}_k
$$

describes the distribution of positions after $k$ steps.
描述 $k$ 步之后的位置分布。

*   The steady-state distribution is given by the eigenvector of $P$ with eigenvalue 1.
    稳态分布由特征向量 $P$ 给出，特征值为 1 。
*   The speed of convergence depends on the gap between the largest eigenvalue (which is always 1) and the second largest eigenvalue.
    收敛速度取决于最大特征值（始终为 1 ）与第二大特征值之间的差距。

### Example 10.3.1
例 10.3.1

Consider a simple 3-node cycle graph:
考虑一个简单的 3 节点循环图：

$$
P = \begin{bmatrix}0 & 1 & 0 \\0 & 0 & 1 \\1 & 0 & 0\end{bmatrix}.
$$

```
This Markov chain cycles deterministically among the nodes. Eigenvalues are the cube roots of unity: $1, e^{2\\pi i/3}, e^{4\\pi i/3}. The eigenvalue \\1$corresponds to the steady state, which is the uniformdistribution$(1/3,1/3,1/3)$.

这个马尔可夫链在节点之间确定性地循环。特征值是 统一：$1,e^{2\\pi i/3},e^{4\\pi i/3} 。

特征值 \\ 1 $corresponds to the steady state, which is the uniformdistribution$ (1/3,1/3,1/3)$。
```

### Applications
应用

*   Search engines: Google’s PageRank algorithm models the web as a Markov chain, where steady-state probabilities rank pages.
    搜索引擎：Google 的 PageRank 算法将网络建模为马尔可夫链，其中稳态概率对网页进行排名。
*   Network analysis: Eigenvalues of adjacency or Laplacian matrices reveal communities, bottlenecks, and robustness.
    网络分析：邻接矩阵或拉普拉斯矩阵的特征值揭示社区、瓶颈和稳健性。
*   Epidemiology and information flow: Random walks model how diseases or ideas spread through networks.
    流行病学和信息流：随机游动模拟疾病或思想如何通过网络传播。

### Why this matters
为什么这很重要

Linear algebra transforms network problems into matrix problems. Eigenvalues and eigenvectors reveal connectivity, flow, stability, and long-term dynamics. Networks are everywhere-social media, biology, finance, and the internet-so these tools are indispensable.
线性代数将网络问题转化为矩阵问题。特征值和特征向量揭示了连通性、流动、稳定性和长期动态。网络无处不在——社交媒体、生物、金融和互联网——因此这些工具不可或缺。

### Exercises 10.3
练习10.3

1.  Write the adjacency matrix of a square graph with 4 nodes. Compute $A^2$ and interpret the entries.
    写出一个有 4 个节点的正方形图的邻接矩阵。计算 $A^2$ 并解释其中的元素。
    
2.  Show that the Laplacian of a connected graph has exactly one zero eigenvalue.
    证明连通图的拉普拉斯算子恰好有一个零特征值。
    
3.  Find the steady-state distribution of the Markov chain with
    找到马尔可夫链的稳态分布
    
    $$
    P = \begin{bmatrix} 0.5 & 0.5 \\ 0.4 & 0.6 \end{bmatrix}.
    $$
    
4.  Explain how eigenvalues of the Laplacian can detect disconnected components of a graph.
    解释拉普拉斯算子的特征值如何检测图中不连续的组成部分。
    
5.  Describe how PageRank modifies the transition matrix of the web graph to ensure a unique steady-state distribution.
    描述 PageRank 如何修改网络图的转换矩阵以确保唯一的稳态分布。
    

## 10.4 Machine Learning Connections
10.4 机器学习连接

Modern machine learning is built on linear algebra. From the representation of data as matrices to the optimization of large-scale models, nearly every step relies on concepts such as vector spaces, projections, eigenvalues, and matrix decompositions.
现代机器学习建立在线性代数的基础上。从数据矩阵表示到大规模模型的优化，几乎每一步都依赖于向量空间、投影、特征值和矩阵分解等概念。

### Data as Matrices
数据作为矩阵

A dataset with $m$ examples and $n$ features is represented as a matrix $X \in \mathbb{R}^{m \times n}$:
具有 $m$ 个示例和 $n$ 个特征的数据集表示为矩阵 $X \in \mathbb{R}^{m \times n}$ ：


$$
X = \begin{bmatrix}
\text{-} & \mathbf{x}_1^T & \text{-} \\
\text{-} & \mathbf{x}_2^T & \text{-} \\
  & \vdots &   \\
\text{-} & \mathbf{x}_m^T & \text{-}
\end{bmatrix},
$$


where each row $\mathbf{x}_i \in \mathbb{R}^n$ is a feature vector. Linear algebra provides tools to analyze, compress, and transform this data.
其中每行 $\mathbf{x}_i \in \mathbb{R}^n$ 是一个特征向量。线性代数提供了分析、压缩和转换此类数据的工具。

### Linear Models
线性模型

At the heart of machine learning are linear predictors:
机器学习的核心是线性预测器：

$\hat{y} = X\mathbf{w},$

where $\mathbf{w}$ is the weight vector. Training often involves solving a least squares problem or a regularized variant such as ridge regression:
其中 $\mathbf{w}$ 是权重向量。训练通常涉及求解最小二乘问题或正则化变体，例如岭回归：

$\min_{\mathbf{w}} \|X\mathbf{w} - \mathbf{y}\|^2 + \lambda \|\mathbf{w}\|^2.$

This is solved efficiently using matrix factorizations.
使用矩阵分解可以有效地解决这个问题。

### Singular Value Decomposition (SVD)
奇异值分解（SVD）

The SVD of a matrix $X$ is
矩阵 $X$ 的 SVD 为

$X = U \Sigma V^T,$

where $U, V$ are orthogonal and $\Sigma$ is diagonal with nonnegative entries (singular values).
其中 $U, V$ 是正交的， $\Sigma$ 是对角的，具有非负项（奇异值）。

*   Singular values measure the importance of directions in feature space.
    奇异值衡量特征空间中方向的重要性。
*   SVD is used for dimensionality reduction (low-rank approximations), topic modeling, and recommender systems.
    SVD 用于降维（低秩近似）、主题建模和推荐系统。

### Eigenvalues in Machine Learning
机器学习中的特征值

*   PCA (Principal Component Analysis): diagonalization of the covariance matrix identifies directions of maximal variance.
    PCA（主成分分析）：协方差矩阵的对角化确定了最大方差的方向。
*   Spectral clustering: uses eigenvectors of the Laplacian to group data points into clusters.
    谱聚类：使用拉普拉斯算子的特征向量将数据点分组成聚类。
*   Stability analysis: eigenvalues of Hessian matrices determine whether optimization converges to a minimum.
    稳定性分析：Hessian 矩阵的特征值决定优化是否收敛到最小值。

### Neural Networks
神经网络

Even deep learning, though nonlinear, uses linear algebra at its core:
即使是深度学习，尽管是非线性的，其核心也使用线性代数：

*   Each layer is a matrix multiplication followed by a nonlinear activation.
    每一层都是矩阵乘法，然后是非线性激活。
*   Training requires computing gradients, which are expressed in terms of matrix calculus.
    训练需要计算梯度，以矩阵微积分来表示。
*   Backpropagation is essentially repeated applications of the chain rule with linear algebra.
    反向传播本质上是链式法则与线性代数的重复应用。

### Why this matters
为什么这很重要

Machine learning models often involve datasets with millions of features and parameters. Linear algebra provides the algorithms and abstractions that make training and inference possible. Without it, large-scale computation in AI would be intractable.
机器学习模型通常涉及具有数百万个特征和参数的数据集。线性代数提供了使训练和推理成为可能的算法和抽象。如果没有它，人工智能中的大规模计算将变得难以处理。

### Exercises 10.4
练习10.4

1.  Show that ridge regression leads to the normal equations
    证明岭回归可以得出正态方程

$$
(X^T X + \lambda I)\mathbf{w} = X^T \mathbf{y}.
$$

2.  Explain how SVD can be used to compress an image represented as a matrix of pixel intensities.
    解释如何使用 SVD 来压缩以像素强度矩阵表示的图像。
    
3.  For a covariance matrix $\Sigma$, show why its eigenvalues represent variances along principal components.
    对于协方差矩阵 $\Sigma$ ，说明为什么它的特征值表示沿主成分的方差。
    
4.  Give an example of how eigenvectors of the Laplacian matrix can be used for clustering a small graph.
    举例说明如何使用拉普拉斯矩阵的特征向量对小图进行聚类。
    
5.  In a neural network with one hidden layer, write the forward pass in matrix form.
    在具有一个隐藏层的神经网络中，以矩阵形式写出前向传递。
