from collections import deque

deque_list = deque()
for i in range(5):
  deque_list.append(i)

print(deque_list)

# deque([0, 1, 2, 3, 4])

# deque_list.pop() 수행시키면 오른쪽 요소부터 하나씩 추출됨
deque_list.pop()
deque_list.pop()
deque_list.pop()
deque_list


from collections import deque

deque_list = deque()
for i in range(5):

    deque_list.appendleft(i)
print(deque_list)
