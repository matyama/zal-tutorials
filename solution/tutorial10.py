#!/usr/bin/env python3

from solution.tutorial08 import Queue, Stack


def find_path(graph, start, goal, fringe):

    def construct_path(pred, n):
        path = []
        while True:
            path = [n] + path # this can be optimized using `deque`
            if n not in pred:
                break
            n = pred[n]
        return path

    def successors(g, n):
        return g.get(n, [])

    # initialize path and state
    p = dict()
    state = dict()

    # add initial node to the fringe
    fringe.add(start)

    # while the fringe is non-empty
    while fringe:

        # retrieve first node in the fringe and mark it as open
        node = fringe.remove()
        state[node] = 'OPEN'

        # check terminal condition
        if node == goal:
            # return reversed path from the goal
            return construct_path(p, node)

        # expand current node
        for succ in successors(graph, node):
            # check whether the successor is unvisited
            if succ not in state:
                # update path
                p[succ] = node
                # add successor to the fringe
                fringe.add(succ)

        # mark current node as closed
        state[node] = 'CLOSED'

    return []


def dfs(graph, start, goal):
    """
    Find and return a path between `start` and `goal`. Use `Depth First Search` algorithm.

    :param graph: graph represented as an adjacency list
    :param start: initial vertex/node
    :param goal: terminal vertex/node
    :return: path between `start` and `goal` as `list` if one exists, otherwise empty `list`
    """
    return find_path(graph, start, goal, Stack())


def bfs(graph, start, goal):
    """
    Find and return a path between `start` and `goal`. Use `Breadth First Search` algorithm.

    :param graph: graph represented as an adjacency list
    :param start: initial vertex/node
    :param goal: terminal vertex/node
    :return: path between `start` and `goal` as `list` if one exists, otherwise empty `list`
    """
    return find_path(graph, start, goal, Queue())


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
