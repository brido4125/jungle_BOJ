N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0


def solve(length, row, col):
    global blue
    global white

    if length == 0:
        return
    else:
        half = length // 2
        sum = 0
        for i in range(length):
            for j in range(length):
                first = board[row][col]
                if first != board[i + row][j + col]:
                    solve(half, row, col)
                    solve(half, row, col + half)
                    solve(half, row + half, col)
                    solve(half, row + half, col + half)
                    return  # 4등분된 면 전부 solve 하면 호출된 함수 종료해야함
                else:
                    sum += board[i + row][j + col]
        if sum == 0:
            white += 1
        elif sum == length ** 2:
            blue += 1


solve(N, 0, 0)

print(white)
print(blue)
