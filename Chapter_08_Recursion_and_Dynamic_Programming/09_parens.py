import unittest


def parens(n):
    '''
    8.9 Parens: implement an algorithm to print all valid (e.g., properly 
    opened and closed) combinations of n pairs of parentheses.

    EXAMPLE
    Input: 3
    Output: ((())), (()()), (())(), ()(()), ()()()
    '''
    result = _parens(['('], n - 1, n)

    return result


def _parens(result, n_opened, n_closed):
    if n_opened == 0 and n_closed == 0:
        return result

    result_opened = []

    if n_opened > 0:
        result_opened = _parens([r + '(' for r in result], n_opened - 1, n_closed)

    result_closed = []

    if n_closed > n_opened:
        result_closed = _parens([r + ')' for r in result], n_opened, n_closed - 1)

    return result_opened + result_closed


class ParensTest(unittest.TestCase):
    def test_parens(self):
        actual = parens(3)
        actual = set(actual)
        expected = set(['((()))', '(()())', '(())()', '()(())', '()()()'])
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
