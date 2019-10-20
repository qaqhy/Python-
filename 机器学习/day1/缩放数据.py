from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


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

if __name__ == '__main__':
	mm()
	stand()
