#!/usr/bin/env python3

from solution.graph import Digraph


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
    Find all strongly connected conponenets of given `digraph`.

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
        v.pred = stack
        v.in_stack = True
        return v

    def pop(stack):
        """
        Pop top vertex from the `stack`.

        :param stack: reference to stack top
        :return: (removed top, new stack)
        """
        S, v = stack.pred, stack
        v.pred = None
        v.in_stack = False
        return v, S

    def find_scc(v, index, stack):

        index += 1
        v.index = v.low_link = index
        stack = push(stack, v)

        for w in digraph.adj(v):

            if w.index is None:  # not yet visited
                index, stack = find_scc(w, index, stack)
                v.low_link = min(v.low_link, w.low_link)
            elif w.in_stack:
                v.low_link = min(v.low_link, w.index)

        # if `v` is the head of a SCC
        if v.low_link == v.index:
            component = set()
            while True:
                x, stack = pop(stack)
                # add `x` to `component` and assign the reference back to `x`
                component.add(x)
                x.scc = component
                if x == v:
                    break
            # output the SCC
            scc.append(component)

        return index, stack

    scc = []  # `list` of SCC
    stack = None  # stack top
    index = -1

    for node in digraph.nodes():
        # if node is unvisited
        if node.index is None:
            # collect SCCs from this node
            index, stack = find_scc(node, index, stack)

    # return collected SCCs
    return scc


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