import sys

sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[end].append(start)


def dfs(start):
    global cnt
    for elem in adj_list[start]:
        if not check[elem]:
            cnt += 1
            dfs(elem)

print(adj_list)
check = [False] * (N + 1)
answer = 0
for i in range(1, N + 1):
    if not check[i]:
        cnt = 0
        dfs(i)
        check[i] = cnt

max_value = max(check)

for i in range(1, N + 1):
    if check[i] == max_value:
        print(i, end=' ')
