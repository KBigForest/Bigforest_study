input_num = int(input())
Q = 25
D = 10
N = 5
P = 1


for i in range(input_num):
    x = float(input())
    Q_count = 0
    D_count = 0
    N_count = 0
    P_count = 0
    while x != 0:
        if x < Q:
            pass
        else:
            Q_count += int(x // Q)
            x = x % Q
        
        if x < D:
            pass
        else:
            D_count += int(x // D)
            x = x % D
            
        if x < N:
            pass
        else:
            N_count += int(x // N)
            x = x % N

        if x < P:
            pass
        else:
            P_count += int(x // P)
            x = x % P
    print(Q_count, D_count, N_count, P_count)            
