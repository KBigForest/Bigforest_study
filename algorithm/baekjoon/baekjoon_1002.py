from sys import *
import math
T = int(stdin.readline())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, stdin.readline().split())
    di= (x1-x2)**2+ (y1-y2)**2
    dist = math.sqrt(di)
    if dist == 0 and r1==r2:
        print(-1)
    elif r1+r2 == dist or abs(r1-r2) ==dist:
        print(1)
    elif abs(r1-r2)< dist < r1+r2 :
        print(2)
    else:
        print(0)