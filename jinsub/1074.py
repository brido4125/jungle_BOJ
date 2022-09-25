# input = "2 3 1"
# num, row, col = input.split()

count = 0


def check_dimension(n, r, c):
    global count
    check_r = 0
    check_c = 0
    dimension = 0
    if n == 1:
        count += 2*r+c
        print(count)
    else:
        check_r += r//2**(n-1)
        check_c += c//2**(n-1)
        count += (2 * check_r + check_c) * 4**(n-1)
        check_dimension(n-1, r-check_r*2**(n-1), c-check_c*2**(n-1))


num, row, col = map(int, input().split(' '))

check_dimension(num, row, col)
