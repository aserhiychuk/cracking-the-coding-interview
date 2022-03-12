class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self._head = None

    def append(self, value):
        node = Node(value)

        if self._head is None:
            self._head = node
        else:
            cur = self._head

            while cur.next:
                cur = cur.next

            cur.next = node

    def __iter__(self):
        cur = self._head

        while cur:
            yield cur.value

            cur = cur.next

    def __len__(self):
        cur = self._head
        size = 0

        while cur:
            size += 1
            cur = cur.next

        return size

    def __repr__(self):
        values = []
        cur = self._head

        while cur:
            values.append(cur.__repr__())
            cur = cur.next

        return ' -> '.join(values)


def from_iter(iterator):
    linked_list = LinkedList()

    for v in iterator:
        linked_list.append(v)

    return linked_list
