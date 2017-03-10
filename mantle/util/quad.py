from mantle import FF, Xor2, Xor4

def QuadDecoder(A, B):
    AFF = FF()(A)
    BFF = FF()(B)

    dir = Xor2()
    dir(A, BFF)

    ena = Xor4()
    ena(A, B, AFF, BFF)

    return dir, ena
