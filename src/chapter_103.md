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
  - 量化：将每个数离散化为 $2^b$ 个等级之一；增加一位可以将平方误差降低到原来的四分之一。·