N, M = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(N)]

R, K = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(M)]


answer = [[0] * K for _ in range(N)]


# 행렬의 곱셈 -> 최적화 필요
for i in range(N):
    for j in range(K):
        for k in range(M):
            answer[i][j] += matrixA[i][k] * matrixB[k][j]


for i in range(N):
    for j in range(K):
        print(answer[i][j], end=' ')
    print()
