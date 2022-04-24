import unittest


def kth_multiple(k):
    '''
    17.9 Kth Multiple: Design an atgorithm to find the kth number 
    such that the only prime factors are 3, 5, and 7. Note that 3, 5, 
    and 7 do not have to be factors, but it should not have any other 
    prime factors. For example, the first several multiples would be 
    (in order) 1, 3, 5, 7, 9, 15, 21.
    '''
    factors = [3, 5, 7]
    queues = [[], [], []]

    queues[0].append(1)
    i = 0

    while i < k:
        index = _get_next_queue_index(queues)

        n = queues[index].pop(0)
        i += 1

        for j in range(index, len(queues)):
            queues[j].append(n * factors[j])

    return n


def _get_next_queue_index(queues):
    index = None

    for i in range(len(queues)):
        if queues[i]:
            if index is None or queues[i][0] < queues[index][0]:
                index = i

    return index


class KthMultipleTest(unittest.TestCase):
    def test_kth_multiple(self):
        test_cases = [1, 3, 5, 7, 9, 15, 21, 25, 27, 35, 45, 49, 63, 75, 81, 105]

        for k, expected in enumerate(test_cases, start=1):
            actual = kth_multiple(k)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
