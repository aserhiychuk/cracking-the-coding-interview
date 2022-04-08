import unittest


def word_frequencies(text, word):
    '''
    16.2 Word Frequencies: Design a method to find the frequency 
    of occurrences of any given word in a book. What if we were 
    running this algorithm multiple times?
    '''
    text = text.strip().lower()
    word = word.strip().lower()
    result = 0
    i = 0

    while i <= len(text) - len(word):
        j = 0

        while j < len(word):
            if text[i + j] != word[j]:
                break

            j += 1

        if j == len(word):
            result += 1

        i += 1

    return result


class WordFrequenciesFollowup:
    def __init__(self, text):
        self._text = text.strip().lower()
        self._frequencies = None
        self._calculate_frequencies()

    def _calculate_frequencies(self):
        self._frequencies = {}
        i = 0

        while i < len(self._text):
            start = i

            while i < len(self._text) and self._text[i] != ' ':
                i += 1

            word = self._text[start:i]
            frequency = self._frequencies.get(word, 0)
            self._frequencies[word] = frequency + 1

            while i < len(self._text) and self._text[i] == ' ':
                i += 1

    def get_frequency(self, word):
        word = word.strip().lower()

        return self._frequencies.get(word, 0)


class WordFrequenciesTest(unittest.TestCase):
    def setUp(self):
        self._text = '''
        cat dog tiger sparrow lion cat cheetah seagull
        sparrow lion cat wolf
        '''
        self._test_cases = [
            ('cat', 3),
            ('dog', 1),
            ('sparrow', 2),
            ('bear', 0)
        ]

    def test_word_frequencies(self):
        for word, expected in self._test_cases:
            actual = word_frequencies(self._text, word)
            self.assertEqual(expected, actual)

    def test_word_frequencies_followup(self):
        word_frequencies = WordFrequenciesFollowup(self._text)

        for word, expected in self._test_cases:
            actual = word_frequencies.get_frequency(word)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
