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

推导过程的详细解释

1. 旋转后坐标的分布和放大因子
- **分布正确性**：旋转后坐标 $y_i$ 近似服从 $N(0, 1/d)$，这里的 $1/d$ 是**方差**（variance），不是标准差。标准差（standard deviation）是方差的平方根，所以 $\sigma = \sqrt{1/d} = 1/\sqrt{d}$。
- **为什么乘 $\sqrt{d}$ 而不是 $d$**：
  - 目标：将标准差从 $1/\sqrt{d}$ 放大到 1。
  - 数学：如果一个变量的标准差是 $\sigma$，要放大到 $\sigma' = 1$，需要乘以因子 $1/\sigma = \sqrt{d}$。
  - 验证：$(1/\sqrt{d}) \times \sqrt{d} = 1$，新标准差变为 1。
  - 如果乘 $d$，新标准差会变成 $(1/\sqrt{d}) \times d = \sqrt{d}$，这会过度放大（例如 d=100 时，标准差变成 10），不符合目标。
- **不是写错**：分布是 $N(0, 1/d)$（方差），放大因子是 $\sqrt{d}$（针对标准差）。

2. 为什么要除以 $\|x\|_2$ 而不是别的（如均值）
- **$\|x\|_2$ 的含义**：这是输入向量 $x$ 的 L2 范数（欧几里得长度），$\sqrt{\sum x_i^2}$，表示向量的"大小"或"能量"。
- **为什么用它**：
  - **保持尺度关系**：归一化后，$y' = \eta_x y$ 的坐标标准差变为 1，但向量整体长度会改变。EDEN 需要通过后续的缩放因子 $S$ 来恢复原始向量 $x$ 的尺度，而 $S$ 的公式中包含 $\|x\|_2^2$，所以 $\eta_x$ 中除以 $\|x\|_2$ 确保了归一化向量与 $x$ 的比例关系正确。
  - **不是均值**：旋转后坐标的均值已经是 0（正交变换保持均值），均值不携带尺度信息。用均值（0）除会出错。
  - **直观**：\|x\|_2 直接衡量向量长度，是尺度校正的关键。其他量（如最大坐标）不稳定或不相关。

这个设计确保归一化向量 $y'$ 的坐标服从 $N(0,1)$，便于统一量化，同时通过 $\eta_x$ 保留了与原始向量 $x$ 的尺度关联。

Python 脚本演示
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


RaBitQ (Gao and Long, SIGMOD 2024) is a parallel line of work in approximate nearest-neighbor search. The encoder rotates the input vector with a randomized rotation, stores the sign of every rotated coordinate plus a per-vector normalization scalar, and the decoder estimates inner products from the signs and the scalar. The extended paper (Gao et al., 2024, arXiv:2409.09913) proves that this estimator achieves the asymptotic optimality bound of Alon and Klartag (FOCS 2017) for inner-product quantization. RaBitQ predates TurboQuant and shares the random-rotation backbone with the DRIVE/EDEN line. The two lines reach comparable theoretical results from different framings (federated mean estimation versus ANN search), and the relationship between them is the subject of an ongoing public discussion (arXiv:2604.18555 and arXiv:2604.19528, both 2026).


**翻译**
- RaBitQ（Gao 和 Long，SIGMOD 2024）是在近似最近邻搜索领域的一个并行研究方向。编码器对输入向量施加随机旋转，记录每个旋转后坐标的符号以及每个向量的一个归一化标量；解码器则从这些符号和该标量估计内积。扩展论文（Gao 等，2024，arXiv:2409.09913）证明该估计器在内积量化问题上达到了 Alon 和 Klartag（FOCS 2017）给出的渐近最优下界。RaBitQ 早于 TurboQuant，并与 DRIVE/EDEN 系列共享随机旋转的基础方法。两条研究路线通过不同的表述（联邦均值估计 vs. ANN 搜索）得到相近的理论结果，它们之间的关系目前正在公开讨论中（arXiv:2604.18555 和 arXiv:2604.19528，均为 2026 年）。

**解释**
- **核心思想**: 先用随机正交旋转把原始向量变换到新的坐标系，然后只保存每个坐标的符号（+/-）和一个标量来记录该向量的尺度信息；用这些离散化信息重建或估计两个向量的内积。
- **为什么可行**: 随机旋转将信息均匀分布到坐标上，符号位携带关于投影方向的符号性信息，配合归一化标量可以在概率意义上恢复期望内积，从而实现低比特量化下的良好估计。
- **理论保证**: Gao 等人的扩展论文证明该估计器达到了 Alon 和 Klartag 关于内积量化的渐近最优界（即在高维或样本量趋于无穷时误差率无法被更低的下界显著改善），说明方法在理论上是接近最优的。
- **与其他工作的关系**: RaBitQ 与 TurboQuant 在时间线上有先后关系（RaBitQ 更早），并且与 DRIVE/EDEN 系列共享“随机旋转 + 符号/二值化”这一骨干思想；但两组工作出发点不同（一个从联邦均值/均值估计问题出发，另一个以 ANN 搜索为目标），因此在表述、目标函数和应用侧重点上有差异。
- **当前争论**: 最近（2026 年）有两篇公开的 arXiv 文章讨论这两条路线之间的对应与差异，表明社区正在澄清它们的等价性、优劣与适用场景。

## What is vector quantization, really?


Let's say you have a vector $\mathbf{x} \in \mathbb{R}^d$ of $d=1536$ (1536 dimension vector stored as 1536 floating point numbers). Storing all these floating point numbers is quite space intensive (assume you use float16, you will need 24576 bits to store a single vector) and therefore, you might want to store it using only $b$ bits ($b$ can be as small as 1 or 2 bits) per coordinate (with a total of $b \cdot d$ bits). Later, you want to recover an approximation $\tilde{\mathbf{x}}$ and this should be close to $\mathbf{x}$. 



假设你有一个向量 $\mathbf{x} \in \mathbb{R}^d$，其中 $d = 1536$（也就是一个 1536 维向量，存储为 1536 个浮点数）。存储所有这些浮点数非常占空间（假设你使用 `float16`，存储一个向量需要 $1536 \times 16 = 24576$ 比特）。因此，你可能希望每个坐标只用 $b$ 比特来存储（$b$ 最小可以是 1 或 2），也就是总共用 $b \cdot d$ 比特来存储整个向量。之后，你希望从这些压缩后的比特中恢复出一个近似向量 $\tilde{\mathbf{x}}$，并且这个近似向量应当与原向量 $\mathbf{x}$ 很接近。

解释

- 原向量 $\mathbf{x}$ 有 1536 个实数坐标。
- 用 `float16` 存储时，每个坐标占 16 比特，所以整个向量需要 $1536 \times 16 = 24576$ 比特。
- 为了节省空间，可以对每个坐标做“量化”，用更少的比特表示一个近似值。
- 如果每个坐标只用 $b$ 比特，则总存储量变成 $b \cdot d$ 比特。
- 当 $b = 1$ 或 $2$ 时，压缩比非常大，但恢复后的向量 $\tilde{\mathbf{x}}$ 也会有误差。
- 目标是使恢复后的向量 $\tilde{\mathbf{x}}$ 与原向量 $\mathbf{x}$ 尽量接近，这通常通过最小化某种误差度量（例如欧氏距离 $\|\mathbf{x} - \tilde{\mathbf{x}}\|$）来实现。

关键概念

- 这是一个“矢量量化”问题。
- 关键在于权衡“存储成本”与“近似精度”。
- 更少的比特 $b$ → 更高的压缩率，但逼近误差通常更大。
- 恢复出来的 $\tilde{\mathbf{x}}$ 不是原始向量，而是一个尽量接近的估计值。

Closeness is measured by

**MSE distortion** $D_{\text{mse}} = \mathbb{E} \left[ \|\mathbf{x} - \tilde{\mathbf{x}}\|_2^2 \right]$ 

or 

**inner-product error** $D_{\text{prod}} = \mathbb{E} \left[ |\langle\mathbf{y}, \mathbf{x}\rangle - \langle\mathbf{y}, \tilde{\mathbf{x}}\rangle|^2 \right]$

The second one matters because attention scores and nearest-neighbor queries are all inner products. We would like the estimator to be unbiased: $ \mathbb{E}\left[ \langle\mathbf{y}, \tilde{\mathbf{x}}\rangle \right] = \langle\mathbf{y},\mathbf{x}\rangle$

KEY WORDS
- MSE distortion: average squared error between the true vector and its reconstruction.
- Inner product $\langle x, y\rangle$: how much two vectors point the same way. This is what attention computes.
- Estimator: a rule (here: quantize, then decode) that returns an approximation 
$\hat{s}$ of a true number $s$.
- Unbiased estimator: across many queries, the average  of $\hat{s}$ equals $s$. Individual estimates can be noisy; the mean is on target.

翻译

贴近程度由以下两种方式衡量：

1. **均方误差失真**  $D_{\text{mse}} = \mathbb{E}\left[ \|\mathbf{x} - \tilde{\mathbf{x}}\|_2^2 \right]$
2. **内积误差**  $D_{\text{prod}} = \mathbb{E}\left[ \bigl|\langle \mathbf{y}, \mathbf{x} \rangle - \langle \mathbf{y}, \tilde{\mathbf{x}} \rangle\bigr|^2 \right]$

- 第二种衡量方式很重要，因为注意力机制和最近邻查询本质上都是内积计算。
- 我们希望估计器是无偏的：$\mathbb{E}\left[ \langle \mathbf{y}, \tilde{\mathbf{x}} \rangle \right] = \langle \mathbf{y}, \mathbf{x} \rangle$

解释

- $D_{\text{mse}}$ 表示重构向量 $\tilde{\mathbf{x}}$ 与真实向量 $\mathbf{x}$ 之间的平均平方距离，衡量整体重构误差。
- $D_{\text{prod}}$ 衡量的是在查询向量 $\mathbf{y}$ 下，原向量与重构向量的内积差异的平均平方值。
- 关注 $D_{\text{prod}}$ 的原因是许多任务（如注意力、相似性搜索）依赖内积，内积误差会直接影响结果。
- “估计器”指一个过程：先对 $\mathbf{x}$ 量化压缩，再解码得到 $\tilde{\mathbf{x}}$，用它去近似真实值。
- “无偏估计器”意味着虽然单次估计可能有噪声，但多次平均后，估计值的期望等于真实值，没有系统性偏差。

For each coordinate, pick the closest of $2^b$  evenly-spaced levels in $\left[ -1, 1 \right]$. That is $b$ bits per number. The same rule runs in 2D and 3D first, where the geometry is visible, before the high-dimensional version below.

First, in 2D
Drag the tip of the vector. The vector snaps to the nearest point of a $2^b *2^b$  grid. The green arrow shows the original input. The blue arrow shows where the input is quantized to. The red segment between them is the reconstruction error $x-\tilde{x}$.

翻译

对每个坐标，选择最接近的 $2^b$ 个在区间 $\left[-1, 1\right]$ 上均匀分布的量化水平。也就是说，每个数用 $b$ 比特表示。相同的规则先在二维和三维中运行，这样几何关系可见，然后再推广到下面的高维版本。

先看二维：

- 拖动向量的末端。
- 向量会“吸附”到最近的一个 $2^b \times 2^b$ 网格点上。
- 绿色箭头表示原始输入向量。
- 蓝色箭头表示输入经过量化后的向量。
- 绿色和蓝色之间的红色线段就是重构误差：$x - \tilde{x}$。

解释

- 这里的量化方法是“逐坐标量化”：对每个分量独立地在 $[-1,1]$ 内取 $2^b$ 个候选值。
- 在二维平面上，这些候选值构成一个 $2^b$ 行、$2^b$ 列的格点阵列。
- 原始向量被映射到最近的网格点，因此量化后得到的向量只是原向量的近似值。
- 红色线段表示原向量和量化向量之间的差距，这就是我们希望尽量小的误差。
- 这种几何可视化有助于理解高维量化：在高维空间中，每个分量仍然独立量化，但直观上看不到。

Now at scale (d up to 128)
The same rule applied to every coordinate of a high-dimensional vector. You cannot see the grid anymore, but the per-coordinate errors are still there.

现在放大后（d 值最大为 128）
同一规则适用于高维向量的每个坐标。虽然网格已不可见，但每个坐标的误差仍然存在。

4 种随机输入方式，都是 ML/LLM 场景里测试模型用的，我来解释一下：



1. ✅ Random Unit Vector (Uniform)
各维度独立均匀采样，然后归一化到单位长度。向量在球面上均匀分布，每个方向等概率。没有明显偏好，任何方向的信息量差不多。适合测试模型对"普通输入"的反应。

2. Adversarial: One Spike Coordinate
只有一个坐标特别大（比如第 5 维 = 0.99，其他都接近 0），其余几乎为零。这是故意构造的"对抗性"输入，用来测试模型对极端稀疏输入的敏感度，以及模型是否会被少数几个坐标主导。

3. 🟡 Random Gaussian
各维度独立从标准正态分布 $N(0,1)$ 采样，**不归一化**。向量长度随机关联，服从 $\chi$ 分布。不是均匀分布在球面上，而是越长的向量出现概率越高（高维空间体积的影响）。这通常更接近真实数据在 embedding 空间里的分布特点，因为实际 embedding 往往不是单位球面上均匀的。

4. Few Large Coords (Sparse)
少数几个坐标显著，其他都小，但不是像 #2 那么极端。比如只有 3-5 个维度的值比较大，其余都是噪音。这种结构化稀疏输入测试模型捕捉"局部活跃特征"的能力。

简单说：Gaussian 和 Few Large Coords 更接近真实 embedding 分布；Random Unit Vector 是理论上的基准假设；One Spike 是极端攻击性测试。

Select the spike input. The naive quantizer's grid is spaced evenly over $\left[ -1, 1\right]$. The input has almost all of its magnitude in a single coordinate, whose value falls between the two grid levels nearest to it and so reconstructs poorly. The remaining coordinates are near zero and consume most of the levels despite carrying little of the input's information.


翻译

选择“尖刺输入”。朴素量化器在区间 $[-1,1]$ 上均匀布置网格。输入向量的大部分幅值集中在单个坐标 $x_{i^*}$ 上，该坐标的数值落在最靠近它的两个网格水平之间，因此重构得很差。其余坐标接近零，但量化器仍把大多数量化级别分配给整个区间，浪费了大量不携带信息的级别。

解释（使用行内公式）

- “尖刺输入”指向量 $\mathbf{x}$ 的能量主要集中在某个坐标 $x_{i^*}$，其余坐标几乎为零。  
- 朴素逐坐标量化在 $[-1,1]$ 上为每个分量分配 $2^b$ 个均匀水平；因此在二维上形成 $2^b\times2^b$ 的格点。  
- 若 $x_{i^*}$ 落在两个相邻量化级之间，则量化后得到 $\tilde{x}_{i^*}$ 与 $x_{i^*}$ 的差 $x_{i^*}-\tilde{x}_{i^*}$ 可能较大，导致重构误差（总体为 $x-\tilde{x}$）。  
- 由于大多数级别用于表示接近零的分量，实际携带信息的高幅值坐标没有得到足够精度，造成比特资源浪费。  
- 这种情况会显著增大均方误差 $D_{\text{mse}}=\mathbb{E}\bigl[\|\mathbf{x}-\tilde{\mathbf{x}}\|_2^2\bigr]$ 和内积误差 $D_{\text{prod}}=\mathbb{E}\bigl[|\langle\mathbf{y},\mathbf{x}\rangle-\langle\mathbf{y},\tilde{\mathbf{x}}\rangle|^2\bigr]$，特别是当任务对 $x_{i^*}$ 非常敏感时。  
- 常见改进包括非均匀量化、逐向量缩放、自适应比特分配或稀疏编码，把更多精度分配给重要坐标，从而降低 $D_{\text{mse}}$ 与 $D_{\text{prod}}$。

TAKEAWAY

where the gap shows up

A fixed grid produces small reconstruction errors on inputs whose coordinates are roughly uniform in magnitude, and large reconstruction errors on inputs whose magnitude is concentrated in one or a few coordinates. Next: §2 shows how production systems handle the second case and what they pay for the fix.

记录进度：把此翻译任务标记为已完成并写入待办。

Created 1 todo

翻译（使用行内公式）

固定的网格在那些各坐标大小大致相近的输入上产生较小的重构误差，而在幅值集中在一个或少数几个坐标的输入上产生较大的重构误差。下一步：第2节展示了生产系统如何处理第二种情况，以及为修复它需要付出的代价。

解释（使用行内公式）

- 当向量的各坐标幅值“均匀”时（每个分量规模相近），均匀分布的量化级别能较好覆盖所有分量，因而重构误差小。  
- 对于“尖刺”或“稀疏”输入——即绝大部分能量集中在某些坐标 $x_{i^*}$ 上，而其他坐标接近零——固定均匀网格会把大量表示精度浪费在不重要的近零坐标上，导致重要坐标的量化误差很大。  
- 生产系统通常通过引入额外机制来修复第二类错误，例如逐向量缩放（per-vector scale）、非均匀/对数量化、自适应比特分配或稀疏编码等。  
- 这些修复可以显著降低均方误差 $D_{\text{mse}}$ 和内积误差 $D_{\text{prod}}$，但会带来额外开销——比如更多的元数据（标量/缩放因子）、更复杂的编码/解码逻辑、或增加的计算与存储成本。

## The adversarial coordinate, and why production systems pay a tax

Real embeddings are rarely flat. Trained models are likely to produce outlier channels. This means a few coordinates are much larger than the rest. Having a fixed $\left[ -L, L\right]$ grid either clips the outliers or wastes resolution on the bulk. Production quantizers (GPTQ, AWQ, KIVI, KVQuant) work around this by computing $(min,max)$  (or zero-point and scale) for every small block and storing those in full precision as side information.


翻译

对抗性坐标，以及为什么生产系统要付出“代价”

真实的嵌入向量很少是平坦的。训练好的模型往往会产生异常通道（outlier channels），也就是说少数坐标的数值远大于其余坐标。使用固定的网格 $[-L,L]$ 要么把这些异常值截断（clipping），要么在大多数坐标上浪费分辨率。生产环境中的量化器（如 GPTQ、AWQ、KIVI、KVQuant）通过对每个小块计算 $(\min,\max)$（或零点和尺度）并将其以全精度作为侧信息存储来解决这个问题。

解释

- “异常通道”意味着存在少数坐标 $x_{i^*}$ 的幅值远大于其他坐标，导致分布不平坦。  
- 用固定区间 $[-L,L]$ 的均匀网格量化时，必须在“覆盖异常大值”与“在大多数坐标上保留精度”之间权衡；两者难以兼得。  
- 生产量化器的做法是把向量分成小块（block），对每个小块分别计算本地的 $(\min,\max)$ 或者零点/尺度，然后用该局部参数把该块的值映射到量化网格。  
- 存储这些局部 $(\min,\max)$ 或零点/尺度需要额外的元数据（以全精度存储），这就是生产系统为改善重构和内积保真度而“支付的代价”——额外的存储和少量的计算开销。  
- 该方法能显著降低对异常坐标的量化误差，从而改善 $D_{\text{mse}}$ 与 $D_{\text{prod}}$，但会增加每个向量或每个块的比特开销和实现复杂度。

A 64-dimensional vector whose coordinates are mostly small, with one large outlier shown in red. Three quantizers reconstruct the same vector at the same b-bit budget. Strategy A uses a single fixed grid for the whole vector. Strategy B adapts the grid per block, at the cost of a float16 header per block. Strategy C rotates the vector first and then applies a single fixed grid. The metrics report the RMSE of each reconstruction and the effective bits-per-value once the metadata cost is included.

记录进度：将“翻译并解释量化器比较”任务加入待办并标记为已完成。

Added 1 todo

翻译

一个 64 维向量，其大多数坐标很小，只有一个大的异常值（用红色标示）。三个量化器在相同的每值 $b$ 比特预算下重构同一向量。策略 A 对整个向量使用单一固定网格。策略 B 对每个块自适应网格，但每块额外存储一个 float16 头信息。策略 C 先对向量做旋转（spread 能量），然后再使用单一固定网格。指标报告每种重构的 RMSE 以及在包含元数据成本后每值的有效比特数。

解释

- 向量维度为 $64$，在“尖刺”情形下大部分能量集中在一个坐标，固定网格容易对该坐标量化差。  
- 策略 A（单一固定网格）：实现最简单，但对异常值鲁棒性差，RMSE 往往较高。  
- 策略 B（每块自适应）：对每个块保存局部参数（如 $(\min,\max)$ 或 scale/zero-point），能显著降低局部量化误差，因而降低 RMSE，但每块的 float16 头信息会增加元数据开销，导致有效每值比特数 $b_{\mathrm{eff}}=b+\dfrac{\text{metadata bits}}{64}$ 增大。  
- 策略 C（先旋转再量化）：通过旋转把异常能量分散到多个坐标，使得单一固定网格能更平均地表示所有坐标，RMSE 下降；代价是需要额外计算（以及在某些方案下需要存储或固定旋转矩阵），如果旋转矩阵可共享则不增加每向量元数据。  
- 指标说明：RMSE 可写作 $\mathrm{RMSE}=\sqrt{\mathbb{E}\bigl[\|\mathbf{x}-\tilde{\mathbf{x}}\|_2^2/64\bigr]}$；“有效比特/值”把原始 $b$ 与分摊到每个值的元数据位数相加，用来衡量实际压缩率与精度的权衡。  
- 总结：B 在减少误差上通常优于 A，但付出元数据开销；C 在可行时能同时获得低 RMSE 和低元数据开销（若旋转可共享），但引入计算或系统复杂性。

The effective bits-per-value works out to b + 32/s for the per-block scheme and to b for the other two, because only the per-block scheme stores a float16 scale and zero-point (32 bits together) for every block of s elements. At b=3, s=16 the per-block cost works out to 3 + 2 = 5 bits/value, a 66% surcharge over the nominal b. Strategy C achieves the same storage cost as strategy A while producing the reconstruction quality of strategy B. The rest of this page explains the construction that makes that possible.

翻译

有效每值比特数对于每块方案计算为 $b + \frac{32}{s}$，而另外两个方案则仍为 $b$，因为只有每块方案需要为每个 $s$ 个元素块存储一个 float16 的 scale 和 zero-point（合计 32 比特）。当 $b=3$、$s=16$ 时，每块开销变成 $3 + 2 = 5$ 比特/值，相当于比名义 $b$ 多出 $66\%$。策略 C 在存储成本上与策略 A 相同，同时获得了策略 B 的重构质量。这一页面其余部分解释了使这成为可能的构造。

解释

- 每块方案需要额外元数据：每个块存一个 16-bit scale 和一个 16-bit zero-point，总共 $32$ 比特。
- 如果每个块包含 $s$ 个值，这些元数据摊到每个值上就是 $\frac{32}{s}$ 比特。
- 因此每块方案的有效比特率是 $b + \frac{32}{s}$；其他方案没有这部分额外元数据，仍然是 $b$。
- 以 $b=3$、$s=16$ 为例，额外成本是 $\frac{32}{16}=2$，所以实际每值用 $5$ 比特，等于名义值的 $166\%$。
- 关键点是：策略 C 通过先旋转向量再用固定网格，可以避免每块额外存储 scale/zero-point，因此存储成本与 A 一致，但重构效果达到 B 的水平。
- 后续内容将说明这种“固定网格+旋转”构造的具体方法。

每块的 `scale` 和 `zero-point` 逻辑是把该块内的实数值区间映射到有限的 `2^b` 个整数级别上。

具体步骤：

- 先对当前块内的值求局部范围：
  - $\min = \min_i x_i$
  - $\max = \max_i x_i$

- 用这个范围决定量化步长（scale）：
  - $\text{scale} = \dfrac{\max - \min}{2^b - 1}$

- 用这个范围决定零点（zero-point），通常让最小值对应到整数 0：
  - $\text{zero-point} = \operatorname{round}\!\left(-\,\dfrac{\min}{\text{scale}}\right)$

这样，每个块里的值量化和重构为：

- 量化：$q_i = \operatorname{clamp}\!\left(\operatorname{round}\!\left(\dfrac{x_i}{\text{scale}} + \text{zero-point}\right),\,0,\,2^b-1\right)$
- 解码：$\tilde{x}_i = \text{scale}\,\bigl(q_i - \text{zero-point}\bigr)$

所以 `scale` 决定一个整数级别对应多少实数幅度，`zero-point` 决定整数 0 对应哪个实数值。每块都单独存这一对参数，才能让每块的量化网格自适应局部最小/最大值。

举个具体例子：

假设一个块里的 4 个值是 $[0.1,\ 0.4,\ 0.9,\ 1.2]$，采用 $b=2$ 比特，则每块有 $2^b=4$ 个量化级别。

1. 计算局部范围：
   - $\min=0.1$
   - $\max=1.2$

2. 计算 scale：
   - $\text{scale}=\dfrac{\max-\min}{2^b-1}=\dfrac{1.2-0.1}{3}=0.3667$

3. 计算 zero-point：
   - $\text{zero-point}=\operatorname{round}\!\left(-\,\dfrac{\min}{\text{scale}}\right)=\operatorname{round}\!\left(-\,\dfrac{0.1}{0.3667}\right)=0$

4. 量化每个值：
   - $q_1=\operatorname{round}\!\left(\dfrac{0.1}{0.3667}+0\right)=0$
   - $q_2=\operatorname{round}\!\left(\dfrac{0.4}{0.3667}+0\right)=1$
   - $q_3=\operatorname{round}\!\left(\dfrac{0.9}{0.3667}+0\right)=2$
   - $q_4=\operatorname{clamp}\!\left(\operatorname{round}\!\left(\dfrac{1.2}{0.3667}+0\right),0,3\right)=3$

5. 解码重构：
   - $\tilde{x}_1=0.3667\,(0-0)=0$
   - $\tilde{x}_2=0.3667\,(1-0)=0.3667$
   - $\tilde{x}_3=0.3667\,(2-0)=0.7333$
   - $\tilde{x}_4=0.3667\,(3-0)=1.1000$

这个例子里，块的 $\text{scale}$ 和 $\text{zero-point}$ 是基于该块的最小值和最大值计算出来的，因此量化网格能自适应这一块的范围，而不是用全局固定的 $[-L,L]$ 网格。

Production quantizers handle outliers by paying a per-block metadata tax. TurboQuant must instead be data-oblivious: a single procedure that runs on every vector with no calibration set and no per-block headers. Next: §3 introduces the move that makes a fixed grid work for every input.

Production quantizers 通过支付每块元数据税来处理异常值。TurboQuant 则必须是数据不可知的：一个在每个向量上都运行的单一过程，不依赖校准集，也不存储每块头信息。下一步：第 3 节介绍使固定网格对每个输入都有效的关键步骤。

## Multiply by a random rotation. Watch the spike dissolve.

好的，原文+译文对照：


§3. The Rotation Trick

**Multiply by a random rotation. Watch the spike dissolve.**


**中文：** 乘以一个随机旋转矩阵，然后观察 spike 消失。


**The rotation trick:** apply a random orthogonal transform **Π**, then quantize coordinate-wise. Rotation is lossless, it preserves length and inner products exactly:

$$||Π\mathbf{x}||_2 = ||\mathbf{x}||_2 \quad \cdot \quad \langle Π\mathbf{x}, Π\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle \quad \cdot \quad Π^⊤Π = \mathbf{I}$$



**中文：** **旋转技巧：** 先对向量 **x** 应用一个随机正交变换 **Π**，再对每个坐标独立做量化。旋转是**无损的**，它严格保持向量的欧氏长度和内积：...



Because rotation is exact, all reconstruction error comes from the quantization step alone. After a uniformly random rotation, every coordinate of Π**x** follows the same fixed Beta density (Lemma 1 of the paper), regardless of what **x** looked like. **A single codebook designed once for that density is then optimal for every input.** We build the codebook in **§5**.


**中文：** 因为旋转是精确的，所有重建误差都**只来自量化这一步**。经过均匀随机旋转后，Π**x** 的每个坐标都服从同一个固定的 Beta 分布（见论文 Lemma 1），无论原始 **x** 长什么样。**因此，一个为这个分布专门设计的码本，对所有输入都是最优的。** 我们在 §5 中构建这个码本。


> **Lineage** The random-rotation step and the analysis of the post-rotation Beta density were introduced by **DRIVE (Vargaftik et al., NeurIPS 2021, §3)**. DRIVE also shows the density approaches $\mathcal{N}(0, 1/d)$ as $d$ grows, which is what makes a single fixed codebook work. See **§0.9** for the full mapping.



> **中文：** 📌 **传承：** 随机旋转这一步以及旋转后 Beta 密度的分析，来自于 **DRIVE (Vargaftik et al., NeurIPS 2021, §3)**。DRIVE 还证明了随着维度 d 增大，该分布趋近于 $\mathcal{N}(0, 1/d)$，这就是单一固定码本可行的原因。详见 §0.9 的完整映射。

▼ **How to construct Π**

Generate a $d \times d$ matrix of i.i.d. $\mathcal{N}(0, 1)$ entries and run QR decomposition; keep the orthogonal factor $Q$. The result is uniform on the orthogonal group $O(d)$, which is what Lemma 1 needs.


▼ **如何构造 Π**

生成一个 $d \times d$ 的矩阵，元素独立同分布服从 $\mathcal{N}(0,1)$，做 QR 分解；取正交因子 Q。即得到均匀分布在正交群 $O(d)$ 上的矩阵，这正是 Lemma 1 所需的。


解释

这段讲的是向量量化（Vector Quantization）中一个非常聪明的方法，核心思路如下：

问题是什么？
- 传统量化是对向量的每个坐标独立做量化（比如聚类）。
- 但问题是：**不同输入向量的分布完全不同**。一个稀疏向量（几个坐标大）和一个稠密向量的最佳量化方式是不一样的。一套码本不可能对所有输入都最优。

旋转技巧的解决方案

1. **随机旋转 Π**：在量化之前，先对向量 **x** 乘以一个随机正交矩阵 Π。这步是**无损的**——长度不变，内积不变，信息完全不丢失。

2. **统一分布**：关键洞察是——经过均匀随机旋转后，**任何向量的每个坐标都会服从同一个 Beta 分布**，跟原始向量的结构无关。也就是说，不管你的输入是稀疏的、稠密的、还是只有一个 spike，旋转后都变成"标准化"的状态了。

3. **单一码本就够了**：既然所有输入旋转后都变成同一个分布，那就可以**用一套码本对所有输入都是最优的**，而不需要针对每种输入类型设计不同的码本。

为什么要观察 spike 消失？
原始向量可能有极端的 spike（少数坐标特别大），但旋转会把这种能量**均匀分散到所有维度**上，使得旋转后的向量每个坐标的分布都差不多，避免了少数几个坐标主导量化误差的问题。

构造 Π 的方法
用 QR 分解：从标准正态分布采样得到随机矩阵 A，然后做 QR 分解，Q 就是均匀分布在 $O(d)$（正交群）上的矩阵。这是生成随机正交矩阵的标准做法。

**一句话总结：** 旋转技巧通过随机正交变换，把所有不同结构的输入"洗牌"成统一分布，从而让单一码本能最优地量化所有输入。

A spike in 2D


**A spike in 2D**

Start with the extreme case: a vector with all of its magnitude in one coordinate, $(1, 0)$. Rotate by angle $\theta$ and observe how the magnitude is redistributed across the two coordinates. At $\theta=45^\circ$ the magnitude is split evenly between the two coordinates, giving $(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$. The total length of the vector stays the same throughout.



中文翻译

**2D 中的 Spike（尖峰）**

从一个极端情况开始：假设有一个向量，它的所有能量都集中在一个坐标上，即 $(1, 0)$。对它旋转角度 $\theta$，观察能量如何重新分布到两个坐标上。当 $\theta = 45^\circ$ 时，能量被均匀地分到两个坐标，得到 $(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$。在整个旋转过程中，向量的总长度保持不变。


解释

这段是用**最简单最直观的 2D 例子**来说明旋转技巧的核心思想：

直观演示

1. **旋转前**：向量 $(1, 0)$，只在 x 轴方向有一个尖峰，y 轴方向为 0。这是极度不均衡的"spike"状态。

2. **旋转 45° 后**：向量变成 $(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$，两个坐标的幅度完全相同。尖峰被"打散"了。

3. **关键观察**：总长度始终是 $\sqrt{1^2 + 0^2} = 1$，旋转后长度不变——这就是正交变换（旋转）保持欧氏距离的含义。

为什么这个例子重要？

- **1D spike 是最极端的情况**：想象一个 embedding 向量，其 1536 维中只有一个维度有值，其他全是 0。这种极端稀疏的输入在量化时会遇到麻烦——如果码本设计不合理，这个 spike 就很难被准确表示。
- **旋转后变得"正常"了**：经过随机旋转，尖峰能量被均匀分散到所有维度上，每个坐标的分布都趋于一致，不再有极端的单个坐标主导问题。
- **这个 2D 的例子可以推广到高维**：在 1536 维的空间里，同样的原理会让 spike 能量分散到所有维度上，每个坐标都服从同一个 Beta 分布。

一句话总结

旋转技巧就是：**把一个极度不均衡的向量"搅匀"，让它变成每个维度都差不多均匀分布的状态，从而让统一的码本能高效地量化它。**


The same construction in three dimensions. The spike 
 is rotated by a random orthogonal matrix, which spreads the input's magnitude across all three coordinates of the output. The total length of the vector is preserved. Each fresh draw of the random rotation produces a different spread.

 相同的构造在三维中的效果。这个尖刺向量被一个随机正交矩阵旋转，旋转后输入的幅值被分散到输出的三个坐标上。向量的总长度保持不变。每次重新抽取随机旋转都会得到不同的分布。

At high dimension

 A single rotation in 2-D reduces the largest coordinate to at most half the input's magnitude. A random rotation in 3-D typically leaves one coordinate around 0.7
. At $d=64$ the largest coordinate after rotation is around $1/\sqrt{d}\approx0.125$, regardless of how concentrated the input was.

翻译

在高维情况下：

- 2 维中的一次旋转可以把最大坐标缩小到不超过输入幅值的一半。
- 3 维中的随机旋转通常会让最大坐标约为 $0.7$。
- 在 $d=64$ 时，旋转后的最大坐标大约为 $1/\sqrt{d}\approx0.125$，与输入原本多么集中无关。

解释

- 这段话在说明：随着维度增长，随机正交旋转能把“尖刺”能量更均匀地分散到各个坐标上。
- 在 2D 里，旋转后最大的坐标最多只有原始幅值的一半，因此输入不再只集中在一个方向。
- 在 3D 里，随机旋转后最大坐标通常约为 $0.7$，说明能量已部分分散，但仍有一定偏差。
- 到了高维，比如 $d=64$，随机旋转后每个坐标的典型大小约为 $1/\sqrt{64}\approx 0.125$，这意味着无论原始向量多么“尖刺”，旋转后各坐标都变得比较均匀，极大降低了最坏坐标的幅值。

Rotation preserves length and inner products. The only thing it changes is which coordinates contain the magnitude of the vector. A vector with all of its mass concentrated in one coordinate becomes, after rotation, a vector whose mass is spread across all $d$ coordinates. Every input that gets quantized is of this spread-out kind. Next: §3.5 shows that the same rotated coordinates feed three different decoders across the prior-work map of §0.9.


翻译

旋转保持长度和内积不变。它唯一改变的是向量的幅值（magnitude）"装在"哪些坐标里。一个所有质量都集中在一个坐标上的向量，经过旋转后会变成一个质量分散到全部 $d$ 个坐标上的向量。所有进入量化的输入都是这种"已分散"形态的。下一节（§3.5）会说明：在 §0.9 的先驱工作（prior work）图谱中，**同一组旋转后的坐标会喂给三种不同的解码器**。


解释

这段话是 **§3「旋转技巧」的收尾总结句**，同时也是过渡到 **§3.5「三种解码器」** 的桥段。逐句拆开来看：

句 1：旋转保持长度和内积

$$\|\Pi \mathbf{x}\|_2 = \|\mathbf{x}\|_2, \qquad \langle \Pi \mathbf{x}, \Pi \mathbf{y}\rangle = \langle \mathbf{x}, \mathbf{y}\rangle$$

- 这是正交矩阵（orthogonal matrix）的**等距性（isometry）**。
- 含义：旋转**完全不丢信息**，所有重建误差只能来自后面的量化步骤。
- 这一点正是 §3.1 给出的三个等式所要表达的核心结论。

句 2：它唯一改变的是幅值所在的坐标

- 旋转不会让向量变长或变短，也不会改变两个向量的夹角。
- 它**仅仅**重新分配"哪一维装了多少幅值"。
- 类比：把一杯水从一只高玻璃杯倒进一只矮水杯，水量没变，形状变了。

句 3：集中向量 → 分散向量

- 旋转前：$(1, 0, 0, \ldots, 0)$（极端的"尖刺"）。
- 旋转后：每个坐标大约 $\sim 1/\sqrt{d}$（在 $d=64$ 时大约 $0.125$）。
- 这是为什么可以用**一个固定的码本**——因为尖刺被打散了，旋转后的每个坐标都服从同一个分布（Beta / 趋近 $\mathcal{N}(0,1/d)$），与原始向量长什么样无关。

句 4：所有被量化的输入都是"已分散"形态

- 这是一个**管道（pipeline）声明**：在量化之前先做旋转 Π。
- 因此，§3.5 中讨论解码器时，可以**假设**输入已经是"已分散"形态，而不需要再为每种原始输入单独设计解码器。

## The rotation step is shared. The decoder is what changes.

The random rotation of §3 is the encoder front end shared by every method on the prior-work map of §0.9 (DRIVE 2021, EDEN 2022, RaBitQ 2024, QJL 2024, TurboQuant 2025). The methods differ on the decoder side: each one reads the rotated coordinates and recovers a different quantity from them.

The demo below runs one rotated vector through three decoders in parallel. The mean decoder from DRIVE returns an unbiased estimate of $x$  itself. The inner-product decoder from RaBitQ and QJL returns an estimate of $\langle q,x \rangle $
 against a query. The MSE decoder from EDEN and TurboQuant returns a low-distortion reconstruction 
. Each panel reports its error against the true value and the bits it stored per coordinate to get there.


译文

**旋转步骤是共享的。解码器才是变化之处。**

§3 中的随机旋转是 §0.9 论文地图上每种方法（共 DRIVE 2021、EDEN 2022、RaBitQ 2024、QJL 2024、TurboQuant 2025）共享的编码器前端。这些方法的区别在于**解码器端**：每种方法读取旋转后的坐标，并从中恢复出**不同的量**。

下面的演示将一个旋转后的向量并行地通过三个解码器。DRIVE 的均值解码器返回 x 本身的无偏估计。RaBitQ 和 QJL 的内积解码器返回关于查询 q 的估计值 ⟨q,x⟩。EDEN 和 TurboQuant 的 MSE 解码器返回低失真重建 $\hat{x}$。每个面板报告其误差（相对于真值）以及为达到该精度每位坐标存储的比特数。

 解释

这段话描述的是**量化索引方法（Quantization Indexing Methods）**的核心设计思想：

| 组件 | 作用 | 共享/独特 |
|------|------|-----------|
| **旋转（Rotation）** | 将数据旋转到新坐标系，打破原始维度间的依赖关系 | **所有方法共享** |
| **解码器（Decoder）** | 从旋转后的压缩坐标中恢复目标量 | **每种方法独特** |

**三种解码器：**

1. **均值解码器（DRIVE）** → 恢复原始向量本身 $\hat{x} \approx x$
2. **内积解码器（RaBitQ/QJL）** → 恢复向量与查询的内积 $\langle q, x \rangle$（用于最近邻搜索）
3. **MSE 解码器（EDEN/TurboQuant）** → 恢复最小均方误差意义下的重建 $\hat{x}$

这种"共享编码器 + 独特解码器"的模块化设计允许不同方法复用同一套旋转/量化流程，只需更换解码器即可适配不同任务。


现在我创建 DRIVE Mean encoder/decoder 演示脚本，命名为 `103-1.py`（对应 chapter_103 的第一个 demo）。



Ran terminal command:  pyenv shell qlib && /Users/huhao/.pyenv/versions/3.11.9/bin/python code/103-1.py

代码运行成功，演示效果完全符合理论。

文件已创建

103-1.py — DRIVE 一比特 Mean encoder/decoder 演示

关键要点

| 项 | 编码 | 解码 |
|---|---|---|
| **共享旋转** | $y = R x$ | $R^T$ 逆旋转 |
| **1 比特** | $\text{sign}(y) \in \{+1,-1\}^d$ | 同样使用 |
| **无偏缩放** | $S = \|x\|_2^2 / \|R x\|_1$ | $E[\hat x] = x$ |
| **MSE 缩放** | $S = \|R x\|_1 / d$ | 单次重建误差更小，但有偏 |

运行结果验证

- **无偏性**：200 次试验平均后，$\|\overline{\hat x} - x\| \approx 0.053$（小），说明 $E[\hat x] = x$
- **有偏性**：MSE-optimal 版本 $\approx 0.365$（显著非零），确认其有偏
- **方向**：cos(x, x̂) ≈ 0.79，单次重建与真向量方向基本一致

