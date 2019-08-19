from collections import OrderedDict
from magma import *
from .simulation import gen_sb_ram40_4k_sim

__all__  = ['SB_RAM40_4K']

__all__ += ['RAMB', 'ROMB']

# posedge read clock, posedge write clock
SB_RAM40_4K = DeclareCircuit("SB_RAM40_4K",
    "RDATA", Out(Bits[ 16 ]),
    "RADDR", In(Bits[ 11 ]),
    "RCLK",  In(Clock),
    "RCLKE", In(Enable),
    "RE",    In(Enable),
    "WCLK",  In(Clock),
    "WCLKE", In(Enable),
    "WE",    In(Enable),
    "WADDR", In(Bits[ 11 ]),
    "MASK",  In(Bits[ 16 ]),
    "WDATA", In(Bits[ 16 ]),
    stateful=True,
    simulate=gen_sb_ram40_4k_sim(prc=True, pwc=True),
    coreir_lib='ice40')

# posedge read clock, negedge write clock
# negedge read clock, posedge write clock
# negedge read clock, negedge write clock
# - can get these effects by inverting the RCLK and/or the WCLK
# NEGCLK_R(0|1)
# NEGCLK_W(0|1)


# MASK=0, write-enabled, MASK=1, write-disabled

#
# N is the number of bits of output
#
def init(rom,N,mode=0):
    # INIT_%x 256 bits = 32 bytes = 64 nibbles
    params = OrderedDict({})
    params['WRITE_MODE'] = mode
    params['READ_MODE'] = mode

    # M is the number of high (>8) address values
    #  e.g. if N == 8, then there are 2 high address values
    M = 16//N
    for i in range(16):
        v = 0
        for b in range(256):
            col = (b//M)%N
            # NB. the high address values ocuppy the lowest bit positions
            row = 256*(b%M) + 16*i + b//16
            bit = (rom[row] >> col)&1
            #print('i=%x'%i, 'b=%d'%b, row, col)
            v |= bit << b
        key = 'INIT_%X' % i
        #params[key] = "256'h%064x" % v
        params[key] = (v, 256)
    return params

def wireaddr(addr, n):
    for i in range(n):
        wire(0, addr[10-i])
    return addr[0:11-n]

def _RAMB(height, width, rom=None, readonly=False):
    if not rom:
        rom = height * [0]
    n = len(rom)
    assert height == n

    ram40 = None
    if   n ==  256: # 256x16
        assert width == 16
        params = init(rom,16,mode=0)
        ram40 = SB_RAM40_4K(**params)
        ram40.RADDR = wireaddr(ram40.RADDR, 3)
        if not readonly:
            ram40.WADDR = wireaddr(ram40.WADDR, 3)
    elif n ==  512: # 512x8
        assert width == 8
        params = init(rom,8,mode=1)
        ram40 = SB_RAM40_4K(**params)
        ram40.RADDR = wireaddr(ram40.RADDR, 2)
        RDATA = ram40.RDATA
        ram40.RDATA = array([RDATA[0], RDATA[2], RDATA[4], RDATA[6],
                            RDATA[8], RDATA[10], RDATA[12], RDATA[14]])
        if not readonly:
            WDATA = ram40.WDATA
            wire(0,WDATA[1])
            wire(0,WDATA[3])
            wire(0,WDATA[5])
            wire(0,WDATA[7])
            wire(0,WDATA[9])
            wire(0,WDATA[11])
            wire(0,WDATA[13])
            wire(0,WDATA[15])
            ram40.WDATA = array([WDATA[0], WDATA[2], WDATA[4], WDATA[6],
                                WDATA[8], WDATA[10], WDATA[12], WDATA[14]])
            ram40.WADDR = wireaddr(ram40.WADDR, 2)
    elif n == 1024: # 1024x4
        assert width == 4
        params = init(rom,4,mode=2)
        ram40 =  SB_RAM40_4K(**params)
        ram40.RADDR = wireaddr(ram40.RADDR, 1)
        RDATA = ram40.RDATA
        ram40.RDATA = array([RDATA[1], RDATA[5], RDATA[9], RDATA[13]])
        if not readonly:
            WDATA = ram40.WDATA
            wire(0,WDATA[0])
            wire(0,WDATA[2])
            wire(0,WDATA[3])
            wire(0,WDATA[4])
            wire(0,WDATA[6])
            wire(0,WDATA[7])
            wire(0,WDATA[8])
            wire(0,WDATA[10])
            wire(0,WDATA[11])
            wire(0,WDATA[12])
            wire(0,WDATA[14])
            wire(0,WDATA[15])
            ram40.WDATA = array([WDATA[1], WDATA[5], WDATA[9], WDATA[13]])
            ram40.WADDR = wireaddr(ram40.WADDR, 1)
    elif n == 2048: # 2048x2
        assert width == 2
        params = init(rom,2,mode=3)
        ram40 = SB_RAM40_4K(**params)
        RDATA = ram40.RDATA
        ram40.RDATA = array([RDATA[3], RDATA[11]])
        if not readonly:
            WDATA = ram40.WDATA
            wire(0,WDATA[0])
            wire(0,WDATA[1])
            wire(0,WDATA[2])
            wire(0,WDATA[4])
            wire(0,WDATA[5])
            wire(0,WDATA[6])
            wire(0,WDATA[7])
            wire(0,WDATA[8])
            wire(0,WDATA[9])
            wire(0,WDATA[10])
            wire(0,WDATA[12])
            wire(0,WDATA[13])
            wire(0,WDATA[14])
            wire(0,WDATA[15])
            ram40.WDATA = array([WDATA[3], WDATA[11]])

    if readonly:
        wire( 0, ram40.WE    )
        wire( array(11*[0]), ram40.WADDR )
        wire( array(16*[0]), ram40.WDATA )
    wire(0 if readonly else 1, ram40.WCLKE )
    wire(1, ram40.RCLKE)
    wire(array(16*[0]), ram40.MASK)
    if readonly:
        return AnonymousCircuit("RADDR", ram40.RADDR,
                                "RDATA", ram40.RDATA,
                                "RCLK",  ram40.RCLK,
                                "RE",    ram40.RE)
    else:
        return AnonymousCircuit("RADDR", ram40.RADDR,
                                "RDATA", ram40.RDATA,
                                "RCLK",  ram40.RCLK,
                                "RE",    ram40.RE,
                                "WADDR", ram40.WADDR,
                                "WDATA", ram40.WDATA,
                                "WCLK",  ram40.WCLK,
                                "WE",    ram40.WE)

def RAMB(height, width, ram=None):
    return _RAMB(height, width, ram, readonly=False)

def ROMB(height, width, rom=None):
    return _RAMB(height, width, rom, readonly=True)
