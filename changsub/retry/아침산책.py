import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
pos = [0] + list(map(int, sys.stdin.readline().rstrip('\n')))

board = [[] for _ in range(N + 1)]

answer = 0
visited = [False] * (N + 1)
count = 0

for _ in range(N - 1):
    start, end = map(int, sys.stdin.readline().split())
    board[start].append(end)
    board[end].append(start)
    # 실내에서 시작해서 실내에서 끝나는 경우 추가
    if pos[start] == 1 and pos[end] == 1:
        answer += 2


def dfs(start):
    global count
    visited[start] = True
    for elem in board[start]:
        if pos[start] == 0 and pos[elem] == 1 and visited[elem] == False:
            count += 1
        elif pos[start] == 0 and pos[elem] == 0 and visited[elem] == False:
            dfs(elem)


for i in range(1, N + 1):
    if pos[i] == 0 and visited[i] == False:
        dfs(i)
        answer += count * (count - 1)
        count = 0

print(answer)
