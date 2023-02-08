import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

my_stk = deque()
my_stk.append(N)
board = [0 for i in range(100001)]


# 5 -> 4 -> 8 -> 16 -> 17
def bfs():
    while my_stk:
        popleft = my_stk.popleft()
        back_point = popleft - 1
        up_point = popleft + 1
        double_point = 2 * popleft
        if 0 <= back_point < 100001 and board[back_point] == 0:
            my_stk.append(back_point)
            board[back_point] = board[popleft] + 1
        if 0 <= up_point < 100001 and board[up_point] == 0:
            my_stk.append(up_point)
            board[up_point] = board[popleft] + 1
        if 0 < double_point < 100001 and board[double_point] == 0:
            my_stk.append(double_point)
            board[double_point] = board[popleft] + 1
        if back_point == K or up_point == K or double_point == K:
            return board[popleft] + 1


if N == K:
    print(0)
else:
    print(bfs())
