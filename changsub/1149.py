import sys

N = int(input())
costs = []

for i in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * 3 for _ in range(N)]
dp[0] = costs[0]

# DP 배열을 2차원 배열 사용
# i번째 집을 칠할 수 있는 3가지 경우를 모두 dp 배열에 저장한다
# 구해진 모든 값들 중 최솟값을 출력
# 현재 칠하는 집의 이전 집이 빨강이라도 현재 집을 빨강으로 칠하는 경우의 수도 구함
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + costs[i][2]

print(min(dp[-1]))
