input_num = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
sum_list = []

A.sort(reverse=True) # reverse
      
B.sort()

sum_x =0
x=0
for i in range(input_num):
    x = A[i]*B[i]
    sum_x += x

A
B    
print(sum_x)
