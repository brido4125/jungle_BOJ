import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

start = 1
end = M
answer = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, N + 1):
        small_count = mid // i
        if small_count > N:
            small_count = N
        cnt += small_count
    if cnt < M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)

