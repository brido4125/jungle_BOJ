import sys

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

board = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

node = 0

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    node = start
    board[start][end] = 1
    board[end][start] = 1

component = 0

def dfs(start):
    global component
    visited[start] = 1
    for i in range(1, N + 1):
        if visited[i] == 0 and board[start][i] == 1:
            dfs(i)


# visited를 순차적으로 방문하면서 False인 값을 만나면 component 개수 증가
# 시작 인덱스는 당연히 방문 하지 않았으니 연결 요소 +1
# 이후 dfs() 호출을 종료하고 난 뒤, 다음 번 만나는 False는 탐색하지 않은 연결요소이기에 연결 요소 +1
for i in range(1,N+1):
    if visited[i] == 0:
        component += 1
        dfs(i)

print(component)


