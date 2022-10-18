import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.insert(0, 0)
    target = int(sys.stdin.readline())  # 만들려는 금액
    dp = [[0] * (target + 1) for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(target + 1):
            # 모든 동전은 0원을 한번 만들 수 있음
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j]
                if j - nums[i] >= 0:  # i가 1 이상일 경우
                    dp[i][j] += dp[i][j - nums[i]]
    print(dp[N][target])
