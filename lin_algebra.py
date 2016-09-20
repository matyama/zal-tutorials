#!/usr/bin/env python3


def dot(x, y):
    """
    Implements the dot product x * y.

    :param x vector
    :param y vector
    """
    if len(x) != len(y):
        raise ValueError('x and y have different dimension')

    sum = 0.
    for i in range(len(x)):
        sum += x[i] * y[i]
    return sum


def transpose(A):
    """
    Implements matrix transposition A'.

    :param A: matrix of size m * n
    :return: transposed matrix A' of size n * m
    """
    m, n = len(A), len(A[0])
    B = []
    for j in range(n):
        B.append([])
        for i in range(m):
            B[j].append(A[i][j])
    return B


def mul(A, B):
    """
    Implements matrix multiplication A * B.

    :param A: matrix of size m * p
    :param B: matrix of size p * n
    :return: C = A * B of dimensions m * n
    """

if __name__ == '__main__':

    x = [1, 2, 3]
    y = [2, 2, 1]

    s = dot(x, y)
    print(s)

    A = [x, y]
    B = transpose(A)
    print(B)

