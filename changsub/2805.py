N, M = map(int, input().split())
heights = list(map(int, input().split()))

start = 1
max_blade = max(heights)
cutting_point = (start + max_blade) // 2
max_height = 0

while start <= max_blade:
    namu = 0

    cutting_point = (start + max_blade) // 2

    for height in heights:
        if height > cutting_point:
            namu += (height - cutting_point)

    if namu == M:
        max_height = cutting_point
        break
    elif namu > M:  # 너무 많이 자름, 커팅 포인트를 증가 시켜야함
        start = cutting_point + 1
        max_height = cutting_point
    elif namu < M:
        max_blade = cutting_point - 1

print(max_height)
