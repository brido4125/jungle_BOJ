import sys

N = int(sys.stdin.readline())

adj_list = []

for i in range(N):
    adj_list.append(list(map(int, sys.stdin.readline().split())))

print(adj_list)
