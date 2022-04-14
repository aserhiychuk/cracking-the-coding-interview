import unittest


def diving_board(shorter, longer, k):
    '''
    16.11 Diving Board: You are building a diving board by placing a bunch 
    of planks of wood end-to-end. There are two types of planks, one of length 
    shorter and one of length longer. You must use exactly K planks of wood. 
    Write a method to generate all possible lengths for the diving board.
    '''
    result = []

    for i in range(k + 1):
        length = (k - i) * shorter + i * longer
        result.append(length)

    return result


class DivingBoardTest(unittest.TestCase):
    def test_diving_board(self):
        test_cases = [
            (1, 2, 10, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
            (3, 7, 10, [30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70]),
        ]

        for shorter, longer, k, expected in test_cases:
            actual = diving_board(shorter, longer, k)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
