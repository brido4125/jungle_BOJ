A, B, C = map(int, input().split())

answer = 1


def my_pow(bottom, exponent):
    if exponent == 1:
        return bottom

    half = my_pow(bottom, exponent // 2)

    if exponent % 2 == 1:
        return (half * half) * bottom

    return half * half


def solve(bottom, exponent):
    if exponent == 1:
        return bottom % C

    half = solve(bottom, exponent // 2)

    if exponent % 2 == 1:
        return (half * half % C) * bottom % C

    return half * half % C


print(solve(A, B))
