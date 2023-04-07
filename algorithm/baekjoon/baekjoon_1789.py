target = int(input())
number = 1
number_list = []
sum_target = 0
cnt = 0
while True:
    number += 1
    number_list.append(number)
    sum_target += number
    cnt += 1
    if sum_target >= target:
        break
print(cnt)    
    