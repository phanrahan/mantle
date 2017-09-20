from magma import Circuit, In, Out, Bits, wire, bits, uncurry, fork, cache_definition
from magma.bitutils import int2seq
from mantle import LUT4, Mux
from .RAM import readport

__all__  = ['DefineROM', 'ROM']

def ROM4(data, i, width):
    return fork([uncurry(LUT4(data[i][w])) for w in range(width)])

def ROM4s(n, width, data):
    return [ROM4(data, i, width) for i in range(n//16)]

def MUXs(n, width):
    return [Mux(2,width) for i in range(n)]

#def readport(height, width, roms, raddr):
#
#    n = 1 << height
#    muxs = MUXs(n-1, width)
#    for i in range(n//2):
#        muxs[i](roms[2*i], roms[2*i+1], raddr[0])
#    k = 0
#    l = 1 << (height-1)
#    for i in range(height-1):
#        for j in range(l//2):
#            muxs[k+l+j](muxs[k+2*j], muxs[k+2*j+1], raddr[i+1])
#        k += l
#        l //= 2
#
#    return muxs[n-2]


def interleave16(data, width):
    n = len(data)
    bits = [int2seq(data[i], width) for i in range(n)]
    #print(n, bits)
    data = [ [ [bits[i+j][w] for j in range(16)] for w in range(width)] \
               for i in range(0,n,16) ]
    #print(len(data), data)
    return data

@cache_definition
def DefineROM(height, width, data):
    assert height >= 4
    n = 1 << height

    data = interleave16(data, width)

    TADDR = Bits(height)
    TDATA = Bits(width)

    class _ROM(Circuit):
        name = 'ROM{}x{}'.format(n,width)
        IO = ['RADDR', In(TADDR), 'RDATA', Out(TDATA)]

        @classmethod
        def definition(io):
            roms = ROM4s(n, width, data)
            [roms[i](io.RADDR[0:4]) for i in range(n//16)]
            wire( readport(height-4, width, roms, io.RADDR[4:]), io.RDATA )

    return _ROM

def ROM(height, width, data=None):
    return DefineROM(height, width, data=data)()

