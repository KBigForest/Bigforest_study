import sys
a = sys.stdin.readline()
A = sorted(map(int, sys.stdin.readline().split()))

b = sys.stdin.readline()
B = map(int, sys.stdin.readline().split())

def binary(i, A, start, end):
    if start > end:
        return 0
    mid = (start +end) //2
    if i == A[mid]:
        return 1
    elif i < A[mid]:
        return binary(i, A, start, mid-1)
    else:
        return binary(i, A, mid+1, end)   
     
for i in B:
    start = 0
    end = len(A)-1
    print(binary(i,A,start,end))
