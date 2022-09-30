# N - 1개의 원판은 처음 1 -> 3 -> 2로 옮겨졌다가, 2 -> 1 -> 3으로 최종적으로 옮겨진다.
def hanoi(num, start, to, end):
    if num == 1:
        print(start, end)
    else:
        hanoi(num - 1, start, end, to)
        print(start, end)  # 가장 큰 원판이 1 -> 3으로 옮겨진 것을 출력
        hanoi(num - 1, to, start, end)


N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 2, 3)
