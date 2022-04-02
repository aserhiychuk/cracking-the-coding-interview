import unittest


def eight_queens():
    '''
    8.12 Eight Queens: Write an algorithm to print all ways of arranging 
    eight queens on an 8x8 chess board so that none of them share the same 
    row, column, or diagonal. In this case, "diagonal" means all diagonals, 
    not just the two that bisect the board.
    '''
    return _eight_queens([])


def _eight_queens(board):
    if len(board) == 8:
        return [board] if is_safe(board) else None

    results = []

    for i in range(8):
        if i in board:
            continue

        result = _eight_queens(board + [i])

        if result is not None:
            results += result

    return results


def is_safe(board):
    if set(board) != set(range(len(board))):
        return False

    for i in range(len(board)):
        j = board[i]

        for other_i in range(len(board)):
            if i == other_i:
                continue

            other_j = board[other_i]

            if i - j == other_i - other_j:
                return False

            if i + j == other_i + other_j:
                return False

    return True

# Example 1
# 
#   0 1 2 3 4 5 6 7
# 0 1 _ _ _ _ _ _ _
# 1 _ _ _ _ 1 _ _ _
# 2 _ _ _ _ _ _ _ 1
# 3 _ _ _ _ _ 1 _ _
# 4 _ _ 1 _ _ _ _ _
# 5 _ _ _ _ _ _ 1 _
# 6 _ 1 _ _ _ _ _ _
# 7 _ _ _ 1 _ _ _ _


# Example 2
# 
#   0 1 2 3 4 5 6 7
# 0 _ _ _ _ _ 1 _ _
# 1 _ _ 1 _ _ _ _ _
# 2 _ _ _ _ _ _ 1 _
# 3 _ _ _ 1 _ _ _ _
# 4 1 _ _ _ _ _ _ _
# 5 _ _ _ _ _ _ _ 1
# 6 _ 1 _ _ _ _ _ _
# 7 _ _ _ _ 1 _ _ _

class EightQueensTest(unittest.TestCase):
    def test_eight_queens(self):
        boards = eight_queens()
        self.assertEqual(92, len(boards))

        for board in boards:
            self.assertTrue(is_safe(board))


if __name__ == '__main__':
    unittest.main()
