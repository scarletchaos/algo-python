from algo_py.tree import BinaryTree
import pytest

@pytest.fixture
def tree():
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
    return tree

def test_tree(tree):
    assert tree.root.value == 0
    assert tree.root.left.value == -2
    assert tree.root.right.value == 2

#def test_tree_repr(tree):
#    assert tree.reprHelper(tree.root) == [0, [-2, [-3], [-1]], [2, [1], [3, ['_'], [4, ['_'], [5, ['_'], [6]]]]]]
#    tree.deleteNode(0)
#    assert tree.reprHelper(tree.root) == [1, [-2, [-3], [-1]], [2, ['_'], [3, ['_'], [4, ['_'], [5, ['_'], [6]]]]]]
#    tree.deleteNode(6)
#    assert tree.reprHelper(tree.root) == [1, [-2, [-3], [-1]], [2, ['_'], [3, ['_'], [4, ['_'], [5]]]]]
#    tree.deleteNode(4)
#    assert tree.reprHelper(tree.root) == [1, [-2, [-3], [-1]], [2, ['_'], [3, ['_'], [5]]]]

def test_tree_traversal(tree):
    assert tree.depthTraversal(tree.root, "c") == [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    assert tree.depthTraversal(tree.root, "r") == [-3, -1, -2, 1, 6, 5, 4, 3, 2, 0]
    assert tree.depthTraversal(tree.root, "s") == [0, -2, -3, -1, 2, 1, 3, 4, 5, 6]

def test_tree_width_traversal(tree):
    assert tree.widthTraversal(tree.root) == [0, -2, 2, -3, -1, 1, 3, 4, 5, 6]
