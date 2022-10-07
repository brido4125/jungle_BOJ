import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())

# adj_matrix는 메모리 초과 발생
adj_list = [[] for i in range(N + 1)]

visited = [False] * (N + 1)

answer = [0] * (N + 1)

for _ in range(N - 1):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start].append(end)
    adj_list[end].append(start)


def dfs(node):
    visited[node] = True
    for i in adj_list[node]:
        if not visited[i]:
            answer[i] = node
            dfs(i)


dfs(1)
for i in range(2,N+1):
    print(answer[i])