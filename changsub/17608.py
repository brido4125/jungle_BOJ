import sys

N = int(input())

stack = []

for _ in range(N):
    target = int(sys.stdin.readline())
    if len(stack) == 0:
        stack.append(target)
    else:
        # pop하고 나서 더 비교 해야함
        while stack[-1] <= target:
            stack.pop(-1)
            if len(stack) == 0:
                break
        stack.append(target)

print(len(stack))