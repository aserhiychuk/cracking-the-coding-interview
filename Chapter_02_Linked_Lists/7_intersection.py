from linked_list import *

import unittest


def intersection(linked_list1, linked_list2):
    '''
    2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect.
    Return the intersecting node. Note that the intersection is defined based on reference, not value.
    That is, if the kth node of the first linked list is the exact same node (by reference)
    as the j th node of the second linked list, then they are intersecting.
    '''
    len1 = len(linked_list1)
    len2 = len(linked_list2)

    if len1 < len2:
        linked_list1, linked_list2 = linked_list2, linked_list1

    cur1 = linked_list1._head

    for _ in range(abs(len1 - len2)):
        cur1 = cur1.next

    cur2 = linked_list2._head

    while cur1 is not cur2:
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1


class IntersectionTest(unittest.TestCase):
    def test_intersection(self):
        linked_list1 = from_iter('abcdef')
        linked_list2 = from_iter('12')
        tail2 = linked_list2._head.next
        tail2.next = linked_list1._head.next.next.next.next

        actual = intersection(linked_list1, linked_list2)
        actual = actual.value
        expected = 'e'

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
