import heapq
import sys
N = int(input())
card_list = []
for i in range(N):
    card = int(input())
    card_list.append(card)
card_list = sorted(card_list)
total_sum = 0
if N==1:
    print(total_sum)
else: 
    for i in range(N-1):
        small_card1 = heapq.heappop(card_list)#가장 작은 것
        small_card2 = heapq.heappop(card_list)#두번째로 작은 것
        branch = small_card1 + small_card2
        total_sum += branch
        heapq.heappush(card_list, branch)
    print(total_sum)