from collections import OrderedDict
from magma import *
from magma.bitutils import log2

__all__  = ['RAMB16_S2', 
            'RAMB16_S4',
            'RAMB16_S9',
            'RAMB16_S18',
            'RAMB16_S18_S18']
__all__ += ['RAMB16', 'RAMB16D']
__all__ += ['ROMB16']

RAMB16_S2 = DeclareCircuit("RAMB16_S2",
            "DI", In(Bits[ 2 ]),
            "DO", Out(Bits[ 2 ]),
            "ADDR", In(Bits[ 13 ]),
            "CLK", In(Clock),
            "EN", In(Bit),
            "SSR", In(Bit),
            "WE", In(Bit) )

RAMB16_S4 = DeclareCircuit("RAMB16_S4",
            "DI", In(Bits[ 4 ]),
            "DO", Out(Bits[ 4 ]),
            "ADDR", In(Bits[ 12 ]),
            "CLK", In(Clock),
            "EN", In(Bit),
            "SSR", In(Bit),
            "WE", In(Bit) )

RAMB16_S9 = DeclareCircuit("RAMB16_S9",
            "DI", In(Bits[ 8 ]),
            "DIP", In(Bits[ 1 ]),
            "DO", Out(Bits[ 8 ]),
            "DOP", Out(Bits[ 1 ]),
            "ADDR", In(Bits[ 11 ]),
            "CLK", In(Clock),
            "EN", In(Bit),
            "SSR", In(Bit),
            "WE", In(Bit) )

RAMB16_S18 = DeclareCircuit("RAMB16_S18",
            "DI", In(Bits[ 16 ]),
            "DIP", In(Bits[ 2 ]),
            "DO", Out(Bits[ 16 ]),
            "DOP", Out(Bits[ 2 ]),
            "ADDR", In(Bits[ 10 ]),
            "CLK", In(Clock),
            "EN", In(Bit),
            "SSR", In(Bit),
            "WE", In(Bit) )

# Dual port ram
# No parity bits
# No SSRA/B

RAMB16_S18_S18 = DeclareCircuit("RAMB16_S18_S18",
            "DIA", In(Bits[ 16 ]),
            "DIPA", In(Bits[ 2 ]),
            "DOA", Out(Bits[ 16 ]),
            # "output DOPA", Bits(2),
            "ADDRA", In(Bits[ 10 ]),
            "CLKA", In(Clock),
            "ENA", In(Bit),
            "WEA", In(Bit),
            "SSRA", In(Bit),

            "DIB", In(Bits[ 16 ]),
            "DIPB", In(Bits[ 2 ]),
            "DOB", Out(Bits[ 16 ]),
            # "output DOPB", Bits(2),
            "ADDRB", In(Bits[ 10 ]),
            "CLKB", In(Clock),
            "ENB", In(Bit),
            "WEB", In(Bit),
            "SSRB", In(Bit),
            )


def ramb16_init_bits(rom, width, params):
    n = len(rom)
    if width == 8 or width == 9:

        assert n in [256, 512, 1024, 2048]
        if n != 2048:
            rom += (2048 - n) * [0]

        params = romX8(rom, 2048, params)
        if width == 9:
            params = romX1P(rom, 2048, params)

    if width == 16 or width == 18:

        assert n in [256, 512, 1024]
        if n != 1024:
            rom += (1024 - n) * [0]

        params = romX16(rom, 1024, params)
        if width == 18:
            params = romX2P(rom, 1024, params)

def RAMB16D(rom, init = None):

    """
    Configure a dual-port blocked RAM (currently only one setting)
    """

    width = 16

    params = OrderedDict()
    params['WRITE_MODE_A'] = '"WRITE_FIRST"'
    params['WRITE_MODE_B'] = '"WRITE_FIRST"'
    # initialize RAM output register
    if init is None:
        #init = "%d'h%05X" % (width, 0)
        init = (0, width)
    else:
        #init = "%d'h%05X" % (width, init)
        init = (init, width)
    params["INIT_A"] = init
    params["INIT_B"] = init
    params["SRVAL_A"] = init
    params["SRVAL_B"] = init

    #   512X36  512X32
    #  1024X18 1024X16
    #  2048X9  2048X8
    #  4096X4
    #  8192X2
    # 16384X1
    n = len(rom)
    logn = log2(n)
   
    ramb16_init_bits(rom, width, params)
    ram = RAMB16_S18_S18(**params)

    args = ["CLKA", ram.CLKA, "CLKB", ram.CLKB]
    args += ["ENA", ram.ENA, "ENB", ram.ENB]
    args += ["WEA", ram.WEA, "WEB", ram.WEB]

    # Default: We wanted a dual port ram in the first place,
    # so why not just turn them on all the time?    
    wire(array([0,0]), ram.DIPA)
    wire(array([0,0]), ram.DIPB)
    # wire(1, ram.ENB)
    # wire(1, ram.ENA)
    # wire(1, ram.ENB)
    wire(0, ram.SSRA)
    wire(0, ram.SSRB)

    # reverse the address bits
    # AA = [ram.ADDRA[logn-1-i] for i in range(logn)]
    AA = [ram.ADDRA[i] for i in range(logn)]
    AA = array(AA)

    # reverse the order DI
    #IA = [ram.DIA[ram.DIA.N-1-i] for i in range(ram.DIA.N)]
    IA = [ram.DIA[i] for i in range(ram.DIA.N)]
    IA = array(IA)

    OA = [ram.DOA[i] for i in range(ram.DOA.N)]
    OA = array(OA)

    args += ['IA', IA, "AA", AA, "OA", OA]

    # reverse the address bits
    #AB = [ram.ADDRB[logn-1-i] for i in range(logn)]
    AB = [ram.ADDRB[i] for i in range(logn)]
    AB = array(AB)

    # reverse the order DI
    #IB = [ram.DIB[ram.DIB.N-1-i] for i in range(ram.DIB.N)]
    IB = [ram.DIB[i] for i in range(ram.DIB.N)]
    IB = array(IB)

    # reverse the order DI
    #OB = [ram.DOB[ram.DOB.N-1-i] for i in range(ram.DOB.N)]
    OB = [ram.DOB[i] for i in range(ram.DOB.N)]
    OB = array(OB)

    args += ['IB', IB, "AB", AB, "OB", OB]

    return AnonymousCircuit(args)

def RAMB16(rom, width, init=None):
    """
    Configure a blocked RAM.
    """

    params = OrderedDict()
    params['WRITE_MODE'] = '"WRITE_FIRST"'
    # initialize RAM output register
    if init is None:
        #init = "%d'h%05X" % (width, rom[0])
        init = (rom[0], width)
    else:
        #init = "%d'h%05X" % (width, init)
        init = (init, width)
    params["INIT"] = init
    params["SRVAL"] = init


    #   512X36  512X32
    #  1024X18 1024X16
    #  2048X9  2048X8
    #  4096X4
    #  8192X2
    # 16384X1
    n = len(rom)
    logn = log2(n)

    if width == 8 or width == 9:
        assert n in [256, 512, 1024, 2048]
        if n != 2048:
            rom += (2048 - n) * [0]

        params = romX8(rom, 2048, params)
        if width == 9:
            params = romX1P(rom, 2048, params)

        ram = RAMB16_S9(**params)

    if width == 16 or width == 18:
        assert n in [256, 512, 1024]
        if n != 1024:
            rom += (1024 - n) * [0]

        params = romX16(rom, 1024, params)
        if width == 18:
            params = romX2P(rom, 1024, params)

        ram = RAMB16_S18(**params)

    # reverse the address bits
    #A = [ram.ADDR[logn-1-i] for i in range(logn)]
    A = [ram.ADDR[i] for i in range(logn)]
    A = array(A)

    # reverse the order DI
    #I = [ram.DI[ram.DI.N-1-i] for i in range(ram.DI.N)]
    I = [ram.DI[i] for i in range(ram.DI.N)]

    # reverse the order DI
    #O = [ram.DO[ram.DO.N-1-i] for i in range(ram.DO.N)]
    O = [ram.DO[i] for i in range(ram.DO.N)]

    if   width == 8:
        wire(0, ram.DIP[0])
    elif width == 9:
        I += [ram.DIP[0]]
        O += [ram.DOP[0]]
    elif width == 16:
        wire(0, ram.DIP[0])
        wire(0, ram.DIP[1])
    elif width == 18:
        # reverse
        #I += [ram.DIP[1], ram.DIP[0]]
        #O += [ram.DOP[1], ram.DOP[0]]
        I += [ram.DIP[0], ram.DIP[1]]
        O += [ram.DOP[0], ram.DOP[1]]

    I = array(I)
    O = array(O)

    wire(0, ram.SSR)  # SSR defaults to active high - inverted
    wire(0, ram.WE)   # WE  defaults to active high - inverted

    args = ram.interface.clockargs() + ['CE', ram.EN]
    args += ['I', I, "A", A, "O", O]

    return AnonymousCircuit(args)



def ROMB16(rom, width, init=None):
    rom = RAMB16(rom, width, init=init)

    wire(array(width*[0]), rom.I)
    wire(1, rom.CE)

    return AnonymousCircuit("A", rom.A, "O", rom.O, 'CLK', rom.CLK)

# functions to format INIT strings

def romX32(ram, n, params={}):
    assert True
    return params


def romX16(ram, n, params={}):
    N = 16  # 64 / 4 nibbles
    for i in range(0, n, N):
        val = 0
        nonzero = False
        for j in range(N):
            halfword = ram[i+j] & 0xffff
            if halfword:
                nonzero = True
            val |= halfword << (16*j)
        if nonzero:
            key = "INIT_" + ("%02X" % (i // N))
            params[key] = (val, 256)
    return params


def romX8(ram, n, params={}):
    N = 32  # (64 / 2 nibble)
    for i in range(0, n, N):
        val = 0
        nonzero = False
        for j in range(N):
            byte = ram[i+j] & 0xff
            if byte:
                nonzero = True
            val |= byte << (8*j)
        if nonzero:
            key = "INIT_" + ("%02X" % (i // N))
            params[key] = (val, 256)
    return params


def romX4(ram, n, params={}):
    assert True
    return params


def romX2(ram, n, params={}):
    assert True
    return params


def romX1(ram, n, params={}):
    assert True
    return params

def romX1P(ram, n, params={}):
    N = 256
    for i in range(0, n, N):
        val = 0
        nonzero = False
        for j in range(N):
            bit = (ram[i+j] >> 8) & 0x1
            if bit:
                nonzero = True
            val |= bit << j
        if nonzero:
            key = "INITP_" + ("%02X" % (i // N))
            params[key] = (val, 256)
    return params


def romX2P(ram, n, params={}):
    N = 128
    for i in range(0, n, N):
        val = 0
        nonzero = False
        for j in range(0, N):
            bit2 = (ram[i+j] >> 16) & 0x3
            if bit2:
                nonzero = True
            val |= bit2 << (2*j)
        if nonzero:
            key = "INITP_" + ("%02X" % (i // N))
            params[key] = (val, 256)
    return params


def romX4P(rom, n, params={}):
    assert True
    return params


def romX9(rom, n, params={}):
    params = romX8(ram, n, params)
    params = romX1P(ram, n, params)
    return params


def romX18(ram, n, params={}):
    params = romX16(ram, n, params)
    params = romX2P(ram, n, params)
    return params
