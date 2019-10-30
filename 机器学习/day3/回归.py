import numpy as np
# a = [[1, 2, 3, 4],
# 	 [5, 4, 3, 2]]  # 2行4列
# b = [[2],
# 	 [2],
# 	 [2],
# 	 [2]]  # 4行1列
# c = np.dot(a, b)  # 矩阵a乘以矩阵b
# print(c)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def my_linear():
	"""线性回归直接预测房子价格"""
	# 获取数据
	lb = load_boston()
	# 分割训练集、测试集
	x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)
	# 进行标准化处理，特征值、目标值均进行标准化处理
	std_x = StandardScaler()
	# 特征值
	x_train = std_x.fit_transform(x_train)
	x_test = std_x.transform(x_test)
	# print(f'y_train1:{y_train}')
	# print(f'y_test1:{y_test}')
	# 目标值
	std_y = StandardScaler()
	y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # reshape 将一维数组转换成二维数组
	y_test = std_y.transform(y_test.reshape(-1, 1))
	# print(f'y_train2:{y_train}')
	# print(f'y_test2:{y_test}')

	# 预测数据正确性
	# 正规方程求解预测结果
	lr = LinearRegression()
	lr.fit(x_train, y_train)
	print(f'正规方程13个特征值的回归系数：{lr.coef_}')
	# 预测房子的价格
	y_lr_predict = lr.predict(x_test)
	y_lr_predict = std_y.inverse_transform(y_lr_predict)  # 还原真实数据
	print(f'正规方程测试集里面每个房子的预测价格：{y_lr_predict}')
	print(f'正规方程的均方误差：{mean_squared_error(std_y.inverse_transform(y_test), y_lr_predict)}')

	# 梯度下降进行房价预测
	sgd = SGDRegressor()
	sgd.fit(x_train, y_train)
	print(f'梯度下降13个特征值的回归系数：{sgd.coef_}')
	# 预测房子的价格
	y_sgd_predict = sgd.predict(x_test)
	y_sgd_predict = std_y.inverse_transform(y_sgd_predict)  # 还原真实数据
	print(f'梯度下降测试集里面每个房子的预测价格：{y_sgd_predict}')
	print(f'梯度下降的均方误差：{mean_squared_error(std_y.inverse_transform(y_test), y_sgd_predict)}')


if __name__ == '__main__':
	my_linear()

