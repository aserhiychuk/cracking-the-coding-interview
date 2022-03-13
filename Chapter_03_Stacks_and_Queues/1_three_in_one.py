import unittest


class MultiStack:
    '''
    3.1 Three in One: Describe how you could use a single array to implement three stacks
    '''
    def __init__(self, n_stacks=3, init_size=4):
        self._stack = [None] * (n_stacks * init_size)
        self._sizes = [0] * n_stacks
        self._n_stacks = n_stacks

    def push(self, stack_no, value):
        if max(self._sizes) * self._n_stacks == len(self._stack):
            self._resize()

        size = self._sizes[stack_no]
        self._stack[size * self._n_stacks + stack_no] = value
        self._sizes[stack_no] = size + 1

    def pop(self, stack_no):
        size = self._sizes[stack_no]
        result = self._stack[(size - 1) * self._n_stacks + stack_no]
        self._stack[(size - 1) * self._n_stacks + stack_no] = None
        self._sizes[stack_no] = size - 1

        return result

    def _resize(self):
        resized_stack = [None] * (len(self._stack) * 2)
        resized_stack[0:len(self._stack)] = self._stack
        self._stack = resized_stack



class MultiStackTest(unittest.TestCase):
    def test_multi_stack(self):
        stack = MultiStack()
        stack.push(0, 'a1')
        stack.push(0, 'a2')
        stack.push(0, 'a3')
        stack.push(0, 'a4')
        self.assertEqual(12, len(stack._stack))
        stack.push(0, 'a5')
        self.assertEqual(24, len(stack._stack))
        stack.push(1, 'b1')
        stack.push(1, 'b2')

        self.assertListEqual([5, 2, 0], stack._sizes)

        self.assertEqual('a5', stack.pop(0))
        self.assertEqual('b2', stack.pop(1))

        self.assertListEqual([4, 1, 0], stack._sizes)


if __name__ == '__main__':
    unittest.main()
