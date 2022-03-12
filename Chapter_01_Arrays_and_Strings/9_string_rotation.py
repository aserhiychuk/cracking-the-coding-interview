import unittest


def is_substring(s1, s2):
    return s1 in s2


def string_rotation(s1, s2):
    '''
    1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
    (e.g. "waterbottle" is a rotation of "erbottlewat").
    '''
    if len(s1) != len(s2):
        return False

    return is_substring(s1, s2 + s2)


class StringRotationTest(unittest.TestCase):
    def test_true(self):
        test_cases = [
            ('waterbottle', 'waterbottle'),
            ('waterbottle', 'erbottlewat'),
            ('asldkfjlaskfd', 'laskfdasldkfj')
        ]

        for s1, s2 in test_cases:
            actual = string_rotation(s1, s2)
            self.assertTrue(actual)

    def test_false(self):
        test_cases = [
            ('a', 'aa'),
            ('a', 'ab'),
            ('abc', 'caa'),
        ]

        for s1, s2 in test_cases:
            actual = string_rotation(s1, s2)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
