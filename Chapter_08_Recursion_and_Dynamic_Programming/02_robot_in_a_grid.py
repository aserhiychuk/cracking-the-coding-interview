import unittest


def robot_in_a_grid(grid):
    '''
    8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner 
    of grid with r rows and c columns. The robot can only move in two directions, 
    right and down, but certain cells are "off limits" such that the robot cannot 
    step on them. Design an algorithm to find a path for the robot from the top 
    left to the bottom right.
    '''
    assert grid[0][0] == 0

    result = _robot_in_a_grid(grid, 0, 0, [(0, 0)])

    return result


def _robot_in_a_grid(grid, i, j, path):
    n_rows = len(grid)
    n_cols = len(grid[i])

    if i == n_rows - 1 and j == n_cols - 1:
        return path

    if j < n_cols - 1 and grid[i][j + 1] == 0:
        result = _robot_in_a_grid(grid, i, j + 1, path + [(i, j + 1)])

        if isinstance(result, list):
            return result

    if i < n_rows - 1 and grid[i + 1][j] == 0:
        result = _robot_in_a_grid(grid, i + 1, j, path + [(i + 1, j)])

        if isinstance(result, list):
            return result

    return None


class RobotInAGridTest(unittest.TestCase):
    def test_invalid_input(self):
        grid = [
            [1, 0],
            [0, 0]
        ]
        with self.assertRaises(AssertionError):
            robot_in_a_grid(grid)

    def test_success(self):
        grid = [
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]
        ]
        actual = robot_in_a_grid(grid)
        expected = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4)]
        self.assertListEqual(expected, actual)

    def test_failure(self):
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        actual = robot_in_a_grid(grid)
        self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()
