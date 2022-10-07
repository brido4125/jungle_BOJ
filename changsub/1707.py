import sys

sys.setrecursionlimit(10 ** 6)

T = int(input())


for i in range(T):
    V, E = map(int, sys.stdin.readline().split())

    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for k in range(E):
        start, end = map(int, sys.stdin.readline().split())
        adj_list[start].append(end)
        adj_list[end].append(start)


    # 연결되어 있는 점들이 가지는 A or B 값은 무조건 달라야 이분 그래프 조건을 만족한다.
    def dfs(startIndex):
        for v in adj_list[startIndex]:
            if visited[v] == 0:
                if visited[startIndex] == 'A':
                    visited[v] = 'B'
                else:
                    visited[v] = 'A'
                s = dfs(v)
                if not s:
                    return False
            elif visited[startIndex] == visited[v]:
                return False
        return True

    result = True

    for i in range(1, V+1):
        if visited[i] == 0:
            visited[i] = 'A'
            result = dfs(i)
            if not result:
                break

    print("YES") if result is True else print("NO")



