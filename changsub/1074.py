N, r, c = map(int, input().split())

board_len = (2 ** N)
answer = 0


def solving(len, r, c):
    global answer
    if len == 1:
        return
    half = len // 2
    if r < half <= c:
        # 2사분면
        answer += (half ** 2)
    elif r >= half > c:
        # 3사분면
        answer += 2 * (half ** 2)
    elif r >= half and c >= half:
        # 4사분면
        answer += 3 * (half ** 2)
    if r >= half:
        r -= half
    if c >= half:
        c -= half
    solving(half, r, c)


solving(board_len, r, c)
print(answer)
