import unittest


def is_one_away(s1, s2):
    '''
    1.5 One Away: There are three types of edits that can be performed on strings:
    insert a character, remove a character, or replace a character. Given two strings,
    write a function to check if they are one edit (or zero edits) away.

    EXAMPLE
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
    '''
    if len(s1) == len(s2):
        # check replace
        n_diff = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                n_diff += 1

        return n_diff <= 1
    elif abs(len(s1) - len(s2)) == 1:
        if len(s1) == len(s2) - 1:
            # s1 is longer
            s1, s2 = s2, s1

        # check insert in s1
        offset = 0

        for i in range(len(s2)):
            if s1[i + offset] != s2[i]:
                offset += 1

                if offset > 1:
                    return False
    else:
        return False

    return True


class IsOneAwayTest(unittest.TestCase):
    def test_true(self):
        test_cases = [
            ('pale', 'ple'),
            ('ple', 'pale'),
            ('pale', 'pales'),
            ('pale', 'bale')
        ]
        
        for s1, s2 in test_cases:
            actual = is_one_away(s1, s2)
            self.assertTrue(actual)

    def test_false(self):
        test_cases = [
            ('pale', 'bake'),
            ('pale', 'paless'),
            ('__pale', 'pale'),
            ('pale', '__pale'),
            ('_pale', 'pale_'),
            ('pale_', '_pale')
        ]

        for s1, s2 in test_cases:
            actual = is_one_away(s1, s2)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
