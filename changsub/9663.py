# # M : 현재 놓인 퀸의 갯수, N과 동일한 경우 모든 퀸이 체스판이 놓인 상태
# # row : 현재 놓인 퀸의 row 위치
# # col : 현재 놓인 퀸의 col 위치
# def reculsive(M, row, col):
#     if M == N:
#         # 조건이 완성 된 상태
#         return
#     for i in range(N):
#         if col != i:
#             reculsive(M + 1, row + 1, i)
#         check[row + 1][i] = 0
#
#
# for row in range(N):
#     reculsive(1, row, 0)

n = int(input())

cnt = 0
column = [0] * n


def validation(x):
    for i in range(x):
        if column[x] == column[i] or abs(column[x] - column[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global cnt
    if x == n:
        cnt += 1
        return
    else:
        for i in range(n):
            column[x] = i
            if validation(x):
                n_queens(x + 1)


n_queens(0)
print(cnt)
