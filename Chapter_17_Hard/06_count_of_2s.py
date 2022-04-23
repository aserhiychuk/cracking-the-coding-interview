import math
import unittest


def count_of_2s(n):
    '''
    17.6 Count of 2s: Write a method to count the number of 2s 
    that appear in all the numbers between 0 and n (inclusive).

    EXAMPLE
    Input: 25
    Output: 9 (2, 12, 20, 21, 22, 23, 24 and 25. Note that 22 counts for two 2s.)
    '''
    n_10s = math.log(n, 10)
    n_10s = math.ceil(n_10s)

    result = 0

    for i in range(n_10s):
        digit = n // 10**i
        digit %= 10

        result += (n // 10**(i + 1)) * 10**i

        if digit == 2:
            result += n % 10**i + 1
        elif digit > 2:
            result += 10**i

    return result


class CountOf2sTest(unittest.TestCase):
    def test_count_of_2s(self):
        for n in range(1, 1000):
            actual = count_of_2s(n)
            self.assertEqual(self._expected(n), actual)

    def _expected(self, n):
        result = 0

        for i in range(n + 1):
            result += len([d for d in str(i) if d == '2'])

        return result


if __name__ == '__main__':
    unittest.main()
