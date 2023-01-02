import heapq
import sys

N = int(sys.stdin.readline())

my_heap = []

for i in range(N):
    target = int(sys.stdin.readline())
    # tuple은 첫번째 요소끼리 비교,두번째 요소끼리 비교하는 식으로 비교 진행
    elem = (abs(target),target)

    if target != 0:
        heapq.heappush(my_heap, elem)
    else:
        if len(my_heap) == 0:
            print(0)
        else:
            poped = heapq.heappop(my_heap)
            print(poped[1])
