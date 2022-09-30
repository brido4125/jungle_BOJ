import sys
from bisect import bisect_right
N, C = map(int, sys.stdin.readline().split())

houses = [ int(sys.stdin.readline()) for _ in range(N)]

houses.sort()
lo = 1
hi = houses[N-1] - houses[0] + 1
location = houses[0]
max_distance = 1
router = 1
while lo < hi:
    mid = (hi + lo) // 2
    current = houses[0]
    while current < houses[N-1]:
        current += mid
        if current in houses:
            router += 1
        else:
            if current <= houses[N-1]:
                current = houses[bisect_right(houses,current)]
                router += 1
            else: break
    if router >= C :
        max_distance = max(max_distance, mid)
        lo = mid + 1
    else:
        hi = mid