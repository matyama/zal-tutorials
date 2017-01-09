#!/usr/bin/env python3


class Graph(object):
    """
    Class representing an (weighted) undirected simple graph.
    """

    def __init__(self, edges=set()):
        """
        Construct this graph from given (possibly empty) `set` of `edges`.

        :param edges: `set` edges represented as tuples of vertices and optionally a weight
        """
        pass

    def add_edge(self, u, v, weight=1.):
        """
        Add an undirected edge `{u, v}`, optionally with `weight`.

        :param u: first vertex/node
        :param v: second vertex/node
        :param weight: real number representing the weight/cost of added edge
        """
        pass

    def add_edges(self, edges=set()):
        """
        Add a `set` of `edges` to this graph. Edges are given as tuples of nodes.

        :param edges: `set` of tuples representing the edges
        """
        pass

    def remove_edge(self, u, v):
        """
        Remove edge `{u, v}` from this graph.

        :param u: first vertex/node of the removed edge
        :param v: second vertex/node of the removed edge
        """
        pass

    def nodes(self):
        """
        Returns a view on vertices/nodes in this graph.

        :return: `iterable` collection of vertices/nodes
        """
        pass

    def adj(self, u):
        """
        Returns a view on adjacent vertices/nodes of given vertex `u`.

        :param u: vertex for which the adjacent vertices are returned
        :return: `iterable` collection of neighbors of `u`
        """
        pass

    def deg(self, u):
        """
        Returns a degree of given vertex `u`.

        :param u: queried vertex
        :return: `deg(u)`
        """
        pass

    def edges(self):
        """
        Returns a `set` of edges in this graph.

        :return: `set` of edges as tuples of vertices
        """
        pass

    def weight(self, u, v):
        """
        Return a weiht of edge `{u, v}`.

        :param u: first vertex/node of the edge
        :param v: second vertex/node of the edge
        :return: weight `w({u, v})`
        """
        pass

    def edge_weight(self, edge):
        """
        Return a weiht of given `edge` represented as tuple of vertices.

        :param edge: edge as tuple of two vertices
        :return: weight `w(edge)`
        """
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Digraph(Graph):
    """
    Class representing an (weighted) directed simple graph.
    """

    def add_edge(self, u, v, weight=1.):
        pass

    def _add_adj(self, node, adj, weight):
        pass

    def remove_edge(self, u, v):
        """
        Remove edge `(u, v)` from this graph.

        :param u: first vertex/node of the removed edge
        :param v: second vertex/node of the removed edge
        """
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
