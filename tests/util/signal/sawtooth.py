import sys
from magma import *
from mantle import *
from boards.papilio import Papilio

N = 8

papilio = Papilio()
papilio.Clock.on()

for i in range(N):
    papilio.A[i].rename('SIG[%d]' % i).output().on()

main = papilio.main()

counter = Counter(32)
sawtooth = counter.O[8:8+N]

wire( sawtooth, main.SIG )

compile(sys.argv[1], main)

