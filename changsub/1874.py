import sys

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

curr = 1

answer = []
stack = []
flag = True
pop_index = 0

for elem in num_list:
    while curr <= elem:
        stack.append(curr)
        curr += 1
        answer.append('+')

    if stack.pop() != num_list[pop_index]:
        flag = False
        break
    pop_index += 1
    answer.append('-')

if flag:
    for a in answer:
        print(a)
else:
    print("NO")

