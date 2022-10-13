N = int(input())

memoization = [0] * (N + 1)

memoization[0] = 0
memoization[1] = 1

for i in range(2, N + 1):
    memoization[i] = memoization[i - 1] + memoization[i - 2]

print(memoization[N])
