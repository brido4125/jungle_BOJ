import sys

N = int(input())

board = [list(map(int, sys.stdin.readline().rstrip('\n'))) for _ in range(N)]

adj_list = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            adj_list[i+1].append(j+1)

outDegree = [0] * (N+1)
result = [0] * (N + 1)
