a = int(input("> 1번째 숫자: "))
b = int(input("> 2번째 숫자: "))
print()

if a > b:
  print("처음 입력했던", a, "가", b, "보다 더 큽니다")
if a < b:
  print("처음 입력했던", b, "가", a, "보다 더 큽니다")


# if-else
print("Tell me your age?")
myage = int(input())                        # 나이를 입력받아 myage 변수에 할당
if myage < 30:                              # myage가 30미만일 때
  print("Welcome to the club.")
else:                                       # myage가 30이상일 때
  print("Oh! No. You are not accepted.")