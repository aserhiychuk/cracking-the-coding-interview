import unittest


class Node:
    def __init__(self, char):
        self.char = char
        self.is_word = False

        self.children = {}


def multi_search(text, patterns):
    '''
    17.17 Multi Search: Given a string b and an array of smaller strings T, 
    design a method to search b for each small string in T. Return a mapping 
    of each string to a list of its locations.
    '''
    root = Node(None)

    for pattern in patterns:
        node = root

        for c in pattern:
            if c not in node.children:
                node.children[c] = Node(c)

            node = node.children[c]

        node.is_word = True

    result = {pattern: [] for pattern in patterns}

    for i in range(len(text)):
        _search(text, i, '', root, result)

    return result


def _search(text, i, pattern, node, result):
    if i >= len(text):
        return

    if text[i] not in node.children:
        return

    node = node.children[text[i]]
    pattern += node.char

    if node.is_word:
        result[pattern].append(i + 1 - len(pattern))

    _search(text, i + 1, pattern, node, result)


class MultiSearchTest(unittest.TestCase):
    def test_multi_search(self):
        text = 'aliquam aliquet diam ac risus aliquam efficitur tristique enim commodo'
        patterns = ['ali', 'aliquam', 'aliquet', 'que', 'ris']

        actual = multi_search(text, patterns)
        expected = {
            'ali': [0, 8, 30],
            'aliquam': [0, 30],
            'aliquet': [8],
            'que': [11, 54],
            'ris': [24, 49]
        }
        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
