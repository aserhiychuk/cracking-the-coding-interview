import unittest


def recursive_multiply(a, b):
    '''
    8.5 Recursive Multiply: Write a recursive function to multiply two 
    positive integers without using the * operator. You can use addition, 
    subtraction, and bit shifting, but you should minimize the number of 
    those operations.
    '''
    if b == 1:
        return a

    result = recursive_multiply(a, b >> 1)
    result = result << 1

    if b - (b >> 1 << 1) == 1:
        # b is an odd number
        result += a

    return result


class RecursiveMultiplyTest(unittest.TestCase):
    def test_recursive_multiply(self):
        test_cases = [
            (5, 7),
            (3, 1),
            (2, 3),
            (6, 14),
            (9, 8),
            (15, 34),
            (16, 14),
            (13, 25)
        ]

        for a, b in test_cases:
            actual = recursive_multiply(a, b)
            self.assertEqual(a * b, actual)


if __name__ == '__main__':
    unittest.main()
