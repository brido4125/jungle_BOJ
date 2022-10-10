import sys
import heapq


def bfs():
    heap = []
    heapq.heappush(heap, [start, 0])
    visited[start] = 0

    while heap:
        priv, priv_cost = heapq.heappop(heap)
        # 현재 도시까지 가는데 드는 비용이 더 적으면 실행 않고 다음 반복으로
        if visited[priv] < priv_cost:
            continue

        for node, cost in adj_list[priv]:
            target = cost + priv_cost
            if target < visited[node]:
                visited[node] = target
                heapq.heappush(heap, [node, target])


N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [10e9] * (N + 1)

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    adj_list[start].append([end, cost])

start, end = map(int, input().split())

answers = []

bfs()
print(visited[end])
