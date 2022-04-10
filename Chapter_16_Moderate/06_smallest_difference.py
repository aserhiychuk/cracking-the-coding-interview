import unittest


def smallest_difference(array1, array2):
    '''
    16.6 Smallest Difference: Given two arrays of integers, compute 
    the pair of values (one value in each array) with the smallest 
    (non-negative) difference. Return the difference.

    EXAMPLE
    Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
    Output: 3. That is, the pair (11, 8).
    '''
    array1 = sorted(array1)
    array2 = sorted(array2)

    result = None
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        diff = array1[i] - array2[j]

        if diff < 0:
            i += 1
        else:
            if result is None or diff < result:
                result = diff

            j += 1

    return result


class SmallestDifferenceTest(unittest.TestCase):
    def test_smallest_difference(self):
        test_cases = [
            ([30, 1, 3, 15, 11, 2], [23, 4, 127, 235, 5, 7, 19, 8], 3),
            ([30, 1, 3, 15, 11, 2], [23, 4, 127, 14, 235, 5, 7, 19, 8], 1)
        ]

        for array1, array2, expected in test_cases:
            actual = smallest_difference(array1, array2)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
