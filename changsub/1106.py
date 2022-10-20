import sys

C, N = map(int, sys.stdin.readline().split())

costs = []
members = []
for _ in range(N):
    cost, member = map(int, sys.stdin.readline().split())
    costs.append(cost)
    members.append(member)

costs.insert(0, 0)
members.insert(0, 0)


# 1099, 1100의 의미?
dp = [[10e9] * (C + 100) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = 0
    for j in range(1, C + 100):
        first = dp[i - 1][j]
        second = dp[i][j - members[i]] + costs[i]
        dp[i][j] = min(dp[i - 1][j], dp[i][j - members[i]] + costs[i])

print(min(dp[N][C:]))
