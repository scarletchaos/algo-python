from algo_py import linkedlist


class Stack:
    def __init__(self):
        self.items = linkedlist.LinkedList()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items.tail:
            return None
        result = self.items.tail.value
        self.items.delete(result)
        return result

    def isEmpty(self):
        return self.items.head is None
