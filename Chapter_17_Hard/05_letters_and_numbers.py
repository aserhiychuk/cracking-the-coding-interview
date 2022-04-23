import unittest


def letters_and_numbers(array):
    '''
    17.5 Letters and Numbers: Given an array filled with letters and numbers, 
    find the longest subarray with an equal number of letters and numbers.
    '''

    # array:       x  z -5 4  d -2  g  t  4  a  q  w  p  7  8  n
    # array_bool:  1  1  0 0  1  0  1  1  0  1  1  1  1  0  0  1   
    # zeros:       0  0  1 2  2  3  3  3  4  4  4  4  4  5  6  6
    # ones:        1  2  2 2  3  3  4  5  5  6  7  8  9  9  9 10
    # diff:       -1 -2 -1 0 -1  0 -1 -2 -1 -2 -3 -4 -5 -4 -3 -4
    array_bool = [isinstance(a, str) for a in array]

    zeros = [0] * len(array_bool)
    n_zeros = 0
    ones = [0] * len(array_bool)
    n_ones = 0

    for i in range(len(array_bool)):
        if array_bool[i] is False:
            n_zeros += 1
        else:
            n_ones += 1

        zeros[i] = n_zeros
        ones[i] = n_ones

    diff = [n_zeros - n_ones for n_zeros, n_ones in zip(zeros, ones)]

    occurances = {}

    for i in range(len(diff)):
        el = diff[i]

        if el not in occurances:
            index = i
            length = 0
        else:
            index, _ = occurances[el]
            length = i - index

        occurances[el] = (index, length)

    max_length = 0

    for _, (index, length) in occurances.items():
        if max_length <= length:
            max_length = length

    min_index = len(array) - 1

    for _, (index, length) in occurances.items():
        if length == max_length and index < min_index:
            min_index = index

    return array[min_index + 1:min_index + 1 + max_length]


class LettersAndNumbersTest(unittest.TestCase):
    def test_letters_and_numbers(self):
        array = ['x', 'z', -5, 4, 'd', -2, 'g', 't', 4, 'a', 'q', 'w', 'p', 7, 8, 'n']
        actual = letters_and_numbers(array)
        expected = ['z', -5, 4, 'd', -2, 'g', 't', 4]

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
