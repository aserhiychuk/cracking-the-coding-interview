from tree import *
import unittest


def check_subtree(root1, root2):
    '''
    4.10 Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
    algorithm to determine if T2 is a subtree of T1.

    A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2,
    that is, if you cut off the tree at node n, the two trees would be identical.
    '''
    t1 = _pre_order(root1)
    t2 = _pre_order(root2)

    for i in range(len(t1) - len(t2) + 1):
        j = 0

        while j < len(t2):
            if t1[i + j] != t2[j]:
                break

            j += 1

        if j == len(t2):
            return True

    return False


def _pre_order(node):
    if node is None:
        return [None]

    result = [node.value, *_pre_order(node.left), *_pre_order(node.right)]

    return result


class CheckSubtreeTest(unittest.TestCase):
    def test_check_subtree(self):
        # T1
        #             a(1)
        #       a(2)         a(3)
        #   a(4)    a(5)  a(6)
        #        a(7) a(8)   a(9)
        #      a(10)
        # 
        # 
        # T2
        #           a(1)
        #        a(2)  a(3)
        #     a(4)
        a1 = Node('a')
        a2 = Node('a')
        a3 = Node('a')
        a4 = Node('a')
        a5 = Node('a')
        a6 = Node('a')
        a7 = Node('a')
        a8 = Node('a')
        a9 = Node('a')
        a10 = Node('a')
        a1.left = a2
        a1.right = a3
        a2.left = a4
        a2.right = a5
        a3.left = a6
        a5.left = a7
        a5.right = a8
        a6.right = a9
        a7.left = a10

        b1 = Node('a')
        b2 = Node('a')
        b3 = Node('a')
        b4 = Node('a')
        b1.left = b2
        b1.right = b3
        b2.left = b4

        actual = check_subtree(a1, b1)
        self.assertTrue(actual)

        a7.right = Node('a')
        actual = check_subtree(a1, b1)
        self.assertFalse(actual)

        b2.right = Node('a')
        actual = check_subtree(a1, b1)
        self.assertTrue(actual)

        b3.right = Node('a')
        actual = check_subtree(a1, b1)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
