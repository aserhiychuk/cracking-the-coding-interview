from queue import Queue
import unittest


class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False


def longest_word(words):
    '''
    17.15 Longest Word: Given a list of words, write a program to find 
    the longest word made of other words in the list.

    EXAMPLE
    Input: cat, banana, dog, nana, walk, walker, dogwalker
    Output: dogwalker
    '''
    root = Node(None)

    for word in words:
        node = root

        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)

            node = node.children[c]

        node.is_word = True

    result = None

    for i in range(len(words)):
        if _check_word(words[i], root):
            if result is None or len(result) < len(words[i]):
                result = words[i]

    return result


def _check_word(word, root):
    node = root
    i = 0

    while not node.is_word:
        c = word[i]
        node = node.children[c]
        i += 1

    queue = Queue()
    queue.put((i, node))

    while not queue.empty():
        i, node = queue.get()

        other_node = root

        while i < len(word):
            c = word[i]
            node = node.children[c]

            if c not in other_node.children:
                return False

            other_node = other_node.children[c]

            if node.char != other_node.char:
                return False

            i += 1

            if other_node.is_word and i < len(word):
                queue.put((i, node))

        if other_node.is_word:
            return True

    return False


class LongestWordTest(unittest.TestCase):
    def test_longest_word(self):
        words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']

        actual = longest_word(words)
        expected = 'dogwalker'
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
