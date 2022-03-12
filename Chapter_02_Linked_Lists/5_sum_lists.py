from linked_list import *

import unittest


def sum_lists(linked_list1, linked_list2):
    '''
    2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
    The digits are stored in reverse order, such that the Vs digit is at the head of the list.
    Write a function that adds the two numbers and returns the sum as a linked list.

    EXAMPLE
    Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. Output: 2 -> 1 -> 9. That is, 912.

    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem.

    EXAMPLE
    Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295,
    Output:9 -> 1 -> 2. That is, 912.
    '''
    cur1 = linked_list1._head
    cur2 = linked_list2._head
    result = LinkedList()
    prev_value = 0

    while cur1 and cur2:
        s = cur1.value + cur2.value + prev_value
        digit = s % 10
        result.append(digit)
        prev_value = s // 10

        cur1 = cur1.next
        cur2 = cur2.next

    node = cur1 if cur1 else cur2

    while node:
        s = node.value + prev_value
        digit = s % 10
        result.append(digit)
        prev_value = s // 10

        node = node.next

    if prev_value:
        result.append(prev_value)

    return result


class SumListsTest(unittest.TestCase):
    def test_sum_lists(self):
        linked_list1 = from_iter([4, 5])
        linked_list2 = from_iter([1, 8, 6])

        actual = sum_lists(linked_list1, linked_list2)
        actual = [v for v in actual]
        expected = [5, 3, 7]

        self.assertListEqual(expected, actual)


# Follow up
def reverse_linked_list(linked_list):
    cur = linked_list._head

    while cur and cur.next:
        next_node = cur.next
        cur.next = cur.next.next
        next_node.next = linked_list._head
        linked_list._head = next_node


def sum_lists_followup(linked_list1, linked_list2):
    reverse_linked_list(linked_list1)
    reverse_linked_list(linked_list2)

    result =  sum_lists(linked_list1, linked_list2)
    reverse_linked_list(result)

    return result


class SumListsFollowupTest(unittest.TestCase):
    def test_sum_lists_followup(self):
        linked_list1 = from_iter([4, 5])
        linked_list2 = from_iter([1, 8, 6])

        actual = sum_lists_followup(linked_list1, linked_list2)
        actual = [v for v in actual]
        expected = [2, 3, 1]

        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
