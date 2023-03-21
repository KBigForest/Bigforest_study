import sys

M,N = map(int, sys.stdin.readline().split())

a = [print(i) for i in range(M,N+1) if i % j != 0 for j in range(M,N+1)]
