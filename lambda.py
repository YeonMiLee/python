# 일반적인 함수
def f(x, y):
    return x + y

print(f(1, 4))

# 람다 함수
f = lambda x, y: x + y
print(f(1, 4))

# 람다 함수의 다양한 형태
f = lambda x, y : x + y
f(1, 4)

f = lambda x : x ** 2
f(3)

f = lambda x : x / 2
f(3)

f(3,5)    # 오류 - x 1개만 선언했는데 2개 입력해서

target = ['cat', 'tiger', 'dog', 'snake']
def my_key(string):
    return len(string.strip())
print(sorted(target, key=my_key))

# 람다로 변경

