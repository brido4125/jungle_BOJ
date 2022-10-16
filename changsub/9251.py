import sys

sys.setrecursionlimit(10 ** 9)
str1 = sys.stdin.readline().rstrip('\n')
str2 = sys.stdin.readline().rstrip('\n')

memoization = [[0] * len(str2) for _ in range(len(str1))]


def LCS(x, y):
    # index가 board 밖인 경우 에외처리
    if x < 0 or y < 0:
        return 0

    if memoization[x][y] == 0:
        # str 로그 찍기
        if str1[x] == str2[y]:
            memoization[x][y] = LCS(x - 1, y - 1) + 1
        else:
            memoization[x][y] = max(LCS(x - 1, y), LCS(x, y - 1))

    return memoization[x][y]


# print(LCS(len(str1) - 1, len(str2) - 1))

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(str1)][len(str2)])
