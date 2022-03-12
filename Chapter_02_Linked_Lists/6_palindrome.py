from linked_list import *

import unittest


def is_palindrome(linked_list):
    '''
    2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
    '''
    cur = linked_list._head

    if not cur:
        return True

    reversed_list = LinkedList()

    while cur:
        node = Node(cur.value)
        node.next = reversed_list._head
        reversed_list._head = node

        cur = cur.next

    cur1 = linked_list._head
    cur2 = reversed_list._head

    while cur1 and cur2:
        if cur1.value != cur2.value:
            return False

        cur1 = cur1.next
        cur2 = cur2.next

    return True


class IsPalindromTest(unittest.TestCase):
    def test_true(self):
        linked_list = from_iter('abcba')
        actual = is_palindrome(linked_list)

        self.assertTrue(actual)

    def test_false(self):
        linked_list = from_iter('abc')
        actual = is_palindrome(linked_list)

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
