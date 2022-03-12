import unittest


def rotate_matrix(image):
    '''
    1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
    write a method to rotate the image by 90 degrees. Can you do this in place?
    '''
    if not image:
        return image

    n = len(image)

    for row in image:
        assert len(row) == n, 'invalid dimensions'

    for offset in range(n // 2):
        for i in range(offset, n - 1 - offset):
            tmp = image[offset][i]
            image[offset][i] = image[n - 1 - i][offset]
            image[n - 1 - i][offset] = image[n - 1 - offset][n - 1 - i]
            image[n - 1 - offset][n - 1 - i] = image[i][n - 1 - offset]
            image[i][n - 1 - offset] = tmp

    return image


class RotateMatrixTest(unittest.TestCase):
    def test_rotate_matrix_1(self):
        image = [
            [1]
        ]

        expected = [
            [1]
        ]

        actual = rotate_matrix(image)
        self.assertEqual(expected, actual)

    def test_rotate_matrix_2(self):
        image = [
            [1, 2],
            [3, 4]
        ]

        expected = [
            [3, 1],
            [4, 2]
        ]

        actual = rotate_matrix(image)
        self.assertEqual(expected, actual)

    def test_rotate_matrix_3(self):
        image = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        actual = rotate_matrix(image)
        self.assertEqual(expected, actual)

    def test_rotate_matrix_4(self):
        image = [
            [1,   2,  3,  4],
            [5,   6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15, 16]
        ]

        expected = [
            [13,  9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]

        actual = rotate_matrix(image)
        self.assertEqual(expected, actual)

    def test_rotate_matrix_5(self):
        image = [
            [ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

        expected = [
            [21, 16, 11,  6, 1],
            [22, 17, 12,  7, 2],
            [23, 18, 13,  8, 3],
            [24, 19, 14,  9, 4],
            [25, 20, 15, 10, 5]
        ]

        actual = rotate_matrix(image)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
