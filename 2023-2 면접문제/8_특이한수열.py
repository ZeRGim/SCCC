#n == k면 불가능. gcd(1,1) = 1
#k+1 == n 이면 그냥 1,2,3,--n
#k+2???
#gcd(a,a+1) 반드시 1 > 일부러 틀리기 용이?

n, k = map(int, input().split())

if n == k:
    print("Impossible")
    exit()
if n == k+1:
    for i in range(n):
        print(i+1, end=" ")
    exit()
print(k+2, end=" ")
for i in range(2,k+2):
    print(i, end=" ")
for i in range(k+2,n):
    print(i+1, end=" ")
print("1")