from algo_py.doublelinkedlist import DoubleLinkedList
import pytest

@pytest.fixture
def dll():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.prepend(0)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    return dll

def test_dll(dll:DoubleLinkedList):
    assert dll.__repr__() == '0->1->2->3->4'
    assert dll.head.value == 0
    assert dll.tail.value == 4

def test_dll_delete(dll:DoubleLinkedList):
    assert dll.delete(4) == True
    assert dll.__repr__() == '0->1->2->3'
    assert dll.delete(0) == True
    assert dll.__repr__() == '1->2->3'

