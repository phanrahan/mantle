import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.LED.on(4)

main = megawing.main()

clock = Counter(24)

counter = CounterModM( 10, 4 ) 

counter(CE=clock.COUT)

wire( counter, main.LED )

compile(sys.argv[1], main)
