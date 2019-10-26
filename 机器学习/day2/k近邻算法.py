from sklearn.neighbors import KNeighborsClassifier  # k近邻算法API
from sklearn.model_selection import train_test_split, GridSearchCV  # 交叉验证需要的网格搜索API：GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris  # yuan wei hua（鸢尾花数据）
import pandas as pd


def k_api():
	# n_neighbors 查询默认使用的邻居数
	# algorithm
	kn = KNeighborsClassifier(n_neighbors=5)
	# 读取数据
	data = pd.read_csv('./???.csv')  # csv文件是酒店得到的信息，目前没有
	print(data.head(10))
	# 处理数据
	# 1.缩小数据，查询数据筛选
	data = data.query('x > 1.0 & x < 1.25')

	# 2.处理时间
	time_value = pd.to_datetime(data['time'], unit='s')

	# 把日期格式转换成字典格式
	time_value = pd.DatetimeIndex(time_value)
	# 构造特征
	data['day'] = time_value.day
	data['hour'] = time_value.hour
	data['weekday'] = time_value.weekday

	# 把时间戳特征删除
	data.drop(['time'], axis=1)  # axis=1，按列删除
	print(data)

	# 把签到数量少于n个目标位置删除
	place_count = data.groupby('place_id').count()  # 此时的index以悄然变成了place_id  且此时place_count会保留出place_id以外的特征，数值都为次数
	# place_count 是分组之后数据， row_id 变成了具体的次数
	tf = place_count[place_count.row_id > 3].reset_index()  # reset_index作用是使place_id变为数据的一个特征，为具体的次数
	data = data[data['place_id'].isin(tf.place_id)]  # 筛选出data数据当中 place_id 相等的数据

	# 取出数据当中的特征值和目标值
	y = data['place_id']
	x = data.drop(['place_id'], axis=1)  # 按列删除
	# 进行数据的分割训练集和测试集
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)  # 测试集数据占test_size 25%

	# 特征工程（标准化）
	std = StandardScaler()
	# 对测试集和训练集的特征值做标准化
	x_train = std.fit_transform(x_train)
	x_test = std.transform(x_test)

	# 进行算法流程  knn估计器流程
	knn = KNeighborsClassifier(n_neighbors=5)
	knn.fit(x_train, y_train)
	# 得出预测结果
	y_predict = knn.predict(x_test)
	print(f'预测的目标签到位置为：{y_predict}')
	# 得出准确率
	print(f'预测的准确率：{knn.score(x_test, y_test)}')


def k_load_iris():
	# 花萼长度，花萼宽度，花瓣长度，花瓣宽度，种类
	data = pd.read_csv('iris.csv')
	data.columns = ['sl', 'sw', 'pl', 'pw', 'type']
	data = data.query('sl > 5.0')
	y = data['type']  # 目标数据
	x = data.drop(['type'], axis=1)  # 按列删除  特征值数据
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

	# 特征工程（标准化）
	std = StandardScaler()
	# 对测试集和训练集的特征值做标准化
	x_train = std.fit_transform(x_train)
	x_test = std.transform(x_test)

	# 1
	# 进行算法流程  knn估计器流程
	# knn = KNeighborsClassifier(n_neighbors=10)
	# knn.fit(x_train, y_train)
	# # 得出预测结果
	# y_predict = knn.predict(x_test)
	# print(f'预测的目标类型为：{y_predict}')
	# # 得出准确率
	# print(f'预测的准确率：{knn.score(x_test, y_test)}')

	# 2
	# 交叉搜索方法：进行网格搜索（超参数）
	knn = KNeighborsClassifier()  # 网格搜索不设置n_neighbors
	# 构造参数的值进行搜索
	param_grid = {'n_neighbors': [3, 5, 10]}
	gc = GridSearchCV(knn, param_grid=param_grid, cv=2)  # cv是交叉验证的折叠数，通常设置10为最好
	gc.fit(x_train, y_train)
	# 预测准确率
	print(f'预测的准确率：{gc.score(x_test, y_test)}')
	print(f'在交叉验证中最好的结果：{gc.best_score_}')  #
	print(f'在交叉验证中最好的模型：{gc.best_estimator_}')  # n_neighbors
	print(f'每个超参数每次交叉验证的结果：{gc.cv_results_}')


if __name__ == '__main__':
	k_load_iris()

