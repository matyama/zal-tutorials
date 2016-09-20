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

    for n in range(5):
        print('{:d}! ='.format(n), factorial(n))

    for n in range(5):
        for k in range(5):
            print('C({:d}, {:d}) ='.format(n, k), nchoosek(n, k))
