"""
Vigenere cryptosystem
"""


def f(x):
    return ord(x) - ord('A')


def g(x):
    return chr(x + ord('A'))


def gen_key(p):
    key = "AFD"

    if len(key) == len(p):
        return key

    for i in range(len(p) - len(key)):
        key += key[i % len(key)]
    return key


def enc(p):
    c = ""
    key = gen_key(p)
    for i in range(len(p)):
        c += g((f(p[i]) + f(key[i])) % 26)

    return c


def dec(c):
    p = ""
    key = gen_key(c)
    for i in range(len(c)):
        p += g((f(c[i]) - f(key[i])) % 26)

    return p


plain_text = "TOIYEUHUS"
cipher_text = enc(plain_text)

print(cipher_text)
print(dec(cipher_text))
