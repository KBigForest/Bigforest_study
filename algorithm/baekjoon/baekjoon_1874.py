# ## 시간이 오래 걸리는 방식
# import sys
# num = int(input())
# pop_num_list = []
# stack_arr = []
# result= []
# a_list = []
# flag = 0
# for i in range(num):
#     a = int(input())
#     if len(stack_arr)==0:
#         for j in range(1,a+1):
#             stack_arr.append(j)
#             result.append('+')
            
#         x = stack_arr.pop()
#         pop_num_list.append(x)
#         result.append('-')
          
#     else:
#         if a <= stack_arr[-1]:
#             for i in range(a,stack_arr[-1]+1)[::-1]:
#                 if i in pop_num_list:
#                     pass
#                 else:
#                     stack_arr.pop()
#                     pop_num_list.append(i)
#                     result.append('-')
#         elif a in pop_num_list:
#             print('NO')
#             flag = 1    
#             break
#         else:
#             for i in range(stack_arr[-1]+1, a+1):
#                 if i in pop_num_list:
#                     pass
#                 else:
#                     stack_arr.append(i)
#                     result.append('+')
#             x = stack_arr.pop()
#             pop_num_list.append(x)
#             result.append('-')


# if flag == 0:
#     for i in result:
#         print(i)

#정답
# import sys

# num = int(sys.stdin.readline())
# stack = []
# result = []
# cnt = 1
# flag = 1
# for i in range(num):
#     a = int(sys.stdin.readline())
#     #
#     while cnt <= a:
#         stack.append(cnt)
#         result.append('+')
#         cnt += 1
#     if stack[-1] == a:
#         stack.pop()
#         result.append('-')
#     else:
#         print('NO')
#         flag = 0
#         break
# if flag == 1:
#     for i in result:
#         print(i)
        



import sys
num = int(input())
pop_num_list = []
stack_arr = []
result= []
a_list = []
flag = 0
count = 1
count_sum = 1
for i in range(num):
    a = int(input())
    if count_sum <= a:
        for j in range(count_sum,a+1):
                stack_arr.append(j)
                result.append('+')
                count_sum = count + 1
    if stack_arr[-1]== a:          
        stack_arr.pop()
        result.append('-')
    else:
        print('NO')
        flag = 1    
        break
if flag == 0:
    for i in result:
        print(i)
