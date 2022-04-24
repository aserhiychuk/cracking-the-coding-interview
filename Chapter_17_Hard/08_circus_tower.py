import unittest


def circus_tower(people):
    '''
    17.8 Circus Tower: A circus is designing a tower routine consisting of people 
    standing atop one another's shoulders. For practical and aesthetic reasons, 
    each person must be both shorter and lighter than the person below him or her. 
    Given the heights and weights of each person in the circus, write a method to 
    compute the largest possible number of people in such a tower.

    EXAMPLE
    Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110) 
    Output: The longest tower is length 6 and includes from top to bottom:
        (56, 90) (60, 95) (65, 100) (68, 110) (70, 150) (75, 190)
    '''

    # A(65, 112) B(50, 110) C(55, 105) D(72, 109) E(60, 125) F(70, 130) H(68, 122)

    # person            D   F   H   A   E   C   B
    # weight (sorted)  72  70  68  65  60  55  50           
    # height          109 130 122 112 125 105 110       

    # i | height                      | subsequence     |                               
    # --+-----------------------------+-----------------+-------
    # 0 | 109                         | 109             | 109, 1
    # 1 | 109 130                     | 130             | 130, 1
    # 2 | 109 130 122                 | 130 122         | 122, 2
    # 3 | 109 130 122 112             | 130 122 112     | 112, 3
    # 4 | 109 130 122 112 125         | 130 125         | 125, 2
    # 5 | 109 130 122 112 125 105     | 130 122 112 105 | 105, 4
    # 6 | 109 130 122 112 125 105 110 | 130 122 112 110 | 110, 4

    people = sorted(people, key=lambda weight_height: weight_height[0], reverse=True)

    subsequences = []

    for i in range(len(people)):
        _, cur_height = people[i]

        max_count = 0

        for height, count in subsequences:
            if height > cur_height and count > max_count:
                max_count = count

        subsequences.append((cur_height, max_count + 1))

    _, result = max(subsequences, key=lambda height_count: height_count[1])

    return result


class CircusTowerTest(unittest.TestCase):
    def test_circus_tower(self):
        test_cases = [
            ([(65, 112), (50, 110), (55, 105), (72, 109), (60, 125), (70, 130), (68, 122)], 4),
            ([(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)], 6)
        ]

        for people, expected in test_cases:
            actual = circus_tower(people)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
