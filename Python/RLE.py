def length(t):
    a = -1
    rs = 0
    for i in range(len(t)):
        if t[i] != a:
            rs += 1
            a = t[i]

    return rs * 2


def compress(t):
    rs = []
    count = 0
    a = -1
    for i in range(len(t)):
        if t[i] != a:
            rs.append(count)
            count = 1
            rs.append(t[i])
            a = t[i]
        else:
            count += 1

    rs.append(count)
    return rs[1:]


def lengthInverse(ct):
    rs = 0
    for i in range(1, len(ct), 2):
        rs += ct[i]

    return rs


def decompress(ct):
    rs = []
    for i in range(0, len(ct), 2):
        for j in range(ct[i + 1]):
            rs.append(ct[i])
    return rs
