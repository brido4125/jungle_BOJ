N = int(input())

nums = list(map(int, input().split()))


def get_target(nums):
    sum = 0
    for i in range(N - 1):
        sum += abs(nums[i] - nums[i + 1])
    return sum


temps = [0] * N
check = [False] * N

max = 0


def set_seq(L):
    if L == N:
        global max
        target = get_target(temps)
        if max < target:
            max = target
        return
    else:
        for i in range(0, N):
            if not check[i]:
                check[i] = True
                temps[L] = nums[i]
                set_seq(L + 1)
                check[i] = False


set_seq(0)
print(max)
