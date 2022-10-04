import sys
import heapq

N = int(input())

pq = []

for _ in range(N):
    target = int(sys.stdin.readline())
    heapq.heappush(pq, target)


sum = 0

while len(pq) > 1:
    pop_first = heapq.heappop(pq)
    pop_second = heapq.heappop(pq)
    res = pop_first + pop_second
    sum += res
    heapq.heappush(pq, res)
    res = 0

print(sum)
