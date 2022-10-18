import sys

N, K = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

using = []
answer = 0

for i in range(K):

    # 이미 해당 기기가 멀티탭에 사용중인경우
    if seq[i] in using:
        continue
    # 멀티탭에 공간이 있는경우
    elif len(using) != N:
        using.append(seq[i])
        continue
    tmp = 0
    far = 0
    for current in using:
        # 현재 꽂혀있는 기기가 더 이상 사용되지 않으면 뽑아도됨
        if current not in seq[i:]:
            tmp = current
            break
        # seq에서 i번째 이후로 탐색해야함, 이전에는 이미 사용된 값이 존재 할 수 있음
        elif seq[i:].index(current) > far:
            far = seq[i:].index(current)
            tmp = current
    using[using.index(tmp)] = seq[i]
    answer += 1

print(answer)
