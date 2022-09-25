N = int(input())

check = [[0] * N for _ in range(N)]

print(check)


# M : 현재 놓인 퀸의 갯수, N과 동일한 경우 모든 퀸이 체스판이 놓인 상태
# row : 현재 놓인 퀸의 row 위치
# col : 현재 놓인 퀸의 col 위치
def reculsive(M, row, col):
    if M == N:
        # 조건이 완성 된 상태
        return
    for i in range(N):
        if col != i:
            reculsive(M + 1, row + 1, i)
        check[row + 1][i] = 0


for row in range(N):
    reculsive(1, row, 0)
