import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.is_word = False
        self.children = {}


def t9(digits, dictionary):
    '''
    16.20 T9: On old cell phones, users typed on a numeric keypad and the phone 
    would provide a list of words that matched these numbers. Each digit mapped 
    to a set of 0 - 4 letters. Implement an algorithm to return a list of matching 
    words, given a sequence of digits. You are provided a list of valid words 
    (provided in whatever data structure you'd like). The mapping is shown in 
    the diagram below:

                                +-----+-----+-----+
                                |  1  |  2  |  3  |
                                |     | abc | def |
                                +-----+-----+-----+
                                |  4  |  5  |  6  |
                                | ghi | jkl | mno |
                                +-----+-----+-----+
                                |  7  |  8  |  9  |
                                | pqrs| tuv | wxyz|
                                +-----+-----+-----+
                                |     |  0  |     |
                                +-----+-----+-----+

    EXAMPLE
    Input: 8733
    Output: tree, used
    '''
    root = Node(None)

    for word in dictionary.split():
        _create_dictionary(root, word)

    keypad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    mappings = [keypad[digit] for digit in digits if keypad[digit] != '']
    result = set()

    _find_words(root, '', mappings, result)

    return result


def _create_dictionary(node, suffix):
    if not suffix:
        node.is_word = True
        return

    letter = suffix[0]

    if letter not in node.children:
        node.children[letter] = Node(letter)

    _create_dictionary(node.children[letter], suffix[1:])


def _find_words(node, prefix, mappings, result):
    if not mappings:
        if node.is_word:
            result.add(prefix)

        return

    for letter in mappings[0]:
        if letter in node.children:
            _find_words(node.children[letter], prefix + letter, mappings[1:], result)


class T9Test(unittest.TestCase):
    def test_t9(self):
        dictionary = 'tree ear used give faq about hive'

        test_cases = [
            ([8, 7, 3, 3], {'tree', 'used'}),
            ([3, 2, 7], {'ear', 'faq'}),
            ([2, 2, 6, 8, 8], {'about'}),
            ([4, 4, 8, 3], {'give', 'hive'})
        ]

        for digits, expected in test_cases:
            actual = t9(digits, dictionary)
            self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
