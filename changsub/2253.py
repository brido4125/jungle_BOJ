import sys, math

INF = 10001
N, M = map(int, sys.stdin.readline().split())
# l의 의미
l = int(math.sqrt(2 * N)) + 1
dp = [[INF] * (l + 1) for _ in range(N + 1)]
small_stone = set()
for i in range(M):
    m = int(input())
    small_stone.add(m)
dp[1][0] = 0
for i in range(1, N + 1):
    for j in range(1, int(math.sqrt(2 * i)) + 1):
        if i in small_stone:
            continue
        else:
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
a = min(dp[N])
if a == INF:
    print(-1)
else:
    print(a)
