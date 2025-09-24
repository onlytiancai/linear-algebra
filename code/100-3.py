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
