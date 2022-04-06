import unittest


def find_duplicates(array):
    '''
    10.8 Find Duplicates: You have an array with all the numbers from 1 to N, 
    where N is at most 32,000. The array may have duplicate entries and you 
    do not know what N is. With only 4 kilobytes of memory available, how would 
    you print alt duplicate elements in the array?
    '''
    result = set()
    bits = [0] * 1000

    for a in array:
        # i-th number in "bits" array
        i = a // 32
        # j-th bit in i-th number
        j = a % 32

        b = bits[i]
        mask = 1 << j

        if b & mask > 0:
            result.add(a)

        bits[i] = b | mask

    return result


class FindDuplicatesTest(unittest.TestCase):
    def test_find_duplicates(self):
        actual = find_duplicates([9, 6, 9, 5, 4, 1, 3, 5, 3, 2])
        expected = set([9, 3, 5])
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
