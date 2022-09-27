def swap(arr, start, end):
    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp


def partition(arr, start, end):
    pivot = arr[(start + end) // 2]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            swap(arr, start, end)
            start += 1
            end -= 1
    return start


def _quickSort(arr, start, end):
    part2 = partition(arr, start, end)
    if start < part2 - 1:
        _quickSort(arr, start, part2 - 1)
    if part2 < end:
        _quickSort(arr, part2, end)


def quickSort(arr):
    _quickSort(arr, 0, len(arr) - 1)