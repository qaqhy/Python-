from sklearn.preprocessing import MinMaxScaler, StandardScaler, scale
from sklearn.impute import SimpleImputer
import numpy as np


def mm():
	"""归一化缩放"""
	# 1.目的：使得某一个特征不会对最终结果造成更大的影响
	# mms = MinMaxScaler()
	mms = MinMaxScaler(feature_range=(2, 3))  # 缩放特征值到给定范围
	data = mms.fit_transform([[12, 23, 13, 33], [92, 63, 73, 33], [15, 93, 33, 35]])
	print(data)
	# 公式：(x-min)/(max-min)
	# print((15-12)/(92-12) + 2)
	# print((63-23)/(93-23) + 2)


def stand():
	"""标准化缩放"""
	st = StandardScaler()
	data = st.fit_transform([[12, 23, 13, 33], [92, 63, 73, 33], [15, 93, 33, 35]])
	print(data)


def t_scale():
	"""标准化缩放"""
	x_train = np.array([[12, 23, 13, 33], [92, 63, 73, 33], [15, 93, 33, 35]])
	print(x_train)
	data = scale(x_train)
	# data = scale([[12, 23, 13, 33], [92, 63, 73, 33], [15, 93, 33, 35]])
	print(data)


def sm():
	"""缺失值处理"""
	# nan. NaN
	# strategy填补的策略，mean是平均值填补
	# verbose填补按行还是列，0按列平均值填补，1按行平均值填补
	it = SimpleImputer(missing_values=np.nan, strategy='mean', verbose=1)
	data = it.fit_transform([[12, 23, 13, 33], [92, np.nan, np.nan, 33], [15, 93, 33, 35]])
	print(data)


if __name__ == '__main__':
	# mm()
	stand()
	t_scale()
	# sm()
