import sys

N = int(sys.stdin.readline())
wires = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    wires.append((a, b))

wires.sort()

dp = [0] * N

# LIS
for i in range(N):
    dp[i] = 1
    for j in range(i - 1, -1, -1):
        current = wires[i][1]
        if wires[j][1] < current and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(N - max(dp))
