N = int(input())
result = 0 
for i in range(1,N):
    if N == i+sum(map(int,str(i))):
        result = i
        break
if result == 0:
    print(0)
else:
    print(result)