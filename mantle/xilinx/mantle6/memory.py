from magma import *
from ..spartan6.RAMB import RAMB16, ROMB16

__all__ = ['Memory']

#
# Contruct a memory mem[height][width]
#
def Memory(height, width, rom=None, readonly=False):

    if rom:
        assert height == len(rom)
    else:
        rom = height * [0]

    return ROMB16(height, width, rom) if readonly else RAMB16(height, width, rom)

