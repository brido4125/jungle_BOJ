M, N, L = map(int, input().split())

sadae = list(map(int, input().split()))

sadae.sort()


def findNearSadae(x):
    start = 0  # 사대 배열의 첫번째 인덱스
    end = M - 1  # 사대 배열의 마지막 인덱스
    priv = 10e9

    while start <= end:
        mid = (start + end) // 2  # 이분 검색을 위한 사대 인덱스
        if abs(x - priv) > abs(x - sadae[mid]):
            priv = sadae[mid]
        if sadae[mid] <= x:  # 현재 동물의 위치보다 사대가 작은 경우 => 더 우측에 있는 사대로 탐색
            start = mid + 1
        elif sadae[mid] > x:  # 현재 동물의 위치보다 사대가 큰 경우 => 더 좌측에 있는 사대로 탐색
            end = mid - 1

    return priv


animal_x = []
animal_y = []

for _ in range(N):
    x, y = map(int, input().split())
    animal_x.append(x)
    animal_y.append(y)

count = 0

for i in range(N):
    near_sadae = findNearSadae(animal_x[i])
    if L >= abs(near_sadae - animal_x[i]) + animal_y[i]:
        count += 1

print(count)

