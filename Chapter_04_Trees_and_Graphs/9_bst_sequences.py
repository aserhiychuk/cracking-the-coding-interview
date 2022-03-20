from tree import *
import unittest


def bst_sequences(node):
    '''
    4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
    and inserting each element. Given a binary search tree with distinct elements, print all possible arrays
    that could have led to this tree.
    '''
    if node is None:
        return [[]]

    sequences_left = bst_sequences(node.left)
    sequences_right = bst_sequences(node.right)

    result = []

    for s1 in sequences_left:
        for s2 in sequences_right:
            if s1 and s2:
                result.append([node.value, *s1, *s2])
                result.append([node.value, *s2, *s1])
            elif s1:
                result.append([node.value, *s1])
            elif s2:
                result.append([node.value, *s2])
            else:
                result.append([node.value])

    return result


class BstSequencesTest(unittest.TestCase):
    def test_bst_sequences(self):
        #             4 
        #       2           6
        #    1     3     5     7
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n4.left = n2
        n4.right = n6
        n2.left = n1
        n2.right = n3
        n6.left = n5
        n6.right = n7

        actual = bst_sequences(n4)

        expected = [
            [4, 2, 1, 3, 6, 5, 7],
            [4, 6, 5, 7, 2, 1, 3],
            [4, 2, 1, 3, 6, 7, 5],
            [4, 6, 7, 5, 2, 1, 3],
            [4, 2, 3, 1, 6, 5, 7],
            [4, 6, 5, 7, 2, 3, 1],
            [4, 2, 3, 1, 6, 7, 5],
            [4, 6, 7, 5, 2, 3, 1]
        ]
        self.assertListEqual(expected, actual)

 
if __name__ == '__main__':
    unittest.main()
