import numpy as np
a = [[1, 2, 3, 4],
	 [5, 4, 3, 2]]  # 2行4列
b = [[2],
	 [2],
	 [2],
	 [2]]  # 4行1列
c = np.dot(a, b)  # 矩阵a乘以矩阵b
print(c)