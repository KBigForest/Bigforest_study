money = int(input())

change = 1000-money
change_idx=0
change_list = [500,100,50,10,5,1]
cnt = 0
while True:
    if change >= change_list[change_idx]:
        cnt += change//change_list[change_idx]
        change = change%change_list[change_idx]
    elif change ==0:
        break
    else:
        change_idx += 1
print(cnt)

