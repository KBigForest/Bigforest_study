#2475
a = input().split(' ')
a = [int(i)**2 for i in a]
print(sum(a)%10)

#2742
num = int(input())
while num > 0:
    print(num)
    num -= 1

#2577

A = int(input())
B = int(input())
C = int(input())
sum_result = A*B*C
sum_result = list(str(sum_result))
sum_result = [int(i) for i in sum_result]
for i in range(0,10):
    print(sum_result.count(i))
    
#2741
import sys

num = int(sys.stdin.readline().split())
for i in range(1,num+1):
    print(i)
    
#2920

sound = input().split(' ')
if sound == ['1','2','3','4','5','6','7','8']:
    print('ascending')
elif sound == ['8','7','6','5','4','3','2','1']:
    print('descending')
else:
    print('mixed')