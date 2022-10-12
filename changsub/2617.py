import sys
from collections import deque

N, M = map(int, input().split())
# 노드보다 무거운거 추가
heavy_graph = [[] for _ in range(N + 1)]
# 노드보다 가벼운 거 추가
light_graph = [[] for _ in range(N + 1)]

target = (N // 2) + 1

for _ in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    heavy_graph[heavy].append(light)
    light_graph[light].append(heavy)

visited = [False] * (N + 1)
answers = [0] * (N + 1)


def dfs(start, list):
    global count
    visited[start] = True
    for elem in list[start]:
        if not visited[elem]:
            count += 1
            dfs(elem, list)


answer = 0

for i in range(1, N + 1):
    count = 0
    visited = [False] * (N + 1)
    dfs(i, light_graph)
    if count >= target:
        answer += 1
    count = 0
    dfs(i, heavy_graph)
    if count >= target:
        answer += 1

print(answer)
