from linked_list import *

import unittest


def kth_to_last(linked_list, k):
    '''
    2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
    '''
    size = 0

    runner = linked_list._head

    while runner:
        size += 1
        runner = runner.next

    if k >= size:
        return None

    current = linked_list._head

    for _ in range(size - k - 1):
        current = current.next

    return current.value


class KthToLastTest(unittest.TestCase):
    def test_kth_to_last(self):
        linked_list = from_iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        actual = kth_to_last(linked_list, 2)
        expected = 7

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
