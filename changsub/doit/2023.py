import sys

N = int(input())
sys.setrecursionlimit(10 ** 9)

first_num = [2, 3, 5, 7]


def isPrimeNum(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


answer = []


def dfs(level, start):
    if level == N - 1:
        print(start)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            concat = int(str(start) + str(i))
            if isPrimeNum(concat):
                dfs(level + 1, concat)


for num in first_num:
    dfs(0, num)
