import unittest


def build_order(projects, dependencies):
    '''
    4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list
    of pairs of projects, where the second project is dependent on the first project). All of
    a project's dependencies must be built before the project is. Find a build order that will allow
    the projects to be built. If there is no valid build order, return an error.

    EXAMPLE
    Input:
        projects: a, b, c, d, e, f
        dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
    Output: f, e, a, b, d, c
    '''
    adjacency_list = {project: [] for project in projects}

    for project1, project2 in dependencies:
        adjacency_list[project1].append(project2)

    result = []

    while adjacency_list:
        dependent_projects = set()

        for project, dependents in adjacency_list.items():
            dependent_projects.update(dependents)

        independent_projects = [project for project in adjacency_list if project not in dependent_projects]

        assert len(independent_projects) > 0, 'No valid build order'

        result += independent_projects

        for project in independent_projects:
            del adjacency_list[project]

    return result


class BuildOrderTest(unittest.TestCase):
    def test_build_order(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), \
            ('g', 'a'), ('g', 'b'), ('h', 'g')]

        actual = build_order(projects, dependencies)
        expected = ['e', 'f', 'h', 'g', 'a', 'b', 'd', 'c']
        self.assertListEqual(expected, actual)

        with self.assertRaises(AssertionError):
            # cycle
            build_order(projects, dependencies + [('c', 'h')])


if __name__ == '__main__':
    unittest.main()
