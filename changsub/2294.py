import sys

N, target = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

sum = 0

