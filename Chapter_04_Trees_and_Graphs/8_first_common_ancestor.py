from tree import *
import unittest


def first_common_ancestor(root, node1, node2):
    '''
    4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor of
    two nodes in a binary tree. Avoid storing additional nodes in a data structure.

    NOTE: This is not necessarily a binary search tree.
    '''
    result = _dfs(root, node1, node2)

    return result

def _dfs(node, node1, node2):
    if node is None:
        return False

    if node == node1 and node == node2:
        return node

    result_left = _dfs(node.left, node1, node2)

    if isinstance(result_left, Node):
        return result_left

    result_right = _dfs(node.right, node1, node2)

    if isinstance(result_right, Node):
        return result_right

    if result_left is True and result_right is True:
        return node

    if (result_left is True or result_right is True) and (node == node1 or node == node2):
        return node

    return node == node1 or node == node2 or result_left or result_right


class FirstCommonAncestorTest(unittest.TestCase):
    def test_first_common_ancestor(self):
        #             a 
        #       b           c
        #    d     e     f     
        #        g   h     i
        #      j
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
        h = Node('h')
        i = Node('i')
        j = Node('j')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        e.left = g
        e.right = h
        f.right = i
        g.left = j

        actual = first_common_ancestor(a, a, a)
        self.assertEqual('a', actual.value)

        actual = first_common_ancestor(a, b, c)
        self.assertEqual('a', actual.value)

        actual = first_common_ancestor(a, d, g)
        self.assertEqual('b', actual.value)

        actual = first_common_ancestor(a, b, d)
        self.assertEqual('b', actual.value)

        actual = first_common_ancestor(a, g, e)
        self.assertEqual('e', actual.value)

        actual = first_common_ancestor(a, i, d)
        self.assertEqual('a', actual.value)

        actual = first_common_ancestor(i, i, i)
        self.assertEqual('i', actual.value)


if __name__ == '__main__':
    unittest.main()
