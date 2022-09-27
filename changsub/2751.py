import sys

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))


def merge(arr, tmp, start, mid, end):
    for i in range(start, end + 1):
        tmp[i] = arr[i]
    part1 = start
    part2 = mid + 1
    index = start
    while part1 <= mid and part2 <= end:
        if tmp[part1] <= tmp[part2]:
            arr[index] = tmp[part1]
            part1 += 1
        else:
            arr[index] = tmp[part2]
            part2 += 1
        index += 1

    for i in range(0, mid - part1 + 1):
        arr[index + i] = tmp[part1 + i]


def _mergeSort(arr, tmp, start, end):
    if start < end:
        mid = (start + end) // 2
        _mergeSort(arr, tmp, start, mid)
        _mergeSort(arr, tmp, mid + 1, end)
        merge(arr, tmp, start, mid, end)


def mergeSort(arr):
    tmp = [0] * len(nums)  # 들어온 배열의 크기만큼 임시 저장 공간
    _mergeSort(arr, tmp, 0, len(arr) - 1)  # 정렬할 타겟 배열, 임시 배열, 시작점, 끝점을 인자로 넘겨주는 함수


mergeSort(nums)
for elem in nums:
    print(elem)