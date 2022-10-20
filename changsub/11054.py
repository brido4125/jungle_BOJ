N = int(input())
nums = list(map(int, input().split()))

dp_LIS = [1] * N
dp_LDS = [1] * N

for i in range(N):
    for j in range(i - 1, -1, -1):
        one = nums[i]
        two = nums[j]
        if nums[i] > nums[j] and dp_LIS[i] < dp_LIS[j] + 1:
            dp_LIS[i] = dp_LIS[j] + 1

for i in range(N - 1, -1, -1):
    for j in range(i+1, N):
        one = nums[i]
        two = nums[j]
        if nums[i] > nums[j] and dp_LDS[i] < dp_LDS[j] + 1:
            dp_LDS[i] = dp_LDS[j] + 1

bitonic = []
for i in range(N):
    bitonic.append(dp_LDS[i] + dp_LIS[i])

# 중복 요소 -1
print(max(bitonic) - 1)