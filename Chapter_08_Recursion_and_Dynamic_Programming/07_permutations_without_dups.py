import unittest


def permutations_without_dups(s):
    '''
    8.7 Permutations without Dups: Write a method to compute all permutations 
    of a string of unique characters.
    '''
    if not s:
        return ['']

    result = []

    permutations = permutations_without_dups(s[:-1])

    for permutation in permutations:
        if not permutation:
            result.append(s[-1])
        else:
            for j in range(len(permutation) + 1):
                result.append(permutation[:j] + s[-1] + permutation[j:])

    return result


class PermutationsWithoutDupsTest(unittest.TestCase):
    def test_permutations_without_dups(self):
        actual = permutations_without_dups('abc')
        actual = set(actual)
        expected = set(['cba', 'bca', 'bac', 'cab', 'acb', 'abc'])
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
