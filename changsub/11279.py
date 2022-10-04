import heapq
import sys

N = int(input())

heap = []

for _ in range(N):
    target = -(int(sys.stdin.readline()))
    if target == 0:
        # 배열에서 가장 큰 값을 출력 후 삭제
        try:
            print(-(heapq.heappop(heap)))
        except IndexError:
            print(0)
    else:
        heapq.heappush(heap, target)
