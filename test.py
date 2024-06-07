a = "hello"
b = ["hello", "python"]
id(a)
id(b)

a = "python2"
id(a)





import sys      # sys 모듈 호출
print(sys.getsizeof("a"), sys.getsizeof("ab"), sys.getsizeof("abc"))  # 각각의 메모리 크기 출력


import matplotlib.pyplot as plt
plt.pyplot.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()