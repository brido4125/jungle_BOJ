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
