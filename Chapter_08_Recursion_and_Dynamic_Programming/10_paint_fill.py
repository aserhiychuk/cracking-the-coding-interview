import unittest


def paint_fill(matrix, x, y, new_color):
    '''
    Paint Fill: Implement the "paint fill" function that one might see 
    on many image editing programs. That is, given a screen (represented 
    by a two-dimensional array of colors), a point, and a new color, fill 
    in the surrounding area until the color changes from the original cofor.
    '''
    old_color = matrix[x][y]
    matrix[x][y] = new_color

    if x > 0 and matrix[x - 1][y] == old_color:
        paint_fill(matrix, x - 1, y, new_color)

    if y < len(matrix[x]) - 1 and matrix[x][y + 1] == old_color:
        paint_fill(matrix, x, y + 1, new_color)

    if x < len(matrix) - 1 and matrix[x + 1][y] == old_color:
        paint_fill(matrix, x + 1, y, new_color)

    if y > 0 and matrix[x][y - 1] == old_color:
        paint_fill(matrix, x, y - 1, new_color)


class PaintFillTest(unittest.TestCase):
    def _get_matrix(self):
        matrix = [
            [0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1]
        ]

        return [row.copy() for row in matrix]

    def test_paint_fill(self):
        actual = self._get_matrix()
        paint_fill(actual, 0, 0, 2)
        expected = [
            [2, 2, 2, 2, 1],
            [1, 1, 2, 2, 2],
            [1, 1, 1, 2, 2],
            [2, 1, 1, 2, 1],
            [2, 2, 2, 2, 1]
        ]
        self.assertListEqual(expected, actual)

        actual = self._get_matrix()
        paint_fill(actual, 0, 4, 2)
        expected = [
            [0, 0, 0, 0, 2],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1]
        ]
        self.assertListEqual(expected, actual)

        actual = self._get_matrix()
        paint_fill(actual, 1, 0, 2)
        expected = [
            [0, 0, 0, 0, 1],
            [2, 2, 0, 0, 0],
            [2, 2, 2, 0, 0],
            [0, 2, 2, 0, 1],
            [0, 0, 0, 0, 1]
        ]
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
