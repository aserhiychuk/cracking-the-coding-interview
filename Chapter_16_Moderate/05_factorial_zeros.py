import unittest


def factorial_zeros(n):
    '''
    16.5 Factorial Zeros: Write an algorithm which computes the number 
    of trailing zeros in n factorial.
    '''
    n_zeros = 0
    divider = 5

    while divider <= n:
        # how many numbers are divisible by 5, 25, 125, ...
        n_zeros += n // divider
        divider *= 5

    return n_zeros


class FactorialZerosTest(unittest.TestCase):
    def test_factorial_zeros(self):
        test_cases = [
            (3, 0),
            (5, 1),
            (8, 1),
            (10, 2),
            (15, 3),
            (20, 4),
            (25, 6),
            (50, 12),
            (100, 24),
            (125, 31)
        ]

        for n, expected in test_cases:
            actual = factorial_zeros(n)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
