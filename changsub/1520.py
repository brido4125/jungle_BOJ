import sys

sys.setrecursionlimit(10 ** 9)

M, N = map(int, input().split())

board = []
for _ in range(M):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1] * N for _ in range(M)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def dfs(row, col):
    if dp[row][col] != -1:
        return dp[row][col]
    if row == M - 1 and col == N - 1:
        return 1
    dp[row][col] = 0
    for i in range(4):
        currentValue = board[row][col]
        nextRow = row + dy[i]
        nextCol = col + dx[i]
        if 0 <= nextCol < N and 0 <= nextRow < M and board[nextRow][nextCol] < currentValue:
            dp[row][col] += dfs(nextRow, nextCol)
    return dp[row][col]


dfs(0, 0)
print(dp[0][0])
