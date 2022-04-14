from collections import namedtuple
import unittest


Point = namedtuple('Point', ['x', 'y'])
Square = namedtuple('Square', ['point1', 'point2'])


def bisect_squares(square1, square2):
	'''
	16.13 Bisect Squares: Given two squares on a two-dimensional plane, 
	find a line that would cut these two squares in half. Assume that 
	the top and the bottom sides of the square run parallel to the x-axis.
	'''
	center1 = _get_center(square1)
	center2 = _get_center(square2)

	a = (center2.y - center1.y) / (center2.x - center1.x)
	b = center1.y - center1.x * a

	return a, b


def _get_center(square):
	point1, point2 = square
	x = (point1.x + point2.x) / 2
	y = (point1.y + point2.y) / 2

	return Point(x, y)


class BisectSquaresTest(unittest.TestCase):
    def test_bisect_squares(self):
        test_cases = [
        	(Square(Point(4, 5), Point(6, 2)), Square(Point(8, 3), Point(12, 1)), (-0.3, 5)),
        	(Square(Point(8, 3), Point(12, 1)), Square(Point(4, 5), Point(6, 2)), (-0.3, 5)),
        	(Square(Point(4, 2), Point(6, 5)), Square(Point(8, 3), Point(12, 1)), (-0.3, 5)),
        	(Square(Point(-2, 6), Point(1, 1)), Square(Point(-6, 2), Point(0, -2)), (1.4, 4.2))
        ]

        for square1, square2, expected in test_cases:
        	actual = bisect_squares(square1, square2)
        	self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
