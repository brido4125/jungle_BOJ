# N : 도시의 개수
# M : 도로의 개수
# K : 거리정보
# X : 출발 도시의 번호
import sys
from collections import deque

N, M, K, X = map(int, input().split())

board = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    board[start].append(end)

queue = deque()
distance = 1
answers = []
queue.append(X)
visited = [0] * (N + 1)


def bfs():
    global distance
    while queue:
        popleft = queue.popleft()
        priv_distance = visited[popleft]
        if priv_distance == K:
            answers.append(popleft)
        for node in board[popleft]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = priv_distance + 1


bfs()
if len(answers) == 0:
    print(-1)
# cycle 돌아서 자기 자신으로 오는 경우 예외처리
elif len(answers) == 1 and answers[0] == X:
    print(-1)
else:
    answers.sort()
    for elem in answers:
        print(elem)
