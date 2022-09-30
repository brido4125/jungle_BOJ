import sys


def installPossible(distance):
    # 가장 첫번째 집은 무조건 설치한다고 가정
    cnt = 1
    privRouterPosition = house_position[0]

    for elem in house_position:
        if elem - privRouterPosition >= distance:
            cnt += 1
            privRouterPosition = elem

    return cnt


N, C = map(int, input().split())

house_position = []

for _ in range(N):
    house_position.append(int(sys.stdin.readline()))

house_position.sort()

start = 1
end = house_position[-1] - house_position[0] + 1

answer = 0

while start <= end:

    mid = (start + end) // 2

    possible_count = installPossible(mid)

    # 해당 거리만큼 띄워서 설치 가능한 갯수가 부족하면 조건 만족
    # 띄우는 거리를 줄여야함
    if possible_count < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)


