def lower_bound(start, end, target, list):
    while end - start > 0:
        m = (start + end) // 2
        if list[m] < target:
            start = m + 1
        else:
            end = m
    return end


jongyusuk = []
suksun = []
result = [0] * 50001
N, H = map(int, input().split())
for i in range(N):
    obstacle = int(input())
    if i % 2 == 1:
        jongyusuk.append(obstacle)
    else:
        suksun.append(obstacle)

jongyusuk.sort()
suksun.sort()

answer = 0
max = 10e9

for i in range(1, H + 1):
    down_index = lower_bound(0, len(suksun), i, suksun)
    up_index = lower_bound(0, len(jongyusuk), H - i + 1, jongyusuk)
