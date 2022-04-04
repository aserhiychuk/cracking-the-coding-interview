import unittest


def search_in_rotated_array(array, element):
    '''
    10.3 Search in Rotated Array: Given a sorted array of n integers that has been 
    rotated an unknown number of times, write code to find an element in the array. 
    You may assume that the array was originally sorted in increasing order,

    EXAMPLE
    Input: find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    Output: 8 (the index of 5 in the array)
    '''
    return _binary_search(array, element, 0, len(array) - 1)


def _binary_search(array, element, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == element:
            return mid

        if array[low] <= array[mid]:
            # [15, 16, 19, 20, 25, 26, 27, 28, 1, 3, 4, 5]
            if array[low] <= element and element < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # [15, 16, 19, 20, 0, 1, 3, 4, 5, 7, 10, 14]
            if array[mid] < element and element <= array[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


class SearchInRotatedArrayTest(unittest.TestCase):
    def test_search_in_rotated_array(self):
        array1 = [15, 16, 19, 20, 25, 26, 27, 28, 1, 3, 4, 5]
        array2 = [15, 16, 19, 20, 0, 1, 3, 4, 5, 7, 10, 14]
        test_cases = [
            (array1, 25, 4),
            (array1, 26, 5),
            (array1, 28, 7),
            (array1, 1, 8),
            (array1, 5, 11),
            (array1, -5, -1),
            (array1, 6, -1),
            (array1, 14, -1),

            (array2, 19, 2),
            (array2, 20, 3),
            (array2, 0, 4),
            (array2, 5, 8),
            (array2, 14, 11),
            (array2, -5, -1),
            (array2, 11, -1),
            (array2, 30, -1)
        ]

        for array, element, expected in test_cases:
            actual = search_in_rotated_array(array, element)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
