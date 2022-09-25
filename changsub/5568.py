n = int(input())
k = int(input())

# Permutation 문제 => 순열 구하는 백트래킹 문제

n_list = []
for _ in range(n):
    n_list.append(int(input()))

check = [False] * len(n_list)
permutation = [0] * k

answers = []


def selection(L):
    if L == k:
        target = ""
        for elem in permutation:
            target += str(elem)
        answers.append(target)
        return
    for i in range(0, len(n_list)):
        if not check[i]:
            check[i] = True
            permutation[L] = n_list[i]
            selection(L + 1)
            check[i] = False


selection(0)

print(len(set(answers)))
