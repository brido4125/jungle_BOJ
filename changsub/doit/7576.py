import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

# 우 하 좌 상
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

my_queue = deque()

board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

for i in range(M):
    for j in range(N):
        if board[j][i] == 1:
            my_queue.append((i, j))


def bfs():
    max = 0
    while my_queue:
        popleft = my_queue.popleft()
        privX = popleft[0]
        privY = popleft[1]
        privValue = board[privY][privX]
        if max < privValue:
            max = privValue
        for i in range(4):
            currX = privX + dx[i]
            currY = privY + dy[i]
            if 0 <= currY < N and 0 <= currX < M and board[currY][currX] == 0:
                my_queue.append((currX, currY))
                board[currY][currX] = privValue + 1
    return max


answer = bfs() - 1

for i in range(M):
    for j in range(N):
        if board[j][i] == 0:
            answer = -1
            break

if answer == 1:
    answer = 0

print(answer)
