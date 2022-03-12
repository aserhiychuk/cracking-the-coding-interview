import unittest


def check_permutation(s1, s2):
    '''
    1.2 Check permutation: Given two strings, write a method to decide if one is a permutation of the other.
    '''
    if not s1 and not s2:
        return True

    if s1 and not (s2):
        return False

    if not s1 and s2:
        return False

    if len(s1) != len(s2):
        return False

    d1 = {}

    for c in s1:
        count = d1.get(c, 0)
        d1[c] = count + 1

    d2 = {}

    for c in s2:
        count = d2.get(c, 0)
        d2[c] = count + 1

    if len(d1) != len(d2):
        return False

    for c, count1 in d1.items():
        count2 = d2.get(c, 0)

        if count1 != count2:
            return False

    return True


class CheckPermutationTest(unittest.TestCase):
    def test_true(self):
        test_cases = [
            (None, None),
            (None, ''),
            ('', None),
            ('abc', 'cba'),
            ('aaab', 'abaa')
        ]
        
        for s1, s2 in test_cases:
            actual = check_permutation(s1, s2)
            self.assertTrue(actual)

    def test_false(self):
        test_cases = [
            ('abc', ''),
            ('abc', 'abcc')
        ]
        
        for s1, s2 in test_cases:
            actual = check_permutation(s1, s2)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
