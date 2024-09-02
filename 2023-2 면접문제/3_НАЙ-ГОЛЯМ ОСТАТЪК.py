n = int(input())
li = set(map(int, input().split()))
if len(li) == 1:
    print("0")
else:
    li = list(li)
    li.sort()
    print(li[-2])