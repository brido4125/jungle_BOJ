N, K = map(int, input().split())

target = list(input())

answer = []

count = K

for num in target:
    while answer and count > 0 and answer[-1] < num:
        del answer[-1]
        count -= 1
    answer.append(num)

#join => 리스트를 문자열로 일정하게 합쳐주는 기능 수행
print(''.join(answer[:N - K]))
