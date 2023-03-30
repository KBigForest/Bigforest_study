N = int(input())
#3,5키로 봉지 존재
#설탕을 정확히 N키로 배달 시 봉지를 몇 개인지 구하는 프로그램
#정확하게 N키로를 만들 수 없을 땐 -1출력
#일단 4키로, 7, 13

N_copy = N
# basket = 0
# basket_sum = 0
# while True:
#     N_copy -= 5
#     basket += 1    
#     if N==0:
#         break
#     elif (N > 0)and (N <3):
#         basket = 0  
#         N_copy = N
if N_copy <5:
    if N_copy%3 ==0:
        basket = N_copy % 3
        print(basket)
    else:
        print(-1)       
else:
    
N_copy =
1
5
=1
3
=1

-1

2
=2
-1

3
=0

4
3
=1

5
5
=0

6
5
=1
3
3
=0

7
5
=2




14
5
5
3
=1
5
3
3
3
=0

13
5
5
3
=0

12
5
5
=2
5
3
3
=1
3
3
3
3
=0

17
5
5
5
=2
5
5
3
3
=1
5
3
3
3
3

18






x = N_copy // 5  

basket = 0
range(1,3)[::-1]
for i in range(x,0,-1):
    if (N_copy -5*i)<0:
        continue    
    N_copy = N_copy -5*i
    basket += i
    if N_copy == 0:
        break
    elif 
    
print(basket)



if N_copy > 4:
    
    N_copy = N_copy - 5
    count += 1
else:
    N_copy = N_copy -=3
    count += 1
if
elif N_copy == 1:
elif  N_copy == 2:
15//3
15//5
x = 16//5
16-x*5
N_copy
N = 18
N_copy = 18
count = 0
x = N_copy// 5    
while True:
    N_copy -= x*5
    count += x 
    if N_copy == 0:
        break
    elif N_copy == 1:
        N_copy = N
    elif N_copy == 2:
        pass
    elif N_copy < 0:
        while True:
            N_copy += x*5
            y = N_copy //3
            N_copy -= y*3
            count += y 
            
            if N_copy == 0:
                N_copy = N
            elif N_copy == 1:
                N_copy = N
            elif N_copy == 2:
                pass
            else:
                y-=1                    
    else:
        x -= 1 
count