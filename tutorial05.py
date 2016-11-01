#!/usr/bin/env python

import random


def print_data(data):
    """
    Print elements of *data* with 'Znacka' prepended on one line, separated by ','.

    :param data: list of data elements
    """
    pass


def find(data, value):
    """
    Find *value* in *data*.

    :param data: list of data elements
    :param value: queried value
    :return: True if data contain value, False otherwise
    """
    pass


def add(data, value):
    """
    Add *value* to *data* if not already present.

    :param data: list of data elements
    :param value: value to be added
    """
    pass


def remove(data, value):
    """
    Remove *value* from *data* if present.

    :param data: list of data elements
    :param value: value to be removed
    """
    pass


def replace(data, value, replacement='odstraneno'):
    """
    Replace all occurences of *value* in *data* with *replacement*.

    :param data: list of data elements
    :param value: value to be replaced
    :param replacement: replacement value
    """
    pass


def find_replaced(data, label='odstraneno'):
    """
    Find all occurrences of *label* in *data* and return corresponding indexes.

    :param data: list of data elements
    :param label: value to look for in the data
    :return: list of indices to occurrences of *label* in the data
    """
    pass


def reverse(data):
    """
    Reverse the order of elements in *data*. Implement this function "in-place", i.e. without creating auxiliary list.

    :param data: list of data elements
    """
    pass


def randoms(n, lb, ub):
    """
    Create and return list of *n* random numbers uniformly distributed on interval [lb, ub].

    :param n: number of generated random numbers (size of the list)
    :param lb: lower bound on generated values (included)
    :param ub: upper bound on generated values (included)
    :return: list of *n* random numbers from uniform(lb, ub)
    """
    pass


def maximum(array):
    """
    Return maximum value from given *array*.
    Side note: could be implemented using build-in function *max*, but let's not do that :)

    :param array: list of numbers
    :return: max(array) or -inf if empty
    """
    pass


def fibonacci(x):
    """
    Return list of all Fibonacci numbers that are less or equal to *x*.

    :param x: upper bound (included)
    :return: list of Fibonacci numbers less or equal to *x*
    """
    pass


if __name__ == '__main__':
    manufactures = ['Ford', 'Audi', 'Alfa Romeo', 'Skoda', 'Toyota']

    # test print
    print('test print:')
    print_data(manufactures)

    # test find
    print('\ntest find:')
    print(find(manufactures, 'Skoda'))
    print(find(manufactures, 'BMW'))

    # test add
    print('\ntest add:')
    add(manufactures, 'BMW')
    print(manufactures)
    add(manufactures, 'Audi')
    print(manufactures)

    # test remove
    print('\ntest remove:')
    remove(manufactures, 'BMW')
    print(manufactures)
    remove(manufactures, 'BMW')
    print(manufactures)

    # test replace
    print('\ntest replace:')
    replace(manufactures, 'BMW')
    print(manufactures)
    replace(manufactures, 'Alfa Romeo')
    print(manufactures)

    # test find replaced
    print('\ntest find replaced:')
    print(find_replaced(manufactures))

    # test reverse
    print('\ntest reverse:')
    reverse(manufactures)
    print(manufactures)

    # test random array
    print('\ntest random array:')
    array = randoms(10, 1, 1000)
    print(array)

    # test maximum
    print('\ntest maximum:')
    print(maximum(array))
    print(maximum([]))

    # test fibonacci
    print('\ntest fibonacci:')
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(10))
    print(fibonacci(50))
