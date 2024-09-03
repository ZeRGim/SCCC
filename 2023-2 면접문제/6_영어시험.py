n = int(input())
letters = list(input())
letters.sort()
for i in range(n):
    for j in letters:
        print(j, end="")