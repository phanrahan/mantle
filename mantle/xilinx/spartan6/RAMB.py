from collections import OrderedDict
from magma import *
from magma.bitutils import log2

__all__  = ['RAMB16', 'RAMB16D', 'RAMB16BWER']
__all__ += ['ROMB16']


RAMB16BWER = DeclareCircuit("RAMB16BWER",
            "DIA", In(Bits[ 32 ]),
            "DIPA", In(Bits[ 4 ]),
            "DOA", Out(Bits[ 32 ]),
            "DOPA", Out(Bits[ 4 ]),
            "ADDRA", In(Bits[ 14 ]),
            "CLKA", In(Clock),
            "ENA", In(Bit),
            "WEA", In(Bits[ 4 ]),
            "RSTA", In(Bit),
            "REGCEA", In(Bit),

            "DIB", In(Bits[ 32 ]),
            "DIPB", In(Bits[ 4 ]),
            "DOB", Out(Bits[ 32 ]),
            "DOPB", Out(Bits[ 4 ]),
            "ADDRB", In(Bits[ 14 ]),
            "CLKB", In(Clock),
            "ENB", In(Bit),
            "WEB", In(Bits[ 4 ]),
            "RSTB", In(Bit),
            "REGCEB", In(Bit))



def RAMB16D(rom, width, init = None):

    """
    Configure a dual-port blocked RAM
    """

    params = OrderedDict()

    params['DOA_REG'] = 0
    params['DOB_REG'] = 0

    params['WRITE_MODE_A'] = '"WRITE_FIRST"'
    params['WRITE_MODE_B'] = '"WRITE_FIRST"'

    # initialize RAM register
    init = (0, width) if init is None else (init, width)
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
    ram = RAMB16BWER(**params)

    args  = ["CLKA", ram.CLKA, "CLKB", ram.CLKB]
    args += ["ENA", ram.ENA, "ENB", ram.ENB]
    args += ["WEA", ram.WEA, "WEB", ram.WEB]
    args += ["REGCEA", ram.REGCEA, "REGCEB", ram.REGCEB]

    wire(0, ram.RSTA)
    wire(0, ram.RSTB)

    AA = config_ramb16_addr_pins(logn, ram, p = "A")
    IA, OA = config_ramb16_io_pins(width, ram, p = "A")
    args += ['IA', IA, "AA", AA, "OA", OA]

    AB = config_ramb16_addr_pins(logn, ram, p = "B")
    IB, OB = config_ramb16_io_pins(width, ram, p = "B")
    args += ['IB', IB, "AB", AB, "OB", OB]

    return AnonymousCircuit(*args)

def RAMB16(rom, width, init=None):
    """
    Configure a blocked RAM.
    """

    params = OrderedDict()

    #params['DOA_REG'] = 0 # default=0
    #params['DOB_REG'] = 0
    params['WRITE_MODE_A'] = '"WRITE_FIRST"'
    params['WRITE_MODE_B'] = '"WRITE_FIRST"'

    # initialize RAM register
    init = (0, width) if init is None else (init, width)
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
    ram = RAMB16BWER(**params)

    A = array([ram.ADDRB[i] for i in range(14)])

    I = array([ram.DIB[i] for i in range(ram.DIB.N)])

    IP = array([ram.DIPB[i] for i in range(ram.DIPB.N)])

    wire(array([0,0,0,0]), ram.WEB)
    wire(clock(0), ram.CLKB)
    wire(0, ram.RSTB)
    wire(0, ram.REGCEB)
    wire(0, ram.ENB)

    wire(array([0,0,0,0]), ram.WEA)   # WE  defaults to active high - inverted
    wire(0, ram.RSTA)  # RST defaults to active high - inverted
    wire(0, ram.REGCEA)

    A = config_ramb16_addr_pins(logn, ram, p = "A")
    I, O = config_ramb16_io_pins(width, ram, p = "A")
    args  = ['I', I, "A", A, "O", O]

    args += ['CLK', ram.CLKA, 'CE', ram.ENA]

    return AnonymousCircuit(*args)


def ROMB16(rom, width, init=None):
    ramb = RAMB16(rom, width, init=init)

    wire(array((width*[0])), ramb.I)
    wire(1, ramb.CE)

    return AnonymousCircuit("A", ramb.A, "O", ramb.O, 'CLK', ramb.CLK)

# functions to set up io pins

def config_ramb16_addr_pins(addrwidth, ram, p = "A"):
    rA = ram.ADDRA if p == "A" else ram.ADDRB
    R = [rA[i] for i in range(14 - addrwidth, 14)]
    for n in range(0, 14 - addrwidth):
        wire(0, rA[n])
    return array(R)

def config_ramb16_io_pins(width, ram, p = "A"):
    rDIA = ram.DIA if p == "A" else ram.DIB
    rDOA = ram.DOA if p == "A" else ram.DOB

    rDIPA = ram.DIPA if p == "A" else ram.DIPB
    rDOPA = ram.DOPA if p == "A" else ram.DOPB

    if width == 8 or width == 9:
        I = [rDIA[i] for i in range(8)]
        O = [rDOA[i] for i in range(8)]
        for i in range(8, rDIA.N):
            wire(0, rDIA[i])
        if   width == 8:
            for i in range(4):
                wire(0, rDIPA[i])
        elif width == 9:
            I += [rDIPA[0]]
            O += [rDOPA[0]]
            for i in range(1,4):
                wire(0, rDIPA[i])
    if width == 16 or width == 18:
        I = [rDIA[i] for i in range(16)]
        O = [rDOA[i] for i in range(16)]
        for i in range(16, rDIA.N):
            wire(0, rDIA[i])
        if width == 16:
            for i in range(4):
                wire(0, rDIPA[i])
        elif width == 18:
            I += [rDIPA[0], rDIPA[1]]
            O += [rDOPA[0], rDOPA[1]]
            for i in range(2,4):
                wire(0, rDIPA[i])
    return array(I), array(O)

# functions to format INIT strings

def ramb16_init_bits(rom, width, params):
    n = len(rom)
    if width == 8 or width == 9:
        params['DATA_WIDTH_A'] = 9
        params['DATA_WIDTH_B'] = 9

        assert n in [256, 512, 1024, 2048]
        if n != 2048:
            rom += (2048 - n) * [0]

        params = romX8(rom, 2048, params)
        if width == 9:
            params = romX1P(rom, 2048, params)

    if width == 16 or width == 18:
        params['DATA_WIDTH_A'] = 18
        params['DATA_WIDTH_B'] = 18

        assert n in [256, 512, 1024]
        if n != 1024:
            rom += (1024 - n) * [0]

        params = romX16(rom, 1024, params)
        if width == 18:
            params = romX2P(rom, 1024, params)

def romX32(ram, n, params={}):
    assert True
    return params


def romX16(ram, n, params={}):
    N = 16  # 64 / 4 nibbles
    for i in range(0, n, N):
        val = 0
        nonzero = False
        for j in range(N):
            word = ram[i + j] & 0xffff
            if word:
                nonzero = True
            val |= word << (16*j)
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
            word = ram[i+j] & 0xff
            if word:
                nonzero = True
            val |= word << (8*j)
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

# not tested
def romX1P(ram, n, params={}):
    N = 256
    for i in range(0, n, N):
        val = 0
        nonzero = False
        for j in range(0, N, 4):
            nibble = 0
            inst = (ram[i + j - 0] >> 8) & 0x1
            nibble = (nibble << 1) | inst
            inst = (ram[i + j - 1] >> 8) & 0x1
            nibble = (nibble << 1) | inst
            inst = (ram[i + j - 2] >> 8) & 0x1
            nibble = (nibble << 1) | inst
            inst = (ram[i + j - 2] >> 8) & 0x1
            nibble = (nibble << 1) | inst
            if nibble:
                nonzero = True
            val |= nibble << (4*j)
        if nonzero:
            key = "INITP_" + ("%02X" % (i // N))
            params[key] = (val, 256)
    return params


def romX2P(ram, n, params={}):
    N = 128
    for i in range(0, n, N):
        val = 0
        nonzero = False
        for j in range(0, N, 2):
            nibble = 0
            inst = (ram[i + j + 0] >> 16) & 0x3
            nibble = (nibble << 2) | inst
            inst = (ram[i + j + 1] >> 16) & 0x3
            nibble = (nibble << 2) | inst
            if nibble:
                nonzero = True
            val |= nibble << (4*j)
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

