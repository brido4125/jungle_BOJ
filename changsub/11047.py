import sys

N, K = map(int, sys.stdin.readline().split())

coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)


count = 0
for elem in coins:
    if K >= elem:
        coin_number = K // elem
        count += coin_number
        K = K - (coin_number * elem)
    if K == 0:
        break

print(count)