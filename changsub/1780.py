N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

minus_one = 0
one = 0
zero = 0


def calculate(row, col, length):
    global minus_one
    global one
    global zero
    value = board[row][col]
    for i in range(row, row + length):
        for j in range(col, col + length):
            if value != board[i][j]:
                return False
    if value == 0:
        zero += 1
    elif value == -1:
        minus_one += 1
    elif value == 1:
        one += 1
    return True


def solve(N, row, col):
    if not calculate(row, col, N):
        length = N // 3
        solve(length, row, col)
        solve(length, row, col + length)
        solve(length, row, col + length + length)
        solve(length, row + length, col)
        solve(length, row + length + length, col)
        solve(length, row + length, col + length)
        solve(length, row + length, col + length + length)
        solve(length, row + length + length, col + length)
        solve(length, row + length + length, col + length + length)


solve(N, 0, 0)

print(minus_one)
print(zero)
print(one)
