N = int(input())
nums = list(map(int, input().split()))

answer = -10e9

# 배열 크기를 fit하게 설정해서 풀기
dp = [0] * N

dp[0] = nums[0]

for i in range(1, N):
    if dp[i-1] > 0:
        dp[i] = nums[i] + dp[i - 1]
    elif dp[i-1] <= 0:
        dp[i] = nums[i]

print(max(dp))
