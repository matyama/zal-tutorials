#!/usr/bin/env python3


def sieve_of_eratosthenes(n):
    """
    Implements The Sieve of Eratosthenes, which finds prime numbers up to given number n. Complexity: O(n*log(log(n)))

    :param n: upper bound
    :return: list (sieve) of booleans where sieve[i] is True iff i is composed number
    """
    pass


def print_sieve(sieve):
    for i in range(len(sieve)):
        print('{:d} is {:s}'.format(i, 'composed' if sieve[i] else 'prime'))


if __name__ == '__main__':
    composed = sieve_of_eratosthenes(20)
    print_sieve(composed)
