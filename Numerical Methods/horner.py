# p1(x) = 3 * (x - 1) ** 5 + 7 * (x - 1) ** 9
# = (7 * (x - 1) ** 4 + 3) * (x - 1) ** 5
def calc1(x):
    return (7 * (x - 1) ** 4 + 3) * (x - 1) ** 5


# p2(x) = 6 * (x + 2) ** 3 + 9 * (x + 2) ** 7 + 3 * (x + 2) ** 15 - (x + 2) ** 31
# = (((-(x + 2) ** 16 + 3) * (x + 2) ** 8 + 9) * (x + 2) ** 4 + 6) * (x + 2) ** 3
def calc2(x):
    return (((-(x + 2) ** 16 + 3) * (x + 2) ** 8 + 9) * (x + 2) ** 4 + 6) * (x + 2) ** 3


def horner_calc(n, x):
    p = n + 1
    for i in range(n, 0, -1):
        p = p * x + i
    return p


print(horner_calc(7328, 1.1))
# max n = 7328
