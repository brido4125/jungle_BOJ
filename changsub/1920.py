import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
nums = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))


# 시간 초과 로직
# for elem in targets:
#     if elem in nums:
#         print(1)
#     else:
#         print(0)


# Binary Search 이용

def binarySearch(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, end)


nums.sort()
for elem in targets:
    if binarySearch(nums, elem, 0, len(nums) - 1):
        print(1)
    else:
        print(0)
