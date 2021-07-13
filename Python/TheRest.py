"""
Magic Square
"""


def isMagicSquare(m):
    a = sum(m[0])
    for i in range(len(m[0])):
        if sum(m[i]) != a:
            return False

    tmp = 0
    for i in range(len(m)):
        tmp = 0
        for j in range(len(m[0])):
            tmp += m[j][i]
        if tmp != a:
            return False

    tmp = 0

    for i in range(len(m)):
        tmp += m[i][i]
    if tmp != a:
        return False

    tmp = 0

    for i in range(len(m)):
        tmp += m[i][len(m) - i - 1]
    if tmp != a:
        return False
    return True


def inputMatrix():
    m = []
    line = input()
    while line != "":
        m.append([int(i) for i in line.split("\t")])
        line = input()
    print(m)
    return m


# isMagicSquare(inputMatrix())


"""
Password
"""


def checkPassword(s):
    if len(s) < 8 or len(s) > 100:
        return False
    s = list(s)
    flag = False
    for i in s:
        if i in "0123456789":
            flag = True
            break
    if not flag:
        return False

    flag = False
    for i in s:
        if chr(65) <= i <= chr(90):
            flag = True
            break
    if not flag:
        return False

    flag = False
    for i in s:
        if chr(97) <= i <= chr(122):
            flag = True
            break
    if not flag:
        return False

    flag = False
    for i in s:
        if i in "~!@#$%^&*":
            flag = True
            break
    if not flag:
        return False

    return True


# checkPassword("Mim*12345678")


"""
Statistical
"""


def mean(s):
    return sum(s) / len(s)


def variance(s):
    s = [i - mean(s) for i in s]
    rs = 0
    for i in s:
        rs += i ** 2
    return rs / len(s)


def standarddeviation(s):
    import math
    return math.sqrt(variance(s))


"""
Vec
"""


def cosineb2v(u, v):
    import math
    dm = 0
    for i in range(len(u)):
        dm += u[i] * v[i]
    au = 0
    av = 0
    for i in range(len(u)):
        au += u[i] ** 2
        av += v[i] ** 2

    return dm / math.sqrt(au * av)


"""
SortAdv
"""


def customSort(a):
    '''
    Hàm thực hiện sắp xếp các phần tử trong a, theo thứ tự:
    - Chẵn bên trái, lẻ bên phải
    - Chẵn tăng dần, lẻ giảm dần
    ví dụ a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kết quả là [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
    '''
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    even.sort()
    odd.sort()
    odd.reverse()

    return even + odd


"""
AddAdv
"""


# Hoàn thiện hàm addNum(a, b) theo yêu cầu trong đề bài


def addNum(a, b):
    '''
    Cho 2 số nguyên a, b được biểu diễn bởi 2 danh sách
    thực hiện phép cộng 2 số a, b trên 2 danh sách theo quy tắc cộng thông thường. kết quả trả về là 1 danh sách biểu diễn tổng a+b
    ví dụ
    a = [1,2,4,5]
    b =   [7,8,9]

    c = [2,0,3,4]
    '''
    adu1 = 0
    for i in a:
        adu1 = adu1 * 10 + i

    adu2 = 0
    for i in b:
        adu2 = adu2 * 10 + i

    adu3 = adu1 + adu2
    adu3 = str(adu3)
    return [int(i) for i in adu3]
