"""
@author Quang Vinh(SOE)

SHA-256 implementation
"""

import hashlib

initial_hash_values = [
    '6a09e667', 'bb67ae85', '3c6ef372', 'a54ff53a',
    '510e527f', '9b05688c', '1f83d9ab', '5be0cd19'
]

sha256_constants = [
    '428a2f98', '71374491', 'b5c0fbcf', 'e9b5dba5',
    '3956c25b', '59f111f1', '923f82a4', 'ab1c5ed5',
    'd807aa98', '12835b01', '243185be', '550c7dc3',
    '72be5d74', '80deb1fe', '9bdc06a7', 'c19bf174',
    'e49b69c1', 'efbe4786', '0fc19dc6', '240ca1cc',
    '2de92c6f', '4a7484aa', '5cb0a9dc', '76f988da',
    '983e5152', 'a831c66d', 'b00327c8', 'bf597fc7',
    'c6e00bf3', 'd5a79147', '06ca6351', '14292967',
    '27b70a85', '2e1b2138', '4d2c6dfc', '53380d13',
    '650a7354', '766a0abb', '81c2c92e', '92722c85',
    'a2bfe8a1', 'a81a664b', 'c24b8b70', 'c76c51a3',
    'd192e819', 'd6990624', 'f40e3585', '106aa070',
    '19a4c116', '1e376c08', '2748774c', '34b0bcb5',
    '391c0cb3', '4ed8aa4a', '5b9cca4f', '682e6ff3',
    '748f82ee', '78a5636f', '84c87814', '8cc70208',
    '90befffa', 'a4506ceb', 'bef9a3f7', 'c67178f2'
]


def and_bit(a, b):
    return "".join([str(int(a[i]) & int(b[i])) for i in range(len(a))])


def not_bit(a):
    return "".join(['0' if int(a[i]) == 1 else '1' for i in range(len(a))])


def xor_bit(a, b):
    return "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])


def shr_bit(a, n):
    for _ in range(n):
        a = '0' + a[:-1]

    return a


def rotr_bit(a, n):
    for _ in range(n):
        a = a[-1] + a[:-1]
    return a


def dec2bin(d, digit):
    return format(d, "0%db" % digit)


def hex2dec(h):
    return int(h, 16)


def dec2hex(d, digit):
    return format(d, "0%dx" % digit)


def ch(e, f, g):
    return xor_bit(and_bit(e, f), and_bit(not_bit(e), g))


def maj(a, b, c):
    return xor_bit(xor_bit(and_bit(a, b), and_bit(a, c)), and_bit(b, c))


def e_0(a):
    return xor_bit(xor_bit(rotr_bit(a, 2), rotr_bit(a, 13)), rotr_bit(a, 22))


def e_1(e):
    return xor_bit(xor_bit(rotr_bit(e, 6), rotr_bit(e, 11)), rotr_bit(e, 25))


def s_0(a):
    return xor_bit(xor_bit(rotr_bit(a, 7), rotr_bit(a, 18)), shr_bit(a, 3))


def s_1(e):
    return xor_bit(xor_bit(rotr_bit(e, 17), rotr_bit(e, 19)), shr_bit(e, 10))


def add_modulo(nums):
    mod = 2 ** 32
    res = 0
    for i in nums:
        res = (res + i) % mod

    return res


def padding_bits(m):
    length = len(m)
    m += '1'
    while len(m) % 512 != 448:
        m += '0'

    return m + dec2bin(length, 64)


def separate(m):
    return [m[i * 512:i * 512 + 512] for i in range(len(m) // 512)]


def to_bin(m):
    return "".join([str(dec2bin(ord(c), 8)) for c in m])


def message_schedule(m):
    res = [m[i * 32:i * 32 + 32] for i in range(len(m) // 32)]
    for i in range(16, 64):
        res.append(
            dec2bin(add_modulo(
                [int(s_1(res[i - 2]), 2), int(res[i - 7], 2), int(s_0(res[i - 15]), 2), int(res[i - 16], 2)]),
                32))

    return res


def sha256(m):
    blocks = separate(padding_bits(to_bin(m)))
    hash_buffer = [initial_hash_values[i] for i in range(8)]

    for b in blocks:
        words = message_schedule(b)
        a = dec2bin(hex2dec(hash_buffer[0]), 32)
        b = dec2bin(hex2dec(hash_buffer[1]), 32)
        c = dec2bin(hex2dec(hash_buffer[2]), 32)
        d = dec2bin(hex2dec(hash_buffer[3]), 32)
        e = dec2bin(hex2dec(hash_buffer[4]), 32)
        f = dec2bin(hex2dec(hash_buffer[5]), 32)
        g = dec2bin(hex2dec(hash_buffer[6]), 32)
        h = dec2bin(hex2dec(hash_buffer[7]), 32)

        for i in range(64):
            t_1 = add_modulo(
                [int(h, 2), int(ch(e, f, g), 2), int(e_1(e), 2), int(words[i], 2), hex2dec(sha256_constants[i])])
            t_2 = add_modulo([int(e_0(a), 2), int(maj(a, b, c), 2)])

            h = g
            g = f
            f = e
            e = dec2bin(add_modulo([int(d, 2), t_1]), 32)
            d = c
            c = b
            b = a
            a = dec2bin(add_modulo([t_1, t_2]), 32)

        hash_buffer[0] = dec2hex(add_modulo([hex2dec(hash_buffer[0]), int(a, 2)]), 8)
        hash_buffer[1] = dec2hex(add_modulo([hex2dec(hash_buffer[1]), int(b, 2)]), 8)
        hash_buffer[2] = dec2hex(add_modulo([hex2dec(hash_buffer[2]), int(c, 2)]), 8)
        hash_buffer[3] = dec2hex(add_modulo([hex2dec(hash_buffer[3]), int(d, 2)]), 8)
        hash_buffer[4] = dec2hex(add_modulo([hex2dec(hash_buffer[4]), int(e, 2)]), 8)
        hash_buffer[5] = dec2hex(add_modulo([hex2dec(hash_buffer[5]), int(f, 2)]), 8)
        hash_buffer[6] = dec2hex(add_modulo([hex2dec(hash_buffer[6]), int(g, 2)]), 8)
        hash_buffer[7] = dec2hex(add_modulo([hex2dec(hash_buffer[7]), int(h, 2)]), 8)

    return "".join(hash_buffer)


plain = "..."

print("%s\n%s" % (sha256(plain), hashlib.sha256(plain.encode("utf-8")).hexdigest()))

