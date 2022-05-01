from math import sqrt
import unittest


def missing_two(array):
    '''
    17.19 Missing Two: You are given an array with all the numbers 
    from 1 to N appearing exactly once, except for one number that 
    is missing. How can you find the missing number in 0(N) time 
    and 0(1) space? What if there were two numbers missing?
    '''
    n = len(array) + 2

    # x + y = s
    # y = s - x
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(array)
    s = expected_sum - actual_sum

    # (x / 2^x) * (y / 2^y) = p
    # x * y = p * 2^x * 2^y
    # x * (s - x) = p * 2^x * 2^(s - x)
    # x * s - x^2 = p * 2^x * 2^s / 2^x
    # x * s - x^2 = p * 2^s
    # x^2 - s * x + p * 2^s = 0
    # x = (s - sqrt(s^2 - 4 * p * 2^s)) / 2
    p = 1

    for i in range(1, n + 1):
        p *= i / 2**i

    for a in array:
        p /= a
        p *= 2**a

    x = (s - sqrt(s**2 - 4 * p * 2**s)) // 2
    x = int(x)
    y = s - x

    return {x, y}


class MissingTwoTest(unittest.TestCase):
    def test_missing_two(self):
        array = [11, 17, 14, 4, 13, 9, 16, 20, 6, 1, 19, 7, 15, 5, 2, 12, 10, 3, 18, 8]
        expected = {7, 15}

        for e in expected:
            array.remove(e)

        actual = missing_two(array)
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
