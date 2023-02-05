import sys
from collections import deque

T = int(input())
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
pq = deque()


def bfs(start, board):
    pq.append(start)
    x,y = start
    board[y][x] = 0
    while pq:
        privX, privY = pq.popleft()
        for i in range(4):
            nextX = privX + dx[i]
            nextY = privY + dy[i]
            if 0 <= nextX < M and 0 <= nextY < N and board[nextY][nextX] == 1:
                pq.append((nextX, nextY))
                board[nextY][nextX] = 0


for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0 for p in range(M)] for q in range(N)]
    target_points = []
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        board[Y][X] = 1
        target_points.append((X, Y))
    answer = 0
    for t in target_points:
        x, y = t
        if board[y][x] == 1:
            bfs(t, board)
            answer += 1
    print(answer)
