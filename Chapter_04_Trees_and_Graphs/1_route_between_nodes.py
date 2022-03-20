from queue import Queue
from graph import *
import unittest


def route_between_nodes(graph, v1, v2):
    '''
    4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether
    there is a route between two nodes.
    '''
    queue = Queue()
    visited = set()

    queue.put(v1)
    visited.add(v1)

    while not queue.empty():
        v = queue.get()
        adjacent_vertices = graph.adjacency_list[v]

        for u in adjacent_vertices:
            if u not in visited:
                queue.put(u)
                visited.add(u)

    return v2 in visited


class RouteBetweenNodesTest(unittest.TestCase):
    def test_route_between_nodes(self):
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        d = Vertex('d')
        e = Vertex('e')
        graph = Graph()
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_edge(a, b)
        graph.add_edge(a, c)
        graph.add_edge(b, c)
        graph.add_edge(c, d)
        graph.add_edge(d, b)

        actual = route_between_nodes(graph, a, b)
        self.assertTrue(actual)

        actual = route_between_nodes(graph, a, d)
        self.assertTrue(actual)

        actual = route_between_nodes(graph, c, a)
        self.assertFalse(actual)

        actual = route_between_nodes(graph, a, e)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
