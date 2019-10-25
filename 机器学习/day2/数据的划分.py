from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston  # sklearn提供的一个案例
from sklearn.model_selection import train_test_split
# 以下是用于分类的估计器
from sklearn.neighbors import *  # k邻近算法
from sklearn.naive_bayes import *  # 贝叶斯算法
from sklearn.linear_model import LogisticRegression  # 逻辑回归
from sklearn.tree import *  # 决策树和随机森林
# 以下是用于回归的估计器
from sklearn.linear_model import LogisticRegression  # 线性回归
from sklearn.linear_model import Ridge  # 岭回归

li = load_iris()

# print('获取特征值')
# print(li.data)
#
# print('目标值')
# print(li.target)
#
# print(li.DESCR)  # 获取说明
# print(li.target_names)

# 返回值，训练集 train   x_train  y_train   测试集 test   x_test  y_test
# x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)  # 测试集数据占test_size 25%
# print(f'训练集特征值：{x_train}\n训练集特征值目标值：{y_train}')
# print(f'测试集特征值：{x_test}\n测试集特征值目标值：{y_test}')

news = fetch_20newsgroups(subset='all')
print(news.data)
print(news.target)

lb = load_boston()
print('获取特征值')
print(lb.data)

print('目标值')
print(lb.target)

print(lb.DESCR)  # 获取说明




