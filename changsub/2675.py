N = int(input())

for _ in range(N):
    R, S = map(str, input().split())
    R = int(R)
    for i in range(len(S)):
        print(S[i] * R, end="")
    print()
