import sys

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

memoization = [0] * (N + 1)

memoization[0] = stairs[0]  # 0번째 비우고 시작
memoization[1] = stairs[1]

dp = [0] * (N + 1)

dp[0] = stairs[0]  # 0번째 비우고 시작
dp[1] = stairs[1]

# Top-Down 방식
def reculsive(N):
    if N <= 0:
        return 0
    if memoization[N] == 0:
        memoization[N] = max(reculsive(N - 2), reculsive(N - 3) + stairs[N - 1]) + stairs[N]
    return memoization[N]


if N >= 2:
    memoization[2] = stairs[2] + stairs[1]
    dp[2] = stairs[2] + stairs[1]

#Bottom-Up 방식
for i in range(3, N + 1):
    dp[i] = stairs[i] + max(dp[i - 3] + stairs[i - 1], dp[i - 2])
print(reculsive(N))
print(dp[N])
