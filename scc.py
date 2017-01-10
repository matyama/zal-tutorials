#!/usr/bin/env python3

from graph import Digraph


class Node:

    def __init__(self, name):
        self.name = name
        self.index = None  # unique node ID
        self.low_link = None  # ties node to others in SCC
        self.pred = None  # pointer to stack predecessor
        self.in_stack = False  # `True` if node is in stack
        self.scc = None  # SCC this node belongs to

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


def tarjan_scc(digraph):
    """
    Find all strongly connected components of given `digraph`. Use Tarjan's algorithm.
    For implementation see e.g. http://cw.fel.cvut.cz/wiki/_media/courses/a4m33pal/2012pal03.pdf.

    :param digraph: directed graph as instance of `Digraph`
    :return: `list` of `set`s representing strongly connected components of `graph`
    """

    def push(stack, v):
        """
        Push vertex `v` on the `stack`.

        :param stack: reference to stack top
        :param v: node to be added
        :return: new stack top
        """
        pass

    def pop(stack):
        """
        Pop top vertex from the `stack`.

        :param stack: reference to stack top
        :return: (removed top, new stack)
        """
        pass

    def find_scc(v, index, stack):
        pass

    pass


if __name__ == '__main__':

    N = {n: Node(n) for n in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}

    E = [(N['a'], N['b']), (N['b'], N['c']), (N['b'], N['e']),
         (N['b'], N['f']), (N['c'], N['d']), (N['c'], N['g']),
         (N['d'], N['c']), (N['d'], N['h']), (N['h'], N['d']),
         (N['h'], N['g']), (N['g'], N['f']), (N['f'], N['g']),
         (N['e'], N['a']), (N['e'], N['f'])]

    G = Digraph(E)
    print('G =', G)
    print('SCC(G) =', tarjan_scc(G))

    print('SCC per node:')
    for n in N.values():
        print('SCC(%s) = %s' % (n, n.scc))