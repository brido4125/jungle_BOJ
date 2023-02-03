import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, sys.stdin.readline().split())
# adj list
adj_list = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

check = [False] * N

global answer


def dfs(depth, index):
    global answer
    if depth >= 4:
        answer = 1
    else:
        for elem in adj_list[index]:
            if not check[elem]:
                check[elem] = True
                dfs(depth + 1, elem)
                check[elem] = False


answer = 0
for i in range(N):
    if answer == 0:
        check[i] = True
        dfs(0, i)
        check[i] = False
    else:
        break

print(answer)
