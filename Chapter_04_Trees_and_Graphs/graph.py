
class Vertex:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Vertex):
            return False

        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f'{self.value}'


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)
