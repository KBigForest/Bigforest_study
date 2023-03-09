#무식한 방법
# import sys

# k, n = map(int, sys.stdin.readline().split())
# lan = []
# for i in range(k):
#     num = int(sys.stdin.readline())
#     lan.append(num)

# start = int(sum(lan)/n)
# while True:
#     result_num = 0
#     for i in lan:
#         result_num += int(i/start)
#     if result_num==n:
#         break
#     else:
#         start -= 1
# print(start)

#이분 탐색 방법
import sys 
k, n = map(int, sys.stdin.readline().split())
lan = []
for i in range(k):
    num = int(sys.stdin.readline())
    lan.append(num)

# 전체 탐색 범위
start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0 #랜선의 개수
    for i in lan:
        lines += i//mid
        
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)