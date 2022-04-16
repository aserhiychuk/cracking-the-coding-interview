import unittest


def sub_sort(array):
    '''
    16.16 Sub Sort: Given an array of integers, write a method to 
    find indices m and n such that if you sorted elements m through n, 
    the entire array would be sorted. Minimize n - m (that is, find 
    the smallest such sequence).

    EXAMPLE
    Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
    Output: (3, 9)
    '''
    m = 0

    while m < len(array) - 1 and array[m] <= array[m + 1]:
        m += 1

    n = len(array) - 1

    while 0 < n and array[n - 1] <= array[n]:
        n -= 1

    if m > n:
        return None, None

    min_index = m
    max_index = m

    for i in range(m, n + 1):
        if array[i] < array[min_index]:
            min_index = i

        if array[max_index] < array[i]:
            max_index = i

    while 0 < m and array[min_index] < array[m - 1]:
        m -= 1

    while n < len(array) - 1 and array[n + 1] < array[max_index]:
        n += 1

    return m, n


class SubSortTest(unittest.TestCase):
    def test_sub_sort(self):
        test_cases = [
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], (None, None)),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], (0, 9)),
            ([0, 1, 7, 2, 3, 4, 5, 6, 8, 9], (2, 7)),
            ([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], (3, 9)),
            ([1, 2, 4, 9, 11, 7, 5, 14, 6, 10, 21, 22, 23], (3, 9)),
            ([1, 2, 4, 7, 10, 11, 7, 5, 14, 12, 6, 7, 16, 18, 19], (3, 11))
        ]

        for array, expected in test_cases:
            actual = sub_sort(array)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
