import heapq
import unittest


def smallest_k(array, k):
    '''
    17.14 Smallest K: Design an algorithm to find the smallest K 
    numbers in an array.
    '''
    heap = []

    for i in range(k):
        heapq.heappush(heap, -array[i])

    for i in range(k + 1, len(array)):
        if -array[i] > heap[0]:
            heapq.heappushpop(heap, -array[i])

    result = {-h for h in heap}

    return result


class SmallestKTest(unittest.TestCase):
    def test_smallest_k(self):
        array = [14, 34, 61, 86, 60, 22, 19, 59, 35, 94, \
            91, 15, 1, 20, 58, 65, 48, 26, 75, 87]
        k = 5

        actual = smallest_k(array, k)
        expected = {1, 14, 15, 19, 20}
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
