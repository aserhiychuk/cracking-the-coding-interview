import unittest


def max_submatrix(matrix):
    '''
    17.24 Max Submatrix: Given an NxN matrix of positive and negative integers, 
    write code to find the submatrix with the largest possible sum.
    '''
    n = len(matrix)

    preprocessed = []

    for _ in range(n):
        row = [None] * n
        preprocessed.append(row)

    for i in range(n):
        for j in range(n):
            s = matrix[i][j]

            if j > 0:
                s += preprocessed[i][j - 1]

            preprocessed[i][j] = s

    for i in range(1, n):
        for j in range(n):
            preprocessed[i][j] += preprocessed[i - 1][j]

    max_sum = None
    top, left, bottom, right = None, None, None, None

    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    s = preprocessed[k][l]

                    if j > 0:
                        s -= preprocessed[k][j - 1]

                    if i > 0:
                        s -= preprocessed[i - 1][l]

                    if i > 0 and j > 0:
                        s += preprocessed[i - 1][j - 1]

                    if max_sum is None or max_sum < s:
                        max_sum = s
                        top, left, bottom, right = i, j, k, l

    return top, left, bottom, right


class MaxSubmatrixTest(unittest.TestCase):
    def test_max_submatrix(self):
        matrix = [
            [-7,  8, -8, -2,  7],
            [-1, -4,  3, -5,  9],
            [-3,  9,  7,  3, -2],
            [ 2,  1,  8, -2, -8],
            [-5,  0, -3, -5,  7]
        ]

        actual = max_submatrix(matrix)
        expected = 2, 1, 3, 3
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
