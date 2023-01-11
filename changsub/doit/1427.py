N = input()

num_length = len(N)

num_ary = []

for i in range(num_length):
    num_ary.append(N[i])

num_ary.sort(reverse=True)

for i in range(num_length):
    print(num_ary[i], end='')
