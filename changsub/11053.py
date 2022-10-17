import sys

N = int(input())

nums = list(map(int, sys.stdin.readline().split()))

dp = [0] * N


def LIS(N):
    if dp[N] == 0:
        dp[N] = 1
        # 자기자신 count 기본으로 하는거라서 1로 초기화
        # 이후 재귀로 자기 자신의 index보다 작은 index 탐색
        # 탐색 중 만약 자기 자신보다 작은 요소 만나면 count 1 증가
        for i in range(N - 1, -1, -1):
            if nums[i] < nums[N]:
                dp[N] = max(dp[N], LIS(i) + 1)
    return dp[N]


for i in range(N):
    LIS(i)

print(max(dp))
