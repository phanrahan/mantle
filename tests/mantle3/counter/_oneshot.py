import sys
from magma import *
from mantle import *
from mantle.util.edge import falling
from mantle.util.debounce import debounce
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Joystick.on()
megawing.LED.on(4)

main = megawing.main()

slow = Counter(16)
select = debounce( main.SELECT, slow.COUT )
run = Not()( select )
# run needs to be held down for at least one second ...

# 1Hz counter
clock = Counter(24)

# counter from 0 to 15
counter = Counter(4, ce=True)

# flip-flop controls counter enable
ff = FF(ce=True)
# next stage of the flip-flop
# - ff=1 if run
# - ff=0 if ~counter.COUT
d = LUT3(I0|(~I1&I2))(run,counter.COUT,ff)
ff(d,CE=clock.COUT)

# enable counter if ff and clock.COUT
ena = LUT2(I0&I1)(ff, clock.COUT)

main.LED( counter(CE=ena) )

compile(sys.argv[1], main)


