from typing import Optional
from algo_py.q import Queue
from algo_py.decorators import timeit
import pdb


class AVLTreeNode:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def is_leaf(self):
        return not (self.left or self.right)

    def __repr__(self) -> str:
        return str(self.value)


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def right_rotate(self, node: AVLTreeNode) -> None:
        tmp = node.left
        if tmp:
            node.left = tmp.right
            tmp.right = node
        else:
            raise Exception("Illegal rotation")
        return tmp

    def left_rotate(self, node: AVLTreeNode) -> None:
        tmp = node.right
        if tmp:
            node.right = tmp.left
            tmp.left = node
        else:
            raise Exception("Illegal rotation")
        return tmp

    def get_height(self, node: Optional[AVLTreeNode]) -> int:
        return node.height if node else 0

    def get_balance_factor(self, node: AVLTreeNode) -> int:
        return self.get_height(node.left) - self.get_height(node.right)

    # insertions
    def insert_node(self, value):
        if not self.root:
            self.root = AVLTreeNode(value)
            return

        self.root = self._insert_node(value, self.root)


    def _insert_node(self, value, node):
        if not node:
            return AVLTreeNode(value)
        if node.value == value:
            raise Exception("Values in search tree must be unique!")
        elif value > node.value:
            node.right = self._insert_node(value, node.right)
        else:
            node.left = self._insert_node(value, node.left)

        bf = self.get_balance_factor(node)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        if bf > 1:
            if not node.left:
                raise Exception("How in the world did this happen?")
            if value < node.left.value:
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        if bf < -1:
            if not (node and node.right):
                raise Exception("How in the world did this happen?")
            if value > node.right.value:
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)

                              

        return node

    # deletions
    def delete_node(self, value):
        self.root = self._delete_node(value, self.root)

    def _delete_node(self, value, node):
        if node == None:
            raise Exception("Node with given value doesn't exist!")

        if value > node.value:
            node.right = self._delete_node(value, node.right)
        elif value < node.value:
            node.left = self._delete_node(value, node.left)
        else:
            if node.is_leaf():
                return None
            elif node.left and node.right:
                tmp = node.right
                node.value = tmp.value
                while tmp.right:
                    tmp.value = tmp.right.value
                    tmp = tmp.right
                tmp.right = None

            elif node.left:
                return node.left
            else:
                return node.right
        
        bf = self.get_balance_factor(node)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        if bf > 1:
            if not node.left:
                raise Exception("How in the world did this happen?")
            if self.get_balance_factor(node.left) >= 0:
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        if bf < -1:
            if not (node and node.right):
                raise Exception("How in the world did this happen?")
            if self.get_balance_factor(node.right) <= 0:
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
            
        return node


    def widthTraversal(self, node) -> list:
        q = Queue()
        result = []
        q.push(node)
        while not q.isEmpty():
            curr = q.pop()
            if not curr:
                raise Exception("What")
            result.append(curr.value)
            if curr.left:
                q.push(curr.left)
            if curr.right:
                q.push(curr.right)
        return result


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert_node(0)
    tree.insert_node(1)
    tree.insert_node(2)
    print(tree.root)
    tree.insert_node(3)
    tree.insert_node(4)
    tree.insert_node(5)
    tree.insert_node(6)
    tree.insert_node(7)
    print(tree.widthTraversal(tree.root))
    tree.insert_node(8)
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
    print(tree.widthTraversal(tree.root))
