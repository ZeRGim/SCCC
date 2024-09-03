import sys
input = sys.stdin.readline

t = int(input())

def change(n:int,x:int):
    return n-x+1

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = [change(n,i) for i in arr]
    if arr[0] >= arr2[0]:
        res = arr2[0]
    else:
        res = arr[0]
    TF = True
    for i in range(1,n):
        temp = []
        if res > arr[i] and res > arr2[i]:
            TF = False
            break
        if res <= arr[i]:
            temp.append(arr[i])
        if res <= arr2[i]:
            temp.append(arr2[i])
        if temp:
            res = min(temp)
    if TF:
        print("YES")
    else:
        print("NO")