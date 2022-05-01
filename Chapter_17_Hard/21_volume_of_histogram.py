import unittest


def volume_of_histogram(histogram):
    '''
    17.21 Volume of Histogram: Imagine a histogram (bar graph). Design 
    an algorithm to compute the volume of water it could hold if someone 
    poured water across the top. You can assume that each histogram bar 
    has width 1.

    EXAMPLE
    Input: {0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0}

              X
              X ~ ~ ~ ~ X
        X ~ ~ X ~ ~ ~ ~ X
        X ~ ~ X ~ ~ X ~ X
        X ~ ~ X ~ ~ X ~ X
        X ~ ~ X ~ ~ X ~ X ~ X
    0 0 4 0 0 6 0 0 3 0 5 0 1 0 0 0

    Output: 26
    '''
    highest_left = [0] * len(histogram)
    highest_right = [0] * len(histogram)

    highest = 0

    for i in range(len(histogram)):
        if histogram[i] > highest:
            highest = histogram[i]

        highest_left[i] = highest

    highest = 0

    for i in range(len(histogram) - 1, -1, -1):
        if histogram[i] > highest:
            highest = histogram[i]

        highest_right[i] = highest

    result = 0

    for i in range(len(histogram)):
        result += min(highest_left[i], highest_right[i]) - histogram[i]

    return result


class VolumeOfHistogramTest(unittest.TestCase):
    def test_volume_of_histogram(self):
        histogram = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]

        actual = volume_of_histogram(histogram)
        expected = 26
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
