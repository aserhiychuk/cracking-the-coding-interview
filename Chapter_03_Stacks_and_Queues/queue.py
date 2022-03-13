class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, value):
        node = Node(value)

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def dequeue(self):
        if self._head is None:
            return None

        value = self._head.value

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next

        return value

    def peek(self):
        if self._head is None:
            return None

        return self._head.value
