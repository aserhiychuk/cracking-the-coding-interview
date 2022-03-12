import unittest


def is_unique(s):
    '''
    1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    '''
    if not s or len(s) < 2:
        return True

    visited = set()

    for c in s:
        if c in visited:
            return False

        visited.add(c)

    return True


def is_unique_followup(s):
    if not s or len(s) < 2:
        return True

    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False

    return True


class IsUniqueTest(unittest.TestCase):
    def test_none(self):
        actual = is_unique(None)
        self.assertTrue(actual)

    def test_empty(self):
        actual = is_unique('')
        self.assertTrue(actual)

    def test_single_character(self):
        actual = is_unique('a')
        self.assertTrue(actual)

    def test_all_unique(self):
        actual = is_unique('ab')
        self.assertTrue(actual)

    def test_duplicate(self):
        actual = is_unique('abcdaf')
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
