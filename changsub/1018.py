n, m = map(int, input().split())

board = [list(map(str, input())) for _ in range(n)]

answers = []

for p in range(n - 7):
    for q in range(m - 7):
        countB = 0 # B로 시작하는 8 by 8을 만들기 위해 필요한 카운팅
        countW = 0 # W로 시작하는 8 by 8을 만들기 위해 필요한 카운팅
        for i in range(p, p + 8):
            for j in range(q, q + 8):
                if (i + j) % 2 == 0:# 짝수 인덱스
                    if board[i][j] != 'W':
                        countW += 1
                    if board[i][j] != 'B': # B로 시작하는 보드는 짝수 인덱스가 B이어야하니까 B가 아니면 countB +1
                        countB += 1
                else: # 홀수 인덱스
                    if board[i][j] != 'W': # B로 시작하는 보드는 홀수 인덱스가 W이어야하니까 W가 아니면 countB +1
                        countB += 1
                    if board[i][j] != 'B':
                        countW += 1

        answers.append(countB)
        answers.append(countW)


print(min(answers))
