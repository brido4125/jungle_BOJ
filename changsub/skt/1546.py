import sys

N = sys.stdin.readline()

nums = list(map(int, input().split()))

max = max(nums)


def mutate(target):
    return target / max * 100


sum = 0

for elem in nums:
    if elem != nums:
        elem = mutate(elem)
    sum += elem

print(sum / int(N))
