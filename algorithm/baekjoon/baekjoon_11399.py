import sys
num = int(sys.stdin.readline())
num_list = input().split()

num_list = [int(i) for i in num_list]
num_list.sort()
sum_value = 0
for i in range(1,num+1):
    sum_value += sum(num_list[:i])
print(sum_value)