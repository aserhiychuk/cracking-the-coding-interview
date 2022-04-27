import unittest


class BiNode:
    def __init__(self, data):
        self.node1 = None
        self.node2 = None
        self.data = data


def bi_node(root):
    '''
    17.12 BiNode: Consider a simple data structure called BiNode, which has 
    pointers to two other nodes,

    public class BiNode {
        public BiNode node1, node2;
        public int data;
    }

    The data structure BiNode could be used to represent both a binary tree 
    (where node1 is the left node and node2 is the right node) or a doubly 
    linked list (where node1 is the previous node and node2 is the next node). 
    Implement a method to convert a binary search tree (implemented with BiNode) 
    into a doubly linked list. The values should be kept in order and the
    operation should be performed in place (that is, on the original data structure).
    '''
    _traverse_in_order(root)

    head = root

    while head.node1:
        head = head.node1

    return head


def _traverse_in_order(node):
    if node is None:
        return None, None

    if node.node1:
        left_smallest, left_biggest = _traverse_in_order(node.node1)
        left_biggest.node2 = node
        node.node1 = left_biggest
    else:
        left_smallest = node

    if node.node2:
        right_smallest, right_biggest = _traverse_in_order(node.node2)
        right_smallest.node1 = node
        node.node2 = right_smallest
    else:
        right_biggest = node

    return left_smallest, right_biggest


class BiNodeTest(unittest.TestCase):
    def test_bi_node(self):
        #             6 
        #       1           9
        #    0     4     7
        #        3   5     8
        #      2
        n0 = BiNode(0)
        n1 = BiNode(1)
        n2 = BiNode(2)
        n3 = BiNode(3)
        n4 = BiNode(4)
        n5 = BiNode(5)
        n6 = BiNode(6)
        n7 = BiNode(7)
        n8 = BiNode(8)
        n9 = BiNode(9)

        n6.node1 = n1
        n6.node2 = n9
        n1.node1 = n0
        n1.node2 = n4
        n4.node1 = n3
        n4.node2 = n5
        n3.node1 = n2
        n9.node1 = n7
        n7.node2 = n8

        node = bi_node(n6)

        # assert forward pass
        actual = [node.data]

        while node.node2:
            node = node.node2
            actual.append(node.data)

        expected = list(range(10))
        self.assertListEqual(expected, actual)

        # assert backward pass
        actual = []

        while node:
            actual.append(node.data)
            node = node.node1

        expected = list(reversed(range(10)))
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
