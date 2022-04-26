import re
import unittest


def word_distance(text, word1, word2):
    '''
    17.11 Word Distance: You have a large text file containing words. 
    Given any two words, find the shortest distance (in terms of number 
    of words) between them in the file. If the operation will be repeated 
    many times for the same file (but different pairs of words), can you 
    optimize your solution?
    '''
    text = re.sub('\.|,', '', text)
    text = text.split()
    words = {
        word1: None,
        word2: None
    }

    min_distance = None
    i = 0

    while i < len(text):
        while i < len(text) and text[i] not in words:
            i += 1

        if i < len(text):
            words[text[i]] = i

            if words[word1] and words[word2]:
                distance = abs(words[word1] - words[word2])

                if min_distance is None or distance < min_distance:
                    min_distance = distance

        i += 1

    return min_distance


class WordDistanceTest(unittest.TestCase):
    def test_word_distance(self):
        text = '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum 
        ornare fringilla dui. Praesent erat lectus, ultricies eu dolor a, 
        fringilla lobortis tellus. Sed sodales tortor in magna maximus porta. 
        Aenean sit amet turpis id nisl viverra ultricies. Sed convallis dictum 
        auctor. Proin volutpat laoreet tortor nec blandit. Fusce condimentum 
        ornare sapien eu scelerisque. Pellentesque in odio in dolor elementum 
        tempor. Vestibulum eget tincidunt ante. Proin congue in elit et ornare. 
        Sed id aliquam orci. Nulla eget tellus sed massa tincidunt pulvinar.
        '''

        test_cases = [
            ('dolor', 'Vestibulum', 3),
            ('elit', 'ultricies', 8),
            ('eget', 'Sed', 5)
        ]

        for word1, word2, expected in test_cases:
            actual = word_distance(text, word1, word2)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
