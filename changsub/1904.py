import sys

N = int(input())
sys.setrecursionlimit(10 ** 9)

# 1 <= N <= 1,000,000 조건
memoization = [0] * (N + 2)

# N = 1이 들어올 경우 배열을 N + 1만큼 만들면 memoization[2] = 2에서 IndexError 발생
memoization[1] = 1
memoization[2] = 2


# Top-Down 방식
def tile(N):
    if memoization[N] == 0:
        memoization[N] = (tile(N - 1) + tile(N - 2)) % 15746
    return memoization[N]


#Bottom-Up 방식
for i in range(3, N + 1):
    memoization[i] = (memoization[i - 1] + memoization[i - 2]) % 15746

print(memoization[N])
print(tile(N))
