"""
Affine cryptosystem
"""


def f(x):
    return ord(x) - ord('A')


def g(x):
    return chr(x + ord('A'))


a = 5
b = 7


def enc(p):
    c = ""
    for i in p:
        c += g((a * f(i) + b) % 26)

    return c


def dec(c):
    a_inv = 0
    while a_inv < 26:
        if a * a_inv % 26 == 1:
            break
        a_inv += 1

    p = ""
    for i in c:
        p += g((a_inv * (f(i) - b)) % 26)

    return p


plain_text = "VIETNAMCHIENTHANG"

cipher_text = enc(plain_text)

print(cipher_text)
print(dec(cipher_text))
