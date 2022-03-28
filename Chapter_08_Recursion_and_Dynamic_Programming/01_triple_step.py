import unittest


def triple_step(n):
    '''
    8.1 Triple Step: A child is running up a staircase with n steps and can 
    hop either 1 step, 2 steps, or 3 steps at a time, implement a method to 
    count how many possible ways the child can run up the stairs.
    '''
    if n == 0:
        return 0

    result = 1

    if n >= 3:
        result += triple_step(n - 3)

    if n >= 2:
        result += triple_step(n - 2)

    if n >= 1:
        result += triple_step(n - 1)

    return result


class TripleStepTest(unittest.TestCase):
    def test_triple_step(self):
        actual = triple_step(3)
        self.assertEqual(4, actual)

        actual = triple_step(5)
        self.assertEqual(15, actual)

        actual = triple_step(10)
        self.assertEqual(326, actual)


if __name__ == '__main__':
    unittest.main()
