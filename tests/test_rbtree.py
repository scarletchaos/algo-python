import pytest
from algo_py.rbtree import BLACK, RED, RBTree

@pytest.fixture 
def tree():
    tree = RBTree()
    for i in [5, 2, 8, 1, 3, 6, 9]:
        tree.insert_node(10*i)
    return tree

def test_rbtree_turns(tree: RBTree): 
    assert tree.widthTraversal(tree.root) == ['b50', 'b20l', 'b80r', 'r10l', 'r30r', 'r60l', 'r90r', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'bNIL']
    tree.insert_node(11)
    assert tree.widthTraversal(tree.root) == ['b50', 'r20l', 'b80r', 'b10l', 'b30r', 'r60l', 'r90r', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'bNIL', 'r11r', 'bNIL', 'bNIL']
