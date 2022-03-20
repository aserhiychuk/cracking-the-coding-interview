import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def successor(node):
    '''
    4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node
    in a binary search tree. You may assume that each node has a link to its parent.
    '''
    if node is None:
        return None

    if node.right is not None:
        successor = node.right

        while successor.left is not None:
            successor = successor.left

        return successor.value

    successor = node.parent

    while successor and successor.value < node.value:
        successor = successor.parent

    if successor and successor.value > node.value:
        return successor.value

    return None


class SuccessorTest(unittest.TestCase):
    def test_successor(self):
        n7 = Node(7)
        n3 = Node(3)
        n9 = Node(9)
        n1 = Node(1)
        n4 = Node(4)
        n8 = Node(8)
        n10 = Node(10)
        n2 = Node(2)
        n7.left = n3
        n3.parent = n7
        n7.right = n9
        n9.parent = n7
        n3.left = n1
        n1.parent = n3
        n3.right = n4
        n4.parent = n3
        n9.left = n8
        n8.parent = n9
        n9.right = n10
        n10.parent = n9
        n1.right = n2
        n2.parent = n1
        #         7 
        #      3      9
        #    1   4  8   10
        #     2

        self.assertEqual(3, successor(n2))
        self.assertEqual(2, successor(n1))
        self.assertEqual(4, successor(n3))
        self.assertEqual(7, successor(n4))
        self.assertEqual(8, successor(n7))
        self.assertEqual(10, successor(n9))
        self.assertIsNone(successor(n10))
        self.assertEqual(9, successor(n8))


if __name__ == '__main__':
    unittest.main()
