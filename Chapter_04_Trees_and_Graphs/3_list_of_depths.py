from queue import Queue
from tree import *
import unittest


def list_of_depths(root):
    '''
    4.3 List of Depths: Given a binary tree, design an algorithm which creates a linkedlist of
    all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
    '''
    result = []

    queue = Queue()
    queue.put([root, 0])
    prev_depth = None

    while not queue.empty():
        node, depth = queue.get()

        if depth != prev_depth:
            result.append([])

        result[-1].append(node.value)

        if node.left:
            queue.put([node.left, depth + 1])

        if node.right:
            queue.put([node.right, depth + 1])

        prev_depth = depth

    return result


class ListOfDepthsTest(unittest.TestCase):
    def test_list_of_depths(self):
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
        k = Node('k')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        c.right = g
        d.left = h
        d.right = i
        e.left = j
        e.right = k
        actual = list_of_depths(a)

        expected = [['a'], ['b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j', 'k']]
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
