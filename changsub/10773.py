K = int(input())

nums = []

for _ in range(K):
    target = int(input())
    if target == 0:
        nums.pop(-1)
    else:
        nums.append(target)


print(sum(nums))
