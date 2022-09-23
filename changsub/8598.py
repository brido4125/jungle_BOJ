N = int(input())
for _ in range(N):
    target = input()
    count = 0
    score = 0
    priv = target[0]
    if priv == 'O':
        score += 1
        count += 1

    for i in range(1, len(target)):
        if priv == 'O' and target[i] == 'O':
            count += 1
            score += count
        elif priv == 'X' and target[i] == 'O':
            count = 1
            score += count
        priv = target[i]

    print(score)