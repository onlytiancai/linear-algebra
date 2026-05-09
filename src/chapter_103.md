# TurboQuant 学习

https://arkaung.github.io/interactive-turboquant/#hero


## 基础概念

- Vector: ordered list of numbers / arrow from the origin. 
  - 向量：有序的数字列表 / 从原点出发的箭头。
- Length & inner product: the norm $\sqrt{\sum x_i^2}$ and how much two vectors point the same way. 
  - 长度与内积：范数 $\sqrt{\sum x_i^2}$，以及两个向量指向同一方向的程度。
- MSE: average squared error. 
  - 均方误差：平均平方误差。
- Unbiased: the average of many estimates equals the truth. 
  - 无偏：大量估计值的平均等于真实值。
- Rotation: change of basis that preserves lengths and angles. 
  - 旋转：保持长度和角度的基变换。
- CLT: sum of many independent randoms converges to a Gaussian. 
  - 中心极限定理：大量独立随机变量的和收敛于高斯分布。
- High-D concentration: each coordinate of a random unit vector has mean  and standard deviation $1/\sqrt{d}$. 
  - 高维集中：随机单位向量的每个坐标均值为 0，标准差为 $1/\sqrt{d}$。
- Quantization: snap each number to one of $2^b$ levels; one extra bit quarters the squared error.
  - 量化：将每个数离散化为 $2^b$ 个等级之一；增加一位可以将平方误差降低到原来的四分之一。


  Read [](file:///Users/huhao/src/linear-algebra/src/chapter_103.md)


Modern language models store large tables of high-dimensional vectors: KV caches, embeddings, attention keys. TurboQuant compresses each coordinate of these vectors to 2–4 bits with provably near-optimal distortion, no memory overhead for scale factors, and no training or calibration. This page explains how it works.

## 简介

这段话介绍 **TurboQuant** 的核心思想：

**背景**：现代语言模型（如 GPT、LLaMA）需要存储大量的高维向量，包括：
- **KV caches**：注意力机制中的键值缓存
- **Embeddings**：词元/词的向量表示
- **Attention keys**：注意力机制中的 K（键）向量

这些向量表占用大量显存，是大模型推理的主要瓶颈之一。

**TurboQuant 的解决方案**：将向量的每个维度压缩到 2-4 位（而非传统的 32 位浮点数），特点包括：

| 特性 | 含义 |
|------|------|
| **Near-optimal distortion** | 有数学证明的近最优压缩效果 |
| **No memory overhead for scale factors** | 不需要额外的缩放因子，节省内存 |
| **No training or calibration** | 无需微调或校准，直接使用 |

**核心思想**：利用高维随机向量的"集中"特性——坐标值近似服从均值为 0、标准差为 $1/\sqrt{d}$ 的分布，只需平移缩放后直接量化，无需逐向量校准。

## 内容介绍

The central claim of this page: in high dimensions, a random rotation turns every input vector into one whose coordinates follow a known fixed distribution. A codebook designed once for that distribution then works for every input. The rest of the page constructs that codebook and applies it to MSE, mean, and inner-product estimation.

Read [](file:///Users/huhao/src/linear-algebra/src/chapter_103.md)



翻译

> 本页的核心论点：在高维空间中，随机旋转将任意输入向量转化为坐标服从已知固定分布的向量。因此，一个针对该分布一次性设计好的码本（codebook）适用于所有输入。本页的其余部分将构建这个码本，并将其应用于 MSE、均值和内积的估计。

---

解释

**一个关键观察（Central Claim）**

在高维空间中，如果我们对一个向量做随机旋转（random rotation），这个向量的坐标会变得"接近"一个固定的分布——不依赖于原始输入。这意味着：

| 步骤 | 含义 |
|------|------|
| 1. 输入任意向量 | 例如 LLM 中的词向量、KV cache 向量 |
| 2. 随机旋转（正交变换） | 等价于换一组正交基来表示这个向量 |
| 3. 旋转后的坐标 | 服从可预测的已知分布（例如标准正态分布的缩放） |

**为什么有用**

传统量化需要对每个向量单独计算缩放因子（per-vector scale），这带来了内存开销。TurboQuant 的关键 insight 是：

> **随机旋转 + 固定分布 = 一次设计，处处使用**

- 码本（codebook）只需设计一次，存储起来
- 处理任意输入时，直接查表量化即可
- 无需校准、无需训练

**后续应用**

本页会：
1. 构造这个通用码本
2. 证明它对 MSE 估计是最优的
3. 扩展到均值估计和内积估计

## 论文来源

This construction was introduced by DRIVE (Vargaftik et al., NeurIPS 2021) for one-bit federated mean estimation, and generalized to b bits per coordinate by EDEN (Vargaftik et al., ICML 2022). TurboQuant (Zandieh et al., 2025) is the same construction with the per-vector scale parameter fixed to a constant, repackaged for KV-cache compression and inner-product retrieval. 

翻译

> 这一构造最初由 **DRIVE**（Vargaftik 等，NeurIPS 2021）提出，用于一比特联邦均值估计，随后由 **EDEN**（Vargaftik 等，ICML 2022）推广到每坐标 b 比特。**TurboQuant**（Zandieh 等，2025）沿用同一构造，只是将每向量缩放参数固定为常数，并重新包装以适配 KV 缓存压缩和内积检索场景。

---

解释

这是一段技术发展脉络的介绍，说明 TurboQuant 并非凭空发明，而是站在前人肩膀上：

| 时间 | 工作 | 贡献 | 应用场景 |
|------|------|------|----------|
| 2021 | **DRIVE** | 提出基本构造框架 | 一比特联邦均值估计 |
| 2022 | **EDEN** | 将 DRIVE 推广到 b 比特（任意精度） | 每坐标多比特量化 |
| 2025 | **TurboQuant** | 固定缩放参数为常数，去掉 per-vector scale 开销 | KV 缓存压缩 & 内积检索 |

**TurboQuant 的核心改进**

TurboQuant 的"repackaging"实际上是一个关键简化：它将 EDEN 中的**可学习/可变的每向量缩放参数**固定为一个**常数**（可能是 1 或某个全局预设值）。代价是略微损失一点精度，但换来了：
- 零内存开销（不需要存储缩放因子）
- 极简实现（无需校准）

这对于 KV 缓存场景非常关键，因为显存节省比微小的精度损失更重要。

## 向量

Vector
A list of numbers. An arrow in space.
A vector is an ordered list: [0.3, −1.2]. Geometrically it is an arrow from the origin. A d-dimensional vector is an arrow in 
-space, hard to picture past 3-D, but the rules are the same.

翻译

> **向量（Vector）**
> 
> 一个数字列表，空间中的一个箭头。
> 向量是一个有序列表：例如 `[0.3, −1.2]`。从几何上看，它是一条从原点出发的箭头。d 维向量就是 d 维空间中的一个箭头——超过 3 维就难以直观想象了，但运算规则是相同的。

---

解释

这是对向量概念的入门介绍：

| 表述 | 含义 |
|------|------|
| **有序列表** | 向量是有顺序的数字集合，如 `[0.3, −1.2]`，调换顺序就变成不同向量 |
| **空间中的箭头** | 几何视角：向量由方向和长度唯一确定 |
| **d 维空间** | 向量的维度等于列表中数字的数量。3 维以下可以画图想象，4 维以上只能靠数学理解 |
| **规则相同** | 不管多少维，加法、数乘、内积等运算规则保持一致 |

**为什么重要**

在 LLM 中：
- 每个词/词元被表示为一个高维向量（如 4096 维）
- 这些向量构成一个巨大的向量表（embedding table）
- 向量之间的**内积**决定了语义相似度

TurboQuant 正是要压缩这些高维向量，以节省 KV 缓存和 embedding 的存储空间。

## 向量的长度和内积

Length ‖x‖ & Inner Product ⟨x,y⟩
How much one vector points along another.
Length = $\sqrt{\sum x_i^2}$ Inner product $\sum_i v_i w_i = |\mathbf{v}||\mathbf{w}|\cos\theta$
. The inner product reaches its largest positive value when the two arrows point in the same direction. It drops to zero when the two arrows are perpendicular. It becomes negative when the arrows point in opposite directions, with its most negative value when they point exactly opposite.



翻译

> **两个向量指向同一方向的程度。**
> 
> **长度（Length）** = $\sqrt{\sum x_i^2}$
> 
> **内积（Inner product）** = $\sum x_i y_i$
> 
> 当两个箭头方向相同时，内积达到最大的正值。方向垂直时，内积为零。方向相反时，内积变为负值；当两箭头完全反向时，内积达到最小的负值。

---

解释

**几何含义**

内积（点积）本质上衡量的是**两个向量的对齐程度**：

| 关系 | 几何图示 | 内积值 |
|------|----------|--------|
| **同向** | → → | 正的最大值（$\|v\|\|w\|$） |
| **垂直** | → ⊥ ↓ | 0 |
| **反向** | → ← | 负值（趋向 $-\|v\|\|w\|$） |

**数学定义**

$$
\text{内积} = \mathbf{v} \cdot \mathbf{w} = \sum_i v_i w_i = |\mathbf{v}||\mathbf{w}|\cos\theta
$$

其中 $\theta$ 是两向量夹角。当 $\theta = 0°$（同向），$\cos\theta = 1$，内积最大；当 $\theta = 90°$（垂直），$\cos\theta = 0$，内积为零；当 $\theta = 180°$（反向），$\cos\theta = -1$，内积最小。

**为什么重要**

在 LLM 中，内积用于：
- **语义相似度**：词向量内积越大，语义越相近
- **注意力机制（Attention）**：Query 和 Key 的内积决定注意力权重
- **向量检索**：用内积排序找到最相似的向量

## MSE

Mean Squared Error
Why we square the mistake.
Error is the distance between a guess and the truth. Scoring a guess by the signed error lets positive and negative errors cancel, which means the score does not penalise being off. Squaring forces every error to count as a positive number and gives big errors a larger penalty than small ones. The guess that minimises the mean of squared errors is the data’s average: it is the unique number that minimises the sum of squared distances to the points.

The first moment of a quantity X is its mean $E[X]$; the second moment is the mean of its square $E[X^2]$. A zero-mean variable has a vanishing first moment because positive and negative deviations cancel. Its second moment is strictly positive whenever any deviation is nonzero, because squared values are nonnegative and cannot cancel. The MSE above is itself a second moment of the residual error. This distinction returns in §7, where the per-input gap $\bar{y} - y$
 averages to zero in the first moment, while its square averages to a strictly positive quantity in the second.

The average has a property we will use in §7. It lies between the data’s most extreme points, so its magnitude is smaller than at least one of them. When a quantizer compresses a whole bin of values down to the bin’s average, the stored value is smaller in magnitude than the bin’s largest values. The reconstruction is a shrunken version of the input. An inner product against a shrunken reconstruction comes out smaller than the same inner product against the input.


翻译

> **均方误差（Mean Squared Error）**
> 
> **为什么要对误差求平方。**
> 
> 误差是猜测值与真实值之间的距离。如果用带符号的误差来评分，正负误差会相互抵消，这意味着评分无法惩罚偏离。取平方后，每个误差都被强制记为正数，且大误差比小误差受到更重的惩罚。最小化均方误差的猜测值是数据的平均值——它是使所有点到该点的平方距离之和最小的唯一数值。
> 
> 随机变量 X 的**一阶矩**是其均值 $E[X]$；**二阶矩**是其平方的均值 $E[X^2]$。零均值变量的一阶矩为零，因为正负偏差相互抵消。只要存在任何非零偏差，其二阶矩必然为正，因为平方值非负，不能相互抵消。上述 MSE 本身就是残差的一个二阶矩。这个区别在 §7 会再次出现：其中每个输入的 gap $\bar{y} - y$ 在一阶矩上平均为零，但其平方在二阶矩上平均为一个严格正数。
> 
> 均值有一个我们将在 §7 使用的性质。它位于数据最极端点之间，因此其幅度至少比其中一个极端点更小。当量化器将一整组数值压缩到该组的均值时，存储的值在幅度上小于该组最大的值。重构结果是输入的一个缩小版本。与缩小后的重构做内积，结果会比与原始输入做内积更小。

---

解释

第一段：为什么用 MSE？

| 问题 | MSE 的回答 |
|------|-----------|
| 误差有正有负，互相抵消怎么办？ | 平方强制转正 |
| 大误差和小误差同等对待？ | 平方后大误差惩罚更重 |
| 什么值使 MSE 最小？ | **均值**（唯一最优解） |

**直觉**：误差平方放大了偏离程度——离均值越远，受到的"惩罚"增长得更快。

第二段：矩（Moments）

| 概念 | 定义 | 特性 |
|------|------|------|
| **一阶矩** | $E[X]$（均值） | 正负偏差相消，可为零 |
| **二阶矩** | $E[X^2]$（平方的均值） | 恒非负，只有偏差全为 0 时才为零 |

**关键洞察**：MSE 是残差的二阶矩。一阶矩为 0（无偏）不等于二阶矩也为 0——大偏差即使正负抵消，仍会在平方后留下痕迹。

第三段：均值收缩（Shrinkage）

```
原始数据: [-10, -8, -2, 3, 7]  → 均值 = -2
量化压缩: 全部映射到 bin 均值 -2
```

**收缩效应**：
- 均值比数据中最极端的值更接近零点
- 量化后的值 = 原始 bin 的均值 = **被压缩**了
- 做内积时，收缩后的向量与另一个向量相乘，结果也等比缩小

这在 TurboQuant 中很重要：量化引入的偏差会导致内积（注意力分数）系统性偏小，需要后续校正。

## 无偏估计和有偏估计

Unbiased vs Biased Estimator

Noisy is fine. Systematically off is not.

An estimator is a procedure that takes data and returns a guess $\hat{\theta}$
 for an unknown truth $\theta$. Repeat it on fresh data and the guesses form a cloud. The cloud can fail in two independent ways. Variance is one: individual guesses are noisy. Bias is the other: the procedure is wrong even after averaging many guesses. An estimator with $E[\hat{\theta}]=\theta$ is unbiased; the cloud’s centre sits at regardless of the cloud’s width.

The bullseye below shows both failure modes. Bias is the distance from the cloud’s centre to the crosshair. Variance is the width of the cloud. The two quantities are independent of each other. §7 runs the same bullseye against the MSE quantizer of §6, and the cloud’s centre lands away from the crosshair. §8 runs it against a different estimator whose cloud centres on the crosshair.


翻译

无偏估计和有偏估计

噪声没关系。系统性偏差才是问题。

> **估计量（Estimator）**是一个过程：它接受数据，然后对未知真实值 $\theta$ 返回一个猜测值 $\hat{\theta}$。如果在新的数据上重复这个过程，猜测值会形成一个云团（分布）。这个云团可能以两种独立的方式失效。**方差（Variance）**是第一类：单个猜测值有噪声。**偏差（Bias）**是另一类：即使对大量猜测取平均，这个过程本身就是错的。如果一个估计量满足 $E[\hat{\theta}] = \theta$，它就是**无偏**的；无论云团多宽，其中心都位于靶心处。

> 下方的靶图展示了两种失效模式。偏差是云团中心到靶心（crosshair）的距离。方差是云团的宽度。这两个量是相互独立的。§7 会用同样的靶图来检验 §6 中 MSE 量化器的表现，云团的中心会落在靶心之外。§8 则会检验另一个估计量，其云团以靶心为中心。

---

解释

核心概念

**估计量（Estimator）**到底是什么？

$$
\hat{\theta} = f(\text{data}) \quad \text{（一个从数据到猜测的函数）}
$$

就像一个射击者每次射击都会在靶上留下一个弹孔。每一发子弹就是一次"估计"，弹孔的分布就是"云团"。

两种错误模式

| 模式 | 含义 | 类比 |
|------|------|------|
| **方差 (Variance)** | 弹孔分散，每次打不准 | 射手手抖，弹着点飘忽不定 |
| **偏差 (Bias)** | 弹孔偏离靶心，系统性歪斜 | 瞄准镜歪了，弹孔永远偏左/偏上 |

**关键**：方差和偏差是**独立的**——你可以同时有低方差+高偏差（弹孔集中但歪了），也可以有高方差+低偏差（弹孔散但都在靶心附近）。

无偏估计

$$
E[\hat{\theta}] = \theta
$$

无偏意味着：**即使单次估计可能出错，但大量估计的平均值等于真实值**。

| 有偏 | 无偏 |
|------|------|
| $E[\hat{\theta}] \neq \theta$ | $E[\hat{\theta}] = \theta$ |
| 系统性错误 | 随机错误 |
| 无论多少样本都无法消除 | 样本越多越接近真相 |

在 TurboQuant 中的意义

这篇论文后续章节（§7、§8）会检验量化器的表现：
- **§7 的 MSE 量化器**：可能有偏差（偏差 > 0），即量化后的估计系统性地偏离真实值
- **§8 的另一种估计量**：可能是无偏的（偏差 = 0）

这直接关系到 **TurboQuant 能否用于注意力机制**——如果偏差不为零，注意力分数会被系统性地压缩或放大。

## 旋转

Rotation
A rigid spin. Preserves lengths and angles.
A rotation matrix R spins space. The key property: $\|Rx\|=\|x\|$
 and $\langle Rx,Ry\rangle=\langle x,y\rangle$. Rotation only changes the basis the coordinates are written in, not the geometry.

Read [](file:///Users/huhao/src/linear-algebra/src/chapter_103.md#337-337), lines 337 to 342



> **旋转（Rotation）**
>
> 一种刚性的转动。保持长度和角度。
>
> 旋转矩阵 R 让空间旋转。其关键性质：$\|Rx\| = \|x\|$ 且 $\langle Rx, Ry\rangle = \langle x, y\rangle$。旋转只改变坐标写入的基，而不改变几何本身。

---

解释

**什么是旋转矩阵**

旋转矩阵是一个 $d \times d$ 的正交矩阵 $R$（满足 $R^T R = I$），它对向量 $x$ 做"刚性转动"——像拧动一个刚体上的箭头，但不拉伸或压缩它。

**两个关键性质**

| 性质 | 数学表达 | 几何含义 |
|------|----------|----------|
| **保长度** | $\|Rx\| = \|x\|$ | 旋转不改变向量的模长 |
| **保内积** | $\langle Rx, Ry\rangle = \langle x, y\rangle$ | 旋转不改变任意两个向量之间的夹角 |

这两条其实互为因果——保内积自然推出保长度（令 $y = x$ 即可）。

**"换基不换几何"**

```
   同一个几何向量  →  │  不同坐标系   │ → 得到不同坐标
   
   R 旋转的是坐标系（基），向量本身不变
```

| 视角 | 观察到的变化 | 实际发生的事 |
|------|-------------|--------------|
| **坐标系视角** | 坐标改变了 | 基向量被旋转了 |
| **向量视角** | 向量没变 | 几何关系保持 |

**为什么重要**

TurboQuant 的核心 insight 是：在高维空间做一次**随机旋转**后，向量的每个坐标服从一个固定的分布（与输入无关）。这使得我们可以"一次设计，处处使用"——码本只需设计一次，就能对任意向量做量化。

旋转的作用是**消除输入向量和坐标分布之间的关联**，让坐标变得"各向同性"（isotropic）——无论输入向量长什么样，旋转后坐标的统计特性都是一样的。

## 中心极限定理

Where bell-curves come from (CLT)
Add up many small randoms → Gaussian.
The Central Limit Theorem says that summing enough independent random numbers produces a distribution close to a bell curve. The shape of each individual term in the sum does not affect the limit. A sum of coin flips converges to the same Gaussian shape as a sum of uniform draws or a sum of skewed draws. A rotated coordinate is one of these sums: it is a weighted combination of every coordinate of the original vector, with random weights. After a random rotation, each new coordinate is therefore approximately Gaussian, which is the property TurboQuant relies on for every input.

翻译

**钟形曲线从何而来（中心极限定理）**

将许多小的随机数相加 → 得到高斯分布（正态分布）。

中心极限定理指出：足够多独立随机数之和产生的分布接近钟形曲线。每个单独项的形状不影响这个极限结果。抛硬币求和与均匀分布求和或偏态分布求和，最终收敛到相同的高斯形状。旋转后的坐标就是这些求和的一种：它是原始向量每个坐标的加权和，权重是随机的。经过随机旋转后，每个新坐标因此近似服从高斯分布——这正是 TurboQuant 对每个输入维度的依赖特性。

---

解释

**核心思想**：大量独立随机变量的和趋于高斯分布，与各自分布无关。

**三个要点**：

| 要点 | 含义 |
|------|------|
| **独立同分布求和** | 无论单个随机变量是什么分布（均匀、偏态、二项），只要相互独立且数量够多，和就趋近高斯 |
| **旋转 = 加权和** | 旋转后的某个坐标，是原向量所有坐标的加权和，本质上是一种特殊的求和 |
| **实际应用** | 高维随机向量经随机旋转后，每个新坐标近似高斯分布 → 可用统一的量化策略 |

**为什么有用**：TurboQuant 利用旋转让所有坐标都具备近似高斯分布的统计特性，从而可以用相同的方法压缩，无需针对每个向量单独校准。

## 高维空间

Life in many dimensions

Pick a random point on a unit sphere in $d$ dimensions. In 2-D any coordinate is possible. The unit-sphere constraint $\sum_i X_i^2=1$ and rotational symmetry imply that every coordinate has mean $0$ and standard deviation  ${1}/{\sqrt{d}}$. As $d$ grows, the marginal of $X_i$  narrows around zero. This is measure concentration, and it is the core fact TurboQuant exploits.



## 高维空间的生活

翻译

> 在 $d$ 维空间中随机取一个单位球面上的点。在 2 维中，坐标可以是任何值。单位球约束 $\sum_i X_i^2=1$ 和旋转对称性意味着每个坐标的均值为 0，标准差为 $1/\sqrt{d}$。随着 $d$ 增大，$X_i$ 的边缘分布向零收缩。这就是测度集中（measure concentration），是 TurboQuant 所利用的核心事实。

---

解释

直观理解

| 维度 | 坐标分布特征 |
|------|--------------|
| **2 维** | 单位圆上随机一点，坐标可以是 $[0.7, 0.7]$ 这样较大的值 |
| **100 维** | 单位球上随机一点，每个坐标大约在 $\pm 0.1$ 范围内 |
| **1000 维** | 每个坐标大约在 $\pm 0.03$ 范围内，几乎都接近 0 |

为什么标准差是 $1/\sqrt{d}$

单位球面约束：$\sum_i X_i^2 = 1$

如果每个坐标独立且"平摊"能量：
$$d \cdot \text{Var}(X_i) \approx 1 \implies \text{Var}(X_i) = \frac{1}{d} \implies \text{SD}(X_i) = \frac{1}{\sqrt{d}}$$

测度集中（Measure Concentration）

**核心现象**：随着维度增加，向量的各个坐标越来越"挤向"零点附近。

| 维度 $d$ | 坐标标准差 | 坐标范围（±3σ） |
|----------|-----------|-----------------|
| 10 | ~0.316 | ~[-0.95, 0.95] |
| 100 | 0.1 | ~[-0.3, 0.3] |
| 1000 | 0.032 | ~[-0.095, 0.095] |
| 4096 (LLM 典型) | 0.016 | ~[-0.047, 0.047] |

为什么 TurboQuant 利用这个事实

1. **坐标分布可预测**：无论原始向量是什么，经过随机旋转后，每个坐标都服从均值为 0、标准差为 $1/\sqrt{d}$ 的分布
2. **统一的量化策略**：码本只需针对这个固定分布设计一次
3. **无需 per-vector 校准**：不需要为每个向量单独计算缩放因子，节省内存开销

这正是 TurboQuant 能够在高维空间中实现"near-optimal distortion"同时保持"no memory overhead for scale factors"的关键数学基础。


用大白话解释单位圆/单位球

2 维情况：单位圆

你随手在纸上画一个圆：

这个圆上任意一点 P，到原点 O 的距离永远是 **1**。

如果 P 的坐标是 **(x, y)**，那么：
$$x^2 + y^2 = 1^2 = 1$$

这就是 $\sum_i X_i^2 = 1$ 在 2 维时的样子。

例子

| 点 | 坐标 | 验证 x² + y² |
|----|------|-------------|
| (1, 0) | 在圆右端 | 1² + 0² = 1 ✓ |
| (0, 1) | 在圆上端 | 0² + 1² = 1 ✓ |
| (0.6, 0.8) | 在圆上 | 0.36 + 0.64 = 1 ✓ |
| (0.707, 0.707) | 在圆上 | 0.5 + 0.5 = 1 ✓ |

随机取一个点

在单位圆上**随机取一个点**，意思是：
- 随便扔一个飞镖到圆周上
- 每个角度被选中的概率相同（均匀分布）

这时候：
- **x 和 y 都不能随便取任意值**
- 它们必须满足 x² + y² = 1
- 如果 x = 0.9，那么 y 必须约等于 ±0.44（因为 0.9² + y² = 1）

3 维情况：单位球

到了 3 维，"圆"变成了"球面"（surface of a sphere）：

$$x^2 + y^2 + z^2 = 1$$

在单位球面上随机取一个点，每个坐标都不能自由取值，必须满足这个约束。

d 维推广

到了 d 维，没有办法画图了，但数学上一样：

$$x_1^2 + x_2^2 + ... + x_d^2 = 1$$

这就是 $\sum_i X_i^2 = 1$。

---

为什么是 1（单位）

"单位"的意思是这个圆/球的**半径是 1**。

- 半径 = 1 → 周长/表面积正好是某个好看的数字
- 半径 = 2 → 公式就变成 x² + y² = 4，不方便
- 所以数学上喜欢用单位球（半径=1）作为标准情况




向量的均值和方差，说的是每个分量

一个具体的例子

假设 d=3，我们在单位球上随机取一个点，得到向量：

$$\mathbf{X} = (X_1, X_2, X_3) = (0.5, -0.3, 0.8)$$

| 分量 | 值 |
|------|-----|
| $X_1$ | 0.5 |
| $X_2$ | -0.3 |
| $X_3$ | 0.8 |

 "每个分量的均值"是什么意思

**均值**说的是：如果我们随机取 1000 个点，每个点都得到一个向量。

取 1000 次后：
- $X_1$ 这个分量出现了 1000 个值 → 这 1000 个值的平均，就是 **$X_1$ 的均值**
- $X_2$ 这个分量出现了 1000 个值 → 这 1000 个值的平均，就是 **$X_2$ 的均值**
- $X_3$ 这个分量出现了 1000 个值 → 这 1000 个值的平均，就是 **$X_3$ 的均值**

因为**旋转对称性**，$X_1, X_2, X_3$ 的分布完全一样，所以：
$$E[X_1] = E[X_2] = E[X_3] = 0$$

一图看懂

```
随机取一个点 → (0.5, -0.3, 0.8)
随机取一个点 → (-0.1, 0.7, 0.7)
随机取一个点 → (0.2, 0.1, -0.97)
...
随机取一个点 → (-0.4, 0.6, 0.6)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
X₁ 分量收集了1000个值: [0.5, -0.1, 0.2, ..., -0.4] → 平均 ≈ 0
X₂ 分量收集了1000个值: [-0.3, 0.7, 0.1, ..., 0.6] → 平均 ≈ 0  
X₃ 分量收集了1000个值: [0.8, 0.7, -0.97, ..., 0.6] → 平均 ≈ 0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

方差同理

$$Var(X_i) = E[X_i^2] - (E[X_i])^2 = E[X_i^2] - 0 = E[X_i^2]$$

因为单位球约束 $\sum X_i^2 = 1$，平均下来每个分量分到的"能量"是 $1/d$：

$$Var(X_i) = \frac{1}{d} = \frac{1}{3} \approx 0.333$$

---

总结

| 说法 | 意思 |
|------|------|
| "每个坐标的均值是 0" | 大量随机点，取第 1 分量求平均 ≈ 0，第 2 分量求平均 ≈ 0，... |
| "每个坐标的标准差是 1/√d" | 每个分量散布的程度：d 越大，散布越小 |

**关键直觉**：一个 d 维单位向量，长度固定为 1，它的 d 个分量必须"分这个长度"，d 越大，每个分量分到的自然越小。

## 量化

Quantization, in one dimension
Snap every number to the nearest of $2^b$ levels.

This is what $b$ bits per number means. With $b=2$ you get 4 levels, $b=3$ gives 8. The gap between levels is your worst-case error. Adding one bit halves the gap, so the squared error drops by 4× per bit, the $4^{-b}$ factor that shows up later.

翻译

> **量化（Quantization），一维情况**
>
> 将每个数映射到 $2^b$ 个最近电平之一。
>
> 这就是"每数 $b$ 比特"的含义。$b=2$ 得到 4 个电平，$b=3$ 得到 8 个。电平之间的间隔就是最坏情况误差。每增加 1 比特，间隔减半，因此平方误差每比特下降 4 倍——即后续会出现的 $4^{-b}$ 因子。

---

解释

什么是量化

量化本质上是一个**离散化**操作：将连续的实数映射到有限个离散值。

```
连续世界: 0.3, 0.31, 0.317, 0.3289, 0.35, ...
    ↓ 量化 (b=2, 4 levels)
离散世界: 0,    0,    0,      0,       0.5,  ...
           ↑                    ↑
        映射到最近的电平      映射到最近的电平
```

 $b$ 比特控制精度

| 比特数 $b$ | 电平数 $2^b$ | 应用场景 |
|------------|--------------|----------|
| 1 | 2 | 极端压缩（如 sign 函数） |
| 2 | 4 | TurboQuant 低精度 |
| 3 | 8 | TurboQuant 中精度 |
| 4 | 16 | TurboQuant 高精度 |
| 8 | 256 | 典型浮点量化 |
| 32 | ~40 亿 | 全精度 float32 |

误差分析

假设数值范围归一化到 $[-1, 1]$，$2^b$ 个电平均匀分布：

| 参数 | 值 |
|------|-----|
| **电平间隔（gap）** | $\Delta = \frac{2}{2^b} = 2^{1-b}$ |
| **最坏情况误差** | $\frac{\Delta}{2} = 2^{-b}$ |
| **平方误差（最坏）** | $(2^{-b})^2 = 4^{-b}$ |

**关键洞察**：每增加 1 比特：
- 电平数翻倍：$2^b \to 2^{b+1}$
- 间隔减半：$\Delta \to \Delta/2$
- 平方误差降到原来的 $\frac{1}{4}$

这就是 $4^{-b}$ 的来源。

直观例子

假设 $b=2$（4 电平），范围 $[-1, 1]$：

```
电平位置:  -1.0   -0.33    0.33    1.0
             ▲      ▲       ▲      ▲
             │      │       │      │
        ┌────┴──────┴───────┴──────┴────┐
        │ -1.0~ -0.66 │ -0.66~0.0 │ 0.0~0.66 │ 0.66~1.0 │
        └─────────────────────────────────────────┘
        每个区间映射到区间中心的电平
```

落在 $[-0.66, 0.0)$ 的数全部被量化成 $-0.33$，误差最大约为 $0.33$。

---

在 TurboQuant 中的意义

量化是 TurboQuant 压缩高维向量的核心操作：

| 步骤 | 说明 |
|------|------|
| 1. 随机旋转 | 让每个坐标服从已知分布（高斯） |
| 2. 标准化 | 映射到 $[-1, 1]$ 或类似固定范围 |
| 3. 量化 | 每坐标 $b$ 比特，$4^{-b}$ 误差 |
| 4. 存储 | 原始 float32 → $b$ bits，大幅节省内存 |

$4^{-b}$ 这个因子后续会出现在 MSE 界限的分析中，用于证明 TurboQuant 的压缩误差上界。