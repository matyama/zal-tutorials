#!/usr/bin/env python3

import math
from combinatorics import factorial


def range_sum_loop(a, b):
    pass


def range_sum_func(a, b):
    pass


def range_sum_expr(a, b):
    pass


def euler_naive(num_iters):
    pass


def euler(num_iters):
    pass


def sqrt(x):
    pass


def prime(n):
    pass


if __name__ == '__main__':

    # function range(n) creates a generator/iterator of numbers from interval [0,n), the default step is 1
    r = range(10)
    print(r, type(r))

    # in order to display the sequence, we can use list() constructor
    print(list(r))

    # one can also define the initial element - in this case the sequence starts with 1
    r2 = range(1, 5)
    print(list(r2))

    # typical usage is in a for loop - the body is in this case evaluated for i = 2, 4, 6, 8
    for i in range(2, 10, 2):
        print(i)

    print('continue, break:')

    # with any loop comes in hand pair of statements: continue and break
    for i in range(5):
        if i == 1:
            # when continue is called, the rest of the block is not evaluated and the loop continues with next iter.
            continue
        if i == 3:
            # when break is called, the loop execution breaks at this point and we continue after the loop body
            break
        print(i)

    print('while:')

    # next loop type is while which iterates while it's loop condition is satisfied
    x = 2
    while x ** 2 < 100:
        print(x ** 2)
        x += 2

    # advanced usage of for is "list comprehension"
    squares = [x ** 2 for x in range(2, 10, 2)]
    print(type(squares), squares)

    # one can even use if filter in list comprehensions
    odd = [x for x in range(1, 10) if x % 2 == 1]
    print(odd)

    # how to create your own generator? - simply use () in comprehension
    even = (2 * k for k in range(10))
    print(type(even), even, list(even))

    print('range_sum:')

    print(range_sum_loop(2, 10))
    print(range_sum_func(2, 10))
    print(range_sum_expr(2, 10))

    print("euler's number:")
    print(euler_naive(100))
    print(euler(100))
    print(math.e)

    print('sqrt:')
    print(sqrt(5.))
    print(math.sqrt(5.))

    print('primality test')
    print(prime(13))
    print(prime(256))
