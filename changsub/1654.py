import sys

K, N = map(int, input().split())

nums = []
for _ in range(K):
    nums.append(int(sys.stdin.readline()))

max_value = max(nums)

start = 1 # 잘린 랜선의 길이가 0이 될 수 없다
end = max_value
answer = 0

while start <= end:
    sum = 0
    mid = (start + end) // 2
    # N개 만큼의 랜선을 만들어야 한다.
    for elem in nums:
        sum += (elem // mid)
    if N > sum:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid


print(answer)
