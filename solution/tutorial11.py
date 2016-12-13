#!/usr/bin/env python3

from solution.tutorial06 import swap, randoms


def heap_sort(array):
    """
    Sort given `array` "in place" using Heap Sort (in ascending order).

    :param array: `list` of elements to be sorted
    """
    n = len(array)

    # create a heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, i, n - 1)

    # sort
    for i in range(n - 1, 0, -1):
        swap(array, 0, i)
        heapify(array, 0, i - 1)


def heapify(a, top, bottom):
    # a[2*i] and a[2*i+1] are children of a[i]
    succ = 2 * top + 1
    top_val = a[top]

    # try to find a child < `top_val`
    if succ < bottom and a[succ + 1] > a[succ]:
        succ += 1

    # while children < `top_val` move children up
    while succ <= bottom and a[succ] > top_val:
        a[top] = a[succ]
        # skip to next child
        top = succ
        succ = 2 * succ + 1
        if succ < bottom and a[succ + 1] > a[succ]:
            succ += 1

    # put `top_val` where it belongs
    a[top] = top_val


if __name__ == '__main__':
    # create an array with 10 integers randomly selected from interval [1, 1000]
    data = randoms(10, 1, 1000)
    print(data)

    heap_sort(data)
    print(data)
