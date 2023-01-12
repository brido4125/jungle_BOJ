import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
my_tuple = []
for i in range(1, len(nums) + 1):
    my_tuple.append((nums[i - 1], i))

my_tuple.sort(key=lambda x: x[0])

sum_ary = [my_tuple[0][0]]

for i in range(1,len(my_tuple)):
    sum_ary.append(sum_ary[i-1] + my_tuple[i][0])

print(sum(sum_ary))
