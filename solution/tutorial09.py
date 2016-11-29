#!/usr/bin/env python3

from solution.tutorial06 import swap, randoms


def fibonacci(n):
    """
    Compute first `n` Fibonacci numbers. Use iterative algorithm.

    :param n: number of Fibonacci numbers to return
    :return: `list` of first `n` Fibonacci numbers
    """

    if n < 1:
        raise ValueError('n < 1')

    if n == 1:
        return [0]

    fibs = [0, 1]
    fib = fib_n1 = 1
    while len(fibs) < n:
        fibs.append(fib)
        fib_n1, fib_n2 = fib, fib_n1
        fib = fib_n1 + fib_n2
    return fibs


def fibonacci_rec(n):
    """
    Compute first `n` Fibonacci numbers. Use recursive algorithm.

    :param n: number of Fibonacci numbers to return
    :return: `list` of first `n` Fibonacci numbers
    """

    def collect(f1, f2, fibs):
        if len(fibs) == n:
            return fibs
        f = f1 + f2
        fibs.append(f)
        return collect(f2, f, fibs)

    if n < 1:
        raise ValueError('n < 1')

    return [0] if n == 1 else collect(0, 1, [0, 1])


def gcd(a, b):
    """
    Compute greatest common divisor of numbers `a` and `b`.

    :param a: non-negative integer
    :param b: non-negative integer
    :return: `gcd(a, b)`
    """

    def gcd_rec(x, y):
        # if the reminder `y` is zero, return `x`
        if y == 0:
            return x
        # else iterate with `x := y` and `y` as the reminder of `x / y`
        return gcd_rec(y, x % y)

    # check input values
    if a < 0 or b < 0:
        raise ValueError('invalid arguments: a=%d, b=%d' % (a, b))

    # check input order - expected `a >= b`
    if a < b:
        return gcd(b, a)

    # call recursive function to compute `gcd(a, b)`
    return gcd_rec(a, b)


def lcm(a, b):
    """
    Compute least common multiplier of numbers `a` and `b`.

    :param a: non-negative integer
    :param b: non-negative integer
    :return: `lcm(a, b)`
    """
    return (a * b) // gcd(a, b)


def reverse(array):
    """
    List elements from given array in reversed order and return them as a new `list`.

    :param array: `list` of elements
    :return: `list` of elements from `array` in reversed order
    """

    def rev(a, r, i):
        # termination condition - when iterated the whole input list (`i < 0`), return reversed list `r`
        if i < 0:
            return r
        # otherwise append i-th element from input array (notice: we use index `i` so that the order will be reversed)
        r.append(a[i])
        # iterate: call `rev` for `i-1`
        return rev(a, r, i - 1)

    # initialize the algorithm by calling `rev` with empty resutl and `i = len(array)-1`
    return rev(array, [], len(array) - 1)


def quick_sort(array):
    """
    Sort given `list` "in place" in ascending order. Use `Quicksort` algorithm. Asymptotic complexity of running
    Quicksort on an array with `n` elements is O(n^2). Quicksort is not stable!

    :param array: `list` of elements to be sorted
    """

    def qsort(a, low, high):
        """
        Sort given `list` on positions between `low` and `high` (inclusive).

        :param a: `list` of elements to be sorted from `low` to `high` position
        :param low: index of the first element to be sorted in `a`
        :param high: index of the last element to be sorted in `a`
        """

        # init pointers `i_left` and `i_right` and select the pivot (e.g. as the first element)
        i_left, i_right = low, high
        pivot = a[low]

        # do while `i_left <= i_right` (i.e. break when `i_left > i_right`)
        while True:

            # move `i_left` to the first element from the left that is greater or equal to the pivot
            while a[i_left] < pivot:
                i_left += 1

            # move `i_right` to the first element from the right that is less or equal to the pivot
            while a[i_right] > pivot:
                i_right -= 1

            if i_left < i_right:
                # swap a[i_left] and a[i_right] and make one step with both pointers
                swap(a, i_left, i_right)
                i_left += 1
                i_right -= 1
            elif i_left == i_right:
                # make one more step so that the loop can break
                i_left += 1
                i_right -= 1

            # break the loop
            if i_left > i_right:
                break

        # divide step - sort the "left" (e < pivot) and "right" (e > pivot) parts separately
        if low < i_right:
            qsort(a, low, i_right)
        if i_left < high:
            qsort(a, i_left, high)

    # call the recursive function on given array
    qsort(array, 0, len(array) - 1)


def merge_sort(array):
    """
    Sort given `list` "in place" in ascending order. Use `Mergesort` algorithm. Asymptotic complexity of running
    Mergesort on an array with `n` elements is O(n*log(n)). Mergesort is stable sorting algorithm.

    :param array: `list` of elements to be sorted
    """

    def merge(a_in, a_out, low, high):
        """
        Merge elements from `a_in` to `a_out`. Consider only elements between `low` and `high`.

        :param a_in: `list` of elements to be merged
        :param a_out: `list` of merged elements
        :param low: index of the first element to consider
        :param high: index of the last element to consider
        """
        half = (low + high) // 2
        i1, i2 = low, half + 1
        j = low

        # compare and merge
        while i1 <= half and i2 <= high:
            if a_in[i1] <= a_in[i2]:
                a_out[j] = a_in[i1]
                i1 += 1
            else:
                a_out[j] = a_in[i2]
                i2 += 1
            j += 1

        # copy the rest
        while i1 <= half:
            a_out[j] = a_in[i1]
            i1 += 1
            j += 1

        # copy the rest
        while i2 <= high:
            a_out[j] = a_in[i2]
            i2 += 1
            j += 1

    def sort(a, aux, low, high):
        """
        Sort given `list` on positions between `low` and `high` (inclusive) using `aux` array.

        :param a: `list` of elements to be sorted from `low` to `high` position
        :param aux: auxiliary `list`
        :param low: index of the first element to be sorted in `a`
        :param high: index of the last element to be sorted in `a`
        """
        half = (low + high) // 2
        if low >= high:
            # too small
            return

        # sort left and right half and merge the results
        sort(a, aux, low, half)
        sort(a, aux, half + 1, high)
        merge(a, aux, low, high)

        # put back to `a`- possible optimization: swap pointers to `a` and `aux`
        for i in range(low, high + 1):
            a[i] = aux[i]

    # call the recursive function on given array
    sort(array, [ai for ai in array], 0, len(array) - 1)


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
