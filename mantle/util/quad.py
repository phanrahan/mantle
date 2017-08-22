from mantle import FF, XOr, XOr

def QuadDecoder(A, B):
    AFF = FF()(A)
    BFF = FF()(B)

    dir = XOr(2)
    dir(A, BFF)

    ena = XOr(4)
    ena(A, B, AFF, BFF)

    return dir, ena
