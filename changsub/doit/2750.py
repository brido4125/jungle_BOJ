import sys

N = int(input())

num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline()))

for i in range(N-1):
    for j in range(N - 1 - i):
        if num_list[j] > num_list[j+1]:
            tmp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = tmp


for e in num_list:
    print(e)
