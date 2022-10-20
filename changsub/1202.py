import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jewelries = []

for _ in range(N):
    w, c = map(int, sys.stdin.readline().split())
    jewelries.append((w, c))

jewelries.sort(key=lambda x: x[0])
bag_afford_limit = []

for _ in range(K):
    bag_afford_limit.append(int(sys.stdin.readline()))
bag_afford_limit.sort()

pq = []
sum = 0
index = 0
# 가방무게를 기준으로 먼저 정렬 후, 힙큐에 해당 무게의 가치를 넣어서 가치순대로 정렬
for bagLimit in bag_afford_limit:
    while index < N and bagLimit >= jewelries[index][0]:
        # min-heap이 아닌 max-heap 사용
        heapq.heappush(pq, -jewelries[index][1])
        index += 1
    if pq:
        sum -= heapq.heappop(pq)

print(sum)
