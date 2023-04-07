#최소 버튼 조작을 통해 누른 수의 최소로 하자
#모든 수의 합이 정확히 여기서 제시하는 T초가 되어야 한다.
#최대한 A > B > C순으로 적게 누르는 것이 핵심
#추가적으로 정확히 맞춰야하는 만큼 T%10!=0일 경우 -1 return



#각 버튼에 해당 하는 초
A = 300
B = 60
C = 10

T = int(input())
cntA = 0
cntB = 0
cntC = 0
if T%10 != 0:
    print(-1)
else:
    while True:
        if T>=A :
            cntA += T//A 
            T = T%A
        elif T>=B:
            cntB += T//B
            T = T%B
        elif T>=C:
            cntC += T//C
            T = T%C
        elif T == 0:
            print(cntA, cntB, cntC)
            break

