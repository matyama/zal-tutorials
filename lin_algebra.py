#!/usr/bin/env python3


def dot(x, y):
    """
    Implements the dot product x * y.

    :param x real vector
    :param y real vector
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

    :param A: real matrix of size m * n
    :return: transposed matrix A' of size n * m
    """
    m, n = len(A), len(A[0])
    B = []
    for j in range(n):
        B.append([])
        for i in range(m):
            B[j].append(A[i][j])
    return B


def add(A, B):
    """
    Implements matrix addition A + B.

    :param A: real matrix of size m * n
    :param B: real matrix of size m * n
    :return: C = A + B
    """
    m, n = len(A), len(A[0])
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(A[i][j] + B[i][j])
    return C


def sub(A, B):
    """
    Implements matrix subtraction A - B.

    :param A: real matrix of size m * n
    :param B: real matrix of size m * n
    :return: C = A - B
    """
    return add(A, smul(-1., B))


def smul(s, A):
    """
    Implements scalar multiplication s * A.

    :param s: real scalar
    :param A: real matrix of size m * n
    :return: B = s * A
    """
    m, n = len(A), len(A[0])
    B = []
    for i in range(m):
        B.append([])
        for j in range(n):
            B[i].append(s * A[i][j])
    return B


def mul(A, B):
    """
    Implements matrix multiplication A * B.

    :param A: real matrix of size m * p
    :param B: real matrix of size p * n
    :return: C = A * B of dimensions m * n
    """
    m, p, n = len(A), len(A[0]), len(B[0])
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(0.)
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C


def diag(x):
    """
    Creates diagonal matrix diag(x) for vector x.
    :param x: real vector
    :return: diagonal matrix D = diag(x)
    """
    n = len(x)
    D = []
    for i in range(n):
        D.append([])
        for j in range(n):
            D[i].append(x[i] if i == j else 0.)
    return D


def eye(n):
    """
    Creates identity (unit) matrix I.
    :param n: size of I
    :return: identity matrix I of dimension n
    """
    return diag([1.] * n)


def zero(n):
    """
    Creates zero (null) matrix Z.
    :param n: size of Z
    :return: null matrix Z of dimension n
    """
    return diag([0.] * n)


def trace(A):
    """
    Implements trace operation trance(A).

    :param A: real matrix of size n * n
    :return: trace(A) = sum_i A[i][i]
    """
    if (len(A) != len(A[0])):
        raise ValueError('calling trace(A) on non-square matrix A')
    tr = 0.
    for i in range(len(A)):
        tr += A[i][i]
    return tr


if __name__ == '__main__':
    x = [1., 2., 3.]
    y = [2., 2., 1.]

    s = dot(x, y)
    print(s)

    A = [x, y]
    print('A', A)

    B = transpose(A)
    print('B = A^T', B)

    C = mul(A, B)
    print('A*B', C)

    A2 = add(A, A)
    print('A+A', A2)

    A3 = smul(3., A)
    print('3*A', A3)

    Z = sub(A, A)
    print('A-A', Z)

    D = diag(x)
    print('D = diag(x)', D)

    td = trace(D)
    print('trace(D)', td)

    I = eye(4)
    print('I = eye(4)', I)

    Z4 = zero(4)
    print('Z = zero(4)', Z4)
