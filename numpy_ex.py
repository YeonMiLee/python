import numpy as np
np.__version__

ar1 = np.array([1, 2, 3, 4, 5])
type(ar1)       # 객체의 자료형 확인
ar2 = np.array([[10, 20, 30],[40, 50, 60]])
ar2

ar3 = np.arange(1, 11, 2)
ar3

ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))
ar4

ar5 = np.zeros((2, 3))
ar5

ar9 = np.dot(ar2, ar4)
ar9

