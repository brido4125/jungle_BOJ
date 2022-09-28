N = int(input())

nums = []
for i in range(N):
    nums.append(i + 1)

board = [list(map(int, input().split())) for _ in range(N)]

check = [False] * N
comb = [0] * (N // 2)
ability = []


# 조합 구하기
def combination(L, start):
    if L == N // 2:
        sum = 0
        for i in range(len(comb)):
            for j in range(len(comb)):
                if i != j:
                    sum += board[comb[i] - 1][comb[j] - 1]
        ability.append(sum)
        return
    for i in range(start, N):
        comb[L] = nums[i]
        combination(L + 1, i + 1)


combination(0, 0)

answers = []
for i in range(len(ability)):
    differ = abs(ability[i] - ability[-1 - i])
    answers.append(differ)

print(min(answers))

