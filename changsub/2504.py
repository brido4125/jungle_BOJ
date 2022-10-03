target = input()
stack = []
value = 1
answer = 0

for i in range(len(target)):
    if target[i] == '(':
        value *= 2
        stack.append(target[i])
    elif target[i] == '[':
        value *= 3
        stack.append(target[i])
    elif target[i] == ')':
        # stack의 원소가 없는 경우 == 완전히 다른 괄호 식을 계산 하거나 or 닫는 괄호의 짝이 맞지 않으면
        if len(stack) == 0 or stack[-1] != '(':
            answer = 0
            break
        if target[i - 1] == '(':
            answer += value
        value //= 2
        stack.pop()
    elif target[i] == ']':
        if len(stack) == 0 or stack[-1] != '[':
            answer = 0
            break
        if target[i - 1] == '[':
            answer += value
        value //= 3
        stack.pop()

if stack:
    answer = 0
print(answer)

