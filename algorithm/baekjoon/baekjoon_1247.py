from sys import *

for _ in range(3):
    n = int(stdin.readline())
    numlist = [int(stdin.readline()) for n in range(n)]
    if sum(numlist) < 0:
        print('-')
    elif sum(numlist) > 0:
        print('+')
    else:
        print('0')
