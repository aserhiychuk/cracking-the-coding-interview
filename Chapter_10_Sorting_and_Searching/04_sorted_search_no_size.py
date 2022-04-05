import unittest


def sorted_search_no_size(listy, x):
    '''
    10.4 Sorted Search, No Size: You are given an array-like data structure 
    Listy which lacks a size method. It does, however, have an elementAt(i) 
    method that returns the element at index i in 0(1) time. If i is beyond 
    the bounds of the data structure, it returns -1. (For this reason, the data
    structure only supports positive integers.) Given a Listy which contains 
    sorted, positive integers, find the index at which an element x occurs. If 
    x occurs multiple times, you may return any index.
    '''
    length = 1

    while listy.element_at(length - 1) != -1:
        length *= 2

    return _binary_search(listy, x, 0, length - 1)


def _binary_search(listy, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        mid_element = listy.element_at(mid)

        if mid_element == -1:
            high = mid - 1
        elif x < mid_element:
            high = mid - 1
        elif mid_element < x:
            low = mid + 1
        else:
            return mid

    return -1


class Listy:
    def __init__(self, array):
        self._array = array

    def element_at(self, i):
        if i < 0 or len(self._array) - 1 < i:
            return -1

        return self._array[i]


class SortedSearchNoSizeTest(unittest.TestCase):
    def test_sorted_search_no_size(self):
        listy = Listy(list(range(1, 101)))
        test_cases = [
            (1, 0),
            (7, 6),
            (45, 44),
            (100, 99),
            (101, -1),
            (1000, -1)
        ]

        for x, expected in test_cases:
            actual = sorted_search_no_size(listy, x)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
