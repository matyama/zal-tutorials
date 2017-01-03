#!/usr/bin/python3

"""
Implementation is largely based on https://svn.python.org/projects/sandbox/trunk/collections/prim_mst_heap.py
"""


def cmp(a, b):
    return (a > b) - (a < b)


class HeapNode:
    __slots__ = ('_item', '_child', '_sibling', '_parent')

    def __init__(self, item):
        self._item = item
        self._clean()

    def value(self):
        return self._item

    def _clean(self):
        self._child = None
        self._sibling = None
        self._parent = None

    def _add_child(self, node):
        node._parent = self
        node._sibling = self._child
        self._child = node

    def _cut(self):
        n = self._parent
        if id(n._child) == id(self):
            n._child = self._sibling
        else:
            n = n._child
            try:
                while id(n._sibling) != id(self):
                    n = n._sibling
                n._sibling = self._sibling
            except AttributeError:
                raise ValueError('internal error')
        self._parent = None
        self._sibling = None

    def _extract(self, heap):
        children = []
        n = self._child
        while n and n._sibling:
            next = n._sibling._sibling
            pair = n._sibling
            n._parent = None
            n._sibling = None
            pair._parent = None
            pair._sibling = None
            children.append(heap._link(n, pair))
            n = next
        if n:
            children.append(n)
        if not children:
            return None

        root = children[-1]
        for i in range(len(children)-2, -1, -1):
            root = heap._link(root, children[i])
        root._parent = None

        return root

    def values(self):
        rv = [self._item, ]
        if self._child:
            rv += self._child.values()
        if self._sibling:
            rv += self._sibling.values()
        return rv


class PairingHeap:

    def __init__(self, values=list(), cmpfunc=None, key=None, reverse=False):
        self._cmpfunc = cmpfunc
        self._key = key
        self._reverse = reverse
        self._root = None
        self._len = 0
        self.heapify(values)

    def heapify(self, values=list()):
        return {v: self.insert(v) for v in values}

    def __len__(self):
        return self._len

    def __bool__(self):
        return len(self) > 0

    def _cmp(self, item1, item2):
        if self._key:
            item1 = getattr(item1, self._key)
            item2 = getattr(item2, self._key)

        c = self._cmpfunc(item1, item2) if self._cmpfunc else cmp(item1, item2)
        return -c if self._reverse else c

    def _link(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1

        if self._cmp(node1._item, node2._item) > 0:
            node2._add_child (node1)
            return node2
        else:
            node1._add_child (node2)
            return node1

    def insert(self, item):
        node = HeapNode(item)
        self._root = self._link(node, self._root)
        self._len += 1
        return node

    def decrease_key(self, node, item):
        node._item = item
        if id(self._root) == id(node):
            return
        node._cut()
        self._root = self._link(node, self._root)

    def delete_min(self):
        if not self._root:
            raise ValueError('no such element')
        old_root = self._root
        self._root = self._root._extract(self)
        self._len -= 1
        old_root._clean()
        return old_root._item

    def values(self):
        return self._root.values()


INF = float('inf')


def heapify(vertices):
    """
    Build a heap from given `vertices`. Keys are set to infinity for each vertex except the first one which gets 0.
    Returns an instance of the heap and `dict` of references to heap nodes indexed by `vertices`.

    :param vertices: `iterable` collection of vertices
    :return: heap and `dict` of heap nodes indexed by `vertices`
    """
    heap = PairingHeap(cmpfunc=lambda x, y: cmp(x[0], y[0]))
    refs = {v: heap.insert((0 if i == 0 else INF, v)) for i, v in enumerate(vertices)}
    return heap, refs


def pop(heap):
    """
    Remove and return the first element (vertex) on the `heap`.

    :param heap: heap created by `heapify`
    :return: first vertex on the heap
    """
    _, v = heap.delete_min()
    return v


def update(heap, ref, v, new_key):
    """
    Update node `ref` in the `heap` to `new_key`

    :param heap: heap created by `heapify`
    :param ref: `v`'s heap node
    :param v: vertex to be updated
    :param new_key: new value (weight/cost) of `v`
    """
    heap.decrease_key(ref, (new_key, v))


def key(refs, v):
    """
    Return the key (weight/cost) of vertex `v` given heap node references `refs`.

    :param refs: `dict` of heap node references created by `heapify`
    :param v: queried vertex
    :return: key (weight/cost) of `v`
    """
    return refs[v].value()[0] if v in refs else -INF
