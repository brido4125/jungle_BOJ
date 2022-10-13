import sys

T = int(input())

memoization = [0] * 105

memoization[1] = 1
memoization[2] = 1
memoization[3] = 1
# 1 + 2 => 4
# 2 + 3 => 5
for i in range(4, 101):
    memoization[i] = memoization[i - 2] + memoization[i - 3]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(memoization[N])
