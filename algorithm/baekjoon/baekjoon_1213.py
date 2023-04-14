N, L = map(int, input().split())
gu = list(map(int, input().split()))
i = 0
j = 0
cnt =0
gu = sorted(gu)
while True:
    try:
        if (gu[j+1]+0.5) - (gu[i]-0.5) <= L:
            j += 1
        else:
            cnt += 1
            i += 1
    except:
        print(cnt)
        break