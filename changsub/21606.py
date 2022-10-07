import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
pos = list(map(int, input()))

pos.insert(0, 'N')
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0
inner_place = 0

# 실외 노드를 기준으로 인접 노드가 실내인 경우 inner_place 1 증가
# 하나의 외부 노드 기준 산책 경로의 개수 = (인접 실내 노드의 개수) * (인접 실내 노드의 개수 - 1)
# 예를 들어 인접 노드의 개수가 4인 경우, (4개의 노드 중 하나 선택 하는 경우의 수) * (선택된 노드 제외한 나머지 노드중 하나 선택하는 경우의 수)
def dfs(startIndex):
    global count, inner_place
    visited[startIndex] = True
    for vertex in adj_list[startIndex]:
        if pos[vertex] == 1:
            inner_place += 1
        elif not visited[vertex] and pos[vertex] == 0:
            dfs(vertex)


for _ in range(N - 1):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start].append(end)
    adj_list[end].append(start)
    # 실내에서 시작해서 실내로 끝나는 산책 경로 계산
    # start와 end 값이 모두 1인 경우
    if pos[start] == 1 and pos[end]:
        count += 2

for i in range(1, N + 1):
    if pos[i] == 0 and not visited[i]:
        dfs(i)
        count += inner_place * (inner_place - 1)
        inner_place = 0 # 새로운 바깥 노드로 dfs 해야하기 때문에 inner_place 0으로 초기화

print(count)
