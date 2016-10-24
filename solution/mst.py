#!/usr/bin/env python3

from solution.graph import Graph
from solution.union_find import UnionFind


def kruskal_mst(graph):
    """
    TODO: docstring

    :param graph:
    :return:
    """

    num_nodes = len(graph.nodes())

    mst = Graph()
    ds = UnionFind(num_nodes)

    for u, v in sorted(graph.edges(), key=graph.edge_weight):
        if not ds.find(u, v):
            ds.union(u, v)
            mst.add_edge(u, v, graph.weight(u, v))
            if len(mst.edges()) == num_nodes - 1:
                return mst

    return mst


if __name__ == '__main__':
    E = {(0, 1, 2), (0, 2, 2), (0, 3, 3), (1, 2, 1),
         (1, 3, 2), (1, 4, 3), (2, 3, 1), (2, 4, 2)}

    G = Graph(E)
    print(G)

    K = kruskal_mst(G)
    w = sum(K.weight(*e) for e in K.edges())
    print('K =', K)
    print('w(K) =', w)
