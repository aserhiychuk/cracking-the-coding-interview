from random import randint
import unittest


def rand7_from_rand5():
    '''
    16.23 Rand7 from Rand5: Implement a method rand7() given rand5(). That is, 
    given a method that generates a random number between 0 and 4 (inclusive), 
    write a method that generates a random number between 0 and 6 (inclusive).
    '''
    while True:
        n = 5 * _rand5() + _rand5()

        if n < 21:
            return n % 7


def _rand5():
    return randint(0, 4)


class Rand7FromRand5Test(unittest.TestCase):
    def test_rand7_from_rand5(self):
        counts = [0] * 7

        for _ in range(100000):
            n = rand7_from_rand5()
            counts[n] = counts[n] + 1

        total_count = sum(counts)
        probs = [count / total_count for count in counts]
        expected_prob = 1 / 7
        max_deviation = 0.1

        for actual_prob in probs:
            deviation = abs((expected_prob - actual_prob) / expected_prob)
            self.assertLess(deviation, max_deviation)


if __name__ == '__main__':
    unittest.main()
