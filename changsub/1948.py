import sys
from collections import deque

N = int(input())
M = int(input())

board = [[] for _ in range(N + 1)]
back = [[] for _ in range(N + 1)]
check = [0] * (N + 1)
indegree = [0] * (N + 1)
visited = [False] * (N + 1)  # 백트랙킹시 vistited 중복 체크

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    board[start].append((end, cost))
    back[end].append((start, cost))
    indegree[end] += 1

start, end = map(int, sys.stdin.readline().split())


def topology():
    global before_end_node, before_end_cost
    queue = deque()
    queue.append(start)
    while queue:
        current = queue.popleft()
        for next, cost in board[current]:
            check[next] = max(check[current] + cost, check[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

    # back-tracking
    queue.append(end)
    count = 0

    while queue:
        now = queue.popleft()
        for pre, cost in back[now]:
            if check[now] == check[pre] + cost:
                count += 1
                if not visited[pre]:
                    queue.append(pre)
                    visited[pre] = True

    print(check[end])
    print(count)


topology()
