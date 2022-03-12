from linked_list import *

import unittest


def delete_middle_node(node):
    '''
    2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle
    (i.e., any node but the first and last node, not necessarily the exact middle)
    of a singly linked list, given only access to that node.

    EXAMPLE
    Input: the node c from the linked list a -> b-> c -> d -> e -> f
    Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
    '''
    node.value = node.next.value
    node.next = node.next.next


class DeleteMiddleNodeTest(unittest.TestCase):
    def test_delete_middle_node(self):
        linked_list = from_iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        node = linked_list._head.next.next.next
        delete_middle_node(node)

        actual = [v for v in linked_list]
        expected = [0, 1, 2, 4, 5, 6, 7, 8, 9]

        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
