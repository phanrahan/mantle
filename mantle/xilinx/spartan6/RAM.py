from collections import OrderedDict
from magma import *
from magma.bitutils import lutinit, log2

__all__  = ['RAM256x1S', 'RAM256', 
            'RAM128x1S', 'RAM128', 
            'RAM128x1D', 'RAM128D', 
            'RAM64x1S',  'RAM64', 
            'RAM64x1D',  'RAM64D',
            'RAM64M',    'RAM64Q',
            'RAM32x1S',  'RAM32', 
            'RAM32x1D',  'RAM32D',
            'RAM32x2S',  'RAM32x2',
            'RAM32M',    'RAM32Q',
            'RAM16',  
            'RAM16D',
            'RAM16x2']
__all__ += ['RAM16DxN', 'DefineRAM16DxN']
__all__ += ['RAM64QxN', 'DefineRAM64QxN']
__all__ += ['read_ram_bits']

RAM256x1S = DeclareCircuit("RAM256X1S",
                            "A", In(Bits[ 8 ]),
                            "D", In(Bit),
                            "O", Out(Bit),
                            "WE", In(Bit),
                            "WCLK", In(Clock))

RAM128x1S = DeclareCircuit("RAM128X1S",
                            "A0", In(Bit),
                            "A1", In(Bit),
                            "A2", In(Bit),
                            "A3", In(Bit),
                            "A4", In(Bit),
                            "A5", In(Bit),
                            "A6", In(Bit),
                            "D", In(Bit),
                            "O", Out(Bit),
                            "WE", In(Bit),
                            "WCLK", In(Clock))


RAM128x1D = DeclareCircuit("RAM128X1D",
                            "A", In(Bits[ 7 ]),
                            "DPRA", In(Bits[ 7 ]),

                            "D", In(Bit),

                            "SPO", Out(Bit),
                            "DPO", Out(Bit),

                            "WE", In(Bit),
                            "WCLK", In(Clock))


RAM64x1S = DeclareCircuit("RAM64X1S",

                           "A0", In(Bit),
                           "A1", In(Bit),
                           "A2", In(Bit),
                           "A3", In(Bit),
                           "A4", In(Bit),
                           "A5", In(Bit),

                           "D", In(Bit),

                           "O", Out(Bit),

                           "WE", In(Bit),
                           "WCLK", In(Clock) )

RAM64x1D = DeclareCircuit("RAM64X1D",

                           "A0", In(Bit),
                           "A1", In(Bit),
                           "A2", In(Bit),
                           "A3", In(Bit),
                           "A4", In(Bit),
                           "A5", In(Bit),

                           "DPRA0", In(Bit),
                           "DPRA1", In(Bit),
                           "DPRA2", In(Bit),
                           "DPRA3", In(Bit),
                           "DPRA4", In(Bit),
                           "DPRA5", In(Bit),

                           "D", In(Bit),

                           "SPO", Out(Bit),
                           "DPO", Out(Bit),

                           "WE", In(Bit),
                           "WCLK", In(Clock) )

RAM32x1S = DeclareCircuit("RAM32X1S",

                           "A0", In(Bit),
                           "A1", In(Bit),
                           "A2", In(Bit),
                           "A3", In(Bit),
                           "A4", In(Bit),

                           "D", In(Bit),

                           "O", Out(Bit),

                           "WE", In(Bit),
                           "WCLK", In(Clock) )

RAM32x2S = DeclareCircuit("RAM32X2S",

                           "A0", In(Bit),
                           "A1", In(Bit),
                           "A2", In(Bit),
                           "A3", In(Bit),
                           "A4", In(Bit),

                           "D0", In(Bit),
                           "D1", In(Bit),

                           "O0", Out(Bit),
                           "O1", Out(Bit),

                           "WE", In(Bit),
                           "WCLK", In(Clock) )

RAM32x1D = DeclareCircuit("RAM32X1D",

                           "A0", In(Bit),
                           "A1", In(Bit),
                           "A2", In(Bit),
                           "A3", In(Bit),
                           "A4", In(Bit),

                           "DPRA0", In(Bit),
                           "DPRA1", In(Bit),
                           "DPRA2", In(Bit),
                           "DPRA3", In(Bit),
                           "DPRA4", In(Bit),

                           "D", In(Bit),

                           "SPO", Out(Bit),
                           "DPO", Out(Bit),

                           "WE", In(Bit),
                           "WCLK", In(Clock) )

RAM32M = DeclareCircuit("RAM32M",
                            "ADDRA", In(Bits[ 5 ]),
                            "ADDRB", In(Bits[ 5 ]),
                            "ADDRC", In(Bits[ 5 ]),
                            "ADDRD", In(Bits[ 5 ]),

                            "DIA",   In(Bits[ 2 ]),
                            "DIB",   In(Bits[ 2 ]),
                            "DIC",   In(Bits[ 2 ]),
                            "DID",   In(Bits[ 2 ]),

                            "DOA",   Out(Bits[ 2 ]),
                            "DOB",   Out(Bits[ 2 ]),
                            "DOC",   Out(Bits[ 2 ]),
                            "DOD",   Out(Bits[ 2 ]),

                            "WE", In(Bit),
                            "WCLK", In(Clock))


RAM64M = DeclareCircuit("RAM64M",
                            "ADDRA", In(Bits[ 6 ]),
                            "ADDRB", In(Bits[ 6 ]),
                            "ADDRC", In(Bits[ 6 ]),
                            "ADDRD", In(Bits[ 6 ]),

                            "DIA",   In(Bit),
                            "DIB",   In(Bit),
                            "DIC",   In(Bit),
                            "DID",   In(Bit),

                            "DOA",   Out(Bit),
                            "DOB",   Out(Bit),
                            "DOC",   Out(Bit),
                            "DOD",   Out(Bit),

                            "WE", In(Bit),
                            "WCLK", In(Clock))



def read_ram_bits(fn):
    def read_ram_init(fn):
        res = []
        fh = open(fn)
        i = 0
        for l in fh.readlines():
            t = []
            for c in l:
                if c != '\n' and c != '\r' and c != ' ' and c != '\t':
                    t.append(int(c))
            res.append(t)
            i += 1
        return res
    return read_ram_init(fn)
def initialization_params_from_bitvectors(rows, cols, xss, width = 1, initword_width = 128, totalbits = 128):
    def pad_to(n, w, xss):
        k = len(xss)
        for i in range(n - k):
            xss.append(w * [0])
        assert (len(xss) == n)
        return xss
    def extract_range(b, e, xss):
        nrows1 = b / width
        ncols1 = b % width
        nrows2 = e / width
        ncols2 = e % width
        res = []
        for i in range(nrows1, nrows2 + 1):
            collow = 0
            colhigh = width
            if i == nrows1:
                collow = ncols1
            if i == nrows2:
                colhigh = ncols2
            for j in range(collow, colhigh):
                res.append(xss[i][j])
        return res
    def get_init_word(i, xss):
        return extract_range(initword_width * i, initword_width * (i + 1), xss)
    def to_const(bits):
        res = ""
        for b in reversed(bits): # change endianness
            res += (str(b))
        return res

    xss = pad_to(rows, cols, xss)
    res = []
    for i in range(totalbits * width / initword_width):
        l = "INIT_"
        p = i
        if i > 0x3F:
            l = "INITP_"
            p = i % 0x3F - 1
        res.append((l + "%02`" % p, ("%d'b" % initword_width)+ to_const(get_init_word(i, xss))))
    params = {}
    for (k,v) in res:
        params[k] = v
    return params

def initialization_params_from_bitvectors_seq(rows, cols, xss, width = 1, initword_width = 128, totalbits = 128):
    ps = initialization_params_from_bitvectors(rows, cols, xss, width, initword_width, totalbits)
    res = []
    for k in sorted(ps.keys()):
        res.append(ps[k])
    return res


def RAM256(ram):
    ram = RAM256x1S(INIT=lutinit(ram,256))

    args  = ['A', ram.A]
    args += ['I', ram.D]
    args += ['O', ram.O]
    args += ["CLK", ram.WCLK]
    args += ["WE", ram.WE]
    return AnonymousCircuit(args)

def RAM128(ram):
    ram128 = RAM128x1S(INIT=lutinit(ram,128))

    A = array([ram128.A0, ram128.A1, ram128.A2, ram128.A3, 
              ram128.A4, ram128.A5, ram128.A6])
    return AnonymousCircuit("A",   A,
                   "I",   ram128.D,
                   "O",  ram128.O,
                   "WE",  ram128.WE,
                   "CLK", ram128.WCLK)

def RAM128D(ram):
    width = 1
    n = 128
    logn = log2(n)

    ram = RAM128x1D(INIT=lutinit(ram,128))

    args  = ['A0', ram.A]
    args += ['A1', ram.DPRA]
    
    args += ['I', ram.D]

    args += ['O0', ram.SPO]
    args += ['O1', ram.DPO]

    args += ["WE", ram.WE]
    args += ["CLK", ram.WCLK]
    return AnonymousCircuit(*args)

def RAM64(ram):
    ram64 = RAM64x1S(INIT=lutinit(ram,64))

    A = array([ram64.A0, ram64.A1, ram64.A2, ram64.A3, ram64.A4, ram64.A5])
    return AnonymousCircuit("A",   A,
                   "I",   ram64.D,
                   "O",  ram64.O,
                   "WE",  ram64.WE,
                   "CLK", ram64.WCLK)

def RAM64D(ram):
    ram64 = RAM64x1D(INIT=lutinit(ram,64))

    A0 = array([ram64.A0, ram64.A1, ram64.A2, ram64.A3, ram64.A4, ram64.A5])
    A1 = array([ram64.DPRA0, ram64.DPRA1, ram64.DPRA2, ram64.DPRA3, ram64.DPRA4, ram64.DPRA5])
    return AnonymousCircuit("A0",  A0,
                   "A1",  A1,
                   "I",   ram64.D,
                   "O0", ram64.SPO,
                   "O1", ram64.DPO,
                   "WE",  ram64.WE,
                   "CLK", ram64.WCLK)

def RAM64Q(ram):
    m = RAM64M(
            INIT_A = lutinit(ram[0],64),
            INIT_B = lutinit(ram[1],64),
            INIT_C = lutinit(ram[2],64),
            INIT_D = lutinit(ram[3],64))

    args =  ['AA', m.ADDRA]
    args += ['AB', m.ADDRB]
    args += ['AC', m.ADDRC]
    args += ['AD', m.ADDRD]

    args += ['IA', m.DIA]
    args += ['IB', m.DIB]
    args += ['IC', m.DIC]
    args += ['ID', m.DID]

    args += ['OA', m.DOA]
    args += ['OB', m.DOB]
    args += ['OC', m.DOC]
    args += ['OD', m.DOD]

    args += ["WE", m.WE]
    args += ["CLK", m.WCLK]

    return AnonymousCircuit(*args)

def RAM32(ram):
    ram32 = RAM32x1S(INIT=lutinit(ram,32))

    A = array([ram32.A0, ram32.A1, ram32.A2, ram32.A3, ram32.A4])
    return AnonymousCircuit("A",   A,
                   "I",   ram32.D,
                   "O",  ram32.O,
                   "WE",  ram32.WE,
                   "CLK", ram32.WCLK)


def RAM32D(ram):
    ram32 = RAM32x1D(INIT=lutinit(ram,32))

    A0 = array([ram32.A0, ram32.A1, ram32.A2, ram32.A3, ram32.A4])
    A1 = array([ram32.DPRA0, ram32.DPRA1, ram32.DPRA2, ram32.DPRA3, ram32.DPRA4])
    return AnonymousCircuit("A0",  A0,
                   "A1",  A1,
                   "I",   ram32.D,
                   "O0", ram32.SPO,
                   "O1", ram32.DPO,
                   "WE",  ram32.WE,
                   "CLK", ram32.WCLK)

def RAM32Q(ram):
    m = RAM32M(INIT_A=lutinit(ram[0],32),
               INIT_B=lutinit(ram[1],32),
               INIT_C=lutinit(ram[2],32),
               INIT_D=lutinit(ram[3],32))

    args =  ['AA', m.ADDRA]
    args += ['AB', m.ADDRB]
    args += ['AC', m.ADDRC]
    args += ['AD', m.ADDRD]

    args += ['IA', m.DIA]
    args += ['IB', m.DIB]
    args += ['IC', m.DIC]
    args += ['ID', m.DID]

    args += ['OA', m.DOA]
    args += ['OB', m.DOB]
    args += ['OC', m.DOC]
    args += ['OD', m.DOD]

    args += ["WE", m.WE]
    args += ["CLK", m.WCLK]

    return AnonymousCircuit(*args)

def RAM32x2(ram1, ram2):
    ram32 = RAM32x2S(INIT_00=lutinit(ram1,32), INIT_01=lutinit(ram2,32))

    A = array([ram32.A0, ram32.A1, ram32.A2, ram32.A3, ram32.A4])
    return AnonymousCircuit("A",   A,
                   "I0",  ram32.D0,
                   "I1",  ram32.D1,
                   "O0", ram32.O0,
                   "O1", ram32.O1,
                   "WE",  ram32.WE,
                   "CLK", ram32.WCLK)


def RAM16(ram):
    ram16 = RAM32(ram)

    wire(0, ram16.A[4])
    return AnonymousCircuit("A",   ram16.A[0:4],
                   "O",  ram16.O,
                   "I",   ram16.I,
                   "WE",  ram16.WE,
                   "CLK", ram16.CLK)

def RAM16D(ram):
    ram16 = RAM32D(ram)

    wire(0, ram16.A0[4])
    wire(0, ram16.A1[4])
    return AnonymousCircuit("A0",  ram16.A0[0:4],
                   "A1",  ram16.A1[0:4],
                   "O0", ram16.O0,
                   "O1", ram16.O1,
                   "I",   ram16.I,
                   "WE",  ram16.WE,
                   "CLK", ram16.CLK)

def RAM16x2(ram0, ram1):
    ram16 = RAM32x2(ram0, ram1)

    wire(0, ram16.A[4])
    return AnonymousCircuit("A",   ram16.A[0:4],
                   "O0", ram16.O0,
                   "O1", ram16.O1,
                   "I0", ram16.I0,
                   "I1", ram16.I1,
                   "WE",  ram16.WE,
                   "CLK", ram16.CLK)


def _RAMName(name, n):
    return name + '%d' % n

RAMCache = {}

def DefineRAM16DxN(n, init=0):

    name = _RAMName('RAM16D_', n)
    if name in RAMCache:
         return RAMCache[name]

    args =  ["A0",  In(Bits[ 4 ]),
             "A1",  In(Bits[ 4 ]),
             "O0", Out(Bits[ 4 ]),
             "O1", Out(Bits[ 4 ]),
             "I",   In(Bits[ 4 ]),
             "WE",  In(Bit),
             "CLK", In(Clock)]

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

def DefineRAM64QxN(n, init=0):
    name = _RAMName('RAM64Q_', n)
    if name in RAMCache:
        return RAMCache[name]

    args = ["A0", In(Bits[ 6 ]),
            "A1", In(Bits[ 6 ]),
            "A2", In(Bits[ 6 ]),
            "A3", In(Bits[ 6 ]),
            "O0", Out(Bits[ n ]),
            "O1", Out(Bits[ n ]),
            "O2", Out(Bits[ n ]),
            "O3", Out(Bits[ n ]),
            "I", In(Bits[ n ]),
            "WE", In(Bit),
            "CLK", In(Clock)]
    define = DefineCircuit(name, *args)

    def ram64q(y):
        # fix init
        return RAM64Q(0)

    ram = braid(col(ram64q, n), forkargs=['A0', 'A1', 'A2', 'A3', 'WE'])

    ram(define.A0, define.A1, define.A2, define.A3, define.I, define.WE)
    wire(ram.OA, define.O0)
    wire(ram.OB, define.O1)
    wire(ram.OC, define.O2)
    wire(ram.OD, define.O3)

    EndCircuit()
    RAMCache[name] = define
    return define

def RAM64QxN(n, init = 0):
    return DefineRAM64QxN(n, init=init)()

