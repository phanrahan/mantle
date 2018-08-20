from magma import Circuit, In, Out, Bits, wire, bits, uncurry, fork, cache_definition
from magma.bitutils import int2seq
from mantle import LUT
from mantle import Mux
from .RAM import readport

__all__  = ['DefineROM', 'ROM']

def ROM4(data, i, width):
    return fork([uncurry(LUT(data[i][w], 4)) for w in range(width)])

def ROM4s(n, width, data):
    return [ROM4(data, i, width) for i in range(n//16)]

def MUXs(n, width):
    return [Mux(2,width) for i in range(n)]

def interleave16(data, width):
    n = len(data)
    bits = [int2seq(data[i], width) for i in range(n)]
    #print(n, bits)
    data = [ [ [bits[i+j][w] for j in range(16)] for w in range(width)] \
               for i in range(0,n,16) ]
    #print(len(data), data)
    return data

def DefineROM(height, width, data):
    assert height >= 4
    n = 1 << height

    data = interleave16(data, width)

    TADDR = Bits(height)
    TDATA = Bits(width)

    class _ROM(Circuit):
        name = f'ROM{n}x{width}'
        IO = ['RADDR', In(TADDR), 'RDATA', Out(TDATA)]

        @classmethod
        def definition(io):
            roms = ROM4s(n, width, data)
            [roms[i](io.RADDR[0:4]) for i in range(n//16)]
            wire( readport(height-4, width, roms, io.RADDR[4:]), io.RDATA )

    return _ROM

def ROM(height, width, data=None):
    return DefineROM(height, width, data=data)()

