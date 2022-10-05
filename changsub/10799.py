target = list(map(str, input()))

stack = []

answer = 0
priv = ''

for elem in target:
    if not stack:
        if elem == '(':
            answer += 1
        stack.append(elem)
        priv = elem

    else:
        if priv == '(' and elem == ')':
            stack.pop(-1)
            priv = elem
            answer -= 1
            answer += len(stack)
        elif elem == '(':
            stack.append(elem)
            priv = elem
            answer += 1
        elif elem == ')':
            stack.pop(-1)
            priv = elem

print(answer)
