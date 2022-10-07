N = int(input())

nums = list(map(int, input().split()))

total = sum(nums)

flag = False


def dfs(level, sum):
    global flag
    if flag:
        return
    if level == N:
        if total - sum == sum:
            flag = True
    else:
        dfs(level+1, sum + nums[level])
        dfs(level+1, sum)


dfs(0,0)
if flag:
    print("YES")
else:
    print("NO")