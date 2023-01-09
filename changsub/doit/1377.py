import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))

sorted_arr = sorted(arr)#tuple의 첫번째 요소 기준으로 정렬됨
answer = []

for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)
