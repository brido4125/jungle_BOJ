N = int(input())

if (1 <= N <= 100):
    for i in range(N):
        for j in range(i+1):
            print("*", end="")
        print('')
