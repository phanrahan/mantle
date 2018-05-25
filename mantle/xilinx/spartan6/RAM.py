from collections import OrderedDict
from magma import *

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
                            "input A", Array(8, Bit),
                            "input D", Bit,
                            "output O", Bit,
                            "input WE", Bit,
                            "input WCLK", Bit)

RAM128x1S = DeclareCircuit("RAM128X1S",
                            "input A0", Bit,
                            "input A1", Bit,
                            "input A2", Bit,
                            "input A3", Bit,
                            "input A4", Bit,
                            "input A5", Bit,
                            "input A6", Bit,
                            "input D", Bit,
                            "output O", Bit,
                            "input WE", Bit,
                            "input WCLK", Bit)


RAM128x1D = DeclareCircuit("RAM128X1D",
                            "input A", Array(7, Bit),
                            "input DPRA", Array(7, Bit),

                            "input D", Bit,

                            "output SPO", Bit,
                            "output DPO", Bit,

                            "input WE", Bit,
                            "input WCLK", Bit)


RAM64x1S = DeclareCircuit("RAM64X1S",

                           "input A0", Bit,
                           "input A1", Bit,
                           "input A2", Bit,
                           "input A3", Bit,
                           "input A4", Bit,
                           "input A5", Bit,

                           "input D", Bit,

                           "output O", Bit,

                           "input WE", Bit,
                           "input WCLK", Bit )

RAM64x1D = DeclareCircuit("RAM64X1D",

                           "input A0", Bit,
                           "input A1", Bit,
                           "input A2", Bit,
                           "input A3", Bit,
                           "input A4", Bit,
                           "input A5", Bit,

                           "input DPRA0", Bit,
                           "input DPRA1", Bit,
                           "input DPRA2", Bit,
                           "input DPRA3", Bit,
                           "input DPRA4", Bit,
                           "input DPRA5", Bit,

                           "input D", Bit,

                           "output SPO", Bit,
                           "output DPO", Bit,

                           "input WE", Bit,
                           "input WCLK", Bit )

RAM32x1S = DeclareCircuit("RAM32X1S",

                           "input A0", Bit,
                           "input A1", Bit,
                           "input A2", Bit,
                           "input A3", Bit,
                           "input A4", Bit,

                           "input D", Bit,

                           "output O", Bit,

                           "input WE", Bit,
                           "input WCLK", Bit )

RAM32x2S = DeclareCircuit("RAM32X2S",

                           "input A0", Bit,
                           "input A1", Bit,
                           "input A2", Bit,
                           "input A3", Bit,
                           "input A4", Bit,

                           "input D0", Bit,
                           "input D1", Bit,

                           "output O0", Bit,
                           "output O1", Bit,

                           "input WE", Bit,
                           "input WCLK", Bit )

RAM32x1D = DeclareCircuit("RAM32X1D",

                           "input A0", Bit,
                           "input A1", Bit,
                           "input A2", Bit,
                           "input A3", Bit,
                           "input A4", Bit,

                           "input DPRA0", Bit,
                           "input DPRA1", Bit,
                           "input DPRA2", Bit,
                           "input DPRA3", Bit,
                           "input DPRA4", Bit,

                           "input D", Bit,

                           "output SPO", Bit,
                           "output DPO", Bit,

                           "input WE", Bit,
                           "input WCLK", Bit )

RAM32M = DeclareCircuit("RAM32M",
                            "input  ADDRA", Array(5, Bit),
                            "input  ADDRB", Array(5, Bit),
                            "input  ADDRC", Array(5, Bit),
                            "input  ADDRD", Array(5, Bit),

                            "input  DIA",   Array(2, Bit),
                            "input  DIB",   Array(2, Bit),
                            "input  DIC",   Array(2, Bit),
                            "input  DID",   Array(2, Bit),

                            "output DOA",   Array(2, Bit),
                            "output DOB",   Array(2, Bit),
                            "output DOC",   Array(2, Bit),
                            "output DOD",   Array(2, Bit),

                            "input WE", Bit,
                            "input WCLK", Bit)


RAM64M = DeclareCircuit("RAM64M",
                            "input  ADDRA", Array(6, Bit),
                            "input  ADDRB", Array(6, Bit),
                            "input  ADDRC", Array(6, Bit),
                            "input  ADDRD", Array(6, Bit),

                            "input  DIA",   Bit,
                            "input  DIB",   Bit,
                            "input  DIC",   Bit,
                            "input  DID",   Bit,

                            "output DOA",   Bit,
                            "output DOB",   Bit,
                            "output DOC",   Bit,
                            "output DOD",   Bit,

                            "input WE", Bit,
                            "input WCLK", Bit)



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

    args  = ['input A', ram.A]
    args += ['input I', ram.D]
    args += ['output O', ram.O]
    args += ["input CLK", ram.WCLK]
    args += ["input WE", ram.WE]
    return AnonymousCircuit(args)

def RAM128(ram):
    ram128 = RAM128x1S(INIT=lutinit(ram,128))

    A = array(ram128.A0, ram128.A1, ram128.A2, ram128.A3, 
              ram128.A4, ram128.A5, ram128.A6)
    return AnonymousCircuit("input A",   A,
                   "input I",   ram128.D,
                   "output O",  ram128.O,
                   "input WE",  ram128.WE,
                   "input CLK", ram128.WCLK)

def RAM128D(ram):
    width = 1
    n = 128
    logn = log2(n)

    ram = RAM128x1D(INIT=lutinit(ram,128))

    args  = ['input A0', ram.A]
    args += ['input A1', ram.DPRA]
    
    args += ['input I', ram.D]

    args += ['output O0', ram.SPO]
    args += ['output O1', ram.DPO]

    args += ["input WE", ram.WE]
    args += ["input CLK", ram.WCLK]
    return AnonymousCircuit(*args)

def RAM64(ram):
    ram64 = RAM64x1S(INIT=lutinit(ram,64))

    A = array(ram64.A0, ram64.A1, ram64.A2, ram64.A3, ram64.A4, ram64.A5)
    return AnonymousCircuit("input A",   A,
                   "input I",   ram64.D,
                   "output O",  ram64.O,
                   "input WE",  ram64.WE,
                   "input CLK", ram64.WCLK)

def RAM64D(ram):
    ram64 = RAM64x1D(INIT=lutinit(ram,64))

    A0 = array(ram64.A0, ram64.A1, ram64.A2, ram64.A3, ram64.A4, ram64.A5)
    A1 = array(ram64.DPRA0, ram64.DPRA1, ram64.DPRA2, ram64.DPRA3, ram64.DPRA4, ram64.DPRA5)
    return AnonymousCircuit("input A0",  A0,
                   "input A1",  A1,
                   "input I",   ram64.D,
                   "output O0", ram64.SPO,
                   "output O1", ram64.DPO,
                   "input WE",  ram64.WE,
                   "input CLK", ram64.WCLK)

def RAM64Q(ram):
    m = RAM64M(
            INIT_A = lutinit(ram[0],64),
            INIT_B = lutinit(ram[1],64),
            INIT_C = lutinit(ram[2],64),
            INIT_D = lutinit(ram[3],64))

    args =  ['input AA', m.ADDRA]
    args += ['input AB', m.ADDRB]
    args += ['input AC', m.ADDRC]
    args += ['input AD', m.ADDRD]

    args += ['input IA', m.DIA]
    args += ['input IB', m.DIB]
    args += ['input IC', m.DIC]
    args += ['input ID', m.DID]

    args += ['output OA', m.DOA]
    args += ['output OB', m.DOB]
    args += ['output OC', m.DOC]
    args += ['output OD', m.DOD]

    args += ["input WE", m.WE]
    args += ["input CLK", m.WCLK]

    return AnonymousCircuit(*args)

def RAM32(ram):
    ram32 = RAM32x1S(INIT=lutinit(ram,32))

    A = array(ram32.A0, ram32.A1, ram32.A2, ram32.A3, ram32.A4)
    return AnonymousCircuit("input A",   A,
                   "input I",   ram32.D,
                   "output O",  ram32.O,
                   "input WE",  ram32.WE,
                   "input CLK", ram32.WCLK)


def RAM32D(ram):
    ram32 = RAM32x1D(INIT=lutinit(ram,32))

    A0 = array(ram32.A0, ram32.A1, ram32.A2, ram32.A3, ram32.A4)
    A1 = array(ram32.DPRA0, ram32.DPRA1, ram32.DPRA2, ram32.DPRA3, ram32.DPRA4)
    return AnonymousCircuit("input A0",  A0,
                   "input A1",  A1,
                   "input I",   ram32.D,
                   "output O0", ram32.SPO,
                   "output O1", ram32.DPO,
                   "input WE",  ram32.WE,
                   "input CLK", ram32.WCLK)

def RAM32Q(ram):
    m = RAM32M(INIT_A=lutinit(ram[0],32),
               INIT_B=lutinit(ram[1],32),
               INIT_C=lutinit(ram[2],32),
               INIT_D=lutinit(ram[3],32))

    args =  ['input AA', m.ADDRA]
    args += ['input AB', m.ADDRB]
    args += ['input AC', m.ADDRC]
    args += ['input AD', m.ADDRD]

    args += ['input IA', m.DIA]
    args += ['input IB', m.DIB]
    args += ['input IC', m.DIC]
    args += ['input ID', m.DID]

    args += ['output OA', m.DOA]
    args += ['output OB', m.DOB]
    args += ['output OC', m.DOC]
    args += ['output OD', m.DOD]

    args += ["input WE", m.WE]
    args += ["input CLK", m.WCLK]

    return AnonymousCircuit(*args)

def RAM32x2(ram1, ram2):
    ram32 = RAM32x2S(INIT_00=lutinit(ram1,32), INIT_01=lutinit(ram2,32))

    A = array(ram32.A0, ram32.A1, ram32.A2, ram32.A3, ram32.A4)
    return AnonymousCircuit("input A",   A,
                   "input I0",  ram32.D0,
                   "input I1",  ram32.D1,
                   "output O0", ram32.O0,
                   "output O1", ram32.O1,
                   "input WE",  ram32.WE,
                   "input CLK", ram32.WCLK)


def RAM16(ram):
    ram16 = RAM32(ram)

    wire(0, ram16.A[4])
    return AnonymousCircuit("input A",   ram16.A[0:4],
                   "output O",  ram16.O,
                   "input I",   ram16.I,
                   "input WE",  ram16.WE,
                   "input CLK", ram16.CLK)

def RAM16D(ram):
    ram16 = RAM32D(ram)

    wire(0, ram16.A0[4])
    wire(0, ram16.A1[4])
    return AnonymousCircuit("input A0",  ram16.A0[0:4],
                   "input A1",  ram16.A1[0:4],
                   "output O0", ram16.O0,
                   "output O1", ram16.O1,
                   "input I",   ram16.I,
                   "input WE",  ram16.WE,
                   "input CLK", ram16.CLK)

def RAM16x2(ram0, ram1):
    ram16 = RAM32x2(ram0, ram1)

    wire(0, ram16.A[4])
    return AnonymousCircuit("input A",   ram16.A[0:4],
                   "output O0", ram16.O0,
                   "output O1", ram16.O1,
                   "input  I0", ram16.I0,
                   "input  I1", ram16.I1,
                   "input WE",  ram16.WE,
                   "input CLK", ram16.CLK)


def _RAMName(name, n):
    return name + '%d' % n

RAMCache = {}

def DefineRAM16DxN(n, init=0):

    name = _RAMName('RAM16D_', n)
    if name in RAMCache:
         return RAMCache[name]

    ArrayN = Array(n, Bit)
    args =  ["input A0",  Array4,
             "input A1",  Array4,
             "output O0", ArrayN,
             "output O1", ArrayN,
             "input I",   ArrayN,
             "input WE",  Bit,
             "input CLK", Bit]

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

    ArrayN = Array(n, Bit)
    Array6 = Array(6, Bit)
    args = ["input A0", Array6,
            "input A1", Array6,
            "input A2", Array6,
            "input A3", Array6,
            "output O0", ArrayN,
            "output O1", ArrayN,
            "output O2", ArrayN,
            "output O3", ArrayN,
            "input I", ArrayN,
            "input WE", Bit,
            "input CLK", Bit]
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

