from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])

answer = []

K = K - 1

index = 0
while index <= K:
    if len(answer) == N:
        break
    if index == K:
        popleft = queue.popleft()
        answer.append(popleft)
        index = 0
        continue
    pop_elem = queue.popleft()
    queue.append(pop_elem)
    index += 1

print('<', end='')
for i in range(len(answer) - 1):
    print(answer[i], end=', ')
print(answer[len(answer) - 1], end='')
print('>')
