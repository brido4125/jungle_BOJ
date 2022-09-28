import sys

N = int(input())
k = int(input())

card_list = []
for i in range(N):
    card_list.append(int(sys.stdin.readline()))

check = [False] * N
permutations = [0] * k
answers = []


def operate(a):
    if a == k:
        target = "" 
        for j in permutations:
            target = target + str(j)
        answers.append(target)
        return

    for i in range(0, len(card_list)):
        if not check[i]:
            check[i] = True
            permutations[a] = card_list[i]
            operate(a+1)
            check[i] = False

operate(0)

print(len(set(answers)))
