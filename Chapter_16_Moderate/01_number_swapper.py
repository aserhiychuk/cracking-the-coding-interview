import unittest


def number_swapper(a, b):
    '''
    16.1 Number Swapper: Write a function to swap a number in place 
    (that is, without temporary variables).
    '''
    # Solution 1
    a = a - b
    b = a + b
    a = b - a

    # Solution 2
    # a = a ^ b
    # b = a ^ b
    # a = a ^ b

    return a, b


class NumberSwapperTest(unittest.TestCase):
    def test_number_swapper(self):
        test_cases = [
            (0, 0),
            (0, 6),
            (3, 0),
            (6, 11)
        ]

        for a, b in test_cases:
            actual_a, actual_b = number_swapper(a, b)
            self.assertEqual(b, actual_a)
            self.assertEqual(a, actual_b)


if __name__ == '__main__':
    unittest.main()
