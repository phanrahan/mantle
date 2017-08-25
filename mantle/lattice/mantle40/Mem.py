from ..ice40.RAMB import RAMB, ROMB

__all__ = ['Mem']

#
# Contruct a memory mem[height][width]
#
def Mem(rom, width, readonly=False):
    height = len(rom)
    assert height in [4096, 20146, 1024, 512, 256]

    assert width == 4096 / height

    return ROMB(rom) if readonly else RAMB(rom)
