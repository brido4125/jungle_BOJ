import sys

N = int(input())

value = list(map(int, sys.stdin.readline().split()))

for _ in range(N - 1):
    x,y = map(int, sys.stdin.readline().split())
    value.append(y)

def minimum(M, d, i, j):
    minValue = 10e9
    for k in range(i, j):
        value = M[i][k] + M[k + 1][j]
        value += d[i - 1] * d[k] * d[j]
        if minValue > value:
            minValue = value
    return minValue


def minmult(values):
    n = len(values) - 1
    M = [[-1] * (N + 1) for _ in range(N + 1)]
    for i in range(1, n + 1):
        M[i][i] = 0
    # 대각선 처리 로직
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j] = minimum(M, values, i, j)
    return M


board = minmult(value)
print(board[1][N])
