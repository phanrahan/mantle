import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3.seq import DefineSequencer
from mantle.util.peripherals.debounce import debounce
from mantle.util.edge import falling
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(6)
megawing.LED.on(2)
megawing.Joystick.init(select=True).on()

# define a 16-bit counter 
Counter16 = Counter(16)
# define a 4-bit updown counter with an enable
UpDown4 = UpDownCounter(4, next=True, ce=True)
# define a n-bit Mux2
Mux2xN = Mux(2,2)

main = megawing.main()
incr = main.SWITCH[0]
jump = main.SWITCH[1]
push = main.SWITCH[2]
pop  = main.SWITCH[3]
addr = main.SWITCH[4:6]
O = main.LED

slow = Counter16()
select = debounce(main.SELECT, slow.COUT)
pulse = falling(select)

print('creating seq')
Sequencer2 = DefineSequencer(2)
seq = Sequencer2()

print('wiring seq')
pc = seq(incr, jump, addr, push, pop, pulse)
O(pc)

compile(sys.argv[1], main)

