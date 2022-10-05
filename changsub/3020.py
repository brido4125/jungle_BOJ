def lower_bound(start, end, d, list):
    while end - start > 0:
        m = (start + end) // 2
        if list[m] < d:
            start = m + 1
        else:
            end = m
    return end


up = []
down = []
result = [0] * 50001
N, H = map(int, input().split())
for i in range(N):
    obstacle = int(input())
    if i % 2 == 1:
        up.append(obstacle)
    else:
        down.append(obstacle)

up.sort()
down.sort()

answer = 0
max = 10e9

for i in range(1, H + 1):
    down_index = lower_bound(0, len(down), i, down)
    up_index = lower_bound(0, len(up), H - i + 1, up)
