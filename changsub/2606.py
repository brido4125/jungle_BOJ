import sys

N = int(input())
E = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(E):
    start, end = map(int, sys.stdin.readline().split())
    board[start][end] = 1
    board[end][start] = 1

visited = [0] * (N + 1)
answer = 0


def dfs(start):
    global answer
    visited[start] = 1
    for i in range(1, N + 1):
        if visited[i] == 0 and board[start][i] == 1:
            answer += 1
            dfs(i)


dfs(1)
print(answer)
