n = int(input())
d = n//2
cnt = 0
temp = 0
while cnt < n:
    if n == 1:
        print('1')
        break
    if temp + d > n:
        temp = temp - (d+1)
    else:
        temp += d
    cnt += 1
    print(temp, end=" ")