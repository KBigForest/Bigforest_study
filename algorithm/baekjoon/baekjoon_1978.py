def checkprime(x):
    if x > 2:
        for i in range(2, x):
            if x % i == 0:
                return 0
        return 1           
    elif x == 1:
        return 0
    elif x == 2:
        return 1
N = int(input())
numlist = list(map(int, input().split()))
cnt = 0
for i in numlist:
    cnt += checkprime(i)
print(cnt) 
