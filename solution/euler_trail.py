#!/usr/bin/env python3

from solution.graph import Graph


def euler_trail(graph):
    """
    TODO: implement

    :param graph:
    :return:
    """
    return []


if __name__ == '__main__':
    E = {('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'),
         ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E')}

    G = Graph(E)
    print(G)
