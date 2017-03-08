import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.LED.on(1)

main = megawing.main()

counter = Counter(32)

wire( counter.O[24], main.LED[0] )

compile(sys.argv[1], main)


