from sklearn.datasets import load_iris  # sklearn提供的一个案例
# 以下是用于分类的估计器
from sklearn.neighbors import *  # k邻近算法
from sklearn.naive_bayes import *  # 贝叶斯算法
from sklearn.linear_model import LogisticRegression  # 逻辑回归
from sklearn.tree import *  # 决策树和随机森林
# 以下是用于回归的估计器
from sklearn.linear_model import LogisticRegression  # 线性回归
from sklearn.linear_model import Ridge  # 岭回归

li = load_iris()

print('获取特征值')
print(li.data)

print('目标值')
print(li.target)

print(li.DESCR)  # 获取说明
print(li.target_names)


