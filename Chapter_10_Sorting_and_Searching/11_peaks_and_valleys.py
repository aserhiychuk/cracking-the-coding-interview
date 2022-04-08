import unittest


def peaks_and_valleys(array):
    '''
    10.11 Peaks and Valleys: In an array of integers, a "peak" is an element 
    which is greater than or equal to the adjacent integers and a "valley" is 
    an element which is less than or equal to the adjacent integers. For example, 
    in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. 
    Given an array of integers, sort the array into an alternating sequence of 
    peaks and valleys.

    EXAMPLE
    Input: {5, 3, 1, 2, 3)
    Output: (5, 1, 3, 2, 3}
    '''
    for i in range(len(array) - 2):
        a, b, c = array[i:i + 3]

        if a <= b and b <= c or a >= b and b >= c:
            # asc or desc. swap b and c
            array[i + 1] = c
            array[i + 2] = b


class PeaksAndValleysTest(unittest.TestCase):
    def test_peaks_and_valleys(self):
        test_cases = [
            [5, 3, 1, 2, 3],
            [5, 8, 6, 2, 3, 4, 6],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        ]

        for array in test_cases:
            peaks_and_valleys(array)

            for i in range(len(array) - 2):
                a, b, c = array[i:i + 3]
                self.assertTrue(a <= b and b >= c or a >= b and b <= c)


if __name__ == '__main__':
    unittest.main()
