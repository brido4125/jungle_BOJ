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


def topology():
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        popleft = queue.popleft()
        for elem, need in adj_list[popleft]:
            # popleft가 필요한 부품
            if sum(needs[popleft]) == 0:
                needs[elem][popleft] += need
            else:
                for i in range(1, N + 1):
                    needs[elem][i] += needs[popleft][i] * need

            indegree[elem] -= 1
            if indegree[elem] == 0:
                queue.append(elem)


topology()
print(needs)
