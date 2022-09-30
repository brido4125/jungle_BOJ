from __future__ import annotations
from typing import Any, Type


class Node:
    def __init__(self,
                 key: Any,
                 value: Any,
                 left: Node = None,
                 right: Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key: Any) -> Any:

        currentNode = self.root
        while True:
            if currentNode is None:
                return None
            if key == currentNode.key:
                return currentNode.value
            elif key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

    def add(self, key: Any, value: Any) -> bool:

        def add_node(node: Node, key: Any, value: Any) -> bool:
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right in None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)

            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)



    def remove(self):
        p = self.root
        parent = None
        is_left_child = True
