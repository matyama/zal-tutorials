#!/usr/bin/env python3

from tutorial06 import swap, randoms


def heap_sort(array):
    """
    Sort given `array` "in place" using Heap Sort (in ascending order).

    :param array: `list` of elements to be sorted
    """
    pass


if __name__ == '__main__':
    # create an array with 10 integers randomly selected from interval [1, 1000]
    data = randoms(10, 1, 1000)
    print(data)

    heap_sort(data)
    print(data)
