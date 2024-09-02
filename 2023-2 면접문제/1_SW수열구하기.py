from collections import deque
n = int(input())
li = deque([i for i in range(1,n+1)])
while li:
    print(li.pop(), end= " ")
    if li:
        print(li.popleft(), end=" ")