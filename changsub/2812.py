N, K = map(int, input().split())

target = input()

stack = []

answer = []

length = N - K

start = 0

while length > 0:
    for i in range(start, N - length + 1):
        if not stack:
            stack.append(target[i])
            start = i + 1
        else:
            if stack[-1] < target[i]:
                stack.pop(-1)
                stack.append(target[i])
                start = i + 1
    answer.append(stack[0])
    stack.clear()
    length -= 1

for elem in answer:
    print(elem, end='')
