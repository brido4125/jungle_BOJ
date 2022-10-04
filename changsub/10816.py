import sys

N = int(input())

have = list(map(int, sys.stdin.readline().split()))

dic = {}

for elem in have:
    if elem not in dic.keys():
        dic[elem] = 1
    else:
        dic[elem] += 1

M = int(input())

counting = list(map(int, sys.stdin.readline().split()))

have.sort()


def counting_num(num):
    count = 0
    start = 0
    end = len(have) - 1
    while start <= end:
        mid = (start + end) // 2
        if have[mid] == num:
            count += 1
            return count
        elif have[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return count


answer = []

for target in counting:
    res = counting_num(target)
    if res == 1:
        answer.append(dic[target])
    else:
        answer.append(res)

for elem in answer:
    print(elem, end=' ')
