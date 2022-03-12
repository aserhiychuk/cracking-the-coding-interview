from linked_list import *

import unittest


def loop_detection(linked_list):
    '''
    2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns
    the node at the beginning of the loop.

    DEFINITION
    Circular linked list: A (corrupt) linked list in which a node's next pointer points
    to an earlier node, so as to make a loop in the linked list.

    EXAMPLE
    Input: A->8->C->D->E-> C [the same C as earlier]
    Output: C
    '''
    slow = linked_list._head
    fast = linked_list._head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break

    if not fast.next:
        # no loop
        return False

    # loop detected
    cur1 = linked_list._head
    cur2 = fast

    while cur1 is not cur2:
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1


class LoopDetectionTest(unittest.TestCase):
    def test_loop_detection(self):
        linked_list = from_iter('123456789')
        tail = linked_list._head.next.next.next.next.next.next.next.next
        tail.next = linked_list._head.next.next.next.next

        actual = loop_detection(linked_list)
        actual = actual.value
        expected = '5'

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
