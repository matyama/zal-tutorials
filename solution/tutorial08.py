#!/usr/bin/env python3


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)


class Queue:
    def __init__(self, elements=list()):
        self.head = None
        self.tail = None
        self.size = 0
        for e in elements:
            self.add(e)

    def add(self, e):
        """
        Add an element `e` at the end of this queue.

        :param e: data element
        """
        if self.tail:
            self.tail.next_node = Node(e, prev_node=self.tail)
            self.tail = self.tail.next_node
        else:
            self.head = self.tail = Node(e)
        self.size += 1

    def remove(self):
        """
        Remove and return an element from the beginning of this queue.

        :return: first data element
        """
        if not self:
            raise ValueError('empty queue')
        data = self.head.data
        self.head = self.head.next_node
        if self.head:
            self.head.prevNode = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def list(self):
        """
        Return this queue as a `list`.

        :return: `list` of data elements in this queue
        """
        n = self.head
        l = []
        while n:
            l.append(n.data)
            n = n.next_node
        return l

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.head is not None

    def __str__(self):
        return str(self.list())

    def __repr__(self):
        return str(self)


class Stack:
    def __init__(self, elements=list()):
        self.top = None
        self.size = 0
        for e in elements:
            self.add(e)

    def add(self, e):
        """
        Add an element `e` to the top of this stack.

        :param e: data element
        """
        if self.top:
            old_top = self.top
            self.top = Node(e, next_node=old_top)
            old_top.prev_node = self.top
        else:
            self.top = Node(e)
        self.size += 1

    def remove(self):
        """
        Remove and return an element on from the top of this stack.

        :return: top data element
        """
        if not self:
            raise ValueError('empty stack')
        data = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return data

    def list(self):
        """
        Return this stack as a `list`.

        :return: `list` of data elements in this stack
        """
        n = self.top
        l = []
        while n:
            l.append(n.data)
            n = n.next_node
        return l

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.top is not None

    def __str__(self):
        return str(self.list())

    def __repr__(self):
        return str(self)


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
