import sys
from collections import deque


N = int(sys.stdin.readline())

my_stk = deque([i for i in range(N,0,-1)])

while len(my_stk) != 1:
    my_stk.pop()
    target = my_stk.pop()
    my_stk.appendleft(target)

print(my_stk[0])
