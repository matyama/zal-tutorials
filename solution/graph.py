#!/usr/bin/env python3


class Graph(object):
    """
    TODO: docstring
    """

    def __init__(self, edges=set()):
        self._graph = dict()
        self._edges = set()
        self.add_edges(edges)

    def add_edge(self, u, v, weight=1.):
        self._add_adj(u, v, weight)
        self._add_adj(v, u, weight)

    def add_edges(self, edges=set()):
        for e in edges:
            self.add_edge(*e)

    def _add_adj(self, node, adj, weight):
        if node not in self._graph:
            self._graph[node] = dict()
        self._graph[node][adj] = weight
        if (node, adj) not in self._edges and (adj, node) not in self._edges:
            self._edges.add((node, adj))

    def _check_node(self, u):
        if u not in self._graph:
            raise ValueError('unknown node %s' % u)

    def _check_adj(self, node, adj):
        if adj not in self._graph[node]:
            raise ValueError('unknown adjacent node %s' % adj)

    def _check_edge(self, u, v):
        self._check_node(u)
        self._check_adj(u, v)

    def remove_edge(self, u, v):
        self._check_edge(u, v)
        del self._graph[u][v]
        del self._graph[v][u]
        self._edges.discard((u, v))
        self._edges.discard((v, u))

    def nodes(self):
        return self._graph.keys()

    def adj(self, u):
        self._check_node(u)
        return self._graph[u].keys()

    def deg(self, u):
        self._check_node(u)
        return len(self.adj(u))

    def edges(self):
        return self._edges

    def weight(self, u, v):
        self._check_edge(u, v)
        return self._graph[u][v]

    def edge_weight(self, edge):
        return self.weight(*edge if len(edge) == 2 else (edge[0], edge[1]))

    def __str__(self):
        return self._graph.__str__()

    def __repr__(self):
        return self._graph.__repr__()


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
