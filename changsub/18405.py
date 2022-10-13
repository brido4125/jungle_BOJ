import sys
from collections import deque

N, K = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

time, row, col = map(int, input().split())

# 아래, 오른쪽, 위, 왼쪽
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

current_time = 0


def bfs():
    while queue:
        priv_row, priv_col, second = queue.popleft()
        for i in range(4):
            current_row = priv_row + dy[i]
            current_col = priv_col + dx[i]
            current_second = second + 1
            current_time = current_second
            if 0 <= current_col < N and 0 <= current_row < N and board[current_row][current_col] == 0:
                queue.append((current_row, current_col, current_second))
                board[current_row][current_col] = (board[priv_row][priv_col][0], current_time)


queue = deque()
temp = [] # 탐색을 통해 들어오는 바이러스를 오름차순으로 정렬하는 용도의 리스트
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            temp.append((board[i][j],i, j, 0))
            board[i][j] = (board[i][j], 0)

temp.sort()
# 오름차순 정렬 된 대로 queue에 데이터 삽입
for elem in temp:
    queue.append((elem[1],elem[2],elem[3]))
bfs()

if board[row - 1][col - 1][1] <= time:
    print(board[row - 1][col - 1][0])
else:
    print(0)
