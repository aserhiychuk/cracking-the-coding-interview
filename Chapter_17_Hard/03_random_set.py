from random import random
import unittest


def random_set(array, m):
    '''
    17.3 Random Set: Write a method to randomly generate a set 
    of m integers from an array of size n. Each element must have 
    equal probability of being chosen.
    '''
    element_count = {}

    for el in array:
        if el not in element_count:
            element_count[el] = 0

        count = element_count[el]
        element_count[el] = count + 1

    total_count = len(array)
    array = list(element_count.items())
    result = set()

    for _ in range(m):
        rnd = random()
        running_count = 0

        for i in range(len(array)):
            el, count = array[i]
            running_count += count

            if rnd < running_count / total_count:
                result.add(el)
                array[i] = (el, 0)
                total_count -= count
                break

    return result


class RandomSetTest(unittest.TestCase):
    def test_random_set(self):
        array = [2, 5, 6, 2, 8, 1, 7, 7, 4, 2, 9, 7, 0, 3, 4, 2]
        test_cases = [1, 2, 3, 4, 5]

        for m in test_cases:
            actual = random_set(array, m)
            self.assertEqual(m, len(actual))
            self.assertTrue(actual.issubset(set(array)))


if __name__ == '__main__':
    unittest.main()
