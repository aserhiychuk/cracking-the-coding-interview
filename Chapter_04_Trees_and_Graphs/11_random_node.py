import random
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.n_children = 0


class BinarySearchTree:
    '''
    4.11 Random Node: You are implementing a binary tree class from scratch which, in addition to insert,
    find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes
    should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain
    how you would implement the rest of the methods.
    '''
    def __init__(self):
        self._root = None

    def insert(self, value):
        pass
        # if self._root is None:
        #     self._root = Node(value)

        self._root = self._insert(self._root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            left = self._insert(node.left, value)
            node.left = left
        elif node.value < value:
            right = self._insert(node.right, value)
            node.right = right

        n_left_children = node.left.n_children + 1 if node.left else 0
        n_right_children = node.right.n_children + 1 if node.right else 0

        node.n_children = n_left_children + n_right_children

        return node

    def find(self, value):
        pass

    def delete(self, value):
        pass

    def get_random_node(self):
        if self._root is None:
            return None

        return self._get_random_node(self._root)

    def _get_random_node(self, node):
        weight_left = node.left.n_children + 1 if node.left else 0
        weight_right = node.right.n_children + 1 if node.right else 0
        choice = random.choices([0, 1, 2], [weight_left, 1, weight_right])

        if choice[0] == 0:
            result = self._get_random_node(node.left)
        elif choice[0] == 1:
            result = node.value
        elif choice[0] == 2:
            result = self._get_random_node(node.right)

        return result


class RandomNodeTest(unittest.TestCase):
    def test_random_node(self):
        #             6 
        #       1           9
        #    0     4     7
        #        3   5     8
        #      2
        bst = BinarySearchTree()
        bst.insert(6)
        bst.insert(1)
        bst.insert(9)
        bst.insert(0)
        bst.insert(4)
        bst.insert(7)
        bst.insert(3)
        bst.insert(5)
        bst.insert(8)
        bst.insert(2)

        n_nodes = 10
        n_total = 10000
        counts = {}

        for _ in range(n_total):
            value = bst.get_random_node()
            count = counts.get(value, 0)
            counts[value] = count + 1

            self.assertEqual(n_nodes, len(counts))

        max_deviation = 0.1

        for value, count in counts.items():
            expected_prob = 1 / n_nodes
            actual_prob = count / n_total
            actual_deviation = abs((expected_prob - actual_prob) / expected_prob)

            self.assertLess(actual_deviation, max_deviation)


if __name__ == '__main__':
    unittest.main()
