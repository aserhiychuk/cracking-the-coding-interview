from stack import Stack
import unittest


class MyQueue:
    '''
    3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
    '''
    def __init__(self):
        self._stack = Stack()
        self._buffer = Stack()

    def append(self, value):
        self._stack.push(value)

    def remove(self):
        if self._stack.is_empty():
            return None

        while not self._stack.is_empty():
            v = self._stack.pop()
            self._buffer.push(v)

        result = self._buffer.pop()

        while not self._buffer.is_empty():
            v = self._buffer.pop()
            self._stack.push(v)

        return result


class MyQueueTest(unittest.TestCase):
    def test_my_queue(self):
        queue = MyQueue()

        for i in range(10):
            queue.append(i)

        actual = [queue.remove() for _ in range(10)]
        expected = list(range(10))
        self.assertListEqual(expected, actual)

        self.assertIsNone(queue.remove())


if __name__ == '__main__':
    unittest.main()
