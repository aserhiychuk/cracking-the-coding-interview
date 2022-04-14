import unittest


def best_line(points):
    '''
    16.14 Best Line: Given a two-dimensional graph with points on it, 
    find a line which passes the most number of points.
    '''
    lines = {}

    for i in range(len(points)):
        x1, y1 = points[i]

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]

            if x1 == x2:
                # vertical line. x = a
                a = x1
                b = None
            else:
                # default. y = a * x + b
                a = (y2 - y1) / (x2 - x1)
                b = y1 - x1 * a

            count = lines.get((a, b), 0)
            lines[(a, b)] = count + 1

    max_count = 0
    result = None

    for line, count in lines.items():
        if count > max_count:
            max_count = count
            result = line

    return result


class BestLineTest(unittest.TestCase):
    def test_best_line(self):
        points = [
            (2, 1), (1, 1), (1.5, 2), (2, 4), (3, 3.5), (3.5, 4), 
            (1.5, 0), (0, -3), (2, 3), (3, 1), (4, 2), (2.5, 2)
        ]
        actual = best_line(points)
        self.assertEqual((2, -3), actual)


if __name__ == '__main__':
    unittest.main()
