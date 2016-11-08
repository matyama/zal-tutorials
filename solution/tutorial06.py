#!/usr/bin/env python3

from solution.tutorial05 import randoms


def swap(array, i, j):
    """
    Swap array's i-th and j-th element.

    :param array: list of elements
    :param i: position of the first swapped element
    :param j: position of the second swapped element
    """
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def min_idx(a, i):
    """
    Find index of the element in range of elements from given array *a* starting on given index *i* with minimal value.

    :param a: list of numerically comparable elements
    :param i: index of the first element to be considered
    :return: argmin {a[i], ..., a[n-1]} where n is the array's length
    """
    min_pos = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_pos]:
            min_pos = j
    return min_pos


def selection_sort(array):
    """
    Sort given array "in place" in ascending order using *selection sort*.

    :param array: list of numerically comparable elements
    """
    for i in range(len(array)):
        # compute k = argmin {array[i], ..., array[n-1]} and swap array[i] and array[k]
        k = min_idx(array, i)
        swap(array, i, k)


def insertion_sort(array):
    """
    Sort given array "in place" in ascending order using *insertion sort*.

    :param array: list of numerically comparable elements
    """
    for i in range(len(array)):
        # insert a[i] on appropriate place between a[0], ..., a[i]
        ai, pos = array[i], i
        # while not on the first element and a[i] is smaller than a[pos-1] do
        while pos > 0 and array[pos - 1] > ai:
            # move element a[pos-1] one position up (replace previous element a[pos]) and decrement position pointer
            array[pos] = array[pos - 1]
            pos -= 1
        # place a[i] on it's position
        array[pos] = ai


def nth(array, n=1, sort_strategy=insertion_sort):
    """
    Find the n-th smallest element of given *array*.

    :param array: list of numerically comparable elements
    :param n: requested position of the returned element
    :param sort_strategy: function that takes the array and sorts it
    :return: n-th smallest element of *array*
    """

    if n < 1 or n > len(array):
        raise ValueError("Invalid argument n: %d" % n)
    sort_strategy(array)
    return array[n - 1]


if __name__ == '__main__':
    # create an array with 10 integers randomly selected from interval [1, 1000]
    a1 = randoms(10, 1, 1000)
    print(a1)

    # test swap
    swap(a1, 2, 6)
    print(a1)

    # test min_idx
    print(min_idx(a1, 2))

    # test insertion sort
    insertion_sort(a1)
    print(a1)

    # create another array of random integers from uniform(1, 1000)
    a2 = randoms(10, 1, 1000)
    print(a2)

    # test selection sort
    selection_sort(a2)
    print(a2)

    # test n-th smallest element
    print(nth(a1, 2))
    print(nth(a2, 4))
