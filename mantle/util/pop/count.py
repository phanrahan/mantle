import sys
from magma import *
from mantle import *

count8table = [
    0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
]


def count3to2():
    return fork([ROM3(I0^I1^I2), ROM3((I0&I1)|(I1&I2)|(I2&I0))])

if sys.version_info < (3,):
    lut1 = long(0)
    lut2 = long(0)
    lut4 = long(0)
else:
    lut1 = int(0)
    lut2 = int(0)
    lut4 = int(0)

for i in range(64):
    c = count8table[i]
    b = 1 << i
    if c & 1:
        lut1 |= b
    if c & 2:
        lut2 |= b
    if c & 4:
        lut4 |= b


def count6to3():
    global lut1, lut2, lut4
    luts = [ROM6(lut1), ROM6(lut2), ROM6(lut4)]
    return fork(luts)


def count16(bits):

    bits124a = count6to3()(bits[0:6])
    bits124b = count6to3()(bits[6:12])
    bits124c = count6to3()(bits[12:16] + [0, 0])

    # merge count3to2 into site
    bits1 = [bits124a[0], bits124b[0], bits124c[0]]
    bits12 = count3to2()(bits1)

    bits2 = [bits124a[1], bits124b[1], bits124c[1]]
    bits24 = count3to2()(bits2)

    bits4 = [bits124a[2], bits124b[2], bits124c[2]]
    bits48 = count3to2()(bits4)

    A = [bits12[0], bits24[0], bits48[0],         0]
    B = [0, bits12[1], bits24[1], bits48[1]]

    return AddC(4)(A, B, 0)


def count8(bits):

    bits124 = count6to3()(bits[0:6])

    bits12 = count3to2()(bits[6:8] + [bits124[0]])
    bits1 = bits12[0]

    bits24 = count3to2()([bits124[1], bits12[1], 0])
    bits2 = bits24[0]

    bits48 = count3to2()([bits124[2], bits24[1], 0])
    bits4 = bits48[0]
    bits8 = bits48[1]

    return [bits1, bits2, bits4, bits8]
