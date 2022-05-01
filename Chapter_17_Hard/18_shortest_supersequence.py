from collections import Counter
from queue import Queue
import unittest


def shortest_supersequence(shorter, longer):
    '''
    17.18 Shortest Supersequence: You are given two arrays, one shorter 
    (with all distinct elements) and one longer. Find the shortest subarray 
    in the longer array that contains all the elements in the shorter array. 
    The items can appear in any order.

    EXAMPLE
    Input: {1, 5, 9} | {7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7}
    Output: [7, 10]
    '''
    shorter = set(shorter)
    counter = Counter()
    queue = Queue()
    result = None
    i = 0

    while i < len(longer):
        while i < len(longer) and len(counter) < len(shorter):
            if longer[i] in shorter:
                queue.put(i)
                counter[longer[i]] += 1

            i += 1

        if len(counter) < len(shorter):
            break

        start = queue.get()
        counter[longer[start]] -= 1

        if counter[longer[start]] == 0:
            del counter[longer[start]]

        end = i - 1

        if result is None or end - start < result[1] - result[0]:
            result = start, end

    return result


class ShortestSupersequenceTest(unittest.TestCase):
    def test_shortest_supersequence(self):
        shorter = [1, 5, 9]
        longer = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]

        actual = shortest_supersequence(shorter, longer)
        expected = (7, 10)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
