from magma import *
from mantle import *

def QuadDecoder(A, B):
    AFF = FF()(A)
    BFF = FF()(B)

    dir = Xor2()
    dir(A, BFF)

    ena = Xor4()
    ena(A, B, AFF, BFF)

    return dir, ena
