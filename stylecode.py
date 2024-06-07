# split
items = 'zero one two three'.split()    # 빈칸을 기준으로 문자열 분리
print(items)

print()

example = 'python,jquery,javascript'    # ","를 기준으로 문자열 나누기
example.split(",")
print()

a, b, c = example.split(",")            # 리스트에 있는 각 값을 a, b, c 변수로 언패킹
print(a, b, c)
print()

example = 'theteamlab.univ.edu'
subdomain, domain, tld =example.split('.')    # "."을 기준으로 문자열 나누기 - 언패킹
print(subdomain, domain, tld)
print()


# 중첩반복문 : for문이 작동하는 순서는 왼쪽에 있는 for문이 먼저 작동함
[(x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]  # 리스트안에 튜플 생성
[(x, z, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피'] for z in ['배달시키기', '가서 먹기']] 
print()


# 이차원 리스트
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
print()

stuff = [[w.upper(), w.lower(), len(w)] for w in words]   # 리스트의 각 요소를 대문자, 소문자, 길이로 변환하여 이차원 리스트로 변환
print(stuff)
print()

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]
result = [i + j for i in case_1 for j in case_2]
print(result)
print()

result = [[i + j for i in case_1] for j in case_2]
print(result)
print()