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


> 什么是向量的均值和方差？

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

## 历史论文

DRIVE (Vargaftik et al., NeurIPS 2021) introduced the construction for one bit per coordinate. A sender rotates the input vector by a random orthogonal matrix, sends the sign of every rotated coordinate together with a single scalar scale $S$ , and the receiver inverts the rotation after multiplying the sign vector by $S$. DRIVE derives two scale formulas. The MSE-optimal biased scale is $S=\|R(x)\|_1/d$
. The unbiased scale is $S=\|x|_2^2/\|\R(x)\|_1$, which gives $E[\hat{x}]=x$. DRIVE also shows that a Randomized Hadamard Transform can replace the uniform random rotation at $O(d log d)$ cost (DRIVE, §6).


翻译

> DRIVE（Vargaftik 等，NeurIPS 2021）提出了每坐标 1 比特的构造方法。发送方将输入向量乘以一个随机正交矩阵进行旋转，发送旋转后每个坐标的符号（sign）以及一个标量缩放因子 $S$，接收方将符号向量乘以 $S$ 后再逆旋转。DRIVE 给出了两个缩放公式：MSE 最优的**有偏**缩放为 $S=\|R(x)\|_1/d$；**无偏**缩放为 $S=\|x\|_2^2/\|R(x)\|_1$，可使得 $E[\hat{x}]=x$。DRIVE 还证明了随机 Hadamard 变换可以替换均匀随机旋转，代价为 $O(d \log d)$（DRIVE, §6）。

---

解释

**DRIVE 的通信协议**（一比特量化）：

```
Sender                          Receiver
  │                                │
  │  x (d维向量)                    │
  │  ↓                             │
  │  R (随机正交矩阵)                │
  │  ↓                             │
  │  y = Rx                        │
  │  ↓                             │
  │  sign(y)  ──── 传输 ────→  sign(y)  
  │  S (缩放因子) ─── 传输 ───→  S    │
  │                                │
  │                           S × sign(y)
  │                                ↓
  │                           R^T (逆旋转)
  │                                ↓
  │                           x̂ (重建向量)
```

**两个缩放公式对比**：

| 公式 | 名称 | 特点 |
|------|------|------|
| $S = \frac{\|R(x)\|_1}{d}$ | MSE 最优有偏 | 最小化均方误差，但 $E[\hat{x}] \neq x$ |
| $S = \frac{\|x\|_2^2}{\|R(x)\|_1}$ | 无偏 | $E[\hat{x}] = x$，但 MSE 不是最优 |

**计算效率优化**：

- 均匀随机旋转：$O(d^2)$（矩阵乘法）
- 随机 Hadamard 变换：$O(d \log d)$（快速 Walsh-Hadamard 变换）

这使得 DRIVE 在高维场景下更加实用。


**EDEN (Vargaftik et al., ICML 2022)** generalizes DRIVE to any $b$ bits per coordinate. After the rotation, EDEN normalizes the rotated vector by $\eta_x = \sqrt{d}/\|x\|_2$ so each coordinate is approximately $N(0, 1)$, then quantizes against a Lloyd-Max codebook designed once for the standard normal. The 1-bit codebook is $\{\pm\sqrt{2/\pi}\} \approx \{\pm0.798\}$ and the 2-bit codebook is $\{\pm0.453, \pm1.510\}$. These are the exact codebooks the page derives in §5. EDEN keeps a per-vector scale $S = \|x\|_2^2 / \langle R(x), Q(\eta_x R(x))\rangle$ that yields an unbiased estimate (EDEN, Theorem 2.1).

翻译

> **EDEN (Vargaftik et al., ICML 2022)** 将 DRIVE 推广到每坐标任意 $b$ 比特。在旋转后，EDEN 通过 $\eta_x = \sqrt{d}/\|x\|_2$ 对旋转向量进行归一化，使每个坐标近似服从 $N(0, 1)$，然后针对标准正态分布一次性设计的 Lloyd-Max 码本进行量化。1 比特码本是 $\{\pm\sqrt{2/\pi}\} \approx \{\pm0.798\}$，2 比特码本是 $\{\pm0.453, \pm1.510\}$。这些正是本页在 §5 推导出的确切码本。EDEN 保留一个每向量缩放因子 $S = \|x\|_2^2 / \langle R(x), Q(\eta_x R(x))\rangle$，这产生无偏估计（EDEN, Theorem 2.1）。

---

解释

EDEN 是 DRIVE 的多比特扩展，核心思想是利用旋转后的坐标服从标准正态分布的特性，设计统一的量化码本。

| 步骤 | 含义 |
|------|------|
| **随机旋转** | 与 DRIVE 相同，$y = R x$ |
| **归一化** | $\eta_x = \sqrt{d} / \|x\|_2$，使 $y' = \eta_x y$ 的坐标近似 $N(0,1)$ |
| **量化** | 用 Lloyd-Max 码本量化 $y'$，码本针对标准正态设计 |
| **缩放因子** | $S = \|x\|_2^2 / \langle R(x), Q(\eta_x R(x)) \rangle$，确保无偏估计 |
| **重建** | $\hat{x} = R^T (Q(\eta_x R(x)) \cdot S)$ |

**码本设计**：Lloyd-Max 算法针对标准正态分布优化量化电平，1 比特和 2 比特的具体值通过数学推导得到（见 §5）。

**无偏性**：通过精心设计的 $S$，保证 $E[\hat{x}] = x$，即量化误差的期望为零。

> 解释这个归一化的公式

这个归一化公式 $\eta_x = \sqrt{d} / \|x\|_2$ 是 EDEN 算法中的关键步骤，用于将随机旋转后的向量坐标标准化为近似标准正态分布 $N(0, 1)$。下面我详细解释其含义、推导和作用。

公式分解
- **$\sqrt{d}$**：维度 $d$ 的平方根，用于放大坐标的标准差。
- **$\|x\|_2$**：输入向量 $x$ 的 L2 范数（欧几里得长度），即 $\sqrt{\sum x_i^2}$。
- **整体**：$\eta_x$ 是一个标量缩放因子，将旋转向量 $R(x)$ 乘以它得到归一化向量。

为什么需要归一化？
在高维空间中，随机旋转后的向量 $y = R(x)$ 的每个坐标服从均值 0、标准差 $1/\sqrt{d}$ 的分布（见文档中的"高维空间"部分）。这意味着坐标值很小（尤其在 LLM 典型维度如 4096 时，标准差 ≈ 0.016），直接量化会损失精度。

EDEN 的目标是让每个坐标近似服从 $N(0, 1)$，这样就可以使用针对标准正态分布优化的量化码本（Lloyd-Max 码本），实现更好的压缩效果。

推导过程
1. **旋转后坐标的分布**：$y_i \sim N(0, 1/d)$（近似）。
2. **要变为 $N(0, 1)$**：需要将标准差从 $1/\sqrt{d}$ 放大到 1，即乘以 $\sqrt{d}$。
3. **但要保持向量整体比例**：直接乘 $\sqrt{d}$ 会改变向量的长度，所以除以 $\|x\|_2$ 来补偿，确保归一化向量与原始向量相关联。

最终，归一化向量为 $y' = \eta_x \cdot y = (\sqrt{d} / \|x\|_2) \cdot R(x)$。

在 EDEN 中的作用
- **量化输入**：$y'$ 的坐标近似 $N(0, 1)$，用预设计的码本量化得到 $Q(y')$。
- **重建向量**：结合缩放因子 $S = \|x\|_2^2 / \langle R(x), Q(y') \rangle$，重建 $\hat{x} = R^T (Q(y') \cdot S)$。
- **优势**：无需为每个向量单独设计码本，一次设计（针对 $N(0, 1)$）即可适用于所有输入，节省内存和计算。

这个公式确保了量化过程的通用性和高效性，是 EDEN 从 DRIVE 扩展到多比特的关键创新。

推导过程再解释一下：
- **旋转后坐标的分布**：$y_i \sim N(0, 1/d)$（近似），然后**要变为 $N(0, 1)$**：需要将标准差从 $1/\sqrt{d}$ 放大到 1，即乘以 $\sqrt{d}$。 这里为什么要乘$\sqrt{d}$，而不是d呢？是前面的分布写错了吗？还是后面要乘的因子写错了？
- **但要保持向量整体比例**：直接乘 $\sqrt{d}$ 会改变向量的长度，所以除以 $\|x\|_2$ 来补偿，确保归一化向量与原始向量相关联，这里为什么要除以$\|x\|_2$ 而不是别的呢？比如均值。

能在 code 子目录里写一段python脚本来演示这个宣传和归一化过程吗，加一些可视化。

Optimized tool selection

Created [](file:///Users/huhao/src/linear-algebra/code/eden_demo.py)

### 推导过程的详细解释

#### 1. 旋转后坐标的分布和放大因子
- **分布正确性**：旋转后坐标 $y_i$ 近似服从 $N(0, 1/d)$，这里的 $1/d$ 是**方差**（variance），不是标准差。标准差（standard deviation）是方差的平方根，所以 $\sigma = \sqrt{1/d} = 1/\sqrt{d}$。
- **为什么乘 $\sqrt{d}$ 而不是 $d$**：
  - 目标：将标准差从 $1/\sqrt{d}$ 放大到 1。
  - 数学：如果一个变量的标准差是 $\sigma$，要放大到 $\sigma' = 1$，需要乘以因子 $1/\sigma = \sqrt{d}$。
  - 验证：$(1/\sqrt{d}) \times \sqrt{d} = 1$，新标准差变为 1。
  - 如果乘 $d$，新标准差会变成 $(1/\sqrt{d}) \times d = \sqrt{d}$，这会过度放大（例如 d=100 时，标准差变成 10），不符合目标。
- **不是写错**：分布是 $N(0, 1/d)$（方差），放大因子是 $\sqrt{d}$（针对标准差）。

#### 2. 为什么要除以 $\|x\|_2$ 而不是别的（如均值）
- **$\|x\|_2$ 的含义**：这是输入向量 $x$ 的 L2 范数（欧几里得长度），$\sqrt{\sum x_i^2}$，表示向量的"大小"或"能量"。
- **为什么用它**：
  - **保持尺度关系**：归一化后，$y' = \eta_x y$ 的坐标标准差变为 1，但向量整体长度会改变。EDEN 需要通过后续的缩放因子 $S$ 来恢复原始向量 $x$ 的尺度，而 $S$ 的公式中包含 $\|x\|_2^2$，所以 $\eta_x$ 中除以 $\|x\|_2$ 确保了归一化向量与 $x$ 的比例关系正确。
  - **不是均值**：旋转后坐标的均值已经是 0（正交变换保持均值），均值不携带尺度信息。用均值（0）除会出错。
  - **直观**：\|x\|_2 直接衡量向量长度，是尺度校正的关键。其他量（如最大坐标）不稳定或不相关。

这个设计确保归一化向量 $y'$ 的坐标服从 $N(0,1)$，便于统一量化，同时通过 $\eta_x$ 保留了与原始向量 $x$ 的尺度关联。

### Python 脚本演示
我已经在 eden_demo.py 创建了一个脚本，演示旋转、归一化和简单量化的过程，并添加了可视化（坐标分布直方图）。脚本使用 NumPy 生成随机向量和正交矩阵，Matplotlib 画图。

运行脚本（在终端中 `cd /Users/huhao/src/linear-algebra/code && python eden_demo.py`）会输出：
- 向量长度和坐标样本。
- 归一化因子。
- 量化结果。
- 保存一个 PNG 图像 `eden_demo_visualization.png`，显示三个直方图：旋转前、归一化后、量化后的坐标分布。

这演示了坐标分布从 $N(0, 1/d)$ 变为 $N(0, 1)$ 的过程。


> 有点蒙，我捋一捋：
> - 向量的均值，方差，标准差：说的是多个向量的同一个分量组成的一组数据的均值和方差
> - 向量的l2范数：总是针对同一个向量，表示向量的长度，尺度，能量，虽然它也是一组数的平方和开根号，和标准差有点像。
> 
> 我理解的对吗？



 你的理解基本正确，但有一些细微差别和上下文补充

1. 向量的均值、方差、标准差
- **你的理解**：是的，在统计学/机器学习中，这些通常指**跨多个向量（样本）的同一个分量**组成的分布。例如：
  - 如果有 1000 个 d 维向量，每个向量第 i 个分量形成一个数组，那这个数组的均值/方差/标准差就是"第 i 分量的均值"等。
  - 整体上，向量数据集的"均值向量"是指每个分量分别取均值。
- **在 TurboQuant 上下文中的具体含义**：
  - 文档中"高维空间"部分说的是：**单个随机单位向量**的坐标分布。意思是，随机生成一个单位球面上的向量，它的每个坐标（分量）的分布是均值 0、标准差 1/√d。
  - 这不是跨多个向量的统计，而是**单个向量内部坐标的统计特性**（由于旋转对称性，每个坐标的行为相同）。
  - 例如：对于一个随机单位向量 x，x_i 的均值 ≈ 0，标准差 ≈ 1/√d（d=100 时 ≈ 0.1）。

 2. 向量的 L2 范数
- **你的理解完全正确**：
  - L2 范数 ||x||_2 = √(∑ x_i²) 总是针对**同一个向量**，表示其"长度"、"尺度"或"能量"。
  - 它确实是坐标平方和的开根号，和标准差的形式类似（标准差也是平方和相关的），但：
    - **标准差**：衡量一组数据的分散程度（跨样本或跨分量）。
    - **L2 范数**：衡量单个向量的总"大小"，是标量值。
- **为什么重要**：
  - 在 EDEN 中，||x||_2 用于归一化因子 η_x = √d / ||x||_2，确保归一化后坐标的标准差变为 1，同时保留向量尺度信息，便于后续重建。

你的捋顺思路很好！这有助于区分统计量（跨样本）和向量属性（单个向量）。如果还有疑问，可以继续问。

脚本运行结果
脚本现在运行成功了（安装了 matplotlib 后）。输出显示：
- 原始向量 x 是单位向量（长度 1.0）。
- 旋转后 y 仍是单位向量（正交变换保持长度）。
- 归一化因子 η_x = 10.0（d=100, √100=10）。
- 归一化后 y_norm 长度变为 10.0，坐标分布更接近 N(0,1)（标准差 ≈1）。
- 量化使用了 sign 函数（1-bit）。
- 可视化图像已保存为 `eden_demo_visualization.png`（在 code/ 目录下），显示了三个直方图的变化过程。

> 参考这个脚本，写一个新的脚本，解决如下问题
> - 量化后的向量如何还原重构回去？
> - 重构的向量和最原始的向量的统计特征和几何特征有哪些变化？
> - 对1000个向量旋转，归一化，量化，再重构，和原始值做对比，查看偏差，方差，MSE，是否无偏？
> - 一个向量v和原始向量x求内积，然后把x先量化，再重构后得到向量y，这个v和y求内积，误差会很大吗？量化，还原能否包内积？

检查现有脚本内容，准备基于它编写新的演示脚本。

准备一个新的演示脚本，直接回答你的四个问题：重构方法、统计/几何变化、1000个向量对比，以及内积误差。

已完成：

- 新脚本文件：eden_reconstruction_demo.py
- 功能：
  - 生成 1000 个随机向量
  - 进行随机旋转、归一化、1-bit 量化
  - 执行两种重构：
    - 简单逆缩放重构
    - EDEN 1-bit 无偏缩放重构
  - 比较原始向量与重构向量的
    - 偏差
    - 方差 / MSE
    - 向量范数
    - 余弦相似度
  - 对比内积 `v·x` 与 `v·x_hat` 的误差

脚本运行正常，已生成可视化文件：
- eden_reconstruction_summary.png

运行方式：
```bash
cd /Users/huhao/src/linear-algebra/code
/Users/huhao/.pyenv/versions/3.11.9/bin/python eden_reconstruction_demo.py
```

> 解读这个输出结果，以及4个图表

```
=== 1000 个向量重构统计 ===
简单重构:
  mse: 36.288652
  mean_bias: 0.194022
  mean_norm_orig: 10.012734
  mean_norm_hat: 7.989006
  mean_cosine: 0.799825
  std_cosine: 0.020961
EDEN 无偏重构:
  mse: 57.045102
  mean_bias: 0.073262
  mean_norm_orig: 10.012734
  mean_norm_hat: 12.526806
  mean_cosine: 0.799825
  std_cosine: 0.020961

=== 数据集统计特征 ===
原始均值向量 L2: 0.311566
重构均值向量 L2: 0.376977
均值向量差异 L2: 0.241145
原始 std 均值: 1.002936
重构 std 均值: 1.255233

=== 内积保持测试 (v·x vs v·x_hat) ===
简单重构:
  mean_abs_error: 0.473935
  mean_rel_error: 1.711856
  mse: 0.352507
  corr: 0.800239
EDEN 无偏重构:
  mean_abs_error: 0.599333
  mean_rel_error: 2.572308
  mse: 0.556842
  corr: 0.799418
```

确认可视化脚本中具体绘图内容，然后解释输出和图表。

Read [](file:///Users/huhao/src/linear-algebra/code/eden_reconstruction_demo.py)

输出解读

1. “1000 个向量重构统计”
这个块对比了两种重构方法：

- `简单重构`：只是把量化后的值反归一化并逆旋转得到重构向量
- `EDEN 无偏重构`：额外用了 `S = ||x||^2 / <y, q>` 这种缩放来减少偏差

结果说明：

- `mse`
  - 简单重构：`36.29`
  - EDEN 无偏：`57.05`
  - 说明 EDEN 无偏重构虽然更“无偏”，但总体重构误差更大，MSE 反而更高。这符合偏差-方差权衡：无偏缩放降低偏差，但增加了重构方差/噪声。

- `mean_bias`
  - 简单重构：`0.1940`
  - EDEN 无偏：`0.0733`
  - 这表示 EDEN 的总体重构误差在平均意义上更接近 0，偏差更小。注意这里的 bias 是每个向量元素误差之和的平均，不是 MSE。

- `mean_norm_orig`
  - `10.0127`
  - 这是原始随机高维向量的平均 L2 长度。对于 `d=100` 的标准正态向量，长度应约为 `√100≈10`，因此这个值合理。

- `mean_norm_hat`
  - 简单重构：`7.9890`
  - EDEN 无偏：`12.5268`
  - 说明两种重构在向量尺度上都没有完美还原：
    - 简单重构整体偏小，出现“收缩”
    - EDEN 无偏整体偏大，出现“放大”
  - 这也解释了为什么 EDEN MSE 更高：它把重构长度拉得更长，虽然平均偏差更小，但离原始向量的平方误差更大。

- `mean_cosine` / `std_cosine`
  - 两种方法都约 `0.80` 的余弦相似度，说明重构向量与原始向量的方向大致一致，但不是非常精确。
  - `std_cosine ≈ 0.021` 表明相似度在 1000 个样本中比较稳定，没有极大波动。

---

2. “数据集统计特征”
这个块比较了原始数据集和 EDEN 重构后数据集的整体统计指标：

- `原始均值向量 L2: 0.3116`
- `重构均值向量 L2: 0.3770`
- `均值向量差异 L2: 0.2411`

解释：

- 原始向量的平均向量很小，这是随机高维正态向量的正常现象，平均向量接近 0。
- 重构后的平均向量仍然很小，但稍微偏离了原始平均向量，说明重构没有完全保持“均值不变”，但偏离不大。

- `原始 std 均值: 1.0029`
- `重构 std 均值: 1.2552`

说明 EDEN 重构后各分量的标准差平均值变大了，重构向量的分布比原始数据更“发散”。这和前面 `mean_norm_hat` 偏大一致。

---

 3. “内积保持测试”
这部分用了一个随机方向向量 `v`，比较了 `v·x` 和 `v·x_hat`：

- `mean_abs_error`
  - 简单重构：`0.474`
  - EDEN 无偏：`0.599`
- `mean_rel_error`
  - 简单重构：`1.71`
  - EDEN 无偏：`2.57`
- `mse`
  - 简单重构：`0.3525`
  - EDEN 无偏：`0.5568`
- `corr`
  - 简单重构：`0.800`
  - EDEN 无偏：`0.799`

解释：

- `corr≈0.80` 表示 `v·x` 和 `v·x_hat` 之间有一定线性关系，但并不紧密，重构内积只能大致保留排序/趋势。
- 相对误差很大（>1），说明 `v·x` 可能本身比较小，量化引入的误差在相对尺度上很显著。
- EDEN 无偏反而在这个测试里误差更大，说明“无偏重构”的好处主要在平均偏差上，不一定在某一个固定 `v` 的内积精度上更好。

> 结论：量化+重构不能完美包内积，只有“近似保留”。这里的误差已经不算小，说明 1-bit 量化对内积影响很大。

---

四个图表对应解释

这四个图表实际是：

1. `向量范数分布`
   - 比较原始向量 L2 范数和 EDEN 重构后向量 L2 范数。
   - 你会看到原始向量集中在 10 附近，而重构向量分布更偏大一些，并且更宽。
   - 这与 `mean_norm_hat=12.5268`、`std_hat` 更大的结论一致。

2. `原始与重构余弦相似度`
   - 画的是所有样本的 `cos(x, x_hat)`。
   - 如果图峰值靠近 1，说明方向保留得好；这里峰值应在 0.8 左右，说明方向保留有限。
   - 这个图告诉你“重构向量方向与原始向量对齐程度”。

3. `v·x vs v·x_hat (EDEN)`
   - 散点图中理想情况应落在对角线 `y=x`。
   - 事实上数据点会有散布，说明量化后重构的内积与原始内积存在偏差/噪声。
   - 这直接对应 `corr≈0.80` 和 `mse≈0.56`。

4. `内积误差分布 (EDEN)`
   - 这图显示的是 `v·x_hat - v·x` 的误差分布。
   - 如果分布中心在 0，说明平均上偏差小；但宽度大则说明误差波动大。
   - 这个图配合 `mean_abs_error` 和 `mean_rel_error`，说明量化后的内积误差虽均值不大，但方差显著。

---

总结

- `EDEN 无偏重构`在平均偏差上更好，但代价是更大的 MSE 和更不稳定的尺度。
- `简单重构`更“缩小”，MSE 更低，但它有更大的系统性缩减偏差。
- 对 `v·x` 内积的保持能力并不好，尤其在 1-bit 量化下，内积误差明显，相关系数只有 0.8 左右。
- 这说明：
  - 量化后向量可以部分保留几何信息（方向、相对关系）
  - 但不能完美保留内积，误差仍然较大
  - “无偏”并不等于“内积更准确”

如果你想，我也可以继续把脚本改成
- 显示简单重构和 EDEN 重构的两组内积散点图
- 改成 2-bit / 4-bit 比较
- 或者直接输出 `bias` 与 `variance` 的分解分析

> 再写一个脚本，用1,2,4,8 bit做对比，不需要保存图表，直接展示即可，可搞多个图表

Created file:///Users/huhao/src/linear-algebra/code/eden_bits_comparison.py


新脚本 `eden_bits_comparison.py` 已创建并运行成功。它比较了 1, 2, 4, 8 bit 量化效果，使用 100 个向量（减少样本以加快运行）。

关键结果解读

向量重构指标
- **MSE**：随着比特数增加，MSE 急剧下降（1-bit: 55.78 → 8-bit: 0.04），符合量化理论（每增加 1 bit，MSE 降至 1/4）。
- **Mean Bias**：1-bit 有较大正偏差（0.40），2-bit 负偏差（-0.51），4-bit 和 8-bit 接近 0，说明高比特更无偏。
- **Mean Cosine**：相似度从 1-bit 的 0.80 提升到 8-bit 的 0.9998，方向保留越来越好。
- **Mean Norm**：1-bit 重构向量偏长（12.5），2-bit 稍长（10.9），4/8-bit 接近原始（10.0），尺度恢复更准确。

 内积保持指标
- **Correlation**：从 1-bit 的 0.76 提升到 8-bit 的 0.9999，内积相对关系保留越来越好。
- **Mean Abs Error**：内积绝对误差从 0.55 降到 0.007，相对误差从 1.94 降到 0.07。
- **MSE**：内积 MSE 从 0.51 降到 0.0001。

图表展示
脚本显示了四个子图：
1. **MSE vs Bits**：指数下降曲线，显示量化精度提升。
2. **Mean Bias vs Bits**：1-2 bit 有较大偏差，4-8 bit 趋近 0。
3. **Mean Cosine vs Bits**：快速逼近 1，几何相似度提升。
4. **Inner Product Correlation vs Bits**：同样快速提升，内积保持能力增强。

结论
- **1-bit**：压缩率最高，但精度最低，适合极端压缩场景。
- **2-bit**：平衡点，MSE 降至 19，内积相关性 0.93。
- **4-bit**：MSE 降至 1.2，偏差几乎为 0，内积相关性 0.99。
- **8-bit**：接近完美，MSE 0.04，内积相关性 0.9999。

这演示了 TurboQuant 的核心优势：通过旋转+归一化，量化后仍能较好保持向量几何和内积关系，比特数越多，保持越好。

```
=== 1-bit 量化 ===
向量指标:
  mse: 55.779139
  mean_bias: 0.401442
  mean_norm_orig: 10.041614
  mean_norm_hat: 12.497600
  mean_cosine: 0.804215
  std_cosine: 0.021418
内积指标:
  mean_abs_error: 0.545660
  mean_rel_error: 1.940803
  mse: 0.505335
  corr: 0.763382

=== 2-bit 量化 ===
向量指标:
  mse: 19.322870
  mean_bias: -0.508468
  mean_norm_orig: 10.041614
  mean_norm_hat: 10.905281
  mean_cosine: 0.916109
  std_cosine: 0.008824
内积指标:
  mean_abs_error: 0.299424
  mean_rel_error: 0.897025
  mse: 0.144435
  corr: 0.926201

=== 4-bit 量化 ===
向量指标:
  mse: 1.207547
  mean_bias: -0.004870
  mean_norm_orig: 10.041614
  mean_norm_hat: 10.100669
  mean_cosine: 0.994177
  std_cosine: 0.000957
内积指标:
  mean_abs_error: 0.094754
  mean_rel_error: 0.366733
  mse: 0.013842
  corr: 0.992220

=== 8-bit 量化 ===
向量指标:
  mse: 0.040741
  mean_bias: 0.008274
  mean_norm_orig: 10.041614
  mean_norm_hat: 10.023664
  mean_cosine: 0.999830
  std_cosine: 0.000689
内积指标:
  mean_abs_error: 0.006670
  mean_rel_error: 0.068559
  mse: 0.000116
  corr: 0.999943
```
