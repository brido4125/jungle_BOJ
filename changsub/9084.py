import sys

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.insert(0, 0)
    target = int(sys.stdin.readline())

    dp = [[0] * (target + 1) for _ in range(N + 1)]
    # 모든 몽전으로 만들 수 있는 0의 개수, 즉 동전을 한개도 쓰지 않고 0을 만드는 방법 하나 존재
    for i in range(N+1):
        dp[i][0] = 1

    # N은 주어진 동전의 숫자
    # M은 주어진 구해야하는 값
    for j in range(1,N+1):
        for k in range(1,target+1):# k는 만들수 있는 돈의 가짓수
            dp[j][k] = dp[j-1][k]
            if k >= nums[j]: # 현재 차례인 동전 nums[j]의 크기가 만들려는 금액 k보다 작아야 해당 금액을 만들 수 있음, 예를 들어 3원을 만들려면 4원짜리로는 만들지 못함
                dp[j][k] += dp[j][k - nums[j]]

    print(dp[N][target])





