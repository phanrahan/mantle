from magma import *
from parts.xilinx.spartan6.primitives.RAM import RAM16DxN

__all__ = ['RAM']

def RAM(height, width, init=0):
    assert height in [16]

    return RAM16DxN(width, init=init)()

