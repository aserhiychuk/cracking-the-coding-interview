from tree import *
import unittest


def validate_bst(node):
    '''
    4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
    '''
    if not node:
        return True

    if node.left is not None and node.right is not None:
        return node.left.value < node.value \
            and node.value < node.right.value \
            and validate_bst(node.left) \
            and validate_bst(node.right)
    elif node.left is not None:
        return node.left.value < node.value \
            and validate_bst(node.left)
    elif node.right is not None:
        return node.value < node.right.value \
            and validate_bst(node.right)
    else:
        return True


class ValidateBstTest(unittest.TestCase):
    def test_validate_bst(self):
        a = Node(7)
        b = Node(3)
        c = Node(9)
        d = Node(1)
        e = Node(4)
        f = Node(8)
        g = Node(10)
        h = Node(2)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        c.right = g
        d.right = h
        #         7 
        #      3      9
        #    1   4  8   10
        #     2

        self.assertTrue(validate_bst(a))

        i = Node(5)
        d.left = i
        self.assertFalse(validate_bst(a))


if __name__ == '__main__':
    unittest.main()
