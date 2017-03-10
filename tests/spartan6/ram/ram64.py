import sys
from magma import *
from mantle.xilinx.spartan6.RAM import RAM64
from loam.shields.megawing import MegaWing

def bit(n):
    return n * [0] + n * [1]

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(4)

main = megawing.main()

ram0 = RAM64(32 * bit(1))
ram1 = RAM64(16 * bit(2))
ram2 = RAM64( 8 * bit(4))
ram3 = RAM64( 4 * bit(8))

ADDR = main.SWITCH[0:6]
DI = main.SWITCH[6]
WE = main.SWITCH[7]

wire(ram0(ADDR, DI, WE), main.LED[0])
wire(ram1(ADDR, DI, WE), main.LED[1])
wire(ram2(ADDR, DI, WE), main.LED[2])
wire(ram3(ADDR, DI, WE), main.LED[3])

compile(sys.argv[1], main)
