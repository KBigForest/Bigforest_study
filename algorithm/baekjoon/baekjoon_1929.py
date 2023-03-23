import math
M,N = map(int, input().split())
a = [True]*(N+1)
a[0] = False
a[1] = False
n = int(math.sqrt(N))

for i in range(2,n+1):
    if a[i] == True:
        for j in range(2*i, N+1, i):
            a[j] = False
            
for i in range(M,N+1):
    if a[i]:
        print(i)