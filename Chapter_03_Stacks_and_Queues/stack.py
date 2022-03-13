class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Stack:
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size

    def push(self, value):
        node = Node(value)
        node.next = self._head
        self._head = node
        self._size += 1

    def peek(self):
        if self._head is None:
            return None

        return self._head.value

    def pop(self):
        if self._head is None:
            return None

        result = self._head.value
        self._head = self._head.next
        self._size -= 1

        return result
