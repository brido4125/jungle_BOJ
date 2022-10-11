import sys
from collections import deque

R, C = map(int, input().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False] * C for _ in range(R)]


def dfs(row, col):
    visited[row][col] = True
    for i in range(4):
        nextRow = row + dy[i]
        nextCol = col + dx[i]
        if nextRow < 0 or nextCol < 0 or nextCol >= C or nextRow >= R:
            continue
        if board[nextRow][nextCol] != 0 and visited[nextRow][nextCol] == False:
            dfs(nextRow, nextCol)


def getSeparateNum():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and visited[i][j] == False:
                dfs(i, j)
                cnt += 1


def bfs():
    queue = deque()
    visited = [[False] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                queue.append((i, j))
                visited[i][j] = True

    while queue:
        row, col, = queue.popleft()
        seaNum = 0
        for i in range(4):
            dx = col + dx[i]
            dy = row + dy[i]

            if dx < 0 or dy < 0 or dx >= C or dy >= R:
                continue
            if visited[dy][dx] == False and board[dy][dx] == 0:
                seaNum += 1
        if board[row][col] - seaNum < 0:
            board[row][col] = 0
        else:
            board[row][col] -= seaNum


