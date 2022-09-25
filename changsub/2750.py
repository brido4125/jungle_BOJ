import sys

# N이 1000이하
# 해당 알고리즘은 Selection Sort => O(n**2)
# 1초에 1억번, 최대는 1000 * 1000 = 1000000 => 최대 연산 가능 횟수 백만 번 => 1억번 내라서 통과

N = int(input())

nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(i, N):
        if nums[i] > nums[j]:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

for elem in nums:
    print(elem)