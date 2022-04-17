import unittest


def pattern_matching(value, pattern):
    '''
    16.18 Pattern Matching: You are given two strings, pattern and value. 
    The pattern string consists of just the letters a and b, describing 
    a pattern within a string. For example, the string catcatgocatgo matches 
    the pattern aabab (where cat is a and go is b). It also matches patterns 
    like a, ab, and b. Write a method to determine if value matches pattern.
    '''
    num_of_a = sum([1 for c in pattern if c == 'a'])

    if num_of_a == 0:
        return True

    num_of_b = sum([1 for c in pattern if c == 'b'])

    if num_of_b == 0:
        return True

    # num_of_a * len_a + num_of_b * len_b = len(value)
    len_b = 1

    while len_b <= len(value) / num_of_b:
        if (len(value) - num_of_b * len_b) % num_of_a == 0:
            len_a = (len(value) - num_of_b * len_b) // num_of_a

            examinee = ''
            patterns = {}
            i = 0

            for c in pattern:
                if c == 'a':
                    if 'a' not in patterns:
                        patterns['a'] = value[i:i + len_a]
                else:
                    if 'b' not in patterns:
                        patterns['b'] = value[i:i + len_b]

                p = patterns[c]
                examinee += p
                i += len(p)

            if value == examinee:
                return True

        len_b += 1

    return False


class PatternMatchingTest(unittest.TestCase):
    def test_pattern_matching(self):
        test_cases = [
            ('catcatgocatgo', 'aabab', True),
            ('catcatgocatgo', 'a', True),
            ('catcatgocatgo', 'ab', True),
            ('catcatgocatgo', 'b', True),
            ('cat_cat_go_cat_go', 'aabab', False),
            ('cat_cat_go_cat_go_', 'aabab', True),
            ('onetwoone', 'aba', True),
            ('onetwoone', 'bab', True),
            ('onetwooneone', 'abab', False),
            ('onetwoonetwo', 'abab', True),
            ('onetwoonethree', 'abab', False),
        ]

        for value, pattern, expected in test_cases:
            actual = pattern_matching(value, pattern)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
