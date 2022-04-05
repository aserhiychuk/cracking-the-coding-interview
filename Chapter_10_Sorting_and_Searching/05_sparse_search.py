import unittest


def sparse_search(array, element):
    '''
    10.5 Sparse Search: Given a sorted array of strings that is interspersed with 
    empty strings, write a method to find the location of a given string.

    EXAMPLE
    Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
    Output: 4
    '''
    return _binary_search(array, element, 0, len(array) - 1)


def _binary_search(array, element, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        while mid >= 0 and array[mid] == '':
            mid -= 1

        if mid == -1:
            return -1

        if element < array[mid]:
            high = mid - 1
        elif array[mid] < element:
            low = mid + 1

            while low <= high and array[low] == '':
                low += 1
        else:
            return mid

    return -1


class SparseSearchTest(unittest.TestCase):
    def test_sparse_search(self):
        array = ['', 'at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
        test_cases = [
            ('apple', -1),
            ('at', 1),
            ('ball', 5),
            ('dad', 11),
            ('zebra', -1)
        ]

        for element, expected in test_cases:
            actual = sparse_search(array, element)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
