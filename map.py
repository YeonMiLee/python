# map()
a = list(map(str, range(10)))
print(a)
print()


a = map(int, input().split())
print(a)
print()

print(list(a))
print()


# map이 반환하는  맵 객체는 이터레이터라서 변수 여러개에 저장하는 언패킹 가능
a, b = map(int, input().split())    # 리스트 생략
print()

x = input().split()  # input().split()의 결과는 문자열 리스트
m = map(int, x)      # 리스트의 요소를 INT로 변환, 결과는 맵 객체
a, b = m             # 맵 객체는 변수 여러 개의 저장 할 수 있음