import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj_list = [[] for _ in range(N + 1)]
indegree = [None] + ([0] * N)
needs = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    target, component, cost = map(int, sys.stdin.readline().split())
    adj_list[component].append((target, cost))
    indegree[target] += 1


def topology_sort():
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        for next, cost in adj_list[node]:
            # 만약 현재 node가 기본 부품이면, 즉 필요한 부품이 없으면 == 부품의 합계가 0이면
            if sum(needs[node]) == 0:
                needs[next][node] += cost
            else:
                # 필요한 기본 부품을 누적합
                for i in range(1, N + 1):
                    needs[next][i] += needs[node][i] * cost

            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)


topology_sort()
print(needs)

for x in enumerate(needs[N]):
    if x[1] > 0:
        print(*x)
