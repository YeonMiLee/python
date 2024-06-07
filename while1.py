for i in range(10):
  if i == 5: break      # i가 5가 되면 반복 종료
  print(i)
print("End of Program")   # 반복 종료 후 "End of Program" 출력


# continue문
for i in range(10):
  if i == 5: continue     # i가 5가 되면 i를 출력하지 않음
  print(i)
print("End of Program")   # 반복 종료 후 "End of Program" 출력

# else문
for i in range(10): 
  print(i)
else:
  print("End of Program")