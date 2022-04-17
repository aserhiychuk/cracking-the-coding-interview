import unittest


def sum_swap(array1, array2):
    '''
    16.21 Sum Swap: Given two arrays of integers, find a pair of values 
    (one value from each array) that you can swap to give the two arrays 
    the same sum.

    EXAMPLE
    Input: {4, 1, 2, 1, 1, 2} and {3, 6, 3, 3}
    Output: {1, 3}
    '''
    sum1 = sum(array1)
    sum2 = sum(array2)
    # sum1 - a + b = sum2 - b + a
    # -2 * a + 2 * b = sum2 - sum1
    # b = a + (sum2 - sum1) / 2
    array2_unique = set(array2)

    for a in array1:
        b = a + (sum2 - sum1) / 2

        if b in array2_unique:
            return a, b

    return None


class SumSwapTest(unittest.TestCase):
    def test_sum_swap(self):
        test_cases = [
            ([4, 1, 2, 1, 1, 2], [3, 6, 3, 3], (4, 6)),
            ([4, 1, 2, 1, 1, 2], [3, 1, 5, 4, 2], (1, 3)),
            ([4, 1, 2, 1, 1, 3], [3, 1, 5, 4, 2], None),
        ]

        for array1, array2, expected in test_cases:
            actual = sum_swap(array1, array2)

            if expected is None:
                self.assertIsNone(actual)
            else:
                self.assertTupleEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
