import sys

N = int(sys.stdin.readline())

nums = list(input()) # char 단위로 나

sum = 0

for elem in nums:
    sum += int(elem)

print(sum)
