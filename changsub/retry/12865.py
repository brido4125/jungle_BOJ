import sys

N, K = map(int, sys.stdin.readline().split())

weights= []
values = []

for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    weights.append(x)
    values.append(y)

dp = [[0] * (K + 1) for _ in range(N)]

for i in range(N):
    for j in range(1, K + 1):
        if weights[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])


print(dp[N-1][K])

