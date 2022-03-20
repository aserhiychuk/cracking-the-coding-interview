from tree import *
import unittest


def minimal_tree(data):
    '''
    4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write
    an algorithm to create a binary search tree with minimal height.
    '''
    if not data:
        return None

    mid_index = len(data) // 2
    mid_value = data[mid_index]
    node = Node(mid_value)

    if len(data) > 1:
        node.left = minimal_tree(data[:mid_index])

        if len(data) > 2:
            node.right = minimal_tree(data[mid_index + 1:])

    return node


class MinimalTreeTest(unittest.TestCase):
    def test_minimal_tree(self):
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        root = minimal_tree(data)


        in_order = self._traverse_in_order(root)
        self.assertListEqual(data, in_order)

    def _traverse_in_order(self, node):
        if node is None:
            return []

        left = self._traverse_in_order(node.left)
        right = self._traverse_in_order(node.right)

        return [*left, node.value, *right]


if __name__ == '__main__':
    unittest.main()
