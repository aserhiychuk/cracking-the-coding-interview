import unittest


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)


def word_transformer(word1, word2, dictionary):
    '''
    17.22 Word Transformer: Given two words of equal length that are 
    in a dictionary, write a method to transform one word into another 
    word by changing only one letter at a time. The new word you get 
    in each step must be in the dictionary.

    EXAMPLE
    Input: DAMP, LIKE
    Output: DAMP -> LAMP -> LIMP -> LIME -> LIKE
    '''
    graph = Graph()

    for word in dictionary:
        graph.add_vertex(word)

        for other in graph.adjacency_list:
            if word == other:
                continue

            if _is_one_apart(word, other):
                graph.add_edge(word, other)
                graph.add_edge(other, word)

    result = _dfs(graph, word1, word2, 0, set())

    return result


def _is_one_apart(word1, word2):
    if len(word1) != len(word2):
        return False

    n_differences = 0

    for c1, c2 in zip(word1, word2):
        if c1 == c2:
            continue

        n_differences += 1

        if n_differences > 1:
            return False

    return True


def _dfs(graph, node1, node2, i, visited):
    visited.add(node1)

    for adjacent_vertex in graph.adjacency_list[node1]:
        if adjacent_vertex == node2:
            return [None] * i + [node1, node2]

        if adjacent_vertex not in visited:
            result = _dfs(graph, adjacent_vertex, node2, i + 1, visited)

            if result:
                result[i] = node1

                return result

    return None


class WordTransformerTest(unittest.TestCase):
    def test_word_transformer(self):
        dictionary = [
            'a', 'i', 'be', 'to', 'are', 'eye', 
            'ear', 'arc', 'car', 'dump', 'damp', 'lamp', 
            'lamb', 'limp', 'lime', 'like', 'love', 'line', 
            'life', 'live', 'shall', 'still', 'water', 'stand'
        ]

        test_cases = [
            (('damp', 'like'), ['damp', 'lamp', 'limp', 'lime', 'like']),
            (('be', 'to'), None)
        ]

        for (word1, word2), expected in test_cases:
            actual = word_transformer(word1, word2, dictionary)

            if expected is not None:
                self.assertListEqual(expected, actual)
            else:
                self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()
