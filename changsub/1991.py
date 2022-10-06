import sys


class Node:
    def __init__(self, data, lt, rt):
        self.data = data
        self.lt = lt
        self.rt = rt


# 전위 순회
def preorder(node):
    print(node.data, end='')
    if node.lt != '.':
        preorder(tree[node.lt])
    if node.rt != '.':
        preorder(tree[node.rt])


# 후위 순회
def postorder(node):
    if node.lt != '.':
        preorder(tree[node.lt])
    if node.rt != '.':
        preorder(tree[node.rt])
    print(node.data, end='')


# 중위 순회
def inorder(node):
    if node.lt != '.':
        preorder(tree[node.lt])
    print(node.data, end='')
    if node.rt != '.':
        preorder(tree[node.rt])


N = int(input())

nodes = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

tree = {}

for elem in nodes:
    tree[elem[0]] = Node(elem[0], elem[1], elem[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
