#!/usr/bin/env python3


def filter(pred, iterable):
    """
    Filter function takes unary predicate (function of one parameter returning bool) and some iterable sequence and
    filters out such elements e of the sequence for which pred(e) is false.

    :param pred: unary predicate
    :param iterable: iterable sequence
    :return: generator of elements e form iterable for which pred(e) == False
    """
    pass


def map(f, iterable):
    """
    Function *map* takes unary function (function with one parameter) *f* and some *iterable* sequence and maps each
    element *e* to *f(e)*, creating new sequence of these images.

    :param f: unary mapping function
    :param iterable: iterable sequence
    :return: sequence of f(e) for each element e of iterable
    """
    pass


def reduce(f, iterable, init=None):
    """
    Function *reduce* takes binary function (function of two arguments) *f*, some *sequence* of elements and optionally
    initial value *init*. *Reduce* consecutively applies *f* to it's previous output (initially equal to
    *init* or the first element of *sequence*) and next element of the *sequence*. Finally the accumulated value is
    returned.

    :param f: binary aggregating function
    :param sequence: iterable sequence
    :param init: initial value (default: *None*)
    :return: value aggregated by *f* on *sequence*, optionally initialized by *init*
    """
    pass


def reversed(iterable):
    """
    Function *reversed* takes some *iterable* sequence and returns new sequence with the order of elements reversed.

    :param iterable: iterable sequence
    :return: sequence of elements from *iterable* in reversed order
    """
    pass


if __name__ == '__main__':
    # testing sequence
    seq = list(range(10))
    print(seq)

    # test filter
    even = filter(lambda e: e % 2 == 0, seq)
    print(list(even))

    # test map
    double = map(lambda e: 2 * e, seq)
    print(list(double))

    # test reduce
    total = reduce(lambda s, e: s + e, seq, 0)
    print(total)

    # test reversed
    qes = reversed(seq)
    print(qes)
