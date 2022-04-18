import unittest


def pairs_with_sum(array, target):
    '''
    16.24 Pairs with Sum: Design an algorithm to find all pairs of 
    integers within an array which sum to a specified value.
    '''
    complements = {}

    for n in array:
        complement = target - n

        if complement not in complements:
            complements[complement] = 0

        count = complements[complement]
        complements[complement] = count + 1

    result = set()

    for n in array:
        complement = target - n

        if complement in complements and n <= complement:
            if n == complement and complements[complement] < 2:
                # avoid pairs like (n, n) when n occurs in array only sonce
                continue

            result.add((n, complement))

    return result


class PairsWithSumTest(unittest.TestCase):
    def test_pairs_with_sum(self):
        test_cases = [
            ([-2, 3, 0, 1, 4, 2, -1], 2, {(-2, 4), (-1, 3), (0, 2)}),
            ([-1, 1, 2, 0, 3, -2, 4, 1], 2, {(-2, 4), (-1, 3), (0, 2), (1, 1)}),
        ]

        for array, target, expected in test_cases:
            actual = pairs_with_sum(array, target)
            self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
