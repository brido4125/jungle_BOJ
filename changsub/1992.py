N = int(input())

board = [list(map(int, input())) for _ in range(N)]

sum = 0

for i in range(N):
    for j in range(N):
        sum += board[i][j]



def solve(N, row, col):
    print("(", end='')
    half = N // 2
    sum = 0
    # 1사분면
    for i in range(row, row + half):
        for j in range(col, col + half):
            sum += board[i][j]
    if sum != 0 and sum != half ** 2:
        solve(N // 2, row, col)
    else:
        if sum == 0:
            print(0, end='')
        else:
            print(1, end='')
    sum = 0
    # 2사분면
    for i in range(row, row + half):
        for j in range(col + half, col + half + half):
            sum += board[i][j]
    if sum != 0 and sum != half ** 2:
        solve(N // 2, row, col + half)
    else:
        if sum == 0:
            print(0, end='')
        else:
            print(1, end='')
    sum = 0
    # 3사분면
    for i in range(row + half, row + half + half):
        for j in range(col, col + half):
            sum += board[i][j]
    if sum != 0 and sum != half ** 2:
        solve(N // 2, row + half, col)
    else:
        if sum == 0:
            print(0, end='')
        else:
            print(1, end='')
    sum = 0
    # 4사분면
    for i in range(row + half, row + half + half):
        for j in range(col + half, col + half + half):
            sum += board[i][j]
    if sum != 0 and sum != half ** 2:
        solve(N // 2, row + half, col + half)
    else:
        if sum == 0:
            print(0, end='')
        else:
            print(1, end='')
    print(")", end='')


if sum == 0:
    print(0)
elif sum == N ** 2:
    print(1)
else:
    solve(N, 0, 0)
