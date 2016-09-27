#!/usr/bin/env python3


def factorial(n):
    """
    Computes factorial of n.

    :param n: non-negative integer
    :return: n!
    """
    if n < 0:
        raise ValueError('n! is undefined for n < 0')
    f = 1
    for i in range(n, 1, -1):
        f *= i
    return f


def factorial_rec(n):
    """
    Computes factorial of n. This implementation uses recursion.

    :param n: non-negative integer
    :return: n!
    """
    if n < 0:
        raise ValueError('n! is undefined for n < 0')

    def rec(n):
        return 1 if n <= 1 else n * rec(n - 1)

    return rec(n)


def factorial_tailrec(n):
    """
    Computes factorial of n. This implementation uses tail-recursion (i.e. recursive call is the last call in the body).

    :param n: non-negative integer
    :return: n!
    """
    if n < 0:
        raise ValueError('n! is undefined for n < 0')

    def loop(n, acc):
        return acc if n <= 1 else loop(n - 1, n * acc)

    return loop(n, 1)


def nchoosek(n, k):
    """
    Computes binomial coefficient C(n, k) = n! / (k! * (n - k)!).

    :param n: number of items to choose from
    :param k: number of items chosen
    :return: C(n, k)
    """
    c = 1
    for l in range(k):
        c *= (n - l) / (k - l)
    return int(c)


if __name__ == '__main__':

    # test factorial
    for n in range(5):
        print('{:d}! = {:d} (iter)'.format(n, factorial(n)))
        print('{:d}! = {:d} (rec)'.format(n, factorial_rec(n)))
        print('{:d}! = {:d} (tail-rec)'.format(n, factorial_tailrec(n)))

    # test binomial coefficient
    for n in range(5):
        for k in range(5):
            print('C({:d}, {:d}) ='.format(n, k), nchoosek(n, k))
