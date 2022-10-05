import heapq
import sys
input = sys.stdin.readline

n = int(input())    # 철로 개수
roads = [list(map(int, input().split())) for _ in range(n)]    # 철로 리스트
d = int(input())    # 이동가능한 거리 d
roadList = []   # 정렬 및 예외 처리 후 가공한 철로 리스트
for road in roads:  # 철로 리스트 탐색
    home, office = road  # road : (home , ofiice)
    # home과 office의 차이가 이동가능한 거리일때 정렬해서 넣어줌(튜플의 순서가 다른게 있음)
    if abs(home - office) <= d:
        road = sorted(road)
        roadList.append(road)
# 람다식으로 두번째 value도 오름차순 정렬
roadList.sort(key=lambda x: x[1])
res = 0  # 결과값 설정
heap = []   # 우선 순위 큐 설정
for road in roadList:   # 철로 리스트 탐색

    if not heap:    # 힙이 비었을때 넣어줌.
        heapq.heappush(heap, road)
    else:   # 힙이 존재할때
        # 현재 철로가 힙에서 첫번째 출발지점에서 갈수 없는 지점일때 첫번쨰 출발지점 변경해줘야함.
        while heap[0][0] + d < road[1]:
            heapq.heappop(heap)
            if not heap:    # 예외처리1 힙이 비었을 경우 break
                break
        heapq.heappush(heap, road)  # 현재 철로 넣어주기
    res = max(res, len(heap))   # 결과값 업데이트
# 결과값 출력
print(res)