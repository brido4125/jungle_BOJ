import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

M = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))


def binary_search(num):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if num < num_list[mid]:
            end = mid - 1
        elif num > num_list[mid]:
            start = mid + 1
        else:
            return True
    return False


answer = []

for target in target_list:
    if binary_search(target):
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a)
