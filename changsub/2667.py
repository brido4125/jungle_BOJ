from collections import deque

N = int(input())

board = [list(map(int, input())) for _ in range(N)]
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

pq = deque()


def bfs(row, col):
    count = 1
    point = (row, col)
    board[row][col] = 0
    pq.append(point)
    while pq:
        privRow, privCol = pq.popleft()
        for i in range(4):
            currentRow = privRow + dx[i]
            currentCol = privCol + dy[i]
            if 0 <= currentRow < N and 0 <= currentCol < N and board[currentRow][currentCol] == 1:
                count += 1
                pq.append((currentRow, currentCol))
                board[currentRow][currentCol] = 0
    return count


answers = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            answers.append(bfs(i, j))

answers.sort()
print(len(answers))
for answer in answers:
    print(answer)
