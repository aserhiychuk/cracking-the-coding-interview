import unittest


def urlify(s, length):
    '''
    1.3 URLify: Write a method to replace all spaces in a string with'%20'. You may assume
    that the string has sufficient space at the end of the string to hold the additional characters,
    and that you are given the "true" length of the string.

    Note: if implementing in Java, please use a character array so that you can perform this operation in place.

    EXAMPLE
    Input: "Mr John Smith ", 13
    Output: "Mr%20John%20Smith"
    '''
    if not s:
        return s

    space = '%20'
    n_spaces = 0

    for i in range(length):
        if s[i] == ' ':
            n_spaces += 1

    s = s[:length + n_spaces * 2]
            
    for i in reversed(range(length)):
        if s[i] == ' ':
            s[i + (n_spaces - 1) * 2:i + (n_spaces - 1) * 2 + len(space)] = space
            n_spaces -= 1
        else:
            s[i + n_spaces * 2] = s[i]

    return s


class UrlifyTest(unittest.TestCase):
    def test_replace_spaces(self):
        test_cases = [
            ('', 0, ''),
            ('a', 1, 'a'),
            ('a   ', 1, 'a'),
            ('abc', 3, 'abc'),
            (' abc   ', 4, '%20abc'),
            ('Mr John Smith          ', 13, 'Mr%20John%20Smith')
        ]

        for s, length, expected in test_cases:
            actual = urlify(list(s), length)
            actual = ''.join(actual)
            self.assertEqual(expected, actual)

            
if __name__ == '__main__':
    unittest.main()
