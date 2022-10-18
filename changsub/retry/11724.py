import sys
# 7분 35초 clear

sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start].append(end)
    adj_list[end].append(start)


def dfs(start):
    visited[start] = True
    for elem in adj_list[start]:
        if not visited[elem]:
            dfs(elem)


answer = 0

for i in range(1,N+1):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)
