import unittest


def max_black_square(matrix):
    '''
    17.23 Max Black Square: Imagine you have a square matrix, 
    where each cell (pixel) is either black or white. Design 
    an algorithm to find the maximum subsquare such that all 
    four borders are filled with black pixels.
    '''
    n = len(matrix)

    preprocessed = []

    for i in range(n):
        row = [0] * n
        preprocessed.append(row)

    for i in range(n):
        preprocessed[n - 1][i] = matrix[n - 1][i]
        preprocessed[i][n - 1] = matrix[i][n - 1]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == 0:
                if i == n - 1:
                    a = -1
                else:
                    a, _  = preprocessed[i + 1][j]

                if j == n - 1:
                    b = -1
                else:
                    _, b = preprocessed[i][j + 1]
            else:
                a, b = -1, -1

            preprocessed[i][j] = a + 1, b + 1

    for size in range(n, 0, -1):
        for i in range(n - size + 1):
            for j in range(n - size + 1):
                size_left, size_top = preprocessed[i][j]
                _, size_bottom = preprocessed[i + size - 1][j]
                size_right, _ = preprocessed[i][j + size - 1]

                if size_left >= size and size_top >= size \
                    and size_bottom >= size and size_right >= size:
                    return i, j, size

    return None


class MaxBlackSquareTest(unittest.TestCase):
    def test_max_black_square(self):
        matrix = [
            [0, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1]
        ]

        actual = max_black_square(matrix)
        # (left, top, size)
        expected = (2, 1, 4)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
