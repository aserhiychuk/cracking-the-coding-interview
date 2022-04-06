import unittest


def sorted_matrix_search(matrix, element):
    '''
    10.9 Sorted Matrix Search: Given an M x N matrix in which each row and each 
    column is sorted in ascending order, write a method to find an element.
    '''
    n = len(matrix)
    m = len(matrix[0])

    return _search(matrix, element, 0, 0, n - 1, m - 1)


def _search(matrix, element, low_i, low_j, high_i, high_j):
    if low_i > high_i or low_j > high_j:
        return None

    mid_i = low_i + (high_i - low_i) // 2
    mid_j = low_j + (high_j - low_j) // 2

    if element < matrix[mid_i][mid_j]:
        result = _search(matrix, element, low_i, low_j, high_i, mid_j - 1)

        if result:
            return result

        result = _search(matrix, element, low_i, mid_j, mid_i - 1, high_j)

        if result:
            return result
    elif matrix[mid_i][mid_j] < element:
        result = _search(matrix, element, mid_i + 1, low_j, high_i, mid_j)

        if result:
            return result

        result = _search(matrix, element, low_i, mid_j + 1, high_i, high_j)

        if result:
            return result
    else:
        return (mid_i, mid_j)

    return None


class SortedMatrixSearchTest(unittest.TestCase):
    def test_sorted_matrix_search(self):
        test_cases = [
            (3, (0, 1)),
            (14, (0, 6)),
            (9, (1, 2)),
            (37, (2, 2)),
            (40, (2, 3)),
            (39, (3, 2)),
            (45, (3, 4)),
            (46, (4, 2)),
            (100, (4, 7)),
            (0, None),
            (4, None),
            (18, None),
            (35, None),
            (55, None),
            (101, None)
        ]
        matrix = [
            [ 1,  3,  6,  7,  8, 13, 14,  20], 
            [ 2,  5,  9, 10, 11, 16, 17,  21], 
            [22, 30, 37, 40, 41, 44, 49,  50],
            [23, 33, 39, 43, 45, 51, 60,  99],
            [25, 34, 46, 47, 48, 52, 70, 100]
        ]

        for element, expected in test_cases:
            actual = sorted_matrix_search(matrix, element)

            if expected is not None:
                self.assertTupleEqual(expected, actual)
            else:
                self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()
