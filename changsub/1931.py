import sys

N = int(input())

confs = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    confs.append((x, y))

confs.sort(key=lambda x: (x[1], x[0]))

answer = 0
endTime = 0

for conf in confs:
    if endTime <= conf[0]:
        endTime = conf[1]
        answer += 1

print(answer)
