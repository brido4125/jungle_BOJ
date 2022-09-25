x = int(input())

for i in range(x):
    case = str(input())
    count = 0
    score = 0
    for j in list(case):
        if (j == "O"):
            count = count + 1
            score = score + count
        elif (j == "X"):
            count = 0
    print(score)
