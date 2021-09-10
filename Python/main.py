import time
from math import sqrt

import numpy as np
import scipy.linalg as lg

"""
@author: Quang Vinh
Optimization
"""


def f(a):
    x, y = a[0], a[1]
    return x**4 + y**4 -4*x*y + 1


def grad_f(a):
    x, y = a[0], a[1]
    return np.array([4*x**3-4*y, 4*y**3-4*x])


def hesse_f(a):
    x, y = a[0], a[1]
    return np.array([[12*x**2, -4], [-4, 12*y**2]])


def euclidean_norm_sqr(a):
    return grad_f(a).transpose() @ grad_f(a)


# Số bước lặp tối đa mặc định là 1000
def grad_descent_backtracking_line_search(x, num_iter=1000):
    t = 0.5
    alpha = 0.2
    beta = 0.5
    epsilon = 10 ** -4
    start = time.time()
    i = 0

    while sqrt(euclidean_norm_sqr(x)) >= epsilon and i <= num_iter:
        while f(x - t * grad_f(x)) > f(x) - alpha * t * euclidean_norm_sqr(x):
            t = beta * t

        x -= t * grad_f(x)
        i += 1
    return time.time() - start, x, grad_f(x), i, sqrt(euclidean_norm_sqr(x))


# Số bước lặp tối đa mặc định là 1000
def newton_backtracking_line_search(x, num_iter=1000):
    t = 1
    alpha = 0.3
    beta = 0.5
    epsilon = 10 ** -4
    start = time.time()
    i = 0

    grad = grad_f(x)
    hesse_inv = lg.inv(hesse_f(x))
    delta_nt = -hesse_inv @ grad
    #    lambda_sqr = grad.transpose() @ hesse_inv @ grad

    while sqrt(euclidean_norm_sqr(x)) > epsilon and i <= num_iter:
        grad = grad_f(x)
        hesse_inv = lg.inv(hesse_f(x))
        delta_nt = -hesse_inv @ grad
        #        lambda_sqr = grad.transpose() @ hesse_inv @ grad

        while f(x - t * grad_f(x)) > f(x) - alpha * t * euclidean_norm_sqr(x):
            t = beta * t

        x += t * delta_nt
        i += 1
    return time.time() - start, x, grad_f(x), i, sqrt(euclidean_norm_sqr(x))


print("====== Gradient descent with backtracking line search ======")
x0 = np.array([.8, .8])
print("Starting point: (%.2f,%.2f)" % (x0[0], x0[1]))
rs = grad_descent_backtracking_line_search(x0, 0)
print("Number of iterations: %s" % rs[3])
print("Time elapsed: %s" % rs[0])
print("Approximated stationary point: %s" % rs[1])

print()

x0 = np.array([-1.2, 1])
print("Starting point: (%.2f,%.2f)" % (x0[0], x0[1]))
rs = grad_descent_backtracking_line_search(x0, 50000)
print("Number of iterations: %s" % rs[3])
print("Time elapsed: %s" % rs[0])
print("Approximated stationary point: %s" % rs[1])
print()

print("====== Newton\'s Algorithm with backtracking line search ======")
x0 = np.array([1.2, 1.2])
print("Starting point: (%.2f,%.2f)" % (x0[0], x0[1]))
rs = newton_backtracking_line_search(x0, 50000)
print("Number of iterations: %s" % rs[3])
print("Time elapsed: %s" % rs[0])
print("Approximated stationary point: %s" % rs[1])

print()

x0 = np.array([-1.2, 1])
print("Starting point: (%.2f,%.2f)" % (x0[0], x0[1]))
rs = newton_backtracking_line_search(x0, 50000)
print("Number of iterations: %s" % rs[3])
print("Time elapsed: %s" % rs[0])
print("Approximated stationary point: %s" % rs[1])
