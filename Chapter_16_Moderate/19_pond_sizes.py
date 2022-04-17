from queue import Queue
import unittest


def pond_sizes(matrix):
    '''
    16.19 Pond Sizes: You have an integer matrix representing a plot of land, 
    where the value at that location represents the height above sea level. 
    A value of zero indicates water. A pond is a region of water connected 
    vertically, horizontally, or diagonally. The size of the pond is the total 
    number of connected water cells. Write a method to compute the sizes of all 
    ponds in the matrix.

    EXAMPLE
    Input:
        0 2 1 0
        0 1 0 1
        1 1 0 1
        0 1 0 1
    Output: 2, 4, 1 (in any order)
    '''
    result = set()
    visited = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0 or (i, j) in visited:
                continue

            # new pond found
            pond_size = 0
            queue = Queue()
            queue.put((i, j))
            visited.add((i, j))

            while not queue.empty():
                x, y = queue.get()
                pond_size += 1

                candidates = [
                    (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                    (x, y - 1), (x, y + 1),
                    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
                ]

                for cand_x, cand_y in candidates:
                    if _is_new_water(matrix, cand_x, cand_y, visited):
                        queue.put((cand_x, cand_y))
                        visited.add((cand_x, cand_y))

            result.add(pond_size)

    return result


def _is_new_water(matrix, i, j, visited):
    return i >= 0 and i < len(matrix) \
        and j >= 0 and j < len(matrix[0]) \
        and matrix[i][j] == 0 \
        and (i, j) not in visited


class PondSizesTest(unittest.TestCase):
    def test_pond_sizes(self):
        matrix = [
            [0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]
        ]
        actual = pond_sizes(matrix)
        expected = set([1, 2, 4])
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
