#!/usr/bin/env python3


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Queue:
    def __init__(self, elements=list()):
        pass

    def add(self, e):
        """
        Add an element `e` at the end of this queue.

        :param e: data element
        """
        pass

    def remove(self):
        """
        Remove and return an element from the beginning of this queue.

        :return: first data element
        """
        pass

    def list(self):
        """
        Return this queue as a `list`.

        :return: `list` of data elements in this queue
        """
        pass

    def __len__(self):
        pass

    def __bool__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Stack:
    def __init__(self, elements=list()):
        pass

    def add(self, e):
        """
        Add an element `e` to the top of this stack.

        :param e: data element
        """
        pass

    def remove(self):
        """
        Remove and return an element on from the top of this stack.

        :return: top data element
        """
        pass

    def list(self):
        """
        Return this stack as a `list`.

        :return: `list` of data elements in this stack
        """
        pass

    def __len__(self):
        pass

    def __bool__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


if __name__ == '__main__':

    print('data:')
    data = [2, -1, 7, 13, 22, 0, -1, 4]
    print(data)

    # ---------------------------------- test queue ----------------------------------
    print('\n---- test queue ----')

    print('\ntest queue-add:')

    queue = Queue()
    print(queue, '\thead: %s' % queue.head, 'tail: %s' % queue.tail)
    for e in data:
        queue.add(e)
        print(queue, '\thead: %s' % queue.head, 'tail: %s' % queue.tail)

    print('\ntest queue-remove:')

    for _ in range(len(queue)):
        print(queue.remove(), '\thead: %s' % queue.head, '\ttail: %s' % queue.tail)

    # ---------------------------------- test stack ----------------------------------
    print('\n---- test stack ----')

    print('\ntest stack-add:')

    stack = Stack()
    print(stack, '\ttop: %s' % stack.top)
    for e in data:
        stack.add(e)
        print(stack, '\ttop: %s' % stack.top)

    print('\ntest stack-remove:')

    for _ in range(len(stack)):
        print(stack.remove(), '\ttop: %s' % stack.top)
