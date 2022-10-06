import sys

V, E = map(int, input().split())


def findParent(ary, x):
    if ary[x] != x:
        ary[x] = findParent(ary, ary[x])
    return ary[x]


def unionParent(ary, a, b):
    a = findParent(ary, a)
    b = findParent(ary, b)
    if a < b:
        ary[b] = a
    else:
        ary[a] = b

# index값과 배열의 요소의 값이 동일하게 선언
parent_ary = [i for i in range(V + 1)]

edges = []
res = 0

for i in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, start, end))  # tuple은 처음 원소 기준으로 정렬 가능

edges.sort()

for edge in edges:
    cost, start, end = edge
    # 같으면 이미 포함 엣지로 연결이 되었기 떼문에 비용을 더할 필요가 없음
    if findParent(parent_ary, start) != findParent(parent_ary, end):
        unionParent(parent_ary, start, end)
        res += cost

print(res)
