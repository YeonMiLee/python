# 리스트 선언
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 리스트 출력
print("# 리스트")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()

# 기본연산자
print("# 리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print()

# 함수
print("# 길이 구하기")
print("len(list_a) = ", len(list_a))

cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
cities[0:6] 
cities[5:]  
cities[-8:]
cities[:]
cities[-50:50]
cities[::2]
cities[::-1]


# 덧셈
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color1 + color2)      # 두 리스트 합치기

total_color = color1 + color2