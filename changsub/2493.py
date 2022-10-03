N = int(input())

heights = list(map(int, input().split()))

stack = []
answer = [0] * N

for i in range(len(heights)):
    if not stack:
        stack.append(i)
    else:
        if heights[stack[-1]] < heights[i]:
            while heights[stack[-1]] < heights[i]:
                stack.pop(-1)
                if not stack:
                    break
            if not stack:
                answer[i] = 0
            else:
                answer[i] = stack[-1] + 1
            stack.append(i)
        elif heights[stack[-1]] > heights[i]:
            answer[i] = stack[-1] + 1
            stack.append(i)

for elem in answer:
    print(elem, end=' ')
