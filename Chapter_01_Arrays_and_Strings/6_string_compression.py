import unittest


def string_compression(s):
    '''
    1.6 String Compression: Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string aabcccccaaa would become a2blc5a3, if the "compressed"
    string would not become smaller than the original string, your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a - z).
    '''
    if not s:
        return s

    compressed = []
    i = 0

    while i < len(s):
        compressed.append(s[i])
        j = 1

        while i + j < len(s) and s[i] == s[i + j]:
            j += 1

        compressed.append(str(j))
        i += j

    if len(s) < len(compressed):
        return s
        
    return ''.join(compressed)


class CompressTest(unittest.TestCase):
    def test_string_compression(self):
        test_cases = [
            (None, None),
            ('', ''),
            ('a', 'a'),
            ('aa', 'a2'),
            ('aaa', 'a3'),
            ('abc', 'abc'),
            ('abbccc', 'a1b2c3'),
        ]

        for s, expected in test_cases:
            actual = string_compression(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
