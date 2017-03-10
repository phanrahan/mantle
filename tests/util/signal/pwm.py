import sys
from magma import *
from mantle import Counter
from mantle.util.pwm import PWM
from loam.boards.papilio import Papilio

N = 8

papilio = Papilio()
papilio.Clock.on()
papilio.A[0].rename('SIG').output().on()

main = papilio.main()

counter = Counter(32)
sawtooth = counter.O[8:8+N]

pwm = PWM(N)

wire( pwm( sawtooth, array(0,0,0,0,0,0,1,0)), main.SIG )

compile(sys.argv[1], main)

