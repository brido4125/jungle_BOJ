import sys

N, B = map(int, input().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
MOD = 1000


# 두 행렬 간의 곱셈 진행하는 함수
# 행렬의 row, column은 N
def matrix_calc(a, b):
    answer = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer[i][j] += a[i][k] * b[k][j]
                answer[i][j] %= MOD
    return answer


def solve(matrix, exponent):
    # 행렬의 원소가 1000임과 동시에 지수가 1인 경우 나머지 연산 처리 필요
    if exponent == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= MOD
        return matrix

    half = solve(matrix, exponent // 2)

    if exponent % 2 == 1:
        return matrix_calc(matrix_calc(half, half), matrix)

    return matrix_calc(half, half)


for i in range(N):
    for j in range(N):
        print(solve(matrix, B)[i][j], end=' ')
    print()
