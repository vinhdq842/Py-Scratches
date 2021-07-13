"""
Solve x^2 = a using Newton's method
"""


def f(x, a):
    return x ** 2 - a


def df(x):
    return 2 * x


def newton(_f, x0, a, _df, tol):
    x1 = x0 - _f(x0, a) / _df(x0)

    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = x0 - _f(x0, a) / _df(x0)
    return x1


print(newton(f, 2, 2, df, 10e-9))
