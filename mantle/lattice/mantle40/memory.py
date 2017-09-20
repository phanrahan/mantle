from ..ice40.RAMB import RAMB, ROMB

__all__ = ['Memory']

#
# Contruct a memory mem[height][width]
#
def Memory(height, width, rom=None, readonly=False):

    if rom:
        assert height == len(rom)
    else:
        rom = height * [0]

    return ROMB(height, width, rom) if readonly else RAMB(height, width, rom)
