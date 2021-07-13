from math import factorial


def calc_e(n):
    rs = 1
    for i in range(1, n + 1):
        rs += 1 / factorial(i)
    return rs


print(calc_e(1000))
