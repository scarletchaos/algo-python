from algo_py.stack import Stack
import pytest


def test_stack():
    stack = Stack()

    stack.push("one")
    stack.push("two")

    assert stack.pop() == "two"
    assert stack.pop() == "one"


def test_empty():
    stack = Stack()
    assert stack.isEmpty()

    stack.push("one")
    assert not stack.isEmpty()

    stack.pop()
    assert stack.isEmpty()

