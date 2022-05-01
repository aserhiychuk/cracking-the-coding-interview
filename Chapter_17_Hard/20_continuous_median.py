import heapq
from random import randint
import unittest


class ContinuousMedian:
    '''
    17.20 Continuous Median: Numbers are randomly generated and passed 
    to a method. Write a program to find and maintain the median value 
    as new values are generated.
    '''
    def __init__(self):
        self._left_heap = []
        self._right_heap = []

    def add(self, value):
        if not self._left_heap and not self._right_heap:
            # add to right heap
            heapq.heappush(self._right_heap, value)
        elif not self._left_heap:
            right = self._right_heap[0]

            if value < right:
                # add to left heap
                heapq.heappush(self._left_heap, -value)
            else:
                # add to right heap
                heapq.heappush(self._right_heap, value)
        elif not self._right_heap:
            left = -self._left_heap[0]

            if left < value:
                # add to right heap
                heapq.heappush(self._right_heap, value)
            else:
                # add to left heap
                heapq.heappush(self._left_heap, -value)
        else:
            right = self._right_heap[0]

            if right < value:
                # add to right heap
                heapq.heappush(self._right_heap, value)
            else:
                # add to left heap
                heapq.heappush(self._left_heap, -value)

        if abs(len(self._right_heap) - len(self._left_heap)) > 1:
            # rebalance heaps
            if len(self._right_heap) > len(self._left_heap):
                # move from right to left
                value = heapq.heappop(self._right_heap)
                heapq.heappush(self._left_heap, -value)
            else:
                # move from left to right
                value = -heapq.heappop(self._left_heap)
                heapq.heappush(self._right_heap, value)

    def get(self):
        if len(self._right_heap) < len(self._left_heap):
            return -self._left_heap[0]

        if len(self._right_heap) > len(self._left_heap):
            return self._right_heap[0]

        left = -self._left_heap[0]
        right = self._right_heap[0]

        return (left + right) / 2


class ContinuousMedianTest(unittest.TestCase):
    def test_continuous_median(self):
        continuous_median = ContinuousMedian()
        array = []

        for _ in range(20):
            value = randint(0, 10)

            continuous_median.add(value)
            actual = continuous_median.get()

            array.append(value)
            expected = self._get_median(array)
            self.assertEqual(expected, actual)

    def _get_median(self, array):
        array = sorted(array)
        length = len(array)

        if length % 2 == 0:
            return (array[length // 2 - 1] + array[length // 2]) / 2

        return array[length // 2]


if __name__ == '__main__':
    unittest.main()
