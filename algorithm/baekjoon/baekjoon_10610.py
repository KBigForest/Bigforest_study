N = input()
N_list = []
for i in str(N):
    N_list.append(i)
N_list = sorted(N_list, reverse=True)

if int(''.join(N_list)) % 30 == 0:
    print(int(''.join(N_list)))
else:
    print(-1)