import sys
from collections import deque

N = int(sys.stdin.readline())

# 깊은 복사를 위해 for문으로 배열 생성
adj_list = [[] for _ in range(N + 1)]

# input 정보를 adj_list 형태로
for i in range(N):
    target = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(target) - 1, 2):
        adj_list[target[0]].append((target[j], target[j + 1]))

distance = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]


def bfs(start):
    visited[start] = True
    my_queue = deque([start])
    while my_queue:
        target = my_queue.popleft()
        for elem in adj_list[target]:
            if not visited[elem[0]]:
                distance[elem[0]] += (distance[target] + elem[1])
                my_queue.append(elem[0])
                visited[elem[0]] = True


# 임의의 한점에서 가장 멀리 떨어져 있는 한 점 찾기
bfs(2)
far_node = distance.index(max(distance))#임의의 한점으로부터 가장 멀리 떨어진 점
# visited, distance 리스트 초기화
for i in range(N+1):
    distance[i] = 0
    visited[i] = False
bfs(far_node)
answer = max(distance)
print(answer)
