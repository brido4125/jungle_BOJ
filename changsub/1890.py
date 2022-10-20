import sys

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1] * N for _ in range(N)]


def dfs(row, col):
    if dp[row][col] != -1:
        return dp[row][col]
    if row == N - 1 and col == N - 1:
        return 1
    dp[row][col] = 0
    currentValue = board[row][col]
    dx = (0, currentValue)
    dy = (currentValue, 0)
    for i in range(2):
        nextRow = row + dy[i]
        nextCol = col + dx[i]
        if 0 <= nextRow < N and 0 <= nextCol < N:
            dp[row][col] += dfs(nextRow, nextCol)
    return dp[row][col]


dfs(0, 0)
print(dp[0][0])
