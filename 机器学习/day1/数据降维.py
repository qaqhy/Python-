from sklearn.feature_selection import VarianceThreshold
# 降维：类别型数据==》特征数量为维度数（列数）


def variance():
	"""特征选择-删除低方差的特征"""
	var = VarianceThreshold(threshold=0.0)  # 删除相同的列数据 0.0-10.0
	data = var.fit_transform([[0, 1, 1, 2], [3, 1, 1, 2], [2, 1, 2, 2], [2, 2, 2, 2]])
	print(data)


# 主成分分析
from sklearn.decomposition import PCA
# 本质：PCA是一种分析、简化数据集的技术
# 目的：是数据降维压缩，尽可能降低原数据的维度（复杂度），会损失少量信息
# 作用：可以削减回归分析或者聚类分析中特征的数量


def pca():
	"""主成分分析进行特征降维"""
	# n_components：小数->减少到的特征百分比，一般取0.9~0.95之间
	# n_components：整数->减少的特征数量
	_pca = PCA(n_components=0.9)
	data = _pca.fit_transform([[0, 1, 1, 2], [3, 1, 1, 2], [2, 1, 2, 2], [2, 2, 2, 2]])
	print(data)


def test():
	import pandas as pd
	t = pd.read_csv('./test.csv')
	t1 = pd.read_csv('./test1.csv')
	t2 = pd.read_csv('./test2.csv')
	m = pd.merge(t, t1, on=['A', 'A'])
	m = pd.merge(m, t2, on=['A', 'A'])
	print(m)
	print(m.head(10))


if __name__ == '__main__':
	# variance()
	# pca()
	test()









