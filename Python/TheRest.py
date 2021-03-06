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
    H??m th???c hi???n s???p x???p c??c ph???n t??? trong a, theo th??? t???:
    - Ch???n b??n tr??i, l??? b??n ph???i
    - Ch???n t??ng d???n, l??? gi???m d???n
    v?? d??? a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k???t qu??? l?? [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
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


# Ho??n thi???n h??m addNum(a, b) theo y??u c???u trong ????? b??i


def addNum(a, b):
    '''
    Cho 2 s??? nguy??n a, b ???????c bi???u di???n b???i 2 danh s??ch
    th???c hi???n ph??p c???ng 2 s??? a, b tr??n 2 danh s??ch theo quy t???c c???ng th??ng th?????ng. k???t qu??? tr??? v??? l?? 1 danh s??ch bi???u di???n t???ng a+b
    v?? d???
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
