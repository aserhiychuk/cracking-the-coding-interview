import math
import unittest


def missing_number(array):
    '''
    17.4 Missing Number: An array A contains all the integers from 0 to n, 
    except for one number which is missing. In this problem, we cannot 
    access an entire integer in A with a single operation. The elements of 
    A are represented in binary, and the only operation we can use to access 
    them is "fetch the jth bit of A[i]", which takes constant time. Write 
    code to find the missing integer. Can you do it in 0(n) time?
    '''
    n = len(array)
    n_bits = math.log(n, 2)
    n_bits = math.ceil(n_bits)
    expected = [None] * n_bits

    for i in range(n_bits):
        group_length = 2**(i + 1)

        # number of 0s in all groups but last
        a = (n + 1) // group_length
        n_zeros = a * group_length // 2

        # number of 0s in the last group
        b = (n + 1) % group_length
        n_zeros += min(b, group_length // 2)

        expected[i] = n_zeros

    actual = [0] * n_bits

    for i in range(len(array)):
        for j in range(n_bits):
            bit = _get_bit(array, i, j)

            actual[j] += 1 - bit

    result = [1 - (e - a) for e, a in zip(expected, actual)]
    result = [result[i] * 2**i for i in range(len(result))]
    result = sum(result)

    return result


def _get_bit(array, i, j):
    mask = 1 << j

    return int(array[i] & mask > 0)


class MissingNumberTest(unittest.TestCase):
    def test_missing_number(self):
        n = 15

        for expected in range(1, n):
            array = list(range(n + 1))
            array.remove(expected)

            actual = missing_number(array)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
