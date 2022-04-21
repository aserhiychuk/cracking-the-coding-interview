from random import randint
import unittest


def shuffle():
    '''
    17.2 Shuffle: Write a method to shuffle a deck of cards. It must be 
    a perfect shuffle — in other words, each of the 52! permutations of 
    the deck has to be equally likely. Assume that you are given a random 
    number generator which is perfect.
    '''
    deck = list(range(52))

    for i in range(51, 0, -1):
        n = randint(0, i)

        if n == i:
            continue

        tmp = deck[i]
        deck[i] = deck[n]
        deck[n] = tmp

    return deck


class ShuffleTest(unittest.TestCase):
    def test_shuffle(self):
        actual = shuffle()
        self.assertSetEqual(set(range(52)), set(actual))


if __name__ == '__main__':
    unittest.main()
