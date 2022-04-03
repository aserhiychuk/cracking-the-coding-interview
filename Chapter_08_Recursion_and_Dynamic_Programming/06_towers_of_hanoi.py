import unittest


class Tower:
    def __init__(self, name, n=0):
        self._name = name
        self._tower = list(range(n, 0, -1))

    def push(self, disk):
        assert len(self._tower) == 0 or disk < self._tower[-1], 'Invalid move'

        self._tower.append(disk)

    def pop(self):
        return self._tower.pop()

    def __len__(self):
        return len(self._tower)

    def __repr__(self):
        return f'{self._name}{self._tower}'


def towers_of_hanoi(t1, t2, t3):
    '''
    8.6 Towers of Hanoi: In the classic problem of the Towers of Hanoi, 
    you have 3 towers and N disks of different sizes which can slide onto 
    any tower. The puzzle starts with disks sorted in ascending order of size 
    from top to bottom (i.e., each disk sits on top of an even larger one). 
    You have the following constraints:
    (1) Only one disk can be moved at a time.
    (2) A disk is slid off the top of one tower onto another tower.
    (3) A disk cannot be placed on top of a smaller disk.
    Write a program to move the disks from the first tower to the last using stacks.
    '''
    _towers_of_hanoi(len(t1), t1, t2, t3)


def _towers_of_hanoi(n, src, buf, dest):
    if n == 1:
        disk = src.pop()
        dest.push(disk)
    elif n == 2:
        _towers_of_hanoi(1, src, None, buf)
        _towers_of_hanoi(1, src, None, dest)
        _towers_of_hanoi(1, buf, None, dest)
    else:
        _towers_of_hanoi(n - 1, src, buf, dest)
        _towers_of_hanoi(1, src, None, buf)
        _towers_of_hanoi(n - 1, dest, buf, src)
        _towers_of_hanoi(1, buf, None, dest)
        _towers_of_hanoi(n - 1, src, buf, dest)


class TowersOfHanoiTest(unittest.TestCase):
    def test_towers_of_hanoi(self):
        n = 10
        t1 = Tower('T1', n)
        t2 = Tower('T2')
        t3 = Tower('T3')
        towers_of_hanoi(t1, t2, t3)

        self.assertEqual(0, len(t1))
        self.assertEqual(0, len(t2))
        self.assertEqual(n, len(t3))

        for i in range(1, n + 1):
            disk = t3.pop()
            self.assertEqual(i, disk)


if __name__ == '__main__':
    unittest.main()
