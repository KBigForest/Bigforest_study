S = input()
cnt = 0
if len(S) == 1:
    pass
else:
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            pass
        else:
            cnt += 1
if cnt == 0:
    print(0)
elif cnt == 1:
    print(1)
elif S[0] != S[-1]:
    print(int(cnt/2)+1)
else:
    print(int(cnt/2))