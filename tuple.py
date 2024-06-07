a = 3, 4, 5
b = 7,
c = 'o', 'p', 'q'

print(f'type(a) : {type(a)}')
print(f'type(b) : {type(b)}')
print(f'type(c) : {type(c)}')

print(f'a : {a}')
print(f'b : {b}')
print(f'c : {c}')

print()

# 튜플 반환
def get_info(num, name, phone):
  return num, name, phone     # return이 두개 이상이면 무조건 튜플로 반환

a = '1'
b = 'kim'
c = 'apple'

print()

# 하나의 변수에 받음
result1 = get_info(a, b, c)
print(f'type(result1) = {type(result1)}')
print(f'result1 = {result1}')

print()

# 일일히 하나씩 받음
d, e, f = get_info(a, b, c)   # 언패킹
print(d)
print(e)
print(f)

print()

# 리스트를 튜플로
a1 = [1, 3, 5, 7, 9, 11]
a2 = tuple(a1)

print(f'tuple(리스트) = {a2}')
print()

# 문자열을 튜플로
b1 = "BlockDMask"
b2 = tuple(b1)

print(f'tuple(문자열) = {b2}')
print()

# 딕셔너리를 튜플로
c1 = {'name': 'blockdmask', 'phone0': '010-1234-5678', 'phone_type': 'galaxy'}
c2 = tuple(c1)
c3 = tuple(c1.values())

print(f'tuple(딕셔너리) = {c2}')
print(f'tuple(딕셔너리.values()) = {c3}')
print()






