import sys

N, K = map(int, sys.stdin.readline().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    weights.append(w)
    values.append(v)

memoization = [[0] * (K + 1) for _ in range(N)]


# i가 weights와 values를 순화하는 index
def knapsack(i, k):
    if i < 0:
        return 0
    if memoization[i][k] == 0:
        if weights[i] > k:
            memoization[i][k] = knapsack(i - 1, k)
        else:
            memoization[i][k] = max(knapsack(i - 1, k), knapsack(i - 1, k - weights[i]) + values[i])
    return memoization[i][k]


dp = [[0] * (K + 1) for _ in range(N)]

for i in range(N):
    for j in range(1, K + 1):
        if dp[i][j] == 0:
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])

print(knapsack(N - 1, K))
print(dp[N-1][K])
