# 1. Tuple List로부터 dict 생성
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)

age = mydict["홍대길"]
print(age)        #35

print()

# 딕셔너리 생성
country_code = { }    
country_code = {"America": 1, "Korea": 82, "China": 86, "Japan": 81}
country_code

print()

# 값을 출력하기 위해 values() 사용
country_code["German"] = 49     # 딕셔너리 추가
country_code

country_code.values()

print()


# 키-값 쌍을 모두 보여주기 위해서 items() 사용
country_code.items()    # 딕셔너리 데이터 출력

print()

# key : value 쌍 모두 지우기 - clear
country_code.clear()    # 딕셔너리 안의 모든 요소 삭제

# key로 value 얻기 - get
a = {'name': 'pey', 'phone': '010-1234-5678', 'birth': '1118'}
a.get('name')
#'pey'

print()

# a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 none을 리턴
a = {'name': 'pey', 'phone': '010-1234-5678', 'birth': '1118'}
print(a.get('nokey'))
#none
print(a['nokey'])


# for문과 함께 딕셔너리를 사용하여 키-값 쌍을 화면에 출력하기
for k, v in country_code.items():
  print("Key: ", k)
  print("Value: ", v)

# in 문을 사용하여 특정 키나 값이 해당 변수에 포함되어 있는지 확인
"Korea" in country_code.keys()    # 키에 "Korea" 있는지 확인

82 in country_code.values()       # 값에 82 있는지 확인
