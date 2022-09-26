import sys
from itertools import permutations

N = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cities = []
for i in range(N):
    cities.append(i)

check = [False] * N

seq = [0] * N  # 경로 담는 Array, Permutation 사용

ways = []

all = permutations(list(range(N)))


def permutation(L):
    if L == N:
        target = []
        for elem in seq:
            target.append(elem)
        ways.append(target)
    else:
        for i in range(N):
            if not check[i]:
                check[i] = True
                seq[L] = cities[i]
                permutation(L + 1)
                check[i] = False


# permutation(0)
min = 100000000
for way in ways:
    cost = 0
    flag = True
    for i in range(N - 1):
        tmp = board[way[i]][way[i + 1]]
        if tmp == 0:
            flag = False
            break
        else:
            cost += tmp
    tmp = board[way[N - 1]][way[0]]
    if tmp == 0:
        flag = False
    else:
        cost += tmp
    if flag and min > cost:
        min = cost

print(min)
