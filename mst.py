#!/usr/bin/env python3

from graph import Graph
from union_find import UnionFind

from utils.prim_mst_heap import heapify, pop, update, key


def kruskal_mst(graph):
    """
    Implement Kruskal's algorithm for finding the minimum spanning tree (minimalni kostra grafu). Given a weighted
    connected simple undirected graph G, a spanning tree is a factor of G (sub-graph which has all vertices of G)
    which is a tree. The weight/cost of a spanning tree is the sum of weights/costs of all it's edges.

    Kruskal's algorithm is in theory simple procedure with following steps:

    1. initialize the spanning tree K as an empty graph
    2. sort edges of G in ascending order of their weights/costs
    3. for each edge e in this sorted list:
        a. if adding e to K does not close a cycle (this would violate the tree property of K), add it to K
        b. otherwise continue with next edge until n-1 edges was added (n is the number of vertices)

    The difficult part is the tree property check. An efficient how to implement this is using the *union-find* data
    structure. Testing whether adding edge (u, v) creates a cycle corresponds to querying whether u and v are in
    disjoint sets (operation *find*). Adding an edge then corresponds to *union*.

    As analyzed in the *union-find* exercise, both *union* and *find* take O(log(n)) where n is the number of vertices
    (n = |V(G)|). Denoting the number of edges m (m = |E(G)|), the loop in Kruskal's algorithm takes O(m*log(n)).
    Sorting the edges takes O(m*log(m)) time. Putting these two results together and realizing that in the worst case
    m = n^2, the complexity of the whole procedure is O(m*log(n)).

    :param graph: weighted connected simple undirected graph as instance of Graph
    :return: minimum spanning tree as instance of Graph
    """
    pass


def prim_mst(graph):
    """
    Implement Jarnik-Prim's algorithm for finding the minimum spanning tree (minimalni kostra grafu). Given a weighted
    connected simple undirected graph G, a spanning tree is a factor of G (sub-graph which has all vertices of G)
    which is a tree. The weight/cost of a spanning tree is the sum of weights/costs of all it's edges.

    For implementation see https://en.wikipedia.org/wiki/Prim's_algorithm.

    :param graph: weighted connected simple undirected graph as instance of Graph
    :return: minimum spanning tree as instance of Graph
    """
    pass


if __name__ == '__main__':
    E = {(0, 1, 2), (0, 2, 2), (0, 3, 3), (1, 2, 1),
         (1, 3, 2), (1, 4, 3), (2, 3, 1), (2, 4, 2)}

    G = Graph(E)
    print(G)

    K = kruskal_mst(G)
    w = sum(K.edge_weight(e) for e in K.edges())
    print('K =', K)
    print('w(K) =', w)

    K = prim_mst(G)
    w = sum(K.edge_weight(e) for e in K.edges())
    print('K =', K)
    print('w(K) =', w)
