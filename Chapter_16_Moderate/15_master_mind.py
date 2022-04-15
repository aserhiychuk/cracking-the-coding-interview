import unittest


def master_mind(solution, guess):
    '''
    16.15 Master Mind: The Game of Master Mind is played as follows:
    The computer has four slots, and each slot will contain a ball that is red (ft), 
    yellow (V), green (G) or blue (B). For example, the computer might have RGGB 
    (Slot #1 is red, Slots #2 and #3 are green. Slot #4 is blue).
    You, the user, are trying to guess the solution. You might, for example, guess YRGB.
    When you guess the correct color for the correct slot, you get a "hit." If you guess 
    a color that exists but is in the wrong slot, you get a "pseudo-hit." Mote that a slot 
    that is a hit can never count as a pseudo-hit.
    For example, if the actual solution is RGBY and you guess GGRR, you have one hit and 
    one pseudo-hit. Write a method that, given a guess and a solution, returns the number 
    of hits and pseudo-hits.
    '''
    color_indices = {}

    for i, color in enumerate(solution):
        if color not in color_indices:
            color_indices[color] = set()

        indices = color_indices[color]
        indices.add(i)

    # hits
    hits = set()

    for i, color in enumerate(guess):
        if color in color_indices and i in color_indices[color]:
            hits.add(i)
            color_indices[color].remove(i)

    # pseudo-hits
    n_pseudo_hits = 0

    for i, color in enumerate(guess):
        if i in hits:
            continue

        if color in color_indices and len(color_indices[color]) > 0:
            n_pseudo_hits += 1
            color_indices[color].pop()

    return len(hits), n_pseudo_hits


class MasterMindTest(unittest.TestCase):
    def test_master_mind(self):
        test_cases = [
            ('RGBY', 'GGRR', (1, 1)),
            ('RRRR', 'RRRR', (4, 0)),
            ('RGBY', 'YRGB', (0, 4))
        ]

        for solution, guess, expected in test_cases:
            actual = master_mind(solution, guess)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
