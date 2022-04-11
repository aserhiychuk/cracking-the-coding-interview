import unittest


def number_max(a, b):
    '''
    16.7 Number Max: Write a method that finds the maximum of two numbers. 
    You should not use if-else or any other comparison operator.
    '''
    diff = a - b

    try:
        sign = diff / abs(diff)
    except ZeroDivisionError:
        # numbers are equal
        return a

    index = int((sign + 1) / 2)
    array = [b, a]

    return array[index]


class NumberMaxTest(unittest.TestCase):
    def test_number_max(self):
        test_cases = [
            (15.1234, 4.23, 15.1234),
            (4.23, 15.1234, 15.1234),
            (4.23, 4.23, 4.23),
            (-15.1234, 4.23, 4.23),
            (4.23, -15.1234, 4.23),
            (-15.1234, -15.1234, -15.1234),
            (-15.1234, -4.23, -4.23),
            (-4.23, -15.1234, -4.23)
        ]

        for a, b, expected in test_cases:
            actual = number_max(a, b)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
