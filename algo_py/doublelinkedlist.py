from algo_py.decorators import timeit


class DoubleLinkedListNode:
    def __init__(self, value=None) -> None:
        self.prev = None
        self.next = None
        self.value = value


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    @timeit
    def append(self, value) -> DoubleLinkedListNode:
        new_node = DoubleLinkedListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node.prev = current
            current.next = new_node

        self.tail = new_node
        return new_node

    @timeit
    def prepend(self, value):
        new_node = DoubleLinkedListNode(value)
        current = self.head
        if not self.tail or not self.head:
            self.tail = new_node
            self.head = new_node
        elif current:
            current.prev = new_node.next
            new_node.next = current
            self.head = new_node
        else:
            return None
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
        new_node = DoubleLinkedListNode(value)
        # pdb.set_trace()
        new_node.next, prev.next = prev.next, new_node
        new_node.prev = prev
        if new_node.next:
            new_node.next.prev = new_node
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
