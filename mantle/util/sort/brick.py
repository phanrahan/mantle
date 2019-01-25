from magma import *
from magma.bitutils import log2
from mantle import *
from .swap import swaps, evenoddswaps

__all__  = ['DefineBrickSorter', 'BrickSorter', 'bricksorter']

#
# Brick Sorter
#
def DefineBrickSorter(n):
    assert n % 2 == 0
    T = Bits(n)
    class _BrickSorter(Circuit):
        name = 'BrickSorter{}'.format(n)
        IO = ['I', In(T), "O", Out(T)]
        @classmethod
        def definition(io):
            I = io.I
            for i in range(n//2):
                I = swaps(I)
                I = evenoddswaps(I)
            wire(I, io.O)
    return _BrickSorter

def BrickSorter(n):
    return DefineBrickSorter(n)()

def bricksorter(I):
    return BrickSorter(len(I))(I)
