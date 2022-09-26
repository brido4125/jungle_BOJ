import sys
sys.setrecursionlimit(10**6)

N = int(input())

# 0!=1 재귀함수:프렉탈


def factorial(N):
    if N == 0:  # 이 코드 자체가 factorial(0)
        return 1
    else:
        return N * factorial(N-1)


print(factorial(N))
