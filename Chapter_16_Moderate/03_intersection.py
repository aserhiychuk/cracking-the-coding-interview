from collections import namedtuple
import unittest


Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['start', 'end'])


def intersection(line1, line2):
    '''
    16.3 Intersection: Given two straight line segments (represented as a start 
    point and an end point), compute the point of intersection, if any.
    '''
    if line1.start.x == line1.end.x and line2.start.x == line2.end.x:
        # both vertical
        point = None
    elif line1.start.x == line1.end.x:
        # only first vertical
        a2, b2 = get_coefficients(line2)
        x = line1.start.x
        y = a2 * x + b2
        point = Point(x, y)
    elif line2.start.x == line2.end.x:
        # only second vertical
        a1, b1 = get_coefficients(line1)
        x = line2.start.x
        y = a1 * x + b1
        point = Point(x, y)
    elif (line1.end.y - line1.start.y) / (line1.end.x - line1.start.x) == \
        (line2.end.y - line2.start.y) / (line2.end.x - line2.start.x):
        # parallel
        point = None
    else:
        # default
        a1, b1 = get_coefficients(line1)
        a2, b2 = get_coefficients(line2)
        x = -(b1 - b2) / (a1 - a2)
        y = a1 * x + b1
        point = Point(x, y)

    if point is None or \
        not is_within_segment(line1, point) or \
        not is_within_segment(line2, point):

        return None

    return point


def get_coefficients(line):
    a = (line.end.y - line.start.y) / (line.end.x - line.start.x)
    b = line.start.y - line.start.x * a

    return a, b


def is_within_segment(line, point):
    if point.x < line.start.x and point.x < line.end.x:
        return False

    if line.start.x < point.x and line.end.x < point.x:
        return False

    if point.y < line.start.y and point.y < line.end.y:
        return False

    if line.start.y < point.y and line.end.y < point.y:
        return False

    return True


class IntersectionTest(unittest.TestCase):
    def test_intersection(self):
        test_cases = [
            # intersection
            (Line(Point(2, 0), Point(5, 6)), Line(Point(1, 1), Point(5, 3)), Point(3, 2)),
            (Line(Point(1, 1), Point(5, 3)), Line(Point(2, 0), Point(5, 6)), Point(3, 2)),
            # no intersection
            (Line(Point(1, 1), Point(5, 3)), Line(Point(4, 4), Point(5, 6)), None),
            (Line(Point(4, 4), Point(5, 6)), Line(Point(1, 1), Point(5, 3)), None),
            # both vertical
            (Line(Point(2, 1), Point(2, 4)), Line(Point(4, 2), Point(4, 6)), None),
            # only first vertical
            (Line(Point(2, 1), Point(2, 4)), Line(Point(1, 0), Point(4, 6)), Point(2, 2)),
            # only first vertical, no intersection
            (Line(Point(2, 1), Point(2, 4)), Line(Point(3, 3), Point(4, 5)), None),
            # only second vertical
            (Line(Point(1, 0), Point(4, 6)), Line(Point(2, 1), Point(2, 4)), Point(2, 2)),
            # only second vertical, no intersection
            (Line(Point(3, 3), Point(4, 5)), Line(Point(2, 1), Point(2, 4)), None),
            # both horizontal
            (Line(Point(2, 1), Point(5, 1)), Line(Point(3, 3), Point(7, 3)), None)
        ]

        for line1, line2, expected in test_cases:
            actual = intersection(line1, line2)

            if expected is None:
                self.assertIsNone(actual)
            else:
                self.assertTupleEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
