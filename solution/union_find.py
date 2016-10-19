#!/usr/bin/env python3


class NaiveUnionFind:
    """
    The Union-Find problem is an abstract data structure representing disjoint sets. There are two basic methods:

     * *union(u, v)* - updates this data structure so that u and v are in the same set
     * *find(u, v)* - returns whether u and v are in the same set

     The naive implementation uses array representation where on i-th position is a representative for element i.
     Operation *find* simply compares representatives for u and v and is thus fast - O(1).

     Operation *union* first queries representatives for u and v. If the representatives are same we are ok (u and v
     are already in the same set). If these are different, we must traverse the whole array and replace each occurrence
     of representative for v by the representative of u. Union is in this implementation slow since it takes linear time
     in the number of elements - O(n).
    """

    def __init__(self, n):
        """
        Initialize this data structure for total number of n elements.
        :param n: maximum number of elements in the disjoint sets.
        """
        self._id = list(range(n))

    def union(self, u, v):
        """
        Update this data structure so that u and v are in the same set (union sets with u and v).

        :param u: integer representing an element
        :param v: integer representing an element
        """
        ru, rv = self._id[u], self._id[v]
        if ru != rv:
            self._id = [(ru if r == rv else r) for r in self._id]

    def find(self, u, v):
        """
        Query this data structure whether u and v are in the same set (whether sets with u and v are disjoint).

        :param u: integer representing an element
        :param v: integer representing an element
        :return: True iff u and v are in the same set, False if they are in disjoint sets.
        """
        return self._id[u] == self._id[v]


class UnionFind:
    """
    The Union-Find problem is an abstract data structure representing disjoint sets. There are two basic methods:

     * *union(u, v)* - updates this data structure so that u and v are in the same set
     * *find(u, v)* - returns whether u and v are in the same set

     The optimized implementation represents the disjoint sets as forest where each tree represents one set and has the
     representative in the root. Each node of such tree keeps a reference on it's parent (predecessor) and the size of a
     sub-tree rooted at this node.

     Operation *find* again compares representatives for u and v. Now, however, we must traverse from u (resp. v) to the
     root of it's tree in order to get the representative. Fortunately, the maximum height of a balanced tree is
     logarithmic in it's size and thus *find* takes O(log(n)) time.

     Similarly to the naive implementation, *union* first finds the corresponding representatives. Then compare sizes of
     both trees and add the root of the smaller one as new child of the larger tree's root. In this way we keep all the
     trees balanced and since finding the root takes O(log(n)) and joining two trees can be done in constant time, the
     *union* takes O(log(n)) time.

     Moreover, this implementation can be further improved. We can adopt the *path compression* technique which simply
     states that during the tree traversal (up to the root) in *find*, we can point each node's parent reference to the
     root. This effectively flattens the tree and it can be shown that in this implementation the combination of *union*
     and *find* is very fast (the amortized complexities are inverse Ackermann's function).

     For further info see: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
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
        """
        Update this data structure so that u and v are in the same set (union sets with u and v).

        :param u: integer representing an element
        :param v: integer representing an element
        """
        i, j = self._root(u), self._root(v)
        parent, child = (j, i) if self._size[i] < self._size[j] else (i, j)
        self._add_child(parent, child)

    def find(self, u, v):
        """
        Query this data structure whether u and v are in the same set (whether sets with u and v are disjoint).

        :param u: integer representing an element
        :param v: integer representing an element
        :return: True iff u and v are in the same set, False if they are in disjoint sets.
        """
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
