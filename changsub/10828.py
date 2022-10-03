import sys

N = int(input())

my_stack = []

for _ in range(N):
    inst = sys.stdin.readline().split()
    if inst[0] == 'push':
        my_stack.append(int(inst[1]))
    elif inst[0] == 'pop':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack.pop())
    elif inst[0] == 'size':
        print(len(my_stack))
    elif inst[0] == 'empty':
        if len(my_stack) == 0:
            print(1)
        else:
            print(0)
    elif inst[0] == 'top':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack[-1])
