N = int(input())


def get_avg(scores):
    sum = 0
    for elem in scores:
        sum += elem
    return sum // len(scores)


for _ in range(N):
    scores = list(map(int, input().split()))
    scores.remove(scores[0])
    avg = get_avg(scores)
    count = 0
    for elem in scores:
        if elem > avg:
            count += 1
    percent = count / len(scores) * 100.0
    answer = format(percent, ".3f")
    print(str(answer)+"%")
