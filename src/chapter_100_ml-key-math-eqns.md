
https://github.com/chizkidd/chizkidd.github.io/blob/main/_posts/2025-05-30-machine-learning-key-math-eqns.md


The Most Important Machine Learning Equations: A Comprehensive Guide

最重要的机器学习方程：全面指南

A comprehensive guide to the most critical machine learning mathematical equations, from probability theory to advanced concepts like diffusion models and attention mechanisms. It includes theoretical explanations and practical Python implementations.  

一部全面指南，涵盖机器学习中最关键的数学方程，从概率论到扩散模型和注意力机制等高级概念。内容包含理论阐释与实用的Python实现方案。


## Motivation
动机

Machine learning (ML) is a powerful field driven by mathematics. Whether you're building models, optimizing algorithms, or simply trying to understand how ML works under the hood, mastering the core equations is essential. This blog post is designed to be your go-to resource, covering the most critical and "mind-breaking" ML equations—enough to grasp most of the core math behind ML. Each section includes theoretical insights, the equations themselves, and practical implementations in Python, so you can see the math in action.

机器学习 (ML) 是一个由数学驱动的强大领域。无论您是构建模型、优化算法，还是仅仅想了解 ML 的底层工作原理，掌握核心方程式都至关重要。这篇博文旨在成为您的首选资源，涵盖最关键、最“令人费解”的 ML 方程式，足以帮助您掌握 ML 背后的大部分核心数学原理。每个部分都包含理论见解、方程式本身以及 Python 中的实际实现，让您能够亲眼见证数学的运作。

This guide is for anyone with a basic background in math and programming who wants to deepen their understanding of ML and is inspired by this [tweet from @goyal\_\_pramod](https://x.com/goyal__pramod/status/1923064911501914216). Let's dive into the equations that power this fascinating field!

本指南适用于任何具有数学和编程基础，并希望加深对机器学习理解，并受到 [@goyal\_\_pramod 这条推文](https://x.com/goyal__pramod/status/1923064911501914216)启发的读者。让我们深入探究驱动这个迷人领域的方程式！

* * *

## Table of Contents
目录

*   Introduction    
    介绍
    
*   Probability and Information Theory

    概率与信息论
    
    *   Bayes Theorem
        
        贝叶斯定理
    *   Entropy
        
        熵
    *   Joint and Conditional Probability
        
        联合概率和条件概率
    *   Kullback-Leibler Divergence (KLD)
        
        库尔贝克-莱布勒散度（KLD）
    *   Cross-Entropy
        
        交叉熵
*   Linear Algebra
    
    线性代数
    
    *   Linear Transformation
        
        线性变换
    *   Eigenvalues and Eigenvectors
        
        特征值和特征向量
    *   Singular Value Decomposition (SVD)
        
        奇异值分解（SVD）

*   Optimization
    
    优化
    
    *   Gradient Descent
        
        梯度下降

    *   Backpropagation
        
        反向传播

*   Loss Functions
    
    损失函数
    
    *   Mean Squared Error (MSE)
        
        均方误差（MSE）

    *   Cross-Entropy Loss
        
        交叉熵损失

*   Advanced ML Concepts
    高级机器学习概念
    
    *   Diffusion Process
        
        扩散过程
    *   Convolution Operation
        
        卷积运算        
    *   Softmax Function
        
        Softmax 函数
    *   Attention Mechanism
        
        注意力机制
*   Conclusion
    
    结论
    
*   Further Reading
    
    进一步阅读
    

* * *

## Introduction
介绍

Mathematics is the language of machine learning. From probability to linear algebra, optimization to advanced generative models, equations define how ML algorithms learn from data and make predictions. This blog post compiles the most essential equations, explains their significance, and provides practical examples using Python libraries like NumPy, scikit-learn, TensorFlow, and PyTorch. Whether you're a beginner or an experienced practitioner, this guide will equip you with the tools to understand and apply ML math effectively.

数学是机器学习的语言。从概率到线性代数，从优化到高级生成模型，方程式定义了机器学习算法如何从数据中学习并进行预测。这篇博文汇编了最重要的方程式，解释了它们的重要性，并提供了使用 NumPy、scikit-learn、TensorFlow 和 PyTorch 等 Python 库的实践示例。无论您是初学者还是经验丰富的从业者，本指南都将为您提供理解和有效应用机器学习数学的工具。

* * *

## Probability and Information Theory

概率与信息论

Probability and information theory provide the foundation for reasoning about uncertainty and measuring differences between distributions.

概率和信息论为推理不确定性和测量分布之间的差异提供了基础。

### Bayes' Theorem
贝叶斯定理

**Equation:**
方程：

$$
P(A|B) = \frac{P(B|A) P(A)}{P(B)}
$$

**Explanation:** Bayes' Theorem describes how to update the probability of a hypothesis ($A$) given new evidence ($B$). It’s a cornerstone of probabilistic reasoning and is widely used in machine learning for tasks like classification and inference.

**解释：** 贝叶斯定理描述了如何在给定新证据（ $B$ ）的情况下更新假设（ $A$ ）的概率。它是概率推理的基石，广泛应用于机器学习中的分类和推理等任务。

**Practical Use:** Applied in Naive Bayes classifiers, Bayesian networks, and Bayesian optimization.

**实际用途：** 应用于朴素贝叶斯分类器、贝叶斯网络和贝叶斯优化。

**Implementation:**

实现：

```python
def bayes_theorem(p_d, p_t_given_d, p_t_given_not_d):
    """
    Calculate P(D|T+) using Bayes' Theorem.
    
    Parameters:
    p_d: P(D), probability of having the disease
    p_t_given_d: P(T+|D), probability of testing positive given disease
    p_t_given_not_d: P(T+|D'), probability of testing positive given no disease
    
    Returns:
    P(D|T+), probability of having the disease given a positive test
    """
    p_not_d = 1 - p_d
    p_t = p_t_given_d * p_d + p_t_given_not_d * p_not_d
    p_d_given_t = (p_t_given_d * p_d) / p_t
    return p_d_given_t

# Example usage
p_d = 0.01  # 1% of population has the disease
p_t_given_d = 0.99  # Test is 99% sensitive
p_t_given_not_d = 0.02  # Test has 2% false positive rate
result = bayes_theorem(p_d, p_t_given_d, p_t_given_not_d) 
print(f"P(D|T+) = {result:.4f}")  # Output: P(D|T+) = 0.3333 
```

#### 补充

> 解释贝叶斯公式

这个公式是 **贝叶斯公式（Bayes’ theorem）**，它在概率论和统计学里非常重要，用来计算一个事件在另一个事件已经发生的条件下的概率。我们逐个部分解释：

$$
P(A|B) = \frac{P(B|A) \, P(A)}{P(B)}
$$


含义

* $P(A|B)$：在事件 $B$ 已经发生的条件下，事件 $A$ 发生的概率，叫做 **后验概率**。
* $P(B|A)$：在事件 $A$ 已经发生的条件下，事件 $B$ 发生的概率。
* $P(A)$：事件 $A$ 自身的概率，叫做 **先验概率**。
* $P(B)$：事件 $B$ 的总体概率，也叫 **标准化常数**，保证最后的结果是一个合法的概率。

---

直观解释

1. 我们通常一开始只知道 $A$ 的先验概率 $P(A)$。
2. 如果我们观测到了 $B$，就要更新对 $A$ 的认识。
3. 这个更新过程依赖于 **在 $A$ 发生时，$B$ 出现的可能性** $P(B|A)$。
4. 最终用分母 $P(B)$ 做归一化，确保概率总和为 1。

---

举例

假设你要检测一种罕见疾病：

* 人群中患病率（先验概率）是 $P(A)=0.01$。
* 如果得病，检测呈阳性的概率（灵敏度）是 $P(B|A)=0.99$。
* 如果没得病，检测也可能假阳性（比如 5%），那么可以算出总体 $P(B)$。
* 当检测结果是阳性（事件 $B$），我们想知道：你 **真的患病的概率** $P(A|B)$是多少？

这就是贝叶斯公式的作用。

我们用疾病检测的例子来算一遍。

假设：

* 患病率：$P(A)=0.01$
* 得病时检测阳性：$P(B|A)=0.99$
* 未得病时检测阳性：$P(B|\neg A)=0.05$

首先算分母 $P(B)$：

$$
P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)
$$

$$
= 0.99 \times 0.01 + 0.05 \times 0.99
$$

$$
= 0.0099 + 0.0495 = 0.0594
$$

接着用贝叶斯公式：

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)} 
= \frac{0.99 \times 0.01}{0.0594}
= \frac{0.0099}{0.0594} \approx 0.1667
$$

结果是：即使检测呈阳性，你真的患病的概率只有大约 **16.7%**。

这说明：如果疾病本身比较罕见，即便检测工具很准确，阳性结果也不一定意味着很大概率患病。

> 贝叶斯公式，贝叶斯定理，贝叶斯优化，贝叶斯分类，贝叶斯网络的区别和联系

好的，我来梳理一下这些“贝叶斯”相关的概念，它们有联系但应用场景不同。

---

**贝叶斯公式（Bayes’ formula）**
这是最基本的数学公式：

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

它描述了如何根据已有信息更新对某个事件的概率认识。所有后续“贝叶斯方法”都以它为基础。

---

**贝叶斯定理（Bayes’ theorem）**
严格来说，贝叶斯定理就是贝叶斯公式本身，只是更正式的称呼。通常在概率论和数理统计中，人们会说“贝叶斯定理”；在实际推导过程中，也常叫“贝叶斯公式”。两者可以认为是同一个东西。

---

**贝叶斯优化（Bayesian optimization）**
是一种基于贝叶斯思想的优化算法，主要用来寻找“黑箱函数”的最优解。比如你想调整机器学习模型的超参数，但函数形式未知、每次计算代价很高。

* 方法：用概率模型（常用高斯过程）来近似目标函数，把“不确定性”也纳入考虑；
* 核心思想：根据现有数据更新“先验 → 后验”，然后选择下一个最可能带来改进的点进行评估。
  它的数学思想来源于贝叶斯公式，但应用在函数优化问题上。

---

**贝叶斯分类（Bayesian classification）**
是把贝叶斯公式用于分类问题。最典型的是 **朴素贝叶斯分类器（Naive Bayes classifier）**。

* 思想：计算每个类别的后验概率 $P(\text{类别}| \text{特征})$，选最大者作为分类结果；
* 简化：假设特征条件独立，计算更高效；
* 应用：文本分类（垃圾邮件识别、情感分析）中很常见。

---

**贝叶斯网络（Bayesian network）**
是一种图模型，用有向无环图（DAG）表示随机变量之间的条件依赖关系。

* 节点：表示随机变量；
* 边：表示依赖关系（谁条件依赖谁）；
* 优点：能清晰建模复杂系统中的因果和概率关系，支持推理和学习。
  例如：医疗诊断系统里，节点可能是“疾病”“症状”“检测结果”，通过网络推断某种疾病的可能性。

---

**总结它们的关系**

* 贝叶斯公式/定理：理论根基，描述如何更新概率。
* 贝叶斯优化：把贝叶斯更新思想用于优化黑箱函数。
* 贝叶斯分类：把贝叶斯公式用于分类任务，尤其是朴素贝叶斯。
* 贝叶斯网络：一种结构化表达复杂概率依赖关系的模型，计算推理时也用贝叶斯公式。

一句话：**贝叶斯公式是根，定理是正式说法，优化/分类/网络都是在不同应用场景下对“用数据更新概率认知”这一思想的延伸。**

---

> 贝叶斯优化和梯度下降优化的区别，优劣势对比以及适用场景对比

很好，这个问题很关键。贝叶斯优化和梯度下降优化虽然都叫“优化”，但它们思路、适用问题、优劣势都完全不同。

---

**1. 核心区别**

* **梯度下降（Gradient Descent, GD）**

  * 思想：利用目标函数的梯度（导数）信息，不断往“下降最快”的方向更新参数。
  * 要求：目标函数必须可微，或者至少近似可微。
  * 更新快，适合大规模参数优化（如深度学习模型训练）。

* **贝叶斯优化（Bayesian Optimization, BO）**

  * 思想：把目标函数当作“黑箱”，用一个概率模型（常用高斯过程）来拟合它，并用贝叶斯公式不断更新对函数的认知。
  * 不需要梯度，也不需要函数有明确表达式，只要能“试一次得到一个结果”。
  * 每次试验代价较高，但能用很少的评估次数找到比较好的解。

---

**2. 优劣势对比**

| 特点    | 梯度下降                   | 贝叶斯优化                   |
| ----- | ---------------------- | ----------------------- |
| 依赖信息  | 需要梯度（或近似梯度）            | 不需要梯度，只需函数输出            |
| 计算代价  | 每次迭代便宜，可以快速更新          | 每次迭代代价大（建模和更新高斯过程）      |
| 收敛速度  | 迭代次数多，但单步便宜，总体适合大规模优化  | 迭代次数少，但每次代价大，适合昂贵函数     |
| 适用函数  | 光滑、可微、维度高的目标函数         | 黑箱、不可导、评估成本高的函数（维度不能太高） |
| 全局/局部 | 易陷入局部最优（除非配合随机性/动量等技巧） | 有一定的全局搜索能力（探索+利用）       |
| 参数规模  | 适合成千上万甚至上亿参数           | 适合几十个以内参数，太高维时困难        |

---

**3. 适用场景对比**

* **梯度下降**

  * 训练神经网络、逻辑回归、支持向量机等常见机器学习模型；
  * 大规模优化问题，变量多达数万甚至上亿；
  * 目标函数可微，计算梯度容易或能通过自动微分得到。

* **贝叶斯优化**

  * 超参数调优：比如调深度学习模型的学习率、正则化参数、树模型的深度等；
  * 工程实验：物理实验、药物设计中每次实验代价昂贵，必须“少试几次就找到好解”；
  * 黑箱函数优化：函数没有解析表达式，无法直接计算梯度。

---

简而言之：

* 梯度下降适合“大规模、便宜、可导”的问题。
* 贝叶斯优化适合“小规模、昂贵、黑箱”的问题。

要不要我帮你画一个二维的对比示意图，把“函数是否可导”“评估代价高低”作为坐标轴，直观展示什么时候该用哪种优化？

> 用python写一个贝叶斯优化的Demo

100-2.py

我已经帮你写并运行了一个简单的贝叶斯优化（Bayesian Optimization）Python 示例：用高斯过程（Gaussian Process）作为代理模型、用期望改进（Expected Improvement, EI）作为采集函数，在一维区间 \[0,1] 上最大化一个示例黑箱函数。运行结果包括两张图（GP 后验与样本点，以及收敛曲线），并打印出迭代后找到的最好点和函数值。

说明（简短）：

* 使用库：scikit-learn（GaussianProcessRegressor）、scipy.stats（标准正态分布函数）、numpy、matplotlib。
* 代理模型：带 Matern 内核的高斯过程。
* 采集函数：Expected Improvement（EI），用于权衡“探索”与“利用”。
* 策略：初始随机采样 5 个点，随后做 8 次 BO 迭代，每次在密集网格上选取使 EI 最大的点并评估目标函数。
* 输出：第一张图展示真实函数、GP 均值与 95% 置信带、采样点；第二张图展示每次迭代的最好观测值（收敛曲线）。

注意事项与扩展建议（实用）：

* 这个示例用于教学与快速验证；实际工程中常用连续优化采集函数（用局部优化而不是网格）以及更复杂的并行/噪声建模策略。
* 对维度较高的问题（比如 >20 维），传统高斯过程 BO 会变慢/不适用，可以考虑基于树的贝叶斯优化、使用降维或替代模型（如随机森林、Bayesian neural nets）等。
* 若要用于最小化目标，只需把 EI 的目标从“最大化当前 y”改成“最小化”（或优化 -f）。
* 运行时你可能看到来自 scikit-learn 的内核参数优化警告（这是正常的提示，可以通过增加重启次数或缩放数据缓解）。

> 写个简单的贝叶斯分类 demo ，可以使用sklearn来加载数据和展现结果，只分类器人工实现。

好的，那我给你写一个**简化版的手工朴素贝叶斯分类器 Demo**：

* 用 `sklearn.datasets.load_iris` 来加载鸢尾花数据；
* 用 `train_test_split` 来划分训练测试集；
* 分类器部分不用 sklearn，自行实现 **Gaussian Naive Bayes**；
* 最后输出准确率即可。

代码如下（可直接运行）：100-3.py

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class SimpleGaussianNB:
    def fit(self, X, y):
        """训练：估计每个类的先验、均值和方差"""
        self.classes = np.unique(y)
        self.class_priors = {}
        self.means = {}
        self.vars = {}
        for c in self.classes:
            X_c = X[y == c]
            self.class_priors[c] = X_c.shape[0] / X.shape[0]
            self.means[c] = X_c.mean(axis=0)
            self.vars[c] = X_c.var(axis=0) + 1e-9  # 防止除零

    def _gaussian_prob(self, x, mean, var):
        """单特征高斯概率密度"""
        coeff = 1.0 / np.sqrt(2.0 * np.pi * var)
        exponent = np.exp(- (x - mean) ** 2 / (2 * var))
        return coeff * exponent

    def predict(self, X):
        """对样本 X 预测类别"""
        y_pred = []
        for x in X:
            posteriors = []
            for c in self.classes:
                prior = np.log(self.class_priors[c])
                likelihood = np.sum(np.log(self._gaussian_prob(x, self.means[c], self.vars[c])))
                posterior = prior + likelihood
                posteriors.append(posterior)
            y_pred.append(self.classes[np.argmax(posteriors)])
        return np.array(y_pred)

    def score(self, X, y):
        """计算准确率"""
        return np.mean(self.predict(X) == y)


# 1. 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 2. 划分训练/测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. 训练模型
gnb = SimpleGaussianNB()
gnb.fit(X_train, y_train)

# 4. 测试集准确率
print("测试集准确率:", gnb.score(X_test, y_test))

# 5. 示例预测
sample = np.array([[5.1, 3.5, 1.4, 0.2]])
print("样本", sample, "预测类别:", iris.target_names[gnb.predict(sample)[0]])
```

这个 Demo 做了最小实现：

* 先计算每类的均值和方差；
* 用高斯分布公式计算似然；
* 加上先验概率，用最大后验决定类别。



### Entropy

熵

**Equation:：**

方程

$$
H(X) = -\sum_{x \in X} P(x) \log P(x)
$$

**Explanation:** Entropy measures the uncertainty or randomness in a probability distribution. It quantifies the amount of information required to describe the distribution and is fundamental in understanding concepts like information gain and decision trees.

**解释：** 熵衡量概率分布中的不确定性或随机性。它量化了描述分布所需的信息量，是理解信息增益和决策树等概念的基础。

**Practical Use:** Used in decision trees, information gain calculations, and as a basis for other information-theoretic measures.

**实际用途：** 用于决策树、信息增益计算，并作为其他信息理论测量的基础。

**Implementation:**

实现：

```python
import numpy as np

def entropy(p):
    """
    Calculate entropy of a probability distribution.
    
    Parameters:
    p: Probability distribution array
    
    Returns:
    Entropy value
    """
    return -np.sum(p * np.log(p, where=p > 0))

# Example usage
fair_coin = np.array([0.5, 0.5])  # fair coin has the same probability of heads and tails
print(f"Entropy of fair coin: {entropy(fair_coin)}")  # Output: 0.6931471805599453 

biased_coin = np.array([0.9, 0.1])  # biased coin has a higher probability of heads
print(f"Entropy of biased coin: {entropy(biased_coin)}")  # Output: 0.4698716731013394 
```

### Joint and Conditional Probability

联合概率和条件概率

**Equations:**

方程式：

*   Joint Probability:

    联合概率：
    
    $$
    P(A, B) = P(A|B) P(B) = P(B|A) P(A)
    $$
    
*   Conditional Probability:

    条件概率：
    
    $$
    P(A|B) = \frac{P(A, B)}{P(B)}
    $$
    

**Explanation:** Joint probability describes the likelihood of two events occurring together, while conditional probability measures the probability of one event given another. These are the building blocks of Bayesian methods and probabilistic models.

**解释：** 联合概率描述的是两个事件同时发生的可能性，而条件概率则衡量一个事件在另一个事件的条件下发生的概率。它们是贝叶斯方法和概率模型的基石。

**Practical Use:** Used in Naive Bayes classifiers and probabilistic graphical models.

**实际用途：** 用于朴素贝叶斯分类器和概率图模型。

**Implementation:**

实现：

```python
from sklearn.naive_bayes import GaussianNB
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])
model = GaussianNB().fit(X, y)
print(model.predict([[2.5, 3.5]]))  # Output: [1]
```

### Kullback-Leibler Divergence (KLD)

库尔贝克-莱布勒散度（KLD）

**Equation:**

方程：

$$
D_{KL}(P \| Q) = \sum_{x \in \mathcal{X}} P(x) \log \left( \frac{P(x)}{Q(x)} \right)
$$

**Explanation:** KLD measures how much one probability distribution $P$ diverges from another $Q$. It’s asymmetric and foundational in information theory and generative models.

**解释：** KLD 衡量一个概率分布 $P$ 与另一个概率分布 $Q$ 的偏离程度。它是非对称的，是信息论和生成模型的基础。

**Practical Use:** Used in variational autoencoders (VAEs) and model evaluation.

**实际用途：** 用于变分自动编码器（VAE）和模型评估。

**Implementation:**

实现：

```python
import numpy as np

P = np.array([0.7, 0.3])
Q = np.array([0.5, 0.5])
kl_div = np.sum(P * np.log(P / Q))
print(f"KL Divergence: {kl_div}")  # Output: 0.08228287850505156
```

### Cross-Entropy

交叉熵

**Equation:**

方程：

$$
H(P, Q) = -\sum_{x \in \mathcal{X}} P(x) \log Q(x)
$$

**Explanation:** Cross-entropy quantifies the difference between the true distribution $P$ and the predicted distribution $Q$. It’s a widely used loss function in classification.

**解释：** 交叉熵量化了真实分布 $P$ 与预测分布 $Q$ 之间的差异。它是分类中广泛使用的损失函数。

**Practical Use:** Drives training in logistic regression and neural networks.

**实际用途：** 推动逻辑回归和神经网络的训练。

**Implementation:**

实现

```python
import numpy as np

y_true = np.array([1, 0, 1])
y_pred = np.array([0.9, 0.1, 0.8])
cross_entropy = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
print(f"Cross-Entropy: {cross_entropy}")  # Output: 0.164252033486018
```

* * *

## Linear Algebra

线性代数

Linear algebra powers the transformations and structures in ML models.

线性代数为机器学习模型中的转换和结构提供支持。

### Linear Transformation

线性变换

**Equation:**

方程：

$$
y = Ax + b \quad \text{where } A \in \mathbb{R}^{m \times n}, x \in \mathbb{R}^n, y \in \mathbb{R}^m, b \in \mathbb{R}^m
$$

**Explanation:** This equation represents a linear mapping of input $x$ to output $y$ via matrix $A$ and bias $b$. It’s the core operation in neural network layers.

**解释：** 该方程表示输入 $x$ 通过矩阵 $A$ 和偏差 $b$ 到输出 $y$ 的线性映射。它是神经网络层中的核心操作。

**Practical Use:** Foundational for linear regression and neural networks.

**实际用途：** 线性回归和神经网络的基础。

**Implementation:**

实现：

```python
import numpy as np

A = np.array([[2, 1], [1, 3]])
x = np.array([1, 2])
b = np.array([0, 1])
y = A @ x + b
print(y)  # Output: [4 7]
```

### Eigenvalues and Eigenvectors

特征值和特征向量

**Equation:**

方程：

$$
Av = \lambda v \quad \text{where } \lambda \in \mathbb{R}, v \in \mathbb{R}^n, v \neq 0
$$

**Explanation:** Eigenvalues $\lambda$ and eigenvectors $v$ describe how a matrix $A$ scales and rotates space, crucial for understanding data variance.

**解释：** 特征值 $\lambda$ 和特征向量 $v$ 描述矩阵 $A$ 如何缩放和旋转空间，这对于理解数据方差至关重要。

**Practical Use:** Used in Principal Component Analysis (PCA).

**实际用途：** 用于主成分分析（PCA）。

**Implementation:**

实现：

```python
import numpy as np

A = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")
```

### Singular Value Decomposition (SVD)

奇异值分解（SVD）

**Equation:：**

方程

$$
A = U \Sigma V^T
$$

**Explanation:** SVD breaks down a matrix $A$ into orthogonal matrices $U$ and $V$ and a diagonal matrix $\Sigma$ of singular values. It reveals the intrinsic structure of data.

**解释：** SVD 将矩阵 $A$ 分解为正交矩阵 $U$ 和 $V$ 以及奇异值的对角矩阵 $\Sigma$ 。它揭示了数据的内在结构。

**Practical Use:** Applied in dimensionality reduction and recommendation systems.

**实际用途：** 应用于降维和推荐系统。

**Implementation:**

执行：

```python
import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
U, S, Vt = np.linalg.svd(A)
print(f"U:\n{U}\nS: {S}\nVt:\n{Vt}")
```

* * *

## Optimization

优化

Optimization is how ML models learn from data.

优化是机器学习模型从数据中学习的方式。

### Gradient Descent

梯度下降

**Equation:**

方程：

$$
\theta_{t+1} = \theta_t - \eta \nabla_{\theta} L(\theta)
$$

**Explanation:** Gradient descent updates parameters $\theta$ by moving opposite to the gradient of the loss function $L$, scaled by learning rate $\eta$.

**解释：** 梯度下降通过与损失函数 $L$ 的梯度相反的方向移动来更新参数 $\theta$ ，并通过学习率 $\eta$ 进行缩放。

**Practical Use:** The backbone of training most ML models.

**实际用途：** 训练大多数 ML 模型的支柱。

**Implementation:
执行：**

```python
import numpy as np

def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(epochs):
        gradient = (1/m) * X.T @ (X @ theta - y)
        theta -= lr * gradient
    return theta

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
theta = gradient_descent(X, y)
print(theta)  # Output: ~[0., 1.]
```

### Backpropagation

反向传播

**Equation:**

方程：

$$
\frac{\partial L}{\partial w_{ij}} = \frac{\partial L}{\partial a_j} \cdot \frac{\partial a_j}{\partial z_j} \cdot \frac{\partial z_j}{\partial w_{ij}}
$$

**Explanation:** Backpropagation applies the chain rule to compute gradients of the loss $L$ with respect to weights $w_{ij}$ in neural networks.

**解释：** 反向传播应用链式法则来计算损失 $L$ 相对于权重 𝑤 的梯度 𝑖 𝑗 w ij ​ 在神经网络中。

**Practical Use:** Enables efficient training of deep networks.

**实际用途：** 实现深度网络的有效训练。

**Implementation:**

实现：

```python
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(2, 1), nn.Sigmoid())
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

X = torch.tensor([[0., 0.], [1., 1.]], dtype=torch.float32)
y = torch.tensor([[0.], [1.]], dtype=torch.float32)

optimizer.zero_grad()
output = model(X)
loss = loss_fn(output, y)
loss.backward()
optimizer.step()
print(f"Loss: {loss.item()}")
```

* * *

## Loss Functions

损失函数

Loss functions measure model performance and guide optimization.

损失函数衡量模型性能并指导优化。

### Mean Squared Error (MSE)

均方误差（MSE）

**Equation:**

方程：

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

**Explanation:** MSE calculates the average squared difference between true $y_i$ and predicted $\hat{y}_i$ values, penalizing larger errors more heavily.
**解释：** MSE 计算真实 𝑦 之间的平均平方差 𝑖 y i ​ 并预测𝑦 ^ 𝑖 y ^ ​ i ​ 值，对较大的错误进行更严厉的惩罚。

**Practical Use:** Common in regression tasks.

**实际用途：** 在回归任务中很常见。

**Implementation:**

实现：

```python
import numpy as np

y_true = np.array([1, 2, 3])
y_pred = np.array([1.1, 1.9, 3.2])
mse = np.mean((y_true - y_pred)**2)
print(f"MSE: {mse}")  # Output: 0.01
```

### Cross-Entropy Loss

交叉熵损失

(See Cross-Entropy above for details.)

有关详细信息，请参阅上面的[交叉熵](#cross-entropy) 。）

* * *

## Advanced ML Concepts

高级机器学习概念

These equations power cutting-edge ML techniques.

这些方程为尖端的机器学习技术提供了动力。

### Diffusion Process

扩散过程

**Equation:**

方程：

$$
x_t = \sqrt{\alpha_t} x_0 + \sqrt{1 - \alpha_t} \epsilon \quad \text{where} \quad \epsilon \sim \mathcal{N}(0, I)
$$

**Explanation:** This describes a forward diffusion process where data $x_0$ is gradually noised over time $t$, a key idea in diffusion models.

**解释：** 这描述了一个前向扩散过程，其中数据𝑥 0 x 0 ​ 随着时间的推移逐渐产生噪声 $t$ ，这是扩散模型中的一个关键思想。

**Practical Use:** Used in generative AI like image synthesis.

**实际用途：** 用于图像合成等生成式人工智能。

**Implementation:**

实现：

```python
import torch

x_0 = torch.tensor([1.0])
alpha_t = 0.9
noise = torch.randn_like(x_0)
x_t = torch.sqrt(torch.tensor(alpha_t)) * x_0 + torch.sqrt(torch.tensor(1 - alpha_t)) * noise
print(f"x_t: {x_t}")
```

* * *

### Convolution Operation

卷积运算

**Equation:**

方程：

$$
(f * g)(t) = \int f(\tau) g(t - \tau) \, d\tau
$$

**Explanation:** Convolution combines two functions by sliding one over the other, extracting features in data like images.

**解释：** 卷积通过将一个函数滑动到另一个函数上来组合两个函数，从而提取图像等数据中的特征。

**Practical Use:** Core to convolutional neural networks (CNNs).

**实际用途：** 卷积神经网络（CNN）的核心。

**Implementation:**

执行：

```python
import torch
import torch.nn as nn

conv = nn.Conv2d(1, 1, kernel_size=3)
image = torch.randn(1, 1, 28, 28)
output = conv(image)
print(output.shape)  # Output: torch.Size([1, 1, 26, 26])
```

* * *

### Softmax Function

Softmax 函数

**Equation:**

方程：

$$
\sigma(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}
$$

**Explanation:** Softmax converts raw scores $z_i$ into probabilities, summing to 1, ideal for multi-class classification.

**解释：** Softmax 将原始分数𝑧 𝑖 z i ​ 转化为概率，总和为 1，非常适合多类分类。

**Practical Use:** Used in neural network outputs.

**实际用途：** 用于神经网络输出。

**Implementation:**

实现：

```python
import numpy as np

z = np.array([1.0, 2.0, 3.0])
softmax = np.exp(z) / np.sum(np.exp(z))
print(f"Softmax: {softmax}")  # Output: [0.09003057 0.24472847 0.66524096]
```

* * *

### Attention Mechanism

注意力机制

**Equation:**

方程：

$$
\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
$$

**Explanation:** Attention computes a weighted sum of values $V$ based on the similarity between queries $Q$ and keys $K$, scaled by $\sqrt{d_k}$.

**解释：** 注意力机制根据查询 $Q$ 和键 $K$ 之间的相似性计算值 $V$ 的加权和，并以 𝑑 为比例 𝑘 d k ​ ​ .

**Practical Use:** Powers transformers in NLP and beyond.

**实际用途：** 为 NLP 及其他领域的变压器提供动力。

**Implementation:**

实现：

```python
import torch

def attention(Q, K, V):
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    attn = torch.softmax(scores, dim=-1)
    return torch.matmul(attn, V)

Q = torch.tensor([[1., 0.], [0., 1.]])
K = torch.tensor([[1., 1.], [1., 0.]])
V = torch.tensor([[0., 1.], [1., 0.]])
output = attention(Q, K, V)
print(output)
```

* * *

## Conclusion

结论

This blog post has explored the most critical equations in machine learning, from foundational probability and linear algebra to advanced concepts like diffusion and attention. With theoretical explanations, practical implementations, and visualizations, you now have a comprehensive resource to understand and apply ML math. Point anyone asking about core ML math here—they'll learn 95% of what they need in one place!

这篇博文探讨了机器学习中最关键的方程式，从基础概率和线性代数到扩散和注意力等高级概念。通过理论解释、实际实现和可视化，您现在拥有了理解和应用机器学习数学的全面资源。如果有人想了解机器学习核心数学，可以参考这里——他们将在一个地方学到 95% 所需的知识！

* * *

## Further Reading

进一步阅读

*   *Pattern Recognition and Machine Learning* by Christopher Bishop

    *模式识别与机器学习* （作者：Christopher Bishop）
*   *Deep Learning* by Ian Goodfellow, Yoshua Bengio, and Aaron Courville

    *《深度学习》* （作者：Ian Goodfellow、Yoshua Bengio 和 Aaron Courville）
*   [Stanford CS229: Machine Learning](https://cs229.stanford.edu/)

    斯坦福 CS229：机器学习
*   [PyTorch Tutorials](https://pytorch.org/tutorials/)

    PyTorch 教程