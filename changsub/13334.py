import sys
import heapq

N = int(input())

ranges = []

min_pos = 10e9
max_pos = -10e9

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y < x:  # 위치의 통일감을 위해 작은 죄표 ~ 큰 좌표로 정렬 후 append
        tmp = x
        x = y
        y = tmp
    if min_pos > x:
        min_pos = x
    if max_pos < y:
        max_pos = y
    ranges.append((x, y))

d = int(input())

ranges.sort()
for elem in ranges:
    x, y = elem
    if abs(x - y) > d:
        ranges.remove(elem)

pq = []

res = 0

for elem in ranges:
    if not pq:
        heapq.heappush(pq, elem)
    else:
        while pq[0][0] + d < elem[1]:
            heapq.heappop(pq)
            if not pq:
                break
        heapq.heappush(pq, elem)
    res = max(res,len(pq))

print(res)
