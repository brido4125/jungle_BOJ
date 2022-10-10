import sys
from collections import deque

M, N, H = map(int, input().split())

board = []

queue = deque()

# 아래, 왼쪽, 위, 오른쪽, 위층, 아래층 순으로 탐색
dx = (0, -1, 0, 1, 0, 0)
dy = (1, 0, -1, 0, 0, 0)
dz = (0, 0, 0, 0, 1, -1)

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                queue.append((k, j, i))  # x,y,z순으로
    board.append(tmp)


def bfs():
    global days
    while queue:
        privX, privY, privZ = queue.popleft()
        for i in range(len(dx)):
            currentX = privX + dx[i]
            currentY = privY + dy[i]
            currentZ = privZ + dz[i]
            if 0 <= currentX < M and \
                    0 <= currentY < N and \
                    0 <= currentZ < H and \
                    board[currentZ][currentY][currentX] == 0:
                board[currentZ][currentY][currentX] = board[privZ][privY][privX] + 1
                queue.append((currentX, currentY, currentZ))


not_ripe_tomato = 1
days = -1
bfs()
for i in board:
    for j in i:
        for k in j:
            if k == 0:
                not_ripe_tomato = 0
            days = max(days, k)

if not_ripe_tomato == 0:
    print(-1)
elif days == 1:
    print(0)
else:
    print(days - 1)