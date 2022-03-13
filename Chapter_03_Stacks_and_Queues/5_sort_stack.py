import random
from stack import Stack
import unittest


def sort_stack(stack):
    '''
    3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
    You can use an additional temporary stack, but you may not copy the elements into any other data
    structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
    '''
    if not stack:
        return

    buffer = Stack()

    while not stack.is_empty():
        value = stack.pop()

        while not buffer.is_empty() and buffer.peek() > value:
            stack.push(buffer.pop())

        buffer.push(value)

        while not stack.is_empty() and stack.peek() >= buffer.peek():
            buffer.push(stack.pop())

    while not buffer.is_empty():
        stack.push(buffer.pop())


class SortStackTest(unittest.TestCase):
    def test_sort_stack(self):
        stack = Stack()

        for _ in range(10):
            stack.push(random.randint(0, 10))

        sort_stack(stack)

        while not stack.is_empty():
            value = stack.pop()

            if not stack.is_empty():
                self.assertLessEqual(value, stack.peek())


if __name__ == '__main__':
    unittest.main()
