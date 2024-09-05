n, k = map(int, input().split())
pre = list(input())
res = []
for i in range(k+1,n):
    idx = 0
    idx2 = i-1
    cnto = 0
    cntr = 0
    for j in range(i):
        if pre[j] == "R":
            cntr += 1
        else:
            cnto += 1
    while idx2 < n-1:
        if cntr * k == cnto:
            res.append(i)
        idx2 += 1
        if pre[idx] == "R":
            cntr -= 1
        else:
            cnto -= 1
        if pre[idx2] == "R":
            cntr += 1
        else:
            cnto += 1
        idx += 1
print(max(res))