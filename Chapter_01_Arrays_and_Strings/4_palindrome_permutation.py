import unittest


def is_permutation_of_palindrome(s):
    '''
    1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

    EXAMPLE
    Input: 'Tact Coa'
    Output: True (permutations: "taco cat", "atco eta", etc.)
    '''
    if not s:
        return True

    s = s.lower()
    
    d = {}

    for c in s:
        if c != ' ':
            count = d.get(c, 0)
            d[c] = count + 1

    n_odd = 0

    for c, count in d.items():
        if count % 2 != 0:
            n_odd += 1

    return n_odd <= 1


class IsPermutationOfPalindromeTest(unittest.TestCase):
    def test_true(self):
        test_cases = [
            None,
            '',
            'a',
            'aa',
            'aaa',
            'aAA',
            ' a   a  a     ',
            ' aa   a  a     ',
            'tact coa',
            'Tact Coa',
            'aldkfjhaskldgfa aldkfjhaskldgfa',
            'aldkfjhaskldgfa aldkfjhaskldgfa X'
        ]
        
        for s in test_cases:
            actual = is_permutation_of_palindrome(s)
            self.assertTrue(actual)

    def test_false(self):
        test_cases = [
            'ab',
            'aB',
            'abaa',
            'aldkfjhaskldgfa aldkfjhaskldgfa XY'
        ]
        
        for s in test_cases:
            actual = is_permutation_of_palindrome(s)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
