import heapq
import sys

min_heap = []
max_heap = []

N = int(input())

nums = []
answers = []
for _ in range(N):
    nums = int(sys.stdin.readline())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -nums)
    else:
        heapq.heappush(min_heap,nums)
    if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0] * -1 > min_heap[0]:
        max_value = heapq.heappop(max_heap) * -1
        min_value = heapq.heappop(min_heap)

        heapq.heappush(max_heap,min_value*-1)
        heapq.heappush(min_heap,max_value)

    print(max_heap[0] * -1)


