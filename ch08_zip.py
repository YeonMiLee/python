# zip함수
alist = ['a1', 'a2', 'a3']
blist =['b1', 'b2', 'b3']
for a, b in zip(alist, blist):      # 병렬로 값 추출
  print(a, b)
print()



a, b, c=zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
print()

[sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print()

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

