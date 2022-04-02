import unittest


def coins(n):
    '''
    8.11 Given an infinite number of quarters (25 cents), dimes (10 cents), 
    nickels (5 cents), and pennies (1 cent), write code to calculate the number 
    of ways of representing n cents.
    '''
    return _coins(n, 0, 0, 0, 0)


def _coins(n, a, b, c, d):
    if 25 * a + 10 * b + 5 * c + 1 * d == n:
        return 1

    result = 0

    if 25 * (a + 1) + 10 * b + 5 * c + 1 * d <= n and b == 0 and c == 0 and d == 0:
        result += _coins(n, a + 1, b, c, d)

    if 25 * a + 10 * (b + 1) + 5 * c + 1 * d <= n and c == 0 and d == 0:
        result += _coins(n, a, b + 1, c, d)

    if 25 * a + 10 * b + 5 * (c + 1) + 1 * d <= n and d == 0:
        result += _coins(n, a, b, c + 1, d)

    if 25 * a + 10 * b + 5 * c + 1 * (d + 1) <= n:
        result += _coins(n, a, b, c, d + 1)

    return result


class CoinsTest(unittest.TestCase):
    def test_coins(self):
        test_cases = [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 2),
            (6, 2),
            (7, 2),
            (8, 2),
            (9, 2),
            (10, 4),
            (25, 13),
            (50, 49),
            (100, 242),
            (101, 242)
        ]

        for n, expected in test_cases:
            actual = coins(n)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
