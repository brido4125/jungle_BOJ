from collections import deque

R, C = map(int, input().split())

board = []
hog_queue = deque()
water_queue = deque()
cave_row = ''
cave_col = ''
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

for i in range(R):
    tmp = list(map(str, input()))
    for j in range(C):
        if tmp[j] == 'S':
            hog_queue.append((i, j))
            tmp[j] = 0
        elif tmp[j] == '*':
            water_queue.append((i, j))
        elif tmp[j] == 'D':
            cave_row = i
            cave_col = j
    board.append(tmp)


def bfs():
    # 물 먼저 잠기게 한뒤, 고슴도치 bfs
    waterCount = len(water_queue)
    hogCount = len(hog_queue)
    while water_queue or hog_queue:
        for i in range(waterCount):
            priv_water_row, priv_water_col = water_queue.popleft()
            for j in range(4):
                current_water_col = priv_water_col + dx[j]
                current_water_row = priv_water_row + dy[j]
                if 0 <= current_water_row < R and 0 <= current_water_col < C and board[current_water_row][
                    current_water_col] == '.':
                    board[current_water_row][current_water_col] = '*'
                    water_queue.append((current_water_row, current_water_col))
        waterCount = len(water_queue)

        for k in range(hogCount):
            priv_hog_row, priv_hog_col = hog_queue.popleft()
            for t in range(4):
                current_hog_row = priv_hog_row + dy[t]
                current_hog_col = priv_hog_col + dx[t]
                if current_hog_row == cave_row and current_hog_col == cave_col:
                    board[cave_row][cave_col] = board[priv_hog_row][priv_hog_col] + 1
                if 0 <= current_hog_row < R and 0 <= current_hog_col < C and board[current_hog_row][
                    current_hog_col] == '.':
                    board[current_hog_row][current_hog_col] = board[priv_hog_row][priv_hog_col] + 1
                    hog_queue.append((current_hog_row, current_hog_col))
        hogCount = len(hog_queue)

# 벽을 안써서 틀린거 같음
bfs()
if board[cave_row][cave_col] == 'D':
    print("KAKTUS")
else:
    print(board[cave_row][cave_col])
