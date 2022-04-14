import unittest


'''
16.9 Operations: Write methods to implement the multiply, subtract, 
and divide operations for integers. The results of all of these are 
integers. Use only the add operator, but not minus, times or divide.
'''


def _negate(a):
    return ~a + 1


def multiply(a, b):
    '''
    7 * 39 = 7 * (32 + 4 + 2 + 1) = 
    = 7 * (2^5 + 2^2 + 2^1 + 2^0) = 
    = 7 * 2^5 + 7 * 2^2 + 7 * 2^1 + 7 * 2^0 = 
    = 273
    '''
    if a == 0 or b == 0:
        return 0

    if (a < 0 and b > 0) or (a > 0 and b < 0):
        result = multiply(abs(a), abs(b))

        return _negate(result)

    if a < 0 and b < 0:
        return multiply(abs(a), abs(b))

    cache = []
    i = 0
    pow2 = 1
    x = a

    while pow2 <= b:
        cache.append([pow2, x])

        i += 1
        pow2 += pow2
        x += x

    y = 0
    result = 0

    for pow2, x in reversed(cache):
        if y + pow2 <= b:
            y += pow2
            result += x

    return result


def subtract(a, b):
    return a + _negate(b)


def divide(a, b):
    '''
    39 / 7 = 5
    39 = 7 * 5 = 7 * (2^2 + 2^0) = 7 * 2^2 + 7 * 2^0
    '''
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return -divide(abs(a), abs(b))

    if a < 0 and b < 0:
        return divide(abs(a), abs(b))

    if a < b:
        return 0

    cache = []
    i = 0
    pow2 = 1

    while multiply(b, pow2) <= a:
        cache.append(pow2)

        i += 1
        pow2 += pow2

    result = 0
    s = 0

    for pow2 in reversed(cache):
        if s + multiply(b, pow2) <= a:
            result += pow2
            s += multiply(b, pow2)

    return result


class OperationsTest(unittest.TestCase):
    def test_multiply(self):
        test_cases = [
            (0, 39),
            (7, 0),
            (7, 39),
            (39, 7),
            (1, 39),
            (7, 1),
            (8, 56),
            (-7, 39),
            (7, -39),
            (-7, -39)
        ]

        for a, b in test_cases:
            actual = multiply(a, b)
            self.assertEqual(a * b, actual)

    def test_subtract(self):
        test_cases = [
            (8, 8),
            (29, 8),
            (8, 29),
            (8, 0),
            (0, 8),
            (-8, 29),
            (29, -8),
            (-8, -29),
            (-29, -8)
        ]

        for a, b in test_cases:
            actual = subtract(a, b)
            self.assertEqual(a - b, actual)

    def test_divide(self):
        test_cases = [
            (39, 7),
            (7, 39),
            (0, 39),
            (-39, -7)
        ]

        for a, b in test_cases:
            actual = divide(a, b)
            self.assertEqual(a // b, actual)


if __name__ == '__main__':
    unittest.main()
