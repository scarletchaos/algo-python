from .doublelinkedlist import DoubleLinkedList 

class Queue:
    def __init__(self):
        self.items = DoubleLinkedList()

    def push(self, item):
        self.items.prepend(item)

    def pop(self):
        if not self.items.tail:
            return None
        res = self.items.tail.value
        self.items.delete(res)
        return res

    def isEmpty(self):
        return self.items.head is None
