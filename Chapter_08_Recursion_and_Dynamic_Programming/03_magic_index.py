import unittest


def magic_index(array):
    '''
    8.3 Magic Index: A magic index in an array A[0 ... n-1] is defined to be 
    an index such that A[i] = i. Given a sorted array of distinct integers, 
    write a method to find a magic index, if one exists, in array A.

    FOLLOW UP
    What if the values are not distinct?
    '''
    return _magic_index(array, 0, len(array))


def _magic_index(array, low, high):
    if low >= high:
        return None

    if high - low == 1:
        return low if array[low] == low else None

    mid = (low + high) // 2

    if array[mid] == mid:
        return mid

    if array[mid] < mid:
        return _magic_index(array, mid + 1, high)

    return _magic_index(array, low, mid)


class MagicIndexTest(unittest.TestCase):
    def test_magic_index(self):
        actual = magic_index([4, 5, 6, 7, 8])
        self.assertIsNone(actual)

        actual = magic_index([4, 5, 6, 7, 8, 9])
        self.assertIsNone(actual)

        actual = magic_index([-1, 1, 3, 4, 5])
        self.assertEqual(1, actual)

        actual = magic_index([-1, 1, 3, 4, 5, 8])
        self.assertEqual(1, actual)

        actual = magic_index([0, 2, 3, 4, 5, 8])
        self.assertEqual(0, actual)

        actual = magic_index([-1, 0, 1, 2, 4, 5])
        self.assertEqual(5, actual)


def magic_index_followup(array):
    return _magic_index_followup(array, 0, len(array))


def _magic_index_followup(array, low, high):
    if low >= high:
        return None

    if high - low == 1:
        return low if array[low] == low else None

    mid = (low + high) // 2

    mid_start = mid
    mid_end = mid

    while low < mid_start and array[mid_start - 1] == array[mid]:
        mid_start -= 1

    while mid_end < high - 1 and array[mid] == array[mid_end + 1]:
        mid_end += 1

    if mid_start <= array[mid] and array[mid] <= mid_end:
        return array[mid]

    if array[mid] < mid_start:
        return _magic_index_followup(array, mid_end + 1, high)

    return _magic_index_followup(array, low, mid_start)


class MagicIndexFollowupTest(unittest.TestCase):
    def test_magic_index_followup(self):
        actual = magic_index_followup([7, 7, 7, 7])
        self.assertIsNone(actual)

        actual = magic_index_followup([7, 7, 7, 7, 7])
        self.assertIsNone(actual)

        actual = magic_index_followup([-1, 0, 3, 3, 5])
        self.assertEqual(3, actual)

        actual = magic_index_followup([-1, 1, 1, 4, 5, 8])
        self.assertEqual(1, actual)

        actual = magic_index_followup([0, 0, 0, 0, 5, 8])
        self.assertEqual(0, actual)

        actual = magic_index_followup([-1, 0, 1, 2, 5, 5])
        self.assertEqual(5, actual)


if __name__ == '__main__':
    unittest.main()
