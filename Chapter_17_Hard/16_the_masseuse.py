import unittest


def the_masseuse(requests):
    '''
    17.16 The Masseuse: A popular masseuse receives a sequence of back-to-back 
    appointment requests and is debating which ones to accept. She needs 
    a 15-minute break between appointments and therefore she cannot accept any 
    adjacent requests. Given a sequence of back-to-back appointment requests 
    (all multiples of 15 minutes, none overlap, and none can be moved), find 
    the optimal (highest total booked minutes) set the masseuse can honor. 
    Return the number of minutes.

    EXAMPLE
    Input: {30, 15, 60, 75, 45, 15, 15, 45}
    Output: 180 minutes ({30, 60, 45, 45}).
    '''
    return _the_masseuse(requests, 0, {})


def _the_masseuse(requests, i, cache):
    if i >= len(requests):
        return 0

    if i in cache:
        return cache[i]

    # include next request
    result1 = requests[i]
    result1 += _the_masseuse(requests, i + 2, cache)

    # exclude next request
    result2 = _the_masseuse(requests, i + 1, cache)

    result = max(result1, result2)

    cache[i] = result

    return result


class TheMasseuseTest(unittest.TestCase):
    def test_the_masseuse(self):
        requests = [30, 15, 60, 75, 45, 15, 15, 45]

        actual = the_masseuse(requests)
        expected = 180
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
