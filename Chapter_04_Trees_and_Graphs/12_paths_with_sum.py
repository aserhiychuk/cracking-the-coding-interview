from tree import *
import unittest


def paths_with_sum(root, target):
    '''
    4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value
    (which might be positive or negative). Design an algorithm to count the number of paths that sum
    to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards
    (traveling only from parent nodes to child nodes).
    '''
    result = _dfs(root, target, [])

    return result

def _dfs(node, target, current_sums):
    if node is None:
        return 0

    current_sums = [n + node.value for n in current_sums + [0]]
    result_current = len([n for n in current_sums if n == target])

    result_left = _dfs(node.left, target, current_sums)
    result_right = _dfs(node.right, target, current_sums)

    return result_current + result_left + result_right


class PathsWithSumTest(unittest.TestCase):
    def test_paths_with_sum(self):
        #            14 
        #       1           9
        #   15     4     6    -8
        #        3   10    0
        #      2
        n0 = Node(0)
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n6 = Node(6)
        n8 = Node(-8)
        n9 = Node(9)
        n10 = Node(10)
        n14 = Node(14)
        n15 = Node(15)
        n14.left = n1
        n14.right = n9
        n1.left = n15
        n1.right = n4
        n9.left = n6
        n9.right = n8
        n4.left = n3
        n4.right = n10
        n6.right = n0
        n3.left = n2

        actual = paths_with_sum(n14, 15)
        expected = 6
        # 14 + 1 = 15
        # 15 = 15
        # 1 + 4 + 10 = 15
        # 9 + 6 = 15
        # 9 + 6 + 0 = 15
        # 14 + 9 - 8 = 15
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
