import unittest


def zero_matrix(matrix):
    '''
    1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0.
    '''
    if not matrix:
        return matrix

    zero_indices = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_indices.append([i, j])

    for i, j in zero_indices:
        for k in range(len(matrix[i])):
            matrix[i][k] = 0

        for k in range(len(matrix)):
            matrix[k][j] = 0

    return matrix


class ZeroMatrixTest(unittest.TestCase):
    def test_zero_matrix(self):
        matrix = [
            [ 1,  2,  0,  4],
            [ 5,  6,  7,  8],
            [ 9, 0, 11, 12],
            [13, 14, 15, 16]
        ]
        
        expected = [
            [ 0,  0,  0,  0],
            [ 5,  0,  0,  8],
            [ 0,  0,  0,  0],
            [13,  0,  0, 16]
        ]

        actual = zero_matrix(matrix)
        self.assertEqual(expected, actual)

            
if __name__ == '__main__':
    unittest.main()
