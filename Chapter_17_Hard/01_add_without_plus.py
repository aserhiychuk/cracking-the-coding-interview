import unittest


def add_without_plus(a, b):
    '''
    17.1 Add Without Plus: Write a function that adds two numbers. 
    You should not use + or any arithmetic operators.
    '''
    result, memory = _add(a, b)

    while memory != 0:
        result, memory = _add(result, memory)

    return result


def _add(a, b):
    result = a ^ b
    memory = a & b
    memory <<= 1

    return result, memory


class AddWithoutPlusTest(unittest.TestCase):
    def test_add_without_plus(self):
        test_cases = [
            (7, 5),
            (-7, 5),
            (7, 0),
            (1, 2),
            (8, 8)
        ]

        for a, b in test_cases:
            actual = add_without_plus(a, b)
            self.assertEqual(a + b, actual)


if __name__ == '__main__':
    unittest.main()
