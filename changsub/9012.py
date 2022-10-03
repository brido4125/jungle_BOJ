N = int(input())

for _ in range(N):
    stack = []
    for target in input():
        if target == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(target)
        else:
            stack.append(target)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')