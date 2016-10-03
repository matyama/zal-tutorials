#!/usr/bin/env python3


def norm(x):
    """
    Implements euclidean norm of vector x. Euclidean norm ||x||_2 is defined as sqrt(sum_i x[i]^2)
    :param x: real vector
    :return: ||x||_2
    """
    pass


def vadd(x, y):
    """
    Implements vector addition x+y defined as z[i] = x[i] + y[i] for all i.

    :param x: real vector
    :param y: real vector
    :return: z = x + y
    """
    pass


def vsub(x, y):
    """
    Implements vector subtraction x-y defined as z[i] = x[i] - y[i] for all i.

    :param x: real vector
    :param y: real vector
    :return: z = x - y
    """
    pass


def svmul(s, x):
    """
    Implements multiplication by scalar s * x defined as y[i] = s * x[i] for all i.

    :param s: real scalar
    :param x: real vector
    :return: y = s * x
    """
    pass


def normalize(x):
    """
    Create unit vector u corresponding to x, defined as u = x / norm(x).
    :param x: real vector
    :return: u = x / ||x||_2
    """
    pass


def dot(x, y):
    """
    Implements the dot product x * y. Dot (scalar) product of two real vectors x and y is defined as sum_i x[i] * y[i].

    :param x real vector
    :param y real vector
    """
    pass


def transpose(A):
    """
    Implements matrix transposition A'.
    Matrix B that is equal to transposition of matrix A is defined as B[j][i] = A[i][j] for all i and j.

    :param A: real matrix of size m * n
    :return: transposed matrix A' of size n * m
    """
    pass


def add(A, B):
    """
    Implements matrix addition A + B defined as C[i][j] = A[i][j] + B[i][j] for all i and j.

    :param A: real matrix of size m * n
    :param B: real matrix of size m * n
    :return: C = A + B
    """
    pass


def sub(A, B):
    """
    Implements matrix subtraction A - B defined as C[i][j] = A[i][j] - B[i][j] for all i and j.

    :param A: real matrix of size m * n
    :param B: real matrix of size m * n
    :return: C = A - B
    """
    pass


def smul(s, A):
    """
    Implements scalar multiplication s * A defined as B[i][j] = s * A[i][j] for all i and j.

    :param s: real scalar
    :param A: real matrix of size m * n
    :return: B = s * A
    """
    pass


def mul(A, B):
    """
    Implements matrix multiplication A * B defined as C[i][j] = sum_k A[i][k] * B[k][j] for all i and j.

    :param A: real matrix of size m * p
    :param B: real matrix of size p * n
    :return: C = A * B of dimensions m * n
    """
    pass


def diag(x):
    """
    Creates diagonal matrix D = diag(x) for vector x defined as D[i][i] = x[i] for all i, otherwise 0.

    :param x: real vector
    :return: diagonal matrix D = diag(x)
    """
    pass


def eye(n):
    """
    Creates identity (unit) matrix I defined as I[i][i] = 1 for all i, I[i][j] = 0 for all j != i.
    :param n: size of I
    :return: identity matrix I of dimension n
    """
    pass


def zero(n):
    """
    Creates zero (null) matrix Z defined as Z[i][j] = 0 for all i and j.
    :param n: size of Z
    :return: null matrix Z of dimension n
    """
    pass


def trace(A):
    """
    Implements trace operation trance(A). Trace of a matrix is defined as the sum of elements on the main diagonal.

    :param A: real matrix of size n * n
    :return: trace(A) = sum_i A[i][i]
    """
    pass


def commutator(A, B):
    """
    Implements comutator C of matrices A and B defined as C = A * B - B * A.

    :param A: real matrix
    :param B: real matrix
    :return: C = A * B - B * A
    """
    pass


if __name__ == '__main__':
    x = [1., 2., 3.]
    print('x =', x)
    print('||x||_2 =', norm(x))

    u = normalize(x)
    print('u =', u)
    print('||u||_2 =', norm(u))

    y = [2., 2., 1.]
    print('y =', y)

    z = vadd(x, y)
    print('x+y =', z)

    x3 = svmul(3., x)
    print('3x =', x3)

    null = vsub(y, y)
    print('null =', null)

    s = dot(x, y)
    print('x * y =', s)

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

    print('commutator(I, I)', commutator(I, I))
