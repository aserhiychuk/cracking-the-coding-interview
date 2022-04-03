import unittest


def permutations_with_dups(s):
    '''
    8.8 Permutations with Dups: Write a method to compute all permutations 
    of a string whose characters are not necessarily unique. The list of 
    permutations should not have duplicates.
    '''
    unique_chars = {}

    for c in s:
        count = unique_chars.get(c, 0)
        unique_chars[c] = count + 1

    result = []

    _permutations_with_dups('', len(s), unique_chars, result)

    return result


def _permutations_with_dups(prefix, remaining, unique_chars, result):
    if remaining == 0:
        result.append(prefix)
        return

    for c in unique_chars:
        count = unique_chars[c]

        if count > 0:
            unique_chars[c] -= 1
            _permutations_with_dups(prefix + c, remaining - 1, unique_chars, result)
            unique_chars[c] = count


class PermutationsWithDupsTest(unittest.TestCase):
    def test_permutations_with_dups(self):
        actual = permutations_with_dups('abcc')
        actual = sorted(actual)
        expected = sorted(['cabc', 'cbac', 'cbca', 'cacb', 'ccab', 'ccba', \
            'acbc', 'bcac', 'bcca', 'accb', 'abcc', 'bacc'])
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
