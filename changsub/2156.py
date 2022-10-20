import sys

N = int(input())
values = []
for _ in range(N):
    values.append(int(sys.stdin.readline()))

values.insert(0, 0)

dp = [0] * (N + 1)
dp[1] = values[1]
if N > 1:
    dp[2] = values[1] + values[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], values[i] + values[i - 1] + dp[i - 3], values[i] + dp[i - 2])
print(dp[N])