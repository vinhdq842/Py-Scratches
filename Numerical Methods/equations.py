import scipy.linalg as sla
from numpy import array, dot

# Jacobi and Gauss - Seidel

A = array([[3, 1, 1], [1, 5, 2], [1, 8, 10]])
b = array([5, 8, 19])
# P = array([[3, 0, 0], [0, 5, 0], [0, 0, 10]])
P = array([[3, 0, 0], [1, 5, 0], [1, 8, 10]])

N = A - P
tol = 1e-9
x = array([0, 0, 0])
n_max = 1000

for i in range(1, n_max):
    x = sla.solve(P, -dot(N, x) + b)
    if sla.norm(dot(A, x) - b, 2) < tol:
        print("x =", x)
        print("i =", i + 1)
        break

"""
del A
A = array([[1, 2, 7], [3, 2, 6], [7, 4, 3]])
(p, l, u) = sla.lu(A)

A = array([[1, -2, 4], [1, -1, 1], [1, 0, 0], [1, 1, 1], [1, 3, 9]])
b = array([[2], [3], [3], [1]])

q, r = np.linalg.qr(A)
print(q)

x = sla.inv(r) @ q.T @ b
print(x)
"""
