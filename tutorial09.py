#!/usr/bin/env python3

from tutorial06 import swap, randoms


def fibonacci(n):
    """
    Compute first `n` Fibonacci numbers. Use iterative algorithm.

    :param n: number of Fibonacci numbers to return
    :return: `list` of first `n` Fibonacci numbers
    """
    pass


def fibonacci_rec(n):
    """
    Compute first `n` Fibonacci numbers. Use recursive algorithm.

    :param n: number of Fibonacci numbers to return
    :return: `list` of first `n` Fibonacci numbers
    """
    pass


def gcd(a, b):
    """
    Compute greatest common divisor of numbers `a` and `b`.

    :param a: non-negative integer
    :param b: non-negative integer
    :return: `gcd(a, b)`
    """
    pass


def lcm(a, b):
    """
    Compute least common multiplier of numbers `a` and `b`.

    :param a: non-negative integer
    :param b: non-negative integer
    :return: `lcm(a, b)`
    """
    pass


def reverse(array):
    """
    List elements from given array in reversed order and return them as a new `list`.

    :param array: `list` of elements
    :return: `list` of elements from `array` in reversed order
    """
    pass


def quick_sort(array):
    """
    Sort given `list` "in place" in ascending order. Use `Quicksort` algorithm. Asymptotic complexity of running
    Quicksort on an array with `n` elements is O(n^2). Quicksort is not stable!

    :param array: `list` of elements to be sorted
    """
    pass


def merge_sort(array):
    """
    Sort given `list` "in place" in ascending order. Use `Mergesort` algorithm. Asymptotic complexity of running
    Mergesort on an array with `n` elements is O(n*log(n)). Mergesort is stable sorting algorithm.

    :param array: `list` of elements to be sorted
    """
    pass


if __name__ == '__main__':
    # ---------------------------------- test fibonacci ----------------------------------
    print('Fibonacci series:')
    print('fib_iter(10) =', fibonacci(10))
    print('fib_rec(10) =', fibonacci_rec(10))

    # ---------------------------------- test gcd ----------------------------------
    print('\nGreatest common divisor:')
    print('gcd(4, 2) =', gcd(4, 2))
    print('gcd(140, 15) =', gcd(140, 15))
    print('gcd(133, 15) =', gcd(133, 15))

    # ---------------------------------- test lcm ----------------------------------
    print('\nLeast common multiplier:')
    print('lcm(140, 15) =', lcm(140, 15))

    # ---------------------------------- test reversed ----------------------------------
    print('\nreverse list:')
    data = [5, 4, 3, 2, 1, 0]
    print('data =', data)
    reversed_data = reverse(data)
    print('reversed(data) =', reversed_data)

    # ---------------------------------- test quicksort ----------------------------------
    print('\nQuickSort:')
    data2 = randoms(10, 0, 100)
    print('data2 =', data2)
    quick_sort(data2)
    print('sorted(data2) =', data2)

    # ---------------------------------- test mergesort ----------------------------------
    print('\nMergeSort:')
    data3 = randoms(10, 0, 100)
    print('data3 =', data3)
    merge_sort(data3)
    print('sorted(data3) =', data3)
