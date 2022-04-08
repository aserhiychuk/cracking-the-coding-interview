import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.n_values = 1
        self.left_size = 0
        self.right_size = 0


class Rank:
    '''
    10.10 Rank from Stream: Imagine you are reading in a stream of integers. 
    Periodically, you wish to be able to look up the rank of a number x 
    (the number of values less than or equal to x). Implement the data 
    structures and algorithms to support these operations. That is, implement 
    the method track(int x), which is called when each number is generated, 
    and the method getRankOfNumber(int x), which returns the number of values tess 
    than or equal to x (not including x itself).

    EXAMPLE
    Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
    getRankOfNumber(1) = 0 // values: 
    getRank0fNumber(3) = 1 // values: s[1] = 1
    getRank0fNumber(4) = 3 // values: s[1] = 1, s[2] = 4, s[8] = 3
    '''
    def __init__(self):
        self._root = None

    def track(self, value):
        self._root = self._insert(self._root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
            node.left_size = node.left.left_size + node.left.right_size + node.left.n_values
        elif node.value < value:
            node.right = self._insert(node.right, value)
            node.right_size = node.right.left_size + node.right.right_size + node.right.n_values
        else:
            node.n_values += 1

        return node

    def get_rank(self, value):
        return self._get_rank(self._root, value)

    def _get_rank(self, node, value):
        if node is None:
            return 0

        if value < node.value:
            return self._get_rank(node.left, value)

        if node.value < value:
            result = self._get_rank(node.right, value)

            return result + node.left_size + node.n_values

        return node.left_size + node.n_values - 1


class RankFromStreamTest(unittest.TestCase):
    def test_rank_from_stream(self):
        #             5(2)        
        #         1         9  
        #           4(2)  7   13  
        #         3          
        #                    
        #                    
        stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]
        rank = Rank()

        for value in stream:
            rank.track(value)

        test_cases = [
            (1, 0),
            (3, 1),
            (4, 3),
            (5, 5),
            (7, 6),
            (9, 7),
            (13, 8)
        ]

        for value, expected in test_cases:
            actual = rank.get_rank(value)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
