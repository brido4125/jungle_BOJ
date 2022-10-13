import sys

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, limit = map(int, sys.stdin.readline().split())
    adj_list[start].append((end, limit))
    adj_list[end].append((start, limit))

target1, target2 = map(int, sys.stdin.readline().split())

max = 0

for edge in adj_list[target1]:
    if edge[0] == target2:
        if max < edge[0]:
            max = edge[0]

print(max)

