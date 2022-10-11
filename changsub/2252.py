import sys

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
income = [0] * (N + 1)
answers = []
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start].append(end)
    income[end] += 1

while len(answers) != N:
    for i in range(1, N + 1):
        if visited[i]:
            continue
        elif income[i] == 0:
            answers.append(i)
            visited[i] = True
            for elem in adj_list[i]:
                income[elem] -= 1
            adj_list[i].clear()

for target in answers:
    print(target,end=" ")
