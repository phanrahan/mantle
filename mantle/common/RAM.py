from magma import Circuit, In, Out, Clock, Bit, Bits, wire, repeat, cache_definition
from mantle import Mux, And
from .register import Register
from .decoder import Decoder

__all__  = ['DefineROM', 'ROM']
__all__ += ['DefineRAM', 'RAM']
__all__ += ['DefineDualRAM', 'DualRAM']

def REGs(n, width):
    return [Register(width, has_ce=True) for i in range(n)]

def MUXs(n, width):
    return [Mux(2,width) for i in range(n)]


def readport(height, width, regs, raddr):
    n = 1 << height

    muxs = MUXs(n-1, width)
    for i in range(n//2):
        muxs[i](regs[2*i], regs[2*i+1], raddr[0])

    k = 0
    l = 1 << (height-1)
    for i in range(height-1):
        for j in range(l//2):
            muxs[k+l+j](muxs[k+2*j], muxs[k+2*j+1], raddr[i+1])
        k += l
        l //= 2

    return muxs[n-2]


def writeport(height, width, regs, WADDR, I, WE):
    n = 1 << height

    decoder = Decoder(height)
    enable = And(2,n)
    enable(decoder(WADDR), repeat(WE, n))

    for i in range(n):
        regs[i](I, CE=enable.O[i])


@cache_definition
def DefineROM(height, width):
    n = 1 << height
    TADDR = Bits(height)
    TDATA = Bits(width)

    class _ROM(Circuit):
        name = 'ROM{}x{}'.format(n,width)
        IO = ['RADDR', In(TADDR),
              'RDATA', Out(TDATA),
              'CLK', In(Clock)]

        @classmethod
        def definition(io):
            regs = REGs(n, width)
            rdata = readport(height, width, regs, io.RADDR)
            wire(rdata, io.RDATA)

    return _ROM

def ROM(height, width):
    return DefineROM(height, width)()


@cache_definition
def DefineRAM(height, width):
    n = 1 << height
    TADDR = Bits(height)
    TDATA = Bits(width)

    class _RAM(Circuit):
        name = 'RAM{}x{}'.format(n,width)
        IO = ['RADDR', In(TADDR),
              'RDATA', Out(TDATA),
              'WADDR', In(TADDR),
              'WDATA', In(TDATA),
              'WE', In(Bit),
              'CLK', In(Clock)
             ]

        @classmethod
        def definition(io):
            regs = REGs(n, width)
            writeport(height, width, regs, io.WADDR, io.WDATA, io.WE)
            wire( readport(height, width, regs, io.RADDR), io.RDATA )

    return _RAM

def RAM(height, width):
    return DefineRAM(height, width)()


@cache_definition
def DefineDualRAM(height, width):
    n = 1 << height
    TADDR = Bits(height)
    TDATA = Bits(width)

    class _DualRAM(Circuit):
        name = 'DualRAM{}x{}'.format(n,width)
        IO = ['RADDR0', In(TADDR),
              'RDATA0', Out(TDATA),
              'RADDR1', In(TADDR),
              'RDATA1', Out(TDATA),
              'WADDR', In(TADDR),
              'WDATA', In(TDATA),
              'WE', In(Bit),
              'CLK', In(Clock)]

        @classmethod
        def definition(io):
            regs = REGs(n, width)
            writeport(height, width, regs, io.WADDR, io.WDATA, io.WE)
            wire( readport(height, width, regs, io.RADDR0), io.RDATA0 )
            wire( readport(height, width, regs, io.RADDR1), io.RDATA1 )

    return _DualRAM

def DualRAM(height, width):
    return DefineDualRAM(height, width)()


