import unittest


def power_set(s):
    '''
    8.4 Power Set: Write a method to return all subsets of a set.
    '''
    if not s:
        return [[]]

    result1 = power_set(s[:-1])
    result2 = [el + [s[-1]] for el in result1]

    return result1 + result2


class PowerSetTest(unittest.TestCase):
    def test_power_set(self):
        actual = power_set(['a', 'b', 'c'])
        expected = [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], \
            ['b', 'c'], ['a', 'b', 'c']]
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
