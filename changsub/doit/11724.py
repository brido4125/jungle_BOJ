import sys
sys.setrecursionlimit(10 ** 9)


N, M = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(N + 1)]
check = [False] * (N + 1)

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

answer = 0


def dfs(node):
    if check[node]:
        return
    check[node] = True
    for n in adj_list[node]:
        dfs(n)


for i in range(1, N + 1):
    if not check[i]:
        answer += 1
        dfs(i)

print(answer)
