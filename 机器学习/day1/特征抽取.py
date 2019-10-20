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


from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba


# 字典特征值化
def func_dict():
	"""字典数据抽取"""
	# 实例化
	# dv = DictVectorizer()  # 打印sparse矩阵
	dv = DictVectorizer(sparse=False)  # 打印ndarray类型的数据 （数组，二维度）
	data = dv.fit_transform([{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 80}])
	print(dv.get_feature_names())  # v_dict实例了列名
	print(dv.inverse_transform(data))  # 计算每个数据的特征值
	print(data)


# 文本特征值化
def func_count():
	"""对文本进行特征值化"""
	cv = CountVectorizer()
	# res = cv.fit_transform(["city ni ni bu hao", "ni hao ma"])
	# 不支持对中文的特征抽取，也是不统计单个汉字
	res = cv.fit_transform(["人生苦短，我用python", "人生漫长，我 用python"])
	print(res)
	# 1.统计文章当中所有的词，重复的只看做一次，生成get_feature_names列表
	# 2.对每篇文章，在词的列表里面进行统计每个词出现的次数，生成二维数组
	# 单个字母不统计
	print(cv.get_feature_names())
	print(res.toarray())  # 将矩阵转化成数组形式


def chinese_vec():
	"""中文特征值化"""
	con1 = jieba.cut('人生苦短，我用python')
	con2 = jieba.cut('人生漫长，我用python')
	con1 = ' '.join(list(con1))
	con2 = ' '.join(list(con2))

	cv = CountVectorizer()
	res = cv.fit_transform([con1, con2])
	print(res)
	print(cv.get_feature_names())
	print(res.toarray())  # 将矩阵转化成数组形式


if __name__ == '__main__':
	# func_dict()
	# func_count()
	chinese_vec()

