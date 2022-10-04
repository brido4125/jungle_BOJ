import sys

N = int(input())

ranges = []

min_pos = 10e9
max_pos = -10e9

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y < x: # 위치의 통일감을 위해 작은 죄표 ~ 큰 좌표로 정렬 후 append
        tmp = x
        x = y
        y = tmp
    if min_pos > x:
        min_pos = x
    if max_pos < y:
        max_pos = y
    ranges.append((x, y))

d = int(input())

start_position = min_pos
end_position = start_position + d

