from linked_list import *

import unittest


# runtime: O(n)
# space  : O(n)
def remove_duplicates(linked_list):
    '''
    2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.

    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?
    '''
    if not linked_list:
        return

    visited = set()

    cur = linked_list._head
    visited.add(cur.value)

    while cur.next:
        if cur.next.value not in visited:
            visited.add(cur.next.value)
            cur = cur.next
        else:
            cur.next = cur.next.next


class RemoveDuplicatesTest(unittest.TestCase):
    def test_remove_duplicates(self):
        linked_list = from_iter([7, 3, 2, 7, 3, 8, 5, 1, 9, 7])
        remove_duplicates(linked_list)

        actual = [v for v in linked_list]
        expected = [7, 3, 2, 8, 5, 1, 9]

        self.assertListEqual(expected, actual)


# Pointer reinforcement
# 
# runtime: O(n)
# space  : O(n)
def remove_duplicates_recursive(linked_list):
    if not linked_list:
        return

    visited = set()
    linked_list._head = _remove_duplicates_recursive(linked_list._head, visited)
    
def _remove_duplicates_recursive(node, visited):
    if not node:
        return None

    if node.value in visited:
        return _remove_duplicates_recursive(node.next, visited)

    visited.add(node.value)
    node.next = _remove_duplicates_recursive(node.next, visited)
    
    return node


class RemoveDuplicatesRecursiveTest(unittest.TestCase):
    def test_remove_duplicates_recursive(self):
        linked_list = from_iter([7, 3, 2, 7, 3, 8, 5, 1, 9, 7])
        remove_duplicates_recursive(linked_list)

        actual = [v for v in linked_list]
        expected = [7, 3, 2, 8, 5, 1, 9]

        self.assertListEqual(expected, actual)


# Follow up
# 
# runtime: O(n^2)
# space  : O(1)
def remove_duplicates_followup(linked_list):
    if not linked_list:
        return

    cur = linked_list._head

    while cur.next:
        runner = linked_list._head
        is_duplicate = False

        while runner != cur.next:
            if cur.next.value == runner.value:
                is_duplicate = True
                break

            runner = runner.next

        if not is_duplicate:
            cur = cur.next
        else:
            cur.next = cur.next.next


class RemoveDuplicatesFollowupTest(unittest.TestCase):
    def test_remove_duplicates_followup(self):
        linked_list = from_iter([7, 3, 2, 7, 3, 8, 5, 1, 9, 7])
        remove_duplicates_followup(linked_list)

        actual = [v for v in linked_list]
        expected = [7, 3, 2, 8, 5, 1, 9]

        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
