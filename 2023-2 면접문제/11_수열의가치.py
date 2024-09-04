n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0]*2)
    print(arr[0])
    exit()
    
elif n == 2:
    if arr[0] != arr[1]:
        print(arr[0]+arr[1]+max(arr))
        print(arr[0], arr[1])
    else:
        print(4*arr[0])
        print(arr[0], arr[1])
    exit()
di = {}
for i in arr:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
numlist = list(di.keys())
numlist.sort()

if len(numlist) < 2:
    print(i*di[i]*2)
    for i in arr:
        print(i, end=" ")
else:
    arr = [[i*di[i], i] for i in numlist]
    res = 0
    for i in range(len(numlist)):
        res += arr[i][0]
    res += max(arr)[0]
    print(res)
    for i in range(len(numlist)):
        for j in range(di[numlist[i]]):
            print(numlist[i], end=" ")
    