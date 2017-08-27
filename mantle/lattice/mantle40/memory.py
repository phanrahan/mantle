from ..ice40.RAMB import RAMB, ROMB

__all__ = ['Memory']

#
# Contruct a memory mem[height][width]
#
def Memory(rom, height, width, readonly=False):
    assert height in [4096, 20146, 1024, 512, 256]

    assert height == len(rom)
    assert width == 4096 / height

    return ROMB(rom) if readonly else RAMB(rom)
