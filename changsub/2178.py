from collections import deque

col, row = map(int, input().split())
board = [list(map(int, input())) for _ in range(col)]

# 아래 오른쪽 위 왼쪽 순으로 탐색
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()

queue.append((0, 0))
board[0][0] = 1


def bfs():
    while queue:
        privX, privY = queue.popleft()
        for i in range(4):
            currentX = privX + dx[i]
            currentY = privY + dy[i]
            if 0 <= currentX < row and 0 <= currentY < col and board[currentY][currentX] == 1:
                board[currentY][currentX] = board[privY][privX] + 1
                queue.append((currentX, currentY))


bfs()
print(board[col - 1][row - 1])
