import sys
from magma import *
from mantle import *
from boards.papilio import Papilio

papilio = Papilio()
papilio.Clock.on()
papilio.A[0].rename('SIG').output().on()

main = papilio.main()

counter = Counter(32)
square = counter.O[9]

wire( square, main.SIG )

compile(sys.argv[1], main)

