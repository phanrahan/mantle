from magma import *
from .LUT import ROM4

def _ROMName(name, n):
    return name + '%d' % n

ROMCache = {}

def def_ROM16xN(rom):
    """
    Construct a 16 entry ROM of arbitrary width.

    rom[16][w]
    """
    assert(len(rom) == 16)
    # transpose - rom must be a sequence of sequences
    rom = zip(*rom)
    n = len(rom)

    # could be different memory contents ...
    name = _ROMName('ROM16x', n)
    if name in ROMCache:
        return ROMCache[name]

    args = ['input I', Array4, 'output O', Array(n, Bit)]

    define = DefineCircuit(name, *args)

    def ROM(y):
        return ROM4(rom[y])

    rom = fork(col(ROM, n))

    rom(define.I)
    wire(rom.O, define.O)

    EndCircuit()

    ROMCache[name] = define
    return define

def ROM16xN(rom):
    return def_ROM16xN(rom)()
