#!/usr/bin/env python3

import math
from solution.combinatorics import factorial


def range_sum_loop(a, b):
    s = 0
    for x in range(a, b + 1):
        s += x
    return s


def range_sum_func(a, b):
    return sum(range(a, b + 1))


def range_sum_expr(a, b):
    return (a + b) * (b - a + 1) / 2


def euler_naive(num_iters):
    return sum((1. / factorial(n)) for n in range(num_iters))


def euler(num_iters):
    e, f = 0., 1
    for n in range(1, num_iters + 1):
        e += 1. / f
        f *= n
    return e


def sqrt(x):
    def step(x_n):
        return (x_n + x / x_n) / 2., x_n

    x_new, x_old = step(x / 2.)
    while x_new != x_old:
        x_new, x_old = step(x_new)
    return x_new


def prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i, ub = 5, sqrt(n)
    while i <= ub:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


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
