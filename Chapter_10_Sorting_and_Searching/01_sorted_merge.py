import unittest


def sorted_merge(a, b):
    '''
    10.1 Sorted Merge: You are given two sorted arrays, A and B, 
    where A has a large enough buffer at the end to hold B. Write 
    a method to merge B into A in sorted order.
    '''
    i = len(a) - 1

    while a[i] is None:
        i -= 1

    j = len(b) - 1
    cur_index = i + len(b)

    while i >= 0 and j >= 0:
        if a[i] < b[j]:
            a[cur_index] = b[j]
            j -= 1
        else:
            a[cur_index] = a[i]
            i -= 1

        cur_index -= 1

    while i >= 0:
        a[cur_index] = a[i]
        i -= 1
        cur_index -= 1

    while j >= 0:
        a[cur_index] = b[j]
        j -= 1
        cur_index -= 1


class SortedMergeTest(unittest.TestCase):
    def test_sorted_merge(self):
        a = [1, 4, 6, 7, 9, None, None, None, None, None]
        b = [3, 5, 7, 8]
        sorted_merge(a, b)
        self.assertEqual([1, 3, 4, 5, 6, 7, 7, 8, 9, None], a)


if __name__ == '__main__':
    unittest.main()
