import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(4)
megawing.LED.on(8)

main = megawing.main()

mux16test = Mux(16, 8)

A8 = Out(Array(8,Bit))

muxinputs = [
        A8(0,0,0,0,0,1,0,0),
        A8(1,0,0,0,0,0,1,0),
        A8(0,1,0,0,0,1,0,0),
        A8(1,1,0,0,0,0,1,0),
        A8(0,0,1,0,0,1,0,0),
        A8(1,0,1,0,0,0,1,0),
        A8(0,1,1,0,0,1,0,0),
        A8(1,1,1,0,0,0,1,0),
        A8(0,0,0,1,0,1,0,0),
        A8(1,0,0,1,0,0,1,0),
        A8(0,1,0,1,0,1,0,0),
        A8(1,1,0,1,0,0,1,0),
        A8(0,0,1,1,0,1,0,0),
        A8(1,0,1,1,0,0,1,0),
        A8(0,1,1,1,0,1,0,0),
        A8(1,1,1,1,0,0,1,0)]

muxS = main.SWITCH[0:4]
mux16testO = mux16test(*(muxinputs + [muxS]))
wire(mux16testO, main.LED)

compile(sys.argv[1], main)
