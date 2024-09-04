N, M = map(int, input().split())
arr1 = [1,2,4,2]
arr2 = [4,3,1,3]
if N == 1 and M == 1:
    print("1")
    print("1")
    exit()
if N == 2 and M == 1:
    print("2")
    print("1")
    print("2")
    exit()
if N == 1 and M == 2:
    print("2")
    print("1 2")
    exit()
if N == 2 and M == 2:
    print("4")
    print("1 2")
    print("4 3")
    exit()
if N == 1:
    print("2")
    for i in range(M//2):
        print("1",end=" ")
        print("2",end=" ")
    if M % 2 == 1:
        print("1")
    exit()
if M == 1:
    print("2")
    for i in range(N//2):
        print("1")
        print("2")
    if N % 2 == 1:
        print("1")
    exit()
print("4")
idx = 0
for i in range(N//2):
    idx = 0
    for j in range(M):
        print(arr1[idx], end=" ")
        idx += 1
        if idx >= 4:
            idx = 0
    print()
    idx = 0
    for j in range(M):
        print(arr2[idx], end=" ")
        idx += 1
        if idx >= 4:
            idx = 0
    print()
if N % 2 == 1:
    idx = 0
    for j in range(M):
        print(arr1[idx], end=" ")
        idx += 1
        if idx >= 4:
            idx = 0