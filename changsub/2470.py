N = int(input())

nums = list(map(int, input().split()))

nums.sort()


# min = 10e9

def binarySearch(self, start, end):
    first = 0
    second = 0
    priv = 10e9

    while start <= end:
        mid = (start + end) // 2
        mixed = self + nums[mid]
        if abs(priv) > abs(mixed):
            priv = mixed
            first = self
            second = nums[mid]
        if mixed < 0:
            start = mid + 1
        else:
            end = mid - 1

    return first, second


answers = []
sums = []

for i in range(N - 1):
    target = binarySearch(nums[i], i + 1, N - 1)
    answers.append(target)
    sums.append(abs(sum(target)))

print(*answers[sums.index(min(sums))])
