# 特征抽取
# from sklearn.feature_extraction.text import CountVectorizer
#
# vector = CountVectorizer()
#
# res = vector.fit_transform(["city ni bu hao", "ni hao ma"])
#
# print(vector.get_feature_names())
#
# print(res.toarray())


# 字典特征抽取
from sklearn.feature_extraction import DictVectorizer


def func_dict():
	"""字典数据抽取"""
	# 实例化
	# v_dict = DictVectorizer()  # 打印sparse矩阵
	v_dict = DictVectorizer(sparse=False)  # 打印ndarray类型的数据 （数组，二维度）
	data = v_dict.fit_transform([{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 80}])
	print(v_dict.get_feature_names())  # v_dict实例了列名
	print(data)


if __name__ == '__main__':
	func_dict()

