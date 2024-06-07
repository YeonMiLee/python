# reduce
def add(data):
  result = 0
  for i  in data:
    result += i
  return result

# functools.reduce() 로 최대값 구하기
import functools

num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y : x if x > y else y, num_list)

print(max_num)    # 8 출력
print()

# 최소 값
min_num = functools.reduce(lambda x, y : x if x < y else y, num_list)
print(min_num)