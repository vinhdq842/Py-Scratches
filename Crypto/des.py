"""
@author Quang Vinh(SOE)

DES implementation
"""

# Initial Permutation
init_perm = [58, 50, 42, 34, 26, 18, 10, 2,
             60, 52, 44, 36, 28, 20, 12, 4,
             62, 54, 46, 38, 30, 22, 14, 6,
             64, 56, 48, 40, 32, 24, 16, 8,
             57, 49, 41, 33, 25, 17, 9, 1,
             59, 51, 43, 35, 27, 19, 11, 3,
             61, 53, 45, 37, 29, 21, 13, 5,
             63, 55, 47, 39, 31, 23, 15, 7]

# Inverse Initial Permutation
inv_init_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                 39, 7, 47, 15, 55, 23, 63, 31,
                 38, 6, 46, 14, 54, 22, 62, 30,
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25]

# Expansion table E
expansion_table = [32, 1, 2, 3, 4, 5,
                   4, 5, 6, 7, 8, 9,
                   8, 9, 10, 11, 12, 13,
                   12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21,
                   20, 21, 22, 23, 24, 25,
                   24, 25, 26, 27, 28, 29,
                   28, 29, 30, 31, 32, 1]

# P permutation
p_table = [16, 7, 20, 21,
           29, 12, 28, 17,
           1, 15, 23, 26,
           5, 18, 31, 10,
           2, 8, 24, 14,
           32, 27, 3, 9,
           19, 13, 30, 6,
           22, 11, 4, 25]

# 8 S-boxes
s_box = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

# PC-1
pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# PC-2
pc2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# LSi
ls = [1, 1, 2, 2,
      2, 2, 2, 2,
      1, 2, 2, 2,
      2, 2, 2, 1]


def byte2bin(b):
    return "".join([bin(i)[2:].zfill(8) for i in b])


def bin2byte(x):
    return bytes([int(x[i:i + 8], 2) for i in range(0, len(x), 8)])


def hex2bin(h):
    b = ""
    for i in h:
        b += bin(int(i, 16))[2:].zfill(4)

    return b


def bin2hex(b):
    h = ""
    for i in range(len(b) // 4):
        h += hex(int(b[i * 4:i * 4 + 4], 2))[2:]

    return h


def xor(a, b):
    return "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])


def shl(a, n):
    for i in range(n):
        a = a[1:] + a[0]
    return a


def permute(x, table):
    return "".join([x[i - 1] for i in table])


# the f function
def f(ri, ki):
    ri = permute(ri, expansion_table)
    ri = xor(ri, ki)

    c = ""
    for i in range(8):
        b = ri[i * 6:i * 6 + 6]
        row = int(b[0] + b[5], 2)
        col = int(b[1] + b[2] + b[3] + b[4], 2)
        c += bin(s_box[i][row][col])[2:].zfill(4)

    return permute(c, p_table)


def encrypt(x, key_tab):
    x0 = permute(x, init_perm)
    l, r = x0[0:32], x0[32:64]

    for i in range(16):
        ri = xor(l, f(r, key_tab[i]))
        li = r
        l, r = li, ri

    return permute(r + l, inv_init_perm)


# generate key table
def gen_key_table(k):
    k = permute(k, pc1)
    left, right = k[0:28], k[28:56]

    key_table = []
    for idx in range(16):
        left = shl(left, ls[idx])
        right = shl(right, ls[idx])
        key_table.append(permute(left + right, pc2))

    return key_table


# encrypt a binary string, ECB mode
def encrypt_data(data, key_table):
    encrypted = ""
    for i in range(len(data) // 64):
        block = data[i * 64:i * 64 + 64]
        encrypted += encrypt(block, key_table)

    return encrypted


# decrypt a binary string, ECB mode
def decrypt_data(data, key_table):
    decrypted = ""
    for i in range(len(data) // 64):
        block = data[i * 64:i * 64 + 64]
        decrypted += encrypt(block, key_table[::-1])

    return decrypted


# Triple DES
key1 = hex2bin("0f1571c947d9e859")
key2 = hex2bin("23456789abcdef01")
key3 = hex2bin("0123456789abcdef")
plain_text = hex2bin("02468aceeca86420")

key1 = gen_key_table(key1)
key2 = gen_key_table(key2)
key3 = gen_key_table(key3)

cipher = encrypt_data(plain_text, key1)
print("BlockOut1:", bin2hex(cipher))
cipher = decrypt_data(cipher, key2)
print("BlockOut2:", bin2hex(cipher))
cipher = encrypt_data(cipher, key3)
print("BlockOut3(Ciphertext):", bin2hex(cipher))

plain_text = decrypt_data(cipher, key3)
plain_text = encrypt_data(plain_text, key2)
plain_text = decrypt_data(plain_text, key1)
print("Plain text:", bin2hex(plain_text))
