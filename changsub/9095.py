import sys

T = int(input())


def solve(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return solve(num - 1) + solve(num - 2) + solve(num - 3)


for _ in range(T):
    target = int(sys.stdin.readline())
    print(solve(target))

