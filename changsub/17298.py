import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

answers = [0] * N
my_stack = [0]
for i in range(1, N):
    while len(my_stack) != 0 and num_list[i] > num_list[my_stack[len(my_stack) - 1]]:
        stk_index = my_stack.pop()
        answers[stk_index] = num_list[i]
    my_stack.append(i)

while len(my_stack) != 0:
    stk_index = my_stack.pop()
    answers[stk_index] = -1

for a in answers:
    print(a, end=' ')
