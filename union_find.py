#!/usr/bin/env python3


class NaiveUnionFind:
    """
    TODO: docstring
    """

    def __init__(self, n):
        self._id = list(range(n))

    def union(self, u, v):
        ru, rv = self._id[u], self._id[v]
        if ru != rv:
            self._id = [(ru if r == rv else r) for r in self._id]

    def find(self, u, v):
        return self._id[u] == self._id[v]


class UnionFind:
    """
    TODO: docstring

    This implementation is largely based on https://gist.github.com/tnoda/e26173d7402356ea88fe.
    """

    def __init__(self, n):
        self._id = list(range(n))
        self._size = [1] * n

    def _root(self, i):
        j = i
        while j != self._id[j]:
            self._id[j] = self._id[self._id[j]]
            j = self._id[j]
        return j

    def _add_child(self, parent, child):
        self._id[child] = parent
        self._size[parent] += self._size[child]

    def union(self, u, v):
        i, j = self._root(u), self._root(v)
        parent, child = (j, i) if self._size[i] < self._size[j] else (i, j)
        self._add_child(parent, child)

    def find(self, u, v):
        return self._root(u) == self._root(v)


if __name__ == '__main__':

    n = 10
    edges = [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9), (7, 3), (4, 8), (6, 1)]

    # test naive union-find
    nuf = NaiveUnionFind(n)
    for u, v in edges:
        nuf.union(u, v)

    print('naive union-find')
    print(nuf._id)
    print('find(0, 1) =', nuf.find(0, 1))
    print(nuf._id)

    # test union-find
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)

    print('union-find')
    print(uf._id)
    print('find(0, 1) =', uf.find(0, 1))
    print(uf._id)
