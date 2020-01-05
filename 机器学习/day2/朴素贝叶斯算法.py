from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB  # 朴素贝叶斯算法API
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report  # 分类评估API  召回率、精确率
import pandas as pd


def naviebayes():
	"""朴素贝叶斯进行文本分类"""
	news = fetch_20newsgroups(subset='all')
	# print(f"data:{news.data}")
	# print(f"target:{news.target}")
	# 数据分割
	x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

	# 对数据集进行特征抽取
	tf = TfidfVectorizer()

	# 以训练集当中词的列表进行每篇文章重要性统计
	x_train = tf.fit_transform(x_train)
	# print(tf.get_feature_names())
	x_test = tf.transform(x_test)
	# 进行朴素贝叶斯算法的预测
	mlt = MultinomialNB(alpha=1.0)
	# print(x_train)

	mlt.fit(x_train, y_train)
	y_predict = mlt.predict(x_test)
	# 得出准确率
	print(f'预测的准确率为：{mlt.score(x_test, y_test)}')
	print(f'每个类别精确率和召回率：\n{classification_report(y_test, y_predict, target_names=news.target_names)}')


if __name__ == '__main__':
	naviebayes()


