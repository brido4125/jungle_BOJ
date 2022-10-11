import sys
from collections import deque

N, M = map(int, input().split())
# 노드보다 무거운거 추가
heavy_graph = [[] for _ in range(N + 1)]
# 노드보다 가벼운 거 추가
light_graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

target = (N // 2) + 1

for _ in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    heavy_graph[heavy].append(light)
    light_graph[light].append(heavy)


def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        popleft = queue.popleft()
        if len(heavy_graph[popleft]) == len(light_graph[popleft]):
            continue
        for elem in light_graph[popleft]:
            visited[popleft] = len(light_graph[popleft])
            if elem > popleft:
                if len(heavy_graph[elem]) != 0:
                    visited[popleft] += len(heavy_graph[elem])
                if not visited[elem]:
                    queue.append(elem)
        for elem in heavy_graph[popleft]:
            visited[popleft] = len(heavy_graph[popleft])
            if elem < popleft:
                if len(light_graph[elem]) != 0:
                    visited[popleft] += len(light_graph[elem])
                if not visited[elem]:
                    queue.append(elem)



bfs()
print(visited)
