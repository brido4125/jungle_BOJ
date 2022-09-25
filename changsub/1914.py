N = int(input())


# group_count : 옮기려는 원판의 개수(단, 그룹별로 구성되어야 함 - 큰 원판 위에 작은 원판 조건 만족해야함)
# start_point : 옮기려는 원판 그룹의 현재 위치
# target_point : 옮기려는 원판 그룹의 목표 위치


def hanoi(group_count, start_point, target_point):
    cnt = 0
    if group_count > 1:
        hanoi(group_count - 1, start_point, 6 - start_point - target_point)
    print(f'{start_point} {target_point}')
    cnt += 1
    if group_count > 1:
        hanoi(group_count - 1, 6 - start_point - target_point, target_point)
    return cnt


print((2 ** N) - 1)

if N <= 20:
    hanoi(N, 1, 3)
