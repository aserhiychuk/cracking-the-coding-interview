import unittest


def langtons_ant(k):
    '''
    16.22 Langton's Ant: An ant is sitting on an infinite grid of white 
    and black squares. Initially, the grid is all white and the ant faces 
    right. At each step, it does the following:
    
    (1) At a white square, flip the color of the square, turn 90 degrees 
    right (clockwise), and move forward one unit.
    
    (2) At a black square, flip the color of the square, turn 90 degrees 
    left (counter-clockwise), and move forward one unit.
    
    Write a program to simulate the first K moves that the ant makes and 
    print the final board as a grid. Note that you are not provided with 
    the data structure to represent the grid. This is something you must 
    design yourself. The only input to your method is K. You should print 
    the final grid and return nothing.The method signature might be something 
    like void printKMoves(int K).
    '''
    black_squares = set()
    direction = 0
    i, j = 0, 0

    for _ in range(k):
        if (i, j) in black_squares:
            black_squares.remove((i, j))
            direction -=1 
        else:
            black_squares.add((i, j))
            direction += 1

        direction %= 4

        if direction == 0:
            # right
            j += 1
        elif direction == 1:
            # down
            i += 1
        elif direction == 2:
            # left
            j -= 1
        elif direction == 3:
            # top
            i -= 1

    min_i, max_i, min_j, max_j = None, None, None, None

    for i, j in black_squares:
        if min_i is None or i < min_i:
            min_i = i

        if max_i is None or max_i < i:
            max_i = i

        if min_j is None or j < min_j:
            min_j = j

        if max_j is None or max_j < j:
            max_j = j

    n = max_i - min_i + 1
    m = max_j - min_j + 1

    matrix = []

    for _ in range(n):
        row = [1] * m
        matrix.append(row)

    for i, j in black_squares:
        matrix[i - min_i][j - min_j] = 0

    return matrix


class LangtonsAntTest(unittest.TestCase):
    def test_langtons_ant(self):
        actual = langtons_ant(100)
        expected = [
            [1, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 1, 1]
        ]
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
