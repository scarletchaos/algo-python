from algo_py.decorators import timeit


class LinkedListNode:
    def __init__(self, value=None) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    @timeit
    def append(self, value) -> LinkedListNode:
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.tail = new_node
        return new_node

    @timeit
    def prepend(self, value) -> LinkedListNode:
        new_node = LinkedListNode(value)
        current = self.head
        if not self.tail:
            self.tail = new_node
        else:
            new_node.next = current
            self.head = new_node
        return new_node

    @timeit
    def find(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        return None

    @timeit
    def insert_after(self, prev_value, value):
        prev = self.find(prev_value)
        if not prev:
            return None
        new_node = LinkedListNode(value)
        # pdb.set_trace()
        new_node.next, prev.next = prev.next, new_node
        # print(new_node.value, new_node.next.value)

        # print(f'''{prev.value}->{prev.next.value}->{prev.next.next.value}''')
        return new_node

    @timeit
    def delete(self, value):
        current_node = self.head
        if not current_node:
            return False
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        while current_node.next:
            if current_node.next.value == value:
                if current_node.next == self.tail:
                    self.tail = current_node
                current_node.next = current_node.next.next
                return True
            else:
                current_node = current_node.next
        return False

    @timeit
    def __repr__(self):
        current_node = self.head
        result = []
        while current_node:
            # pdb.set_trace()
            result.append(current_node.value)
            # print(result)
            current_node = current_node.next
        return "->".join([str(item) for item in result])

    def fore(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
