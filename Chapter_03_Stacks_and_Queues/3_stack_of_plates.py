from stack import Stack
import unittest


class SetOfStacks:
    '''
    3.3. Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
    Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
    and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
    should behave identically to a single stack (that is, pop() should return the same values as it would
    if there were just a single stack).

    FOLLOW UP
    Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
    '''
    def __init__(self, capacity=3):
        self._stacks = []
        self._capacity = capacity

    def push(self, value):
        if not self._stacks or len(self._stacks[-1]) >= self._capacity:
            stack = Stack()
            self._stacks.append(stack)

        stack = self._stacks[-1]
        stack.push(value)

    def pop(self):
        if not self._stacks:
            return None

        stack = self._stacks[-1]
        result = stack.pop()

        if stack.is_empty():
            self._stacks.pop()

        return result

    def pop_at(self, i):
        if i >= len(self._stacks):
            return None

        stack = self._stacks[i]
        result = stack.pop()

        if stack.is_empty():
            del self._stacks[i]

        return result


class SetOfStacksTest(unittest.TestCase):
    def test_set_of_stacks(self):
        stack = SetOfStacks(3)

        for i in range(10):
            stack.push(i)

        actual = [self._to_list(stack) for stack in stack._stacks]
        self.assertListEqual([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]], actual)

        stack.pop()
        actual = [self._to_list(stack) for stack in stack._stacks]
        self.assertListEqual([[0, 1, 2], [3, 4, 5], [6, 7, 8]], actual)
        stack.pop()
        actual = [self._to_list(stack) for stack in stack._stacks]
        self.assertListEqual([[0, 1, 2], [3, 4, 5], [6, 7]], actual)

        stack.pop_at(1)
        actual = [self._to_list(stack) for stack in stack._stacks]
        self.assertListEqual([[0, 1, 2], [3, 4], [6, 7]], actual)

    def _to_list(self, stack):
        result = []

        cur = stack._head

        while cur:
            result.insert(0, cur.value)
            cur = cur.next

        return result


if __name__ == '__main__':
    unittest.main()
