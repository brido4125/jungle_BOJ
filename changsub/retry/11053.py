N = int(input())
nums = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = 1
    # i보다 작은 index 중 작은 값이 있으면 증가하는 수열 count
    for j in range(0, i):
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
