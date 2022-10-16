import sys

sys.setrecursionlimit(10 ** 9)
str1 = sys.stdin.readline().rstrip('\n')
str2 = sys.stdin.readline().rstrip('\n')

dp = [[0] * len(str2) for _ in range(len(str1))]


def LCS(x, y):
    # index가 board 밖인 경우 에외처리
    if x < 0 or y < 0:
        return 0

    if dp[x][y] == 0:
        # str 로그 찍기
        if str1[x] == str2[y]:
            dp[x][y] = LCS(x - 1, y - 1) + 1
        else:
            dp[x][y] = max(LCS(x - 1, y), LCS(x, y - 1))

    return dp[x][y]


print(LCS(len(str1) - 1, len(str2) - 1))
