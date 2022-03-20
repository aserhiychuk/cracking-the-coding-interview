from tree import *
import unittest


def check_balanced(root):
    '''
    4.4 Check Balanced: Implement a function to check if a binary tree is balanced.
    For the purposes of this question, a balanced tree is defined to be a tree such that
    the heights of the two subtrees of any node never differ by more than one.
    '''
    if not root:
        return False

    try:
        height = _height(root)
    except AssertionError:
        return False

    return True


def _height(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 0

    height_left = _height(node.left) if node.left is not None else 0
    height_right = _height(node.right) if node.right is not None else 0

    assert abs(height_left - height_right) <= 1, 'Tree is not balanced'

    return max(height_left, height_right) + 1


class CheckBalancedTest(unittest.TestCase):
    def test_check_balanced(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
        h = Node('h')
        i = Node('i')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = h
        c.right = i
        d.left = f
        f.left = g
        #         a 
        #      b     c
        #     d e   h i
        #    f 
        #   g     

        self.assertFalse(check_balanced(None))
        self.assertFalse(check_balanced(a))
        self.assertFalse(check_balanced(b))
        self.assertTrue(check_balanced(c))
        self.assertTrue(check_balanced(d))
        self.assertTrue(check_balanced(e))
        self.assertTrue(check_balanced(f))
        self.assertTrue(check_balanced(g))
        self.assertTrue(check_balanced(h))
        self.assertTrue(check_balanced(i))


if __name__ == '__main__':
    unittest.main()
