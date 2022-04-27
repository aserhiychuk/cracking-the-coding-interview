import unittest


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.is_word = False

        self.children = {}


def re_space(document, dictionary):
    '''
    17.13 Re-Space: Oh, no! You have accidentally removed all spaces, punctuation, 
    and capitalization in a lengthy document. A sentence like "I reset the computer. 
    It still didn't boot!" became "iresetthecomputeritstilldidntboot". You'll deal 
    with the punctuation and capitalization later; right now you need to re-insert 
    the spaces. Most of the words are in a dictionary but a few are not. Given 
    a dictionary (a list of strings) and the document (a string), design an algorithm 
    to unconcatenate the document in a way that minimizes the number of unrecognized 
    characters. 

    EXAMPLE;
    Input: jesslookedjustliketimherbrother
    Output: jess looked just like tim her brother (7 unrecognized characters)
    '''

    # populate trie
    root = Node(None)

    for word in dictionary:
        node = root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node(letter)

            node = node.children[letter]

        node.is_word = True

    # insert spaces
    spaces = []
    i = 0

    while i < len(document):
        longest_word_length = 0
        node = root
        j = 0

        while i + j < len(document):
            letter = document[i + j]

            if letter not in node.children:
                break

            if node.children[letter].is_word:
                longest_word_length = j + 1

            node = node.children[letter]
            j += 1

        if longest_word_length:
            if i > 0 and (not spaces or spaces[-1] != i):
                spaces.append(i)

            if i + longest_word_length < len(document):
                spaces.append(i + longest_word_length)

        i += max(1, longest_word_length)

    spaces = [0] + spaces + [len(document)]
    words = [document[spaces[i]:spaces[i + 1]] for i in range(len(spaces) - 1)]

    return words


class ReSpaceTest(unittest.TestCase):
    def test_re_space(self):
        document = 'jesslookedjustliketimherbrother'
        dictionary = ['looked', 'just', 'like', 'her', 'brother']

        actual = re_space(document, dictionary)
        expected = ['jess', 'looked', 'just', 'like', 'tim', 'her', 'brother']
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
