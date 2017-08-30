from mantle import ROM1, ROM2, ROM3, ROM4, ROM5, ROM6, ROM7, ROM8

__all__  = ['Decode']

def Decode(i, n, invert=False, **kwargs):
    """
    Decode the n-bit number i.

    @return: 1 if the n-bit input equals i
    """

    assert n <= 8

    if n <= 8:
        i = 1 << i
        if invert:
            m = 1 << n
            mask = (1 << m) - 1
            i = mask & (~i)
        if n == 1: return ROM1(i, **kwargs)
        if n == 2: return ROM2(i, **kwargs)
        if n == 3: return ROM3(i, **kwargs)
        if n == 4: return ROM4(i, **kwargs)
        if n == 5: return ROM5(i, **kwargs)
        if n == 6: return ROM6(i, **kwargs)
        if n == 7: return ROM7(i, **kwargs)
        if n == 8: return ROM8(i, **kwargs)
    return None

