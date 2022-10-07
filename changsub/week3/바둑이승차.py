import sys

C, N = map(int, input().split())
dogs = []
for _ in range(N):
    dogs.append(int(sys.stdin.readline()))

max = 0


def dfs(level, sum):
    global max
    if sum > C:
        return
    if level == N:
        if max < sum <= C:
            max = sum
        return
    else:
        dfs(level + 1, sum + dogs[level])
        dfs(level + 1, sum)


dfs(0, 0)
print(max)
