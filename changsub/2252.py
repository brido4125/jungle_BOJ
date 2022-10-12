import sys
from collections import deque

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
answers = []
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start].append(end)
    indegree[end] += 1

queue = deque()

for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    popleft = queue.popleft()
    answers.append(popleft)
    for elem in adj_list[popleft]:
        indegree[elem] -= 1
        if indegree[elem] == 0:
            queue.append(elem)

for target in answers:
    print(target,end=" ")
