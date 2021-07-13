import math

import numpy as np

"""
Hill cryptosystem
"""


def f(x):
    return ord(x) - ord('A')


def g(x):
    return chr(x + ord('A'))


k = "BABABBCCD"

sz = int(math.sqrt(len(k)))
print(sz)
key = []

for i in range(sz):
    row = []
    for j in range(sz):
        row.append(f(k[i * sz + j]))
    key.append(row)

key = np.matrix(key)
print("key: ")
print(key)
det = int(np.linalg.det(key))
det_inv = 0

while det_inv < 26:
    if (det_inv * det) % 26 == 1:
        break
    det_inv += 1

key_inv = (np.linalg.inv(key) * det * det_inv) % 26
key_inv = key_inv.round().astype(int)


def hill_enc(p):
    while len(p) % sz != 0:
        p += "z"
    _p = []

    for i in range(len(p) // sz):
        row = []
        for j in range(sz):
            row.append(f(p[i * sz + j]))
        _p.append(row)

    _p = np.matrix(_p)
    _c = _p @ key % 26
    c = ""

    for i in range(len(p) // sz):
        for j in range(sz):
            c += g(_c[i, j])

    return c


def hill_dec(c):
    _c = []
    for i in range(len(c) // sz):
        row = []
        for j in range(sz):
            row.append(f(c[i * sz + j]))
        _c.append(row)

    _c = np.matrix(_c)
    _p = _c @ key_inv % 26

    p = ""

    for i in range(len(c) // sz):
        for j in range(sz):
            p += g(int(_p[i, j]))

    return p


plain_text = 'CHIENTHANGDAIDICHZ'
cipher_text = hill_enc(plain_text)

print(cipher_text)
print(hill_dec(cipher_text))
