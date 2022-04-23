from collections import Counter
import unittest


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def get_root(self):
        node = self

        while node.parent is not None:
            node = node.parent

        return node


def baby_names(names, synonyms):
    '''
    17.7 Baby Names: Each year, the government releases a list of the 10000 
    most common baby names and their frequencies (the number of babies with 
    that name). The only problem with this is that some names have multiple 
    spellings. For example, "John" and "Jon" are essentially the same name 
    but would be listed separately in the list. Given two lists, one of 
    names/frequencies and the other of pairs of equivalent names, write an 
    atgorithm to print a new list of the true frequency of each name. Note 
    that if John and Jon are synonyms, and Jon and Johnny are synonyms, then 
    John and Johnny are synonyms, (it is both transitive and symmetric.) 
    In the final list, any name can be used as the "real" name,

    EXAMPLE
    Input: 
        Names: John (15), Jon (12), Chris (13), Kris (4), Christopher (19)
        Synonyms: (Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)
    Output: John (27), Kris (36)
    '''
    clusters = {}

    for name1, name2 in synonyms:
        if name1 not in clusters:
            clusters[name1] = Node(name1)

        if name2 not in clusters:
            clusters[name2] = Node(name2)


    for name1, name2 in synonyms:
        root1 = clusters[name1].get_root()
        root2 = clusters[name2].get_root()

        if root1.name != root2.name:
            root2.parent = root1

    names = [(clusters[name].get_root().name, frequency) for name, frequency in names]

    counter = Counter()

    for name, frequency in names:
        counter[name] += frequency

    return set(counter.items())


class BabyNamesTest(unittest.TestCase):
    def test_baby_names(self):
        names = [
            ('John', 15),
            ('Jon', 12),
            ('Chris', 13),
            ('Kris', 4),
            ('Christopher', 19)
        ]
        synonyms = [
            ('Jon', 'John'),
            ('John', 'Johnny'),
            ('Chris', 'Kris'),
            ('Chris', 'Christopher')
        ]

        actual = baby_names(names, synonyms)
        expected = {('Jon', 27), ('Chris', 36)}
        self.assertSetEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
