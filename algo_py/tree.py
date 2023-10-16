from typing import Optional
from .decorators import timeit
from .q import Queue


class BinaryTreeNode:
    def __init__(self, parent=None, value=None) -> None:
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value

    def is_leaf(self):
        return not (self.left or self.right)


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    @timeit
    def findNode(self, value):
        currentNode = self
        while currentNode:
            if currentNode.value == value:
                return currentNode
            currentNode = (
                currentNode.left if currentNode.value > value else currentNode.right
            )
        return None

    @timeit
    def insertNode(self, value):
        if self.root:
            self._insertNode(value, self.root)
        else:
            self.root = BinaryTreeNode(value=value)

    def _insertNode(self, value, parent):
        if value > parent.value:
            if parent.right:
                self._insertNode(value, parent.right)
            else:
                parent.right = BinaryTreeNode(parent=parent, value=value)
        else:
            if parent.left:
                self._insertNode(value, parent.left)
            else:
                parent.left = BinaryTreeNode(parent=parent, value=value)

    @timeit
    def deleteNode(self, value):
        self.root = self._deleteNode(value, self.root)

    def _deleteNode(self, value, node):
        if node == None:
            raise Exception("Node with given value doesn't exist!")

        if value > node.value:
            node.right = self._deleteNode(value, node.right)
        elif value < node.value:
            node.left = self._deleteNode(value, node.left)
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

        return node

    def depthTraversal(
        self, node, type: str = "s", result: Optional[list] = None
    ) -> list:
        if not result:
            result = []
        if type == "s" and node:
            result.append(node.value)
        if node.left:
            result = self.depthTraversal(node.left, type, result)
        if type == "c" and node:
            result.append(node.value)
        if node.right:
            result = self.depthTraversal(node.right, type, result)
        if type == "r" and node:
            result.append(node.value)
        return result

    def widthTraversal(self, node) -> list:
        q = Queue()
        result = []
        q.push(node)
        while not q.isEmpty():
            curr = q.pop()
            if not curr:
                raise Exception("???")
            result.append(curr.value)
            if curr.left:
                q.push(curr.left)
            if curr.right:
                q.push(curr.right)
        return result

    def reprHelper(self, head) -> list:
        result = [head.value]
        if head.left and not head.right:
            result.append(self.reprHelper(head.left))
            result.append(["_"])

        if head.right and not head.left:
            result.append(["_"])
            result.append(self.reprHelper(head.right))

        if head.left and head.right:
            result.append(self.reprHelper(head.left))
            result.append(self.reprHelper(head.right))

        return result


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insertNode(0)
    tree.insertNode(-2)
    tree.insertNode(-3)
    tree.insertNode(-1)
    tree.insertNode(2)
    tree.insertNode(1)
    tree.insertNode(3)
    tree.insertNode(4)
    tree.insertNode(5)
    tree.insertNode(6)
    print(tree.depthTraversal(tree.root, "r"))
    print(tree.widthTraversal(tree.root))
