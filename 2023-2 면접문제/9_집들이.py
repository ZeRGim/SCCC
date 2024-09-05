import sys
input = sys.stdin.readline

R, C = map(int, input().split())

apart = []
for i in range(R):
    apart.append(list(input().strip()))
for i in range(R):
    for j in range(C):
        if apart[i][j] == ".":
            pass