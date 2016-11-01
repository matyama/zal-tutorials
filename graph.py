#!/usr/bin/env python3


class Graph(object):
    """
    TODO: docstring
    """

    def __init__(self, edges=set()):
        pass

    def add_edge(self, u, v, weight=1.):
        pass

    def add_edges(self, edges=set()):
        pass

    def remove_edge(self, u, v):
        pass

    def nodes(self):
        pass

    def adj(self, u):
        pass

    def deg(self, u):
        pass

    def edges(self):
        pass

    def weight(self, u, v):
        pass

    def edge_weight(self, edge):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


if __name__ == '__main__':

    E = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)}

    graph = Graph(E)
    print(graph)

    graph.add_edge(0, 2, 2.)
    print(graph)

    graph.remove_edge(2, 0)
    print(graph)

    graph.add_edge(2, 0)
    print(graph)

    for e in E:
        print('w(%s) = %s' % (set(e), graph.weight(*e)))

    print('N =', set(graph.nodes()))
    print('E =', set(graph.edges()))

    print('adj(0) =', set(graph.adj(0)))
    print('deg(0) =', graph.deg(0))
