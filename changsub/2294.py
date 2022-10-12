import sys
from collections import deque

N, target = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

# 코인 중복 제거
coins = set(coins)

visited = [False] * (target + 1)

depth = 1 # 사용한 동전 개수


def bfs():
    queue = deque()
    find = False
    for coin in coins:
        if coin < target:
            # 주어진 동전 각 1개씩 사용하는 경우 => Depth 1
            queue.append([coin, 1])
            visited[coin] = 1

    while queue:
        pop, depth = queue.popleft()
        if target == pop:
            print(depth)
            find = True
            break
        for coin in coins:
            next = pop + coin
            next_depth = depth + 1
            if next > target:
                continue
            elif next <= target and visited[next] == 0:
                visited[next] = True
                queue.append([next, next_depth])

    if not find:
        print('-1')


bfs()

