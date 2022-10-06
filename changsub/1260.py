import sys
from collections import deque

N, M, V = map(int, input().split())

board = [[0] * (N + 1) for _ in range(N + 1)]
visit = [0] * (N + 1)

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    board[start][end] = 1
    board[end][start] = 1

bfs_answer = []
dfs_answer = []


def bfs(startIndex):
    print(startIndex, end=' ')
    visit[startIndex] = 1
    for i in range(1, N + 1):
        if visit[i] == 0 and board[i][startIndex] == 1:  # board[startIndex][i]로 해도 상관없음
            bfs(i)


def dfs(startIndex):
    queue = deque()
    queue.append(startIndex)
    while queue:
        target = queue.popleft()
        print(target, end=' ')
        visit[target] = 1
        for i in range(1, N + 1):
            if visit[i] == 0 and board[i][target] == 1:
                queue.append(i)
                visit[i] = 1


bfs(V)
visit = [0] * (N + 1)
print()
dfs(V)
