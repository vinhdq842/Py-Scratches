import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

"""
Solve the differential equation
x'(t) = f(t,x) to find x(tf) given x(t0) = x0
Using Euler's and Trapezoidal methods
"""


# x'(t) = t/x
def f(t, x):
    return t / x


def euler_ex(_f, x0, t0, tf, n):
    x = x0
    h = (tf - t0) / n
    rs = [x0]

    for i in range(1, n + 1):
        x = x + h * _f(t0 + i * h, x)
        rs.append(x)
    print(rs[n])

    return rs


def euler_imp(_f, x0, t0, tf, n):
    x = x0
    h = (tf - t0) / n
    rs = [x0]

    for i in range(1, n + 1):
        x = fsolve(lambda xip1: xip1 - x - h * _f(t0 + (i + 1) * h, xip1), x)
        rs.append(x[0])
    print(rs[n])
    return rs


def trap_ex(_f, x0, t0, tf, n):
    x = x0
    h = (tf - t0) / n
    rs = [x0]

    for i in range(1, n + 1):
        y = x + h * _f(t0 + h * i, x)
        x = x + h * (_f(t0 + i * h, x) + _f(t0 + (i + 1) * h, y)) / 2
        rs.append(x)
    print(rs[n])
    return rs


def trap_imp(_f, x0, t0, tf, n):
    x = x0
    h = (tf - t0) / n
    rs = [x0]

    for i in range(1, n + 1):
        x = fsolve(lambda xip1: xip1 - x - h * (_f(t0 + i * h, x) + _f(t0 + (i + 1) * h, xip1)) / 2, x)
        rs.append(x[0])
    print(rs[n])
    return rs


x0, t0, tf, h = 1, 0, 1, 0.001
# x = sqrt(t^2 + 1)

_, a = plt.subplots(2, 2)

a[0][0].plot(np.arange(t0, tf, h), np.array(euler_ex(f, x0, t0, tf, int((tf - t0) / h - 1))))
a[0][0].set_title("Euler Explicit")

a[0][1].plot(np.arange(t0, tf, h), np.array(euler_imp(f, x0, t0, tf, int((tf - t0) / h - 1))))
a[0][1].set_title("Euler Implicit")

a[1][0].plot(np.arange(t0, tf, h), np.array(trap_ex(f, x0, t0, tf, int((tf - t0) / h - 1))))
a[1][0].set_title("Trap Explicit")

a[1][1].plot(np.arange(t0, tf, h), np.array(trap_imp(f, x0, t0, tf, int((tf - t0) / h - 1))))
a[1][1].set_title("Trap Implicit")

plt.show()
