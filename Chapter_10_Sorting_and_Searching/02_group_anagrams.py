import unittest


def group_anagrams(array):
    '''
    10.2 Group Anagrams: Write a method to sort an array of 
    strings so that all the anagrams are next to each other.
    '''
    words = {}

    for s in array:
        word = ''.join(sorted(s.lower()))

        if word not in words:
            words[word] = []

        anagrams = words[word]
        anagrams.append(s)

    i = 0

    for word, anagrams in words.items():
        for anagram in anagrams:
            array[i] = anagram
            i += 1


class GroupAnagramsTest(unittest.TestCase):
    def test_group_anagrams(self):
        array = ['boss', 'ear', 'heart', 'flow', 'earth', 'are', 'wolf', 'night', 'face']
        group_anagrams(array)
        self.assertEqual(1, abs(array.index('are') - array.index('ear')))
        self.assertEqual(1, abs(array.index('heart') - array.index('earth')))
        self.assertEqual(1, abs(array.index('flow') - array.index('wolf')))


if __name__ == '__main__':
    unittest.main()
