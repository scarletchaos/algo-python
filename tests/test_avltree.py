from algo_py.avltree import AVLTree
import pytest


@pytest.fixture
def tree():
    tree = AVLTree()
    tree.insert_node(0)
    tree.insert_node(1)
    return tree

@pytest.fixture
def deltree():
    tree = AVLTree()
    tree.insert_node(1)
    tree.insert_node(0)
    tree.insert_node(2)
    tree.insert_node(3)
    return tree

def test_avltree_lrot(tree):
    assert tree.root.value == 0
    assert tree.root.right.value == 1
    tree.insert_node(2)
    assert tree.root.right.value == 2
    assert tree.root.value == 1
    assert tree.root.left.value == 0
    for i in range(3, 8):
        tree.insert_node(i)

    assert tree.root.value == 3
    assert tree.root.left.value == 1
    assert tree.root.right.value == 5
    assert tree.root.right.left.value == 4
    assert tree.root.right.right.value == 6
    assert tree.root.left.left.value == 0
    assert tree.root.left.right.value == 2
    assert tree.root.right.right.right.value == 7

def test_avltree_rrot():
    tree = AVLTree()
    tree.insert_node(9)
    tree.insert_node(8)
    tree.insert_node(7)
    assert tree.widthTraversal(tree.root) == [8, 7, 9]

    tree.insert_node(6)
    tree.insert_node(5)
    assert tree.widthTraversal(tree.root) == [8, 6, 9, 5, 7]


def test_avltree_deletion(deltree: AVLTree):
    assert deltree.widthTraversal(deltree.root) == [1, 0, 2, 3]
    deltree.delete_node(0)
    assert deltree.widthTraversal(deltree.root) == [2, 1, 3]

