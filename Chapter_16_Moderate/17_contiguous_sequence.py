import unittest


def contiguous_sequence(array):
    '''
    16.17 Contiguous Sequence: You are given an array of integers 
    (both positive and negative). Find the contiguous sequence 
    with the largest sum. Return the sum.

    EXAMPLE
    Input: 2, -8, 3, -2, 4, -10
    Output: 5 (i.e., {3, -2, 4})
    '''
    max_sum = 0
    running_sum = 0
    i = 0

    while i < len(array):
        while i < len(array) and array[i] < 0:
            running_sum += array[i]
            i += 1

        if running_sum < 0:
            running_sum = 0

        while i < len(array) and array[i] >= 0:
            running_sum += array[i]
            i += 1

        if max_sum < running_sum:
            max_sum = running_sum

    return max_sum


class ContiguousSequenceTest(unittest.TestCase):
    def test_contiguous_sequence(self):
        test_cases = [
            ([2, -8, 3, -2, 4, -10], 5),
            ([1, -10, 3, -2, 3, -2, 1, -1, 2], 4),
            ([1, -10, 3, -2, 3, -2, 1, -5, 8], 8),
            ([5, 4, 3, 2, 1], 15),
            ([-5, -3, 1, -2, -4, -6, -8], 1),
            ([1, 2, 3, -1, -2, -3, 1, 2, 3, 4], 10),
            ([1, 2, 3, -1, -2, 1, 2, 3, 4], 13)
        ]

        for array, expected in test_cases:
            actual = contiguous_sequence(array)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
