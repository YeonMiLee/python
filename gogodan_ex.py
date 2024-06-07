print("구구단 몇 단을 계산할까?")
dan = int(input())
print("구구단 ", dan, "을 계산한다.")
for i in range(1, 10):
  result = dan * i
  print(dan, "X", i, "=", result)
