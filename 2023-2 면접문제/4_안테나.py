n = int(input())
temp = list(map(int, input().split()))
max_ = max(temp)
di = {}
dif = {}
for i in temp:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
homelist = list(di.keys())
homelist.sort()
dp = [0]*len(homelist)
dif[homelist[0]] = [sum([di[j] for j in homelist if j <= homelist[0]]), sum([di[j] for j in homelist if j>homelist[0]])]

for i in range(1,len(homelist)):
    dif[homelist[i]] = [dif[homelist[i-1]][0]+di[homelist[i]], dif[homelist[i-1]][1] - di[homelist[i]]]
    dp[0] += (homelist[i]-homelist[0]) * di[homelist[i]]
for i in range(1,len(homelist)):
    dp[i] = dp[i-1] - dif[homelist[i-1]][1] * (homelist[i]-homelist[i-1]) + dif[homelist[i-1]][0] * (homelist[i]-homelist[i-1])
print(homelist[dp.index(min(dp))])