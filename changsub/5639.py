import sys

sys.setrecursionlimit(20_000)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)

        else:
            current = self.root  # 루트 노드로부터 시작
            while True:
                if current.data > data:  # 삽입 되려는 노드의 데이터가 루트보다 작으면
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                if current.data < data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right

    # 후위 순회
    def postorder(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        print(node.data)



tree = Tree()
while True:
    try:
        tree.add(int(sys.stdin.readline()))
    except:
        break

tree.postorder()

