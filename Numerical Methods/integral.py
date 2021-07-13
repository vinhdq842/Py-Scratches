"""
Numerically calculate the integral of f(x) from a to b
Using Trapezoidal and Simpson's methods
"""
import math

mu = 0.3
m = 0.8
b = 0.4
k = 80
g = 9.81


def f(x):
    return mu * g + k * (mu * b + x) * (1 - b / math.sqrt(b ** 2 + x ** 2)) / m


def trapezoidal(_f, a, b):
    return (_f(a) + _f(b)) * (b - a) / 2


def simpson(_f, a, b):
    h = (b - a) / 2
    c = (a + b) / 2
    return (_f(a) + 4 * _f(c) + _f(b)) * h / 3


def comp_trap(_f, a, b, n):
    h = (b - a) / n
    rs = (_f(a) + _f(b)) / 2

    for i in range(1, n):
        rs += _f(a + h * i)

    return rs * h


def comp_simpson(_f, a, b, n):
    h = (b - a) / (2 * n)
    i1 = 0
    for i in range(1, 2 * n):
        i1 += 4 * f(a + i * h) if (i % 2 != 0) else 2 * f(a + i * h)

    return (i1 + _f(a) + _f(b)) * h / 3
