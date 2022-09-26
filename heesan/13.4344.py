N = int(input())

for i in range(N):
    score_list = list(map(int, input().split(" ")))
    avg = sum(score_list[1:]) / score_list[0]

    count = 0
    for i in score_list[1:]:
        if i > avg:
            count = count + 1

    per = (count/score_list[0]) * 100
    print('%.3f' % per + '%')




