import sys

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

dp = [0] * (N)
dp[0] = stairs[0]
priv = 0
index = 0

for i in range(1, N - 1):
    if priv == N - 1 or priv == N - 2:
        index = (i -1)
        break
    if stairs[priv + 1] > stairs[priv + 2]:
        dp[i] = dp[i - 1] + stairs[priv + 1]
        priv += 1
    else:
        dp[i] = dp[i - 1] + stairs[priv + 2]
        priv += 2

if priv == N - 2:
    dp[index] += stairs[-1]


print(dp[index])
