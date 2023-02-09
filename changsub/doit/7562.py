import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(leng, board, start, end):
    my_queue = deque()
    my_queue.append(start)
    while my_queue:
        pop = my_queue.popleft()
        for i in range(8):
            nextX = pop[0] + dx[i]
            nextY = pop[1] + dy[i]
            if nextX == end[0] and nextY == end[1]:
                return board[pop[1]][pop[0]] + 1
            if 0 <= nextX < leng and 0 <= nextY < leng and board[nextY][nextX] == 0:
                point = (nextX, nextY)
                my_queue.append(point)
                board[nextY][nextX] = board[pop[1]][pop[0]] + 1


T = int(sys.stdin.readline())
for v in range(T):
    length = int(sys.stdin.readline())
    board = [[0 for k in range(length)] for q in range(length)]
    sx, sy = map(int, sys.stdin.readline().split())
    start = (sx, sy)
    tx, ty = map(int, sys.stdin.readline().split())
    end = (tx, ty)
    if start[0] == end[0] and start[1] == end[1]:
        print(0)
    else:
        print(bfs(length, board, start, end))
