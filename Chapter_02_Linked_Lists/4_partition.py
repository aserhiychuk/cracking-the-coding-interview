from linked_list import *

import unittest


def partition(linked_list, p):
    '''
    2.4 Partition: Write code to partition a linked list around a value x, such that
    all nodes less than x come before all nodes greater than or equal to x.
    If x is contained within the list, the values of x only need to be after the elements
    less than x (see below). The partition element x can appear anywhere in the "right partition";
    it does not need to appear between the left and right partitions.

    EXAMPLE
    Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    '''
    if not linked_list:
        return None

    cur = linked_list._head

    while cur.next:
        if cur.next.value < p:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = linked_list._head
            linked_list._head = tmp
        else:
            cur = cur.next


class PartitionTest(unittest.TestCase):
    def test_partition(self):
        linked_list = from_iter([1, 6, 0, 0, 4, 0, 10, 3, 4, 1])
        partition(linked_list, 5)

        actual = [v for v in linked_list]
        expected = [1, 4, 3, 0, 4, 0, 0, 1, 6, 10]

        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
