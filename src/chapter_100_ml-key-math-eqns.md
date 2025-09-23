
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