#!/usr/bin/env python3


def factorial(n):
    """
    Computes factorial of n.

    :param n: non-negative integer
    :return: n!
    """
    pass


def factorial_rec(n):
    """
    Computes factorial of n. This implementation uses recursion.

    :param n: non-negative integer
    :return: n!
    """
    pass


def factorial_tailrec(n):
    """
    Computes factorial of n. This implementation uses tail-recursion (i.e. recursive call is the last call in the body).

    :param n: non-negative integer
    :return: n!
    """
    pass


def nchoosek(n, k):
    """
    Computes binomial coefficient C(n, k) = n! / (k! * (n - k)!).

    :param n: number of items to choose from
    :param k: number of items chosen
    :return: C(n, k)
    """
    pass


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
