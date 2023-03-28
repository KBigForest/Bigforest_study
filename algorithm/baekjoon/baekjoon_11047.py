### 시간 복잡도와 공간복잡도에서 굉장히 위험했음
coin_list = []
num, money = map(int, input().split())

for i in range(num):
    coin = int(input())
    coin_list.append(coin)
def get_coin_num(coinlist,money):
    coin_cnt = 0
    for i in coinlist[::-1]:
        if i > money :
            pass
        elif i <= money:
            while True:
                if i > money:
                    break    
                else:
                    money -= i
                    coin_cnt += 1
    return coin_cnt
print(get_coin_num(coin_list, money))

#나머지의 개념을 사용한다면 편함
coin_list = []
num, money = map(int, input().split())
for i in range(num):
    coin = int(input())
    coin_list.append(coin)
def get_coin_num(coinlist,money):
    coin_cnt = 0
    for i in coinlist[::-1]:
        if i > money :
            continue
        while True:
            if i > money:
                break    
            else:
                x = money // i
                money = money % i
                coin_cnt += x
    return coin_cnt
print(get_coin_num(coin_list, money))

#
