import math


def sparseForm(t):
    dic = {}
    for i in range(len(t)):
        if t[i] == 0:
            continue
        dic[i] = t[i]

    return len(t), dic


def revert(spr):
    rs = [0 for i in range(spr[0])]
    for k in spr[1].items():
        rs[k[0]] = k[1]
    return rs


def dot(spr1, spr2):
    u = revert(spr1)
    v = revert(spr2)
    rs = 0
    for i in range(len(u)):
        rs += u[i] * v[i]
    return rs


def getCosinSim(spr1, spr2):
    dm = dot(spr1, spr2)
    u = revert(spr1)
    v = revert(spr2)
    au = 0
    av = 0
    for i in range(len(u)):
        au += u[i] ** 2
        av += v[i] ** 2

    return dm / math.sqrt(au * av)

print()
