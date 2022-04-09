import inspect
import unittest


def tic_tac_win(board):
    '''
    16.4 Tic Tac Win: Design an algorithm to figure out if someone 
    has won a game of tic-tac-toe.
    '''
    n_moves1 = 0
    n_moves2 = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                n_moves1 += 1
            elif board[i][j] == 1:
                n_moves2 += 1

    winner1 = False
    winner2 = False

    if n_moves1 == n_moves2:
        # check both players
        winner1 = n_moves1 >= 3 and check_winner(board, 0)
        winner2 = n_moves2 >= 3 and check_winner(board, 1)
    elif n_moves1 == n_moves2 + 1:
        # check first player only
        winner1 = n_moves1 >= 3 and check_winner(board, 0)
    elif n_moves2 == n_moves1 + 1:
        # check second player only
        winner2 = n_moves2 >= 3 and check_winner(board, 1)
    else:
        # invalid board
        raise ValueError('Invalid board')

    if winner1 and winner2:
        raise ValueError('Invalid board')

    if winner1:
        return 0

    if winner2:
        return 1

    return None


def check_winner(board, player):
    for i in range(3):
        if check_row(board, i, player):
            return True

        if check_col(board, i, player):
            return True

        if check_diag(board, player):
            return True

        if check_reverse_diag(board, player):
            return True

    return False


def check_row(board, row, player):
    for j in range(3):
        if board[row][j] != player:
            return False

    return True


def check_col(board, col, player):
    for i in range(3):
        if board[i][col] != player:
            return False

    return True


def check_diag(board, player):
    for i in range(3):
        if board[i][i] != player:
            return False

    return True


def check_reverse_diag(board, player):
    for i in range(3):
        if board[i][len(board) - 1 - i] != player:
            return False

    return True


class TicTacWinTest(unittest.TestCase):
    def test_tic_tac_win(self):
        test_cases = [
            (
                [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                ],
                None
            ),
            (
                [
                    [None, None, None],
                    [None,    0, None],
                    [None, None, None]
                ],
                None
            ),
            (
                [
                    [1, 1, 0],
                    [0, 0, 1],
                    [1, 0, 0]
                ],
                None
            ),
            (
                [
                    [   1, 1,    1],
                    [None, 0, None],
                    [None, 0,    0]
                ],
                1
            ),
            (
                [
                    [   1, 1,    None],
                    [None,    0,    1],
                    [   1, None,    0]
                ],
                ValueError
            ),
        ]

        for board, expected in test_cases:
            if inspect.isclass(expected):
                with self.assertRaises(expected):
                    tic_tac_win(board)
            elif expected is None:
                actual = tic_tac_win(board)
                self.assertIsNone(actual)
            else:
                actual = tic_tac_win(board)
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
