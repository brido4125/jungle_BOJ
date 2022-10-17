import sys

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    scores = []
    for _ in range(N):
        resume, interview = map(int, sys.stdin.readline().split())
        scores.append((resume, interview))
    scores.sort()
    answer = 1
    min = scores[0][1]
    for i in range(1, N):
        x, y = scores[i]
        # 서류 기준 1등 보다 면접 등수가 작으면 합격 가능(서류 등수는 크지만, 면접은 작기 때문에)
        if y < min:
            min = y
            answer += 1

    print(answer)
