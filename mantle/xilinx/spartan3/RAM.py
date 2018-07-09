from magma import *
from magma.bitutils import lutinit

__all__  = ['RAM16x1S', 'RAM16',
            'RAM16x2S', 'RAM16x2',
            'RAM16x1D', 'RAM16D']
__all__ += ['RAM16DxN', 'DefineRAM16DxN']


RAM16x1S = DeclareCircuit('RAM16X1S',
            "A0", In(Bit),
            "A1", In(Bit),
            "A2", In(Bit),
            "A3", In(Bit),
            "O", Out(Bit),
            "D", In(Bit),
            "WE", In(Bit),
            "WCLK", In(Clock) )

RAM16x2S = DeclareCircuit('RAM16X2S',
            "A0", In(Bit),
            "A1", In(Bit),
            "A2", In(Bit),
            "A3", In(Bit),
            "O0", Out(Bit),
            "O1", Out(Bit),
            "D0", In(Bit),
            "D1", In(Bit),
            "WE", In(Bit),
            "input WCLK", In(Clock) )


RAM16x1D = DeclareCircuit('RAM16X1D',
            "A0", In(Bit),
            "A1", In(Bit),
            "A2", In(Bit),
            "A3", In(Bit),
            "DPRA0", In(Bit),
            "DPRA1", In(Bit),
            "DPRA2", In(Bit),
            "DPRA3", In(Bit),
            "SPO", Out(Bit),
            "DPO", Out(Bit),
            "D", In(Bit),
            "WE", In(Bit),
            "WCLK", In(Clock) )


def RAM16(ram):
    ram16 = RAM16x1S(INIT=lutinit(ram,16))
            
    return AnonymousCircuit("A", array([ram16.A0, ram16.A1, ram16.A2, ram16.A3]),
                   "O",  ram16.O,
                   "I",   ram16.D,
                   "WE",  ram16.WE,
                   "CLK", ram16.WCLK)

def RAM16D(ram):
    ram16 = RAM16x1D(INIT=lutinit(ram,16))
            
    A0 = array([ram16.A0, ram16.A1, ram16.A2, ram16.A3])
    A1 = array([ram16.DPRA0, ram16.DPRA1, ram16.DPRA2, ram16.DPRA3])
    return AnonymousCircuit("input A0",  A0,
                   "input A1",  A1,
                   "output O0", ram16.SPO,
                   "output O1", ram16.DPO,
                   "input I",   ram16.D,
                   "input WE",  ram16.WE,
                   "input CLK", ram16.WCLK)

def RAM16x2(ram0, ram1):
    ram16 = RAM16x2S(INIT_00=lutinit(ram0, 16), INIT_01=lutinit(ram1,16) )
            
    return AnonymousCircuit("input A",   array([ram16.A0, ram16.A1, ram16.A2, ram16.A3]),
                   "output O0",  ram16.O0,
                   "output O1",  ram16.O1,
                   "input  I0",  ram16.D0,
                   "input  I1",  ram16.D1,
                   "input WE",  ram16.WE,
                   "input CLK", ram16.WCLK)

def _RAMName(name, n):
    return name + '%d' % n

RAMCache = {}

def DefineRAM16DxN(n, init=0):

    name = _RAMName('RAM16D_', n)
    if name in RAMCache:
         return RAMCache[name]

    T = Bits(n)
    args =  ["A0",  In(Bits(4)),
             "A1",  In(Bits(4)),
             "O0", Out(T),
             "O1", Out(T),
             "I",   In(T),
             "WE",  In(Bit),
             "CLK", In(Bit)]

    define = DefineCircuit(name, *args)

    def ram16d(y):
        # fix init
        return RAM16D(0)

    ram = braid(col(ram16d, n), forkargs=['A0', 'A1', 'WE'])

    ram(define.A0, define.A1, define.I, define.WE)
    wire( ram.O0, define.O0 )
    wire( ram.O1, define.O1 )

    EndCircuit()

    RAMCache[name] = define
    return define

def RAM16DxN(n, init=0):
    return DefineRAM16DxN(n, init=init)()

