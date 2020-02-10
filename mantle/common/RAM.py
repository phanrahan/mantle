from .register import Register
from .decoder import Decoder
from mantle import And, Mux
from magma import Circuit, In, Out, Clock, Bit, Bits, wire, bits, repeat, cache_definition
from magma.bitutils import clog2

__all__ = ["DefineRAM", "DefineDualRAM"]

def REGs(n, width, has_ce):
    return [Register(width, has_ce=has_ce) for i in range(n)]

def MUXs(n, width):
    return [Mux(2,width) for i in range(n)]


def readport(addr_width, width, regs, raddr):
    n = 1 << addr_width

    muxs = MUXs(n-1, width)
    for i in range(n//2):
        muxs[i](regs[2*i], regs[2*i+1], raddr[0])

    k = 0
    l = 1 << (addr_width-1)
    for i in range(addr_width-1):
        for j in range(l//2):
            muxs[k+l+j](muxs[k+2*j], muxs[k+2*j+1], raddr[i+1])
        k += l
        l //= 2

    return muxs[n-2]


def writeport(addr_width, width, regs, WADDR, I, WE):
    n = 1 << addr_width

    decoder = Decoder(addr_width)
    enable = And(2,n)
    enable(decoder(WADDR), repeat(WE, n))

    for i in range(n):
        regs[i](I, CE=enable.O[i])


def DefineRAM(height, width):
    addr_width = clog2(height)
    TADDR = Bits[ addr_width ]
    TDATA = Bits[ width ]

    class _RAM(Circuit):
        name = f'RAM{height}x{width}'
        IO = ['RADDR', In(TADDR),
              'RDATA', Out(TDATA),
              'WADDR', In(TADDR),
              'WDATA', In(TDATA),
              'WE', In(Bit),
              'CLK', In(Clock)
             ]

        @classmethod
        def definition(io):
            regs = REGs(height, width, has_ce=True)
            writeport(addr_width, width, regs, io.WADDR, io.WDATA, io.WE)
            wire( readport(addr_width, width, regs, io.RADDR), io.RDATA )

    return _RAM


def DefineDualRAM(height, width):
    addr_width = clog2(height)
    TADDR = Bits[ addr_width ]
    TDATA = Bits[ width ]

    class _DualRAM(Circuit):
        name = f'DualRAM{height}x{width}'
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
            regs = REGs(n, width, has_ce=True)
            writeport(addr_width, width, regs, io.WADDR, io.WDATA, io.WE)
            wire( readport(addr_width, width, regs, io.RADDR0), io.RDATA0 )
            wire( readport(addr_width, width, regs, io.RADDR1), io.RDATA1 )

    return _DualRAM
