from stack import Stack
import unittest


class MinStack:
    '''
    3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
    which returns the minimum element? Push, pop and min should all operate in 0(1) time.
    '''
    def __init__(self):
        self._stack = Stack()
        self._mins = Stack()

    def push(self, value):
        self._stack.push(value)

        if not self._mins or value <= self._mins.peek():
            self._mins.push(value)

    def pop(self):
        result = self._stack.pop()

        if result == self._mins.peek():
            self._mins.pop()

        return result

    def min(self):
        if not self._mins:
            return None

        return self._mins.peek()


class MinStackTest(unittest.TestCase):
    def test_min_stack(self):
        stack = MinStack()
        # []
        # []
        stack.push(5)
        # [5]
        # [5]
        self.assertEqual(5, stack.min())
        stack.push(7)
        # [5, 7]
        # [5]
        self.assertEqual(5, stack.min())
        stack.push(3)
        # [5, 7, 3]
        # [5, 3]
        self.assertEqual(3, stack.min())
        stack.push(10)
        # [5, 7, 3, 10]
        # [5, 3]
        self.assertEqual(3, stack.min())
        stack.push(3)
        # [5, 7, 3, 10, 3]
        # [5, 3, 3]
        self.assertEqual(3, stack.min())

        stack.pop()
        # [5, 7, 3, 10]
        # [5, 3]
        self.assertEqual(3, stack.min())
        stack.pop()
        # [5, 7, 3]
        # [5, 3]
        self.assertEqual(3, stack.min())
        stack.pop()
        # [5, 7]
        # [5]
        self.assertEqual(5, stack.min())
        stack.pop()
        # [5]
        # [5]
        self.assertEqual(5, stack.min())
        stack.pop()
        # []
        # []
        self.assertIsNone(stack.min())


if __name__ == '__main__':
    unittest.main()
