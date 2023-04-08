city_num = int(input())
length_list = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))
oil_price = 0
most_cheap_oil_cost = oil_cost[0]
for i in range(len(length_list)):
    if oil_cost[i] < most_cheap_oil_cost:
        most_cheap_oil_cost = oil_cost[i]
    oil_price += length_list[i]*most_cheap_oil_cost
print(oil_price)