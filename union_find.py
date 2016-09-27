#!/usr/bin/env python3


class NaiveUnionFind:
    """
    TODO: docstring
    """

    def __init__(self, n):
        pass

    def union(self, u, v):
        pass

    def find(self, u, v):
        pass


class UnionFind:
    """
    TODO: docstring
    """

    def __init__(self, n):
        pass

    def union(self, u, v):
        pass

    def find(self, u, v):
        pass


if __name__ == '__main__':

    n = 10
    edges = [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9), (7, 3), (4, 8), (6, 1)]

    # test naive union-find
    nuf = NaiveUnionFind(n)
    for u, v in edges:
        nuf.union(u, v)

    print('naive union-find')
    print('find(0, 1) =', nuf.find(0, 1))

    # test union-find
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)

    print('union-find')
    print('find(0, 1) =', uf.find(0, 1))
