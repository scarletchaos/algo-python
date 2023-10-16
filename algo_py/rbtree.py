from algo_py.decorators import timeit
from algo_py.q import Queue
import pdb


RED = True
BLACK = False


class RBTreeNode:
    def __init__(self, value, color=RED) -> None:
        self.value = value
        self.left: "RBTreeNode" | None = None
        self.right: "RBTreeNode" | None = None
        self.color = color
        self.p: "RBTreeNode" | None = None

    def isLeft(self):
        return (self.p.left is self) if self.p else False

    def isRight(self):
        return (self.p.right is self) if self.p else False

    def __repr__(self) -> str:
        return f"{'r' if self.color else 'b'}{str(self.value) if self.value != None else 'NIL'}{('r' if self.p.right == self else 'l') if self.p and self != NIL else ''}"


NIL = RBTreeNode(None, BLACK)


class RBTree:
    def __init__(self) -> None:
        self.root = NIL

    def widthTraversal(self, node) -> list:
        q = Queue()
        result = []
        q.push(node)
        while not q.isEmpty():
            curr = q.pop()
            if not curr:
                raise Exception("???")
            result.append(curr.__repr__())
            if curr.left:
                q.push(curr.left)
            if curr.right:
                q.push(curr.right)
        return result

    def right_rotate(self, node: RBTreeNode) -> None:
        if not (node and node.left):
            raise
        Y = node.left
        B = Y.right
        Y.p = node.p
        node.left = B
        B.p = node
        if node.p:
            if node.isLeft():
                node.p.left = Y
            elif node.isRight():
                node.p.right = Y
        else:
            self.root = Y
        node.p = Y
        Y.right = node

    def left_rotate(self, node: RBTreeNode) -> None:
        if not (node and node.right):
            raise
        Y = node.right
        B = Y.left
        Y.p = node.p
        node.right = B
        B.p = node
        if node.p:
            if node.isLeft():
                node.p.left = Y
            elif node.isRight():
                node.p.right = Y
        else:
            self.root = Y
        node.p = Y
        Y.left = node

    def insert_node(self, value):
        new_node = RBTreeNode(value)
        new_node.left = NIL
        new_node.right = NIL

        curr = self.root
        parent = None
        while curr is not NIL:
            parent = curr
            if value == curr.value:
                raise Exception("Values in search tree must be unique!")
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        if not parent:
            self.root = new_node
        else:
            new_node.p = parent
            if new_node.value > parent.value:
                parent.right = new_node
            if new_node.value < parent.value:
                parent.left = new_node
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.p and node.p.color == RED:
            if not node.p.p:
                raise Exception(
                    "The tree doesn't seem to have been valid on previous step"
                )
            uncle = node.p.p.right if node.p.isLeft() else node.p.p.left

            if uncle.color == RED:
                node.p.color, uncle.color = BLACK, BLACK
                node.p.p.color = RED
                node = node.p.p
            else:
                if node.isRight() and node.p.isLeft():
                    self.left_rotate(node.p)
                elif node.isLeft() and node.p.isRight():
                    self.right_rotate(node.p)
                if node.isLeft() and node.p.isLeft():
                    self.right_rotate(node.p.p)
                    node.p.color = BLACK
                    node.p.right.color = RED
                elif node.isRight() and node.p.isRight():
                    self.left_rotate(node.p.p)
                    node.p.color = BLACK
                    node.p.left.color = RED

        self.root.color = BLACK

    def delete_node(self, value):
        curr = tree.root
        if not curr:
            raise Exception("Delete attempted from empty tree")
        while curr.value != value:
            if value > curr.value:
                curr = curr.right
            else:
                curr = curr.left

        if not curr:
            raise


        if not curr.left and not curr.right:
            if self.root == curr:
                self.root = None
                return
            if curr.color == RED:
                if curr.isLeft():
                    curr.p.left = NIL
                else:
                    curr.p.right = NIL
            else: # curr.color == BLACK
                pass

        else: # only curr.color == BLACK, due to equality of black heights and the fact that there can't be red -> red
            if curr.left and curr.right: # if curr has 2 children then swap it with biggest in its left subtree
                tmp = curr.left
            while tmp.right != NIL:
                tmp = tmp.right
            tmp.value, curr.value = curr.value, tmp.value
            curr = tmp

            if not curr.left:
                curr.value = curr.right.value
                curr.right = NIL
            else:
                curr.value = curr.left.value
                curr.right = NIL

            



if __name__ == "__main__":
    tree = RBTree()
    for i in [5, 2, 8, 1, 3, 6, 9]:
        tree.insert_node(10*i)
    print(tree.widthTraversal(tree.root))
    tree.insert_node(11)
    print(tree.widthTraversal(tree.root))
