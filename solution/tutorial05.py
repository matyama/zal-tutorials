#!/usr/bin/env python

import random


def print_data(data):
    """
    Print elements of *data* with 'Znacka' prepended on one line, separated by ','.

    :param data: list of data elements
    """
    for i, e in enumerate(data):
        print('Znacka ' + str(e), end=', ' if i < len(data) - 1 else '\n')


def find(data, value):
    """
    Find *value* in *data*.

    :param data: list of data elements
    :param value: queried value
    :return: True if data contain value, False otherwise
    """
    for e in data:
        if e == value:
            return True
    return False


def add(data, value):
    """
    Add *value* to *data* if not already present.

    :param data: list of data elements
    :param value: value to be added
    """
    if not find(data, value):
        data.append(value)


def remove(data, value):
    """
    Remove *value* from *data* if present.

    :param data: list of data elements
    :param value: value to be removed
    """
    if find(data, value):
        data.remove(value)


def replace(data, value, replacement='odstraneno'):
    """
    Replace all occurences of *value* in *data* with *replacement*.

    :param data: list of data elements
    :param value: value to be replaced
    :param replacement: replacement value
    """
    for i, e in enumerate(data):
        if e == value:
            data[i] = replacement


def find_replaced(data, label='odstraneno'):
    """
    Find all occurrences of *label* in *data* and return corresponding indexes.

    :param data: list of data elements
    :param label: value to look for in the data
    :return: list of indices to occurrences of *label* in the data
    """
    return [i for i, e in enumerate(data) if e == label]


def reverse(data):
    """
    Reverse the order of elements in *data*. Implement this function "in-place", i.e. without creating auxiliary list.

    :param data: list of data elements
    """
    def swap(array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    n = len(data)
    for i in range(n // 2):
        swap(data, i, n - 1 - i)


def randoms(n, lb, ub):
    """
    Create and return list of *n* random numbers uniformly distributed on interval [lb, ub].

    :param n: number of generated random numbers (size of the list)
    :param lb: lower bound on generated values (included)
    :param ub: upper bound on generated values (included)
    :return: list of *n* random numbers from uniform(lb, ub)
    """
    if ub < lb or n < 1:
        raise ValueError('Illegal argument values.')

    # _ serves as an anonymous placeholder (i.e. imagine this is an arbitrary variable that is not used)
    return [random.randint(lb, ub) for _ in range(n)]


def maximum(array):
    """
    Return maximum value from given *array*.
    Side note: could be implemented using build-in function *max*, but let's not do that :)

    :param array: list of numbers
    :return: max(array) or -inf if empty
    """
    m = -float('inf')
    for e in array:
        if e > m:
            m = e
    return m


def fibonacci(x):
    """
    Return list of all Fibonacci numbers that are less or equal to *x*.

    :param x: upper bound (included)
    :return: list of Fibonacci numbers less or equal to *x*
    """
    fibs = []
    fib = fib_n1 = 1
    while fib <= x:
        fibs.append(fib)
        fib_n1, fib_n2 = fib, fib_n1
        fib = fib_n1 + fib_n2
    return fibs


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
