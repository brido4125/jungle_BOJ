import sys

N, K = map(int, input().split())

levels = []

for _ in range(N):
    levels.append(int(sys.stdin.readline()))

start = min(levels)
end = max(levels) + K
answer = 0
while start <= end:
    mid = (start + end) // 2

    sum = 0
    for elem in levels:
        if mid > elem:
            sum += (mid - elem)

    if sum <= K:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1


print(answer)
