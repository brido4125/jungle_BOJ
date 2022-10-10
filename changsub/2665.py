import sys
from collections import deque

N = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = [list(map(int, sys.stdin.readline().rstrip('\n'))) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]


# visited[][]의 검은색 방 위치에는 해당 검은 방을 가기 위해 필요한 방 변경 횟수를 넣어 줘야함
def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    while queue:
        row, col, = queue.popleft()
        # 해당 노드가 목적지에 도달 했을 경우
        if row == N - 1 and col == N - 1:
            return visited[row][col]
        for i in range(len(dx)):
            currentRow = row + dy[i]
            currentCol = col + dx[i]
            # 기본적으로 board 안에 있고, 방문하지 않은 경우
            if 0 <= currentRow < N and 0 <= currentCol < N and visited[currentRow][currentCol] == -1:
                # 흰방인 경우
                if board[currentRow][currentCol] == 1:
                    visited[currentRow][currentCol] = visited[row][col]
                    queue.appendleft((currentRow, currentCol))
                # 검은방인 경우
                else:
                    visited[currentRow][currentCol] = visited[row][col] + 1
                    queue.append((currentRow, currentCol))


print(bfs())
