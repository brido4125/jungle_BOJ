import sys

T = int(input())


def find_parent(parent, target):
    if parent[target] != target:
        parent[target] = find_parent(parent, parent[target])
    return parent[target]


# index가 작은게 기준으로
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    edges = []
    parent = [i for i in range(0,N+1)]
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        edges.append((start, end))

    count = 0

    for edge in edges:
        start, end = edge
        # start와 end는 이어져 있는 node => parent 배열에서 둘의 값을 동일하게 만들어 이어져 있음을 표혀
        if find_parent(parent, start) != find_parent(parent, end):
            union_parent(parent, start, end)
            count += 1

    print(count)
