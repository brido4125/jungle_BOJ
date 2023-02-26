import sys

N, M = map(int, sys.stdin.readline().split())
sizes = list(map(int, sys.stdin.readline().split()))

# 구해야하는 총 동영상 길이
total_size = sum(sizes)

start = 0
for i in sizes:
    if start < i:
        start = i
end = total_size
answer = 100000

while start <= end:
    # mid의 크기만큼의 블루레이가 M개 존재
    mid = (start + end) // 2
    tmp = 0
    cnt = 0
    for i in range(N):
        if tmp + sizes[i] > mid:
            cnt += 1
            tmp = 0
        tmp += sizes[i]
    if sum != 0:
        cnt += 1
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)
