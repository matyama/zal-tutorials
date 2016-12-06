#!/usr/bin/env python3


def dfs(graph, start, goal):
    """
    Find and return a path between `start` and `goal`. Use `Depth First Search` algorithm.

    :param graph: graph represented as an adjacency list
    :param start: initial vertex/node
    :param goal: terminal vertex/node
    :return: path between `start` and `goal` as `list` if one exists, otherwise empty `list`
    """
    pass


def bfs(graph, start, goal):
    """
    Find and return a path between `start` and `goal`. Use `Breadth First Search` algorithm.

    :param graph: graph represented as an adjacency list
    :param start: initial vertex/node
    :param goal: terminal vertex/node
    :return: path between `start` and `goal` as `list` if one exists, otherwise empty `list`
    """
    pass


if __name__ == '__main__':
    G = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['C'], 'F': []}
    print('G =', G)

    # ---------------------------------- test DFS ----------------------------------
    print('\nDFS:')
    print(dfs(G, 'A', 'C'))
    print(dfs(G, 'A', 'D'))
    print(dfs(dict(), 'A', 'C'))

    # ---------------------------------- test BFS ----------------------------------
    print('\bBFS:')
    print(bfs(G, 'A', 'C'))
    print(bfs(G, 'A', 'D'))
    print(bfs(dict(), 'A', 'C'))
