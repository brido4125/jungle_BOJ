from collections import deque


def direction_change(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1  # 사과는 board에서 1로 지정
L = int(input())
times = {}  # 디렉션이 변하는 시간 대를 딕셔너리로 정의
for i in range(L):
    X, C = input().split()
    times[int(X)] = C

# 위, 우측, 아래, 좌측 디렉션
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# 상 좌 하 우
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]



direction = 3
time = 1  # 시작하면 1초
x = 0
y = 0
board[y][x] = 2  # 뱀이 처음 시작할때 있는 위치
queue = deque([[y, x]])

while True:
    y, x = y + dy[direction], x + dx[direction],
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:  # 현재 뱀이 갈수 있는 위치이면
        if not board[y][x] == 1:  # 사과가 없는 곳
            delY, delX = queue.popleft()
            board[delY][delX] = 0  # 사과가 없으니 원래 뱀이 있던 곳은 0으로 변경
        board[y][x] = 2  # 뱀이 옮겨간 위치는  2로 변경
        queue.append([y, x])
        if time in times.keys():
            direction = direction_change(direction, times[time])
        time += 1
    else:  # 뱀이 벽이나 자기 자신에 부딪혀서 게임이 끝나는 경우
        break

print(time)
