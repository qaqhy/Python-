from sklearn.tree import DecisionTreeClassifier, export_graphviz  # DecisionTreeClassifier决策树API，export_graphviz决策树可视化API
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier  # 导入随机森林预测API
import pandas as pd


def decision():
	"""决策树对泰坦尼克号进行生死预测"""
	# 获取数据
	titanic = pd.read_csv("./data/titanic.txt")

	# 处理数据 提取关键特征，sex, age, pclass都很有可能影响是否幸免
	x = titanic[['pclass', 'age', 'sex']]  # 特征值
	y = titanic['survived']  # 目标值：存活与否

	# 缺失值age处理
	# age数据列 只有633个，对于空缺的 采用平均数或者中位数进行补充 希望对模型影响小
	x['age'].fillna(x['age'].mean(), inplace=True)  # mean是age平均值，inplace=True为替换，inplace=False不替换

	# 分割数据为训练集和测试集 random_state指划分规则 random_state=33
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

	# 特征 -> 类别 -> one_hot编码
	# 使用特征转换器进行特征抽取
	dv = DictVectorizer(sparse=False)  # sparse=False意思是不用稀疏矩阵表示
	# orient='record' 意思是按行转换字典，一行一个字典
	x_train = dv.fit_transform(x_train.to_dict(orient='records'))
	x_test = dv.transform(x_test.to_dict(orient='records'))
	print(dv.get_feature_names())
	# print(x_train)

	# 使用决策树进行预测 初始化决策树分类器
	dtc = DecisionTreeClassifier()  # max_depth=5决策树深度限制为5
	# 训练
	dtc.fit(x_train, y_train)
	# 预测 保存结果
	dtc_y_predict = dtc.predict(x_test)
	print(f'预测准确率为：{dtc.score(x_test, y_test)}')
	# 导出决策树结构
	# export_graphviz(dtc, out_file='./data/titanic.dot', feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'female', 'male'])

	# # 初始化随机森林分类器
	# rfc = RandomForestClassifier()
	# # 训练
	# rfc.fit(x_train, y_train)
	# # 预测
	# rfc_y_predict = rfc.predict(x_test)
	# print(f'预测准确率为：{rfc.score(x_test, y_test)}')


if  __name__ == '__main__':
	decision()

