
m, n = map(int,input().split())
board = []
count = []
for _ in range(m):
    board.append(input())


for a in range(m-7):
    for b in range(n-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                        #처음이 B인 경우 해당하는 인덱스가 'W'아닐 때마다 index1에 1을 추가
                    if board[i][j] != 'B':
                        index2 += 1
                        #처음이 W인 경우 해당하는 인덱스가 'B'아닐 때마다 index1에 1을 추가
                else:

                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))